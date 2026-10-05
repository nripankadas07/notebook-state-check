"""Read-only diagnostics for saved notebook execution state."""
import argparse,json,pathlib

def audit(notebook):
    if not isinstance(notebook,dict) or notebook.get('nbformat')!=4 or not isinstance(notebook.get('cells'),list):
        raise ValueError('expected a nbformat 4 notebook with cells')
    if len(notebook['cells'])>10000: raise ValueError('cell limit exceeded')
    findings=[];seen={};previous=None
    for i,cell in enumerate(notebook['cells']):
        if not isinstance(cell,dict) or cell.get('cell_type') not in ('code','markdown','raw'): raise ValueError(f'cell {i}: invalid cell type')
        if cell['cell_type']!='code':continue
        count=cell.get('execution_count');outputs=cell.get('outputs',[])
        if count is not None and (type(count)is not int or count<1):raise ValueError(f'cell {i}: invalid execution count')
        if not isinstance(outputs,list):raise ValueError(f'cell {i}: outputs must be a list')
        def finding(kind,**extra):findings.append(dict(cell=i,kind=kind,**extra))
        if count is None:
            if outputs:finding('outputs_without_execution_count')
        else:
            if count in seen:finding('duplicate_execution_count',other_cell=seen[count],count=count)
            if previous is not None and count<previous:finding('execution_order_decrease',count=count,previous=previous)
            seen[count]=i;previous=count
        for output in outputs:
            if not isinstance(output,dict):raise ValueError(f'cell {i}: invalid output')
            if output.get('output_type')=='error':finding('saved_error',ename=output.get('ename'))
            if output.get('output_type')=='execute_result' and output.get('execution_count')!=count:
                finding('result_count_mismatch',result_count=output.get('execution_count'),cell_count=count)
    return {'cells':len(notebook['cells']),'findings':findings,'clean_saved_state':not findings}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('notebook');a=p.parse_args()
    try:
        with pathlib.Path(a.notebook).open('rb')as f:raw=f.read(10_000_001)
        if len(raw)>10_000_000:raise ValueError('10 MB notebook limit exceeded')
        result=audit(json.loads(raw));print(json.dumps(result,ensure_ascii=True));return int(bool(result['findings']))
    except (ValueError,OSError,TypeError,RecursionError)as e:print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
