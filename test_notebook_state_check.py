import unittest,copy
from notebook_state_check import audit
def nb(counts):return {'nbformat':4,'cells':[{'cell_type':'code','execution_count':n,'outputs':[]}for n in counts]}
class Tests(unittest.TestCase):
 def test_clean_with_gaps(self):self.assertTrue(audit(nb([2,5,9]))['clean_saved_state'])
 def test_out_of_order(self):self.assertEqual(audit(nb([3,1]))['findings'][0]['kind'],'execution_order_decrease')
 def test_duplicate(self):self.assertEqual(audit(nb([2,2]))['findings'][0]['other_cell'],0)
 def test_stale_and_error(self):
  n=nb([None]);n['cells'][0]['outputs']=[{'output_type':'error','ename':'ValueError'}];k={x['kind']for x in audit(n)['findings']};self.assertEqual(k,{'saved_error','outputs_without_execution_count'})
 def test_result_count(self):
  n=nb([4]);n['cells'][0]['outputs']=[{'output_type':'execute_result','execution_count':3}];self.assertEqual(audit(n)['findings'][0]['kind'],'result_count_mismatch')
 def test_no_mutation(self):
  n=nb([2,1]);before=copy.deepcopy(n);audit(n);self.assertEqual(n,before)
 def test_invalid_count(self):
  for v in [True,0,-1,'2']:
   with self.assertRaises(ValueError):audit(nb([v]))
 def test_invalid_format(self):
  with self.assertRaises(ValueError):audit({'nbformat':3,'cells':[]})
