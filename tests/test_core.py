import unittest,copy,itertools,tempfile
from pathlib import Path
from fractions import Fraction
from src.scoring import conditional_precision as c0,strict_precision as c1,original_b0
from src.annotation_parser import parse,FULL,PARTIAL,NO_SUPPORT
from src.cohort import resolve
from src.data_loader import load

def units(labels,collective='Yes'):
 return [dict(label=x,collective=collective,statement_index=0) for x in labels]
def record():
 return dict(id='x',query='q',response='Text [1].',split='test',system_name='you',citations=[dict(text='[1]',start_index=5,end_index=8,link_target='url')],statements_to_citation_texts={'Text [1].':['[1]']},annotation={'statement_to_annotation':{'Text [1].':dict(statement_is_verification_worthy=True,statement_supported='Yes',citation_annotations=[dict(citation_text='[1]',citation_supports=FULL)])}})
class TestScoring(unittest.TestCase):
 def test_full(self):self.assertEqual(c0(units(['full']),1),1);self.assertEqual(c1(units(['full']),1),1)
 def test_collective_partial(self):self.assertEqual(c0(units(['partial','partial']),2),1);self.assertEqual(c1(units(['partial','partial']),2),0)
 def test_full_blocks_partial(self):self.assertEqual(c0(units(['full','partial']),2),Fraction(1,2))
 def test_partial_without_collective(self):self.assertEqual(c0(units(['partial'],'No'),1),0)
 def test_contradiction(self):self.assertEqual(c0(units(['partial'],'Citations Contradict Each Other'),1),0)
 def test_individual_full_preserved(self):self.assertEqual(c0(units(['full'],'Citations Contradict Each Other'),1),1)
 def test_zero_and_mismatch(self):
  for n in [0,2]:
   with self.assertRaises(ValueError):c0(units(['full']),n)
 def test_null(self):
  with self.assertRaises(ValueError):c0(units(['partial'],None),1)
 def test_original_blocked(self):
  with self.assertRaises(NotImplementedError):original_b0()
 def test_exhaustive_rule(self):
  for n in range(1,5):
   for ls in itertools.product(['full','partial','none'],repeat=n):
    for collective in ['Yes','No','Citations Contradict Each Other']:
     expected=sum(x=='full' for x in ls)
     if collective=='Yes' and 'full' not in ls:expected+=sum(x=='partial' for x in ls)
     self.assertEqual(c0(units(ls,collective),n),Fraction(expected,n))
     self.assertLessEqual(c1(units(ls,collective),n),c0(units(ls,collective),n))
class TestMapping(unittest.TestCase):
 def test_valid(self):self.assertEqual(parse(record())[1],[])
 def test_repeated_marker(self):
  r=record();r['response']='Text [1] [1].';a=r['annotation']['statement_to_annotation'].pop('Text [1].');r['annotation']['statement_to_annotation'][r['response']]=a;r['statements_to_citation_texts']={r['response']:['[1]']};r['citations'].append(dict(text='[1]',start_index=9,end_index=12,link_target='url'))
  self.assertIn('nonbijective_marker_occurrence',parse(r)[1])
 def test_wrong_offset(self):
  r=record();r['citations'][0]['start_index']=4;self.assertIn('invalid_offset',parse(r)[1])
 def test_missing_judgment(self):
  r=record();r['annotation']['statement_to_annotation']['Text [1].']['citation_annotations']=None;self.assertIn('marker_judgment_mismatch',parse(r)[1])
 def test_exceptional_labels(self):
  for label in NO_SUPPORT:
   r=record();r['annotation']['statement_to_annotation']['Text [1].']['citation_annotations'][0]['citation_supports']=label
   u,e=parse(r);self.assertFalse(e);self.assertEqual(c0(u,1),0)
 def test_zero(self):
  r=record();r['citations']=[];r['statements_to_citation_texts']={'Text [1].':[]};r['annotation']['statement_to_annotation']['Text [1].']['citation_annotations']=None;r['annotation']['statement_to_annotation']['Text [1].']['statement_supported']=None;self.assertIn('zero_citations',parse(r)[1])
 def test_repeated_ids(self):
  r=record();rows=[(1,r),(2,copy.deepcopy(r))]
  self.assertEqual(len(resolve(rows,'unique_raw')[0]),0);self.assertEqual(len(resolve(rows,'identical')[0]),1)
  rows[1][1]['annotation']['statement_to_annotation']['Text [1].']['statement_supported']='No'
  self.assertEqual(len(resolve(rows,'identical')[0]),0);self.assertEqual(len(resolve(rows,'distinct_mean')[0]),2)
 def test_invalid_json(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'bad.jsonl';p.write_text('{bad}\n')
   with self.assertRaisesRegex(ValueError,'line 1'):load(p,False)
if __name__=='__main__':unittest.main()
