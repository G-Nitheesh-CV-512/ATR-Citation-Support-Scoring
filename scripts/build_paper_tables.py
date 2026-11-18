"""Generate manuscript tables from actual CSVs, never hard-coded metric values."""
import argparse,csv,json
from pathlib import Path
NAMES={'bing_chat':'Bing Chat','neeva':'Neeva','perplexity':'Perplexity','you':'You'}
def build(root,paper):
 root=Path(root);paper=Path(paper)
 def rows(name,base=root):return list(csv.DictReader((base/'tables'/name).open()))
 lines=[]
 for r in rows('system_scores.csv'):
  lines.append(f"{NAMES[r['system']]} & {float(r['C0_percent']):.3f} & {float(r['C1_percent']):.3f} & {float(r['loss_pp']):.3f} & {r['affected_queries']} \\\\")
 (paper/'system_rows.tex').write_text('\n'.join(lines)+'\n'+chr(92)+'bottomrule\n')
 lines=[]
 for r in rows('pairwise_gaps.csv'):
  lines.append(f"{NAMES[r['system_a']]}--{NAMES[r['system_b']]} & {float(r['gap_C0_pp']):.3f} & {float(r['gap_C1_pp']):.3f} & {float(r['gap_change_pp']):+.3f} \\\\")
 (paper/'gap_rows.tex').write_text('\n'.join(lines)+'\n'+chr(92)+'bottomrule\n')
 lines=[]
 for name,folder in [('Primary',root),('Identical collapse',root/'collapse_identical'),('Distinct mean',root/'distinct_record_mean')]:
  rr=rows('system_scores.csv',folder)
  lines.append(name+' & '+rr[0]['queries']+' & '+' & '.join(f"{float(r['loss_pp']):.3f}" for r in rr)+r' \\')
 (paper/'robustness_rows.tex').write_text('\n'.join(lines)+'\n'+chr(92)+'bottomrule\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--results',default='results/clean_run');p.add_argument('--paper',default='paper');a=p.parse_args();build(a.results,a.paper)
