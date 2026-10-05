from notebook_state_check import audit
import json
n={'nbformat':4,'cells':[{'cell_type':'code','execution_count':3,'outputs':[]},{'cell_type':'code','execution_count':1,'outputs':[]}]}
r=audit(n);assert r['findings'][0]['kind']=='execution_order_decrease';print(json.dumps(r))
