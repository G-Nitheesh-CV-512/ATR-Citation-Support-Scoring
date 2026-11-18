"""Figures solely from saved experiment CSVs. Matplotlib is the sole direct extra dependency."""
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate(out):
 out=Path(out);figdir=out/'figures';figdir.mkdir(exist_ok=True)
 def read(name):return list(csv.DictReader((out/'tables'/name).open()))
 plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
 def save(fig,name):
  fig.tight_layout();fig.savefig(figdir/(name+'.pdf'),metadata={'CreationDate':None});fig.savefig(figdir/(name+'.png'),dpi=240);plt.close(fig)
 rows=read('system_scores.csv');labels=[r['system'] for r in rows]
 fig,ax=plt.subplots(figsize=(6.5,3.4));xx=list(range(4))
 ax.bar([x-.18 for x in xx],[float(r['C0_percent']) for r in rows],.36,label='C0 conditional',color='#2166ac')
 ax.bar([x+.18 for x in xx],[float(r['C1_percent']) for r in rows],.36,label='C1 strict',color='#e08214')
 ax.set(xticks=xx,xticklabels=labels,ylabel='Citation support precision (%)',ylim=(0,100));ax.legend();save(fig,'precision')
 pairs=read('pairwise_gaps.csv');fig,ax=plt.subplots(figsize=(6.5,3.5))
 values=[float(r['gap_change_pp']) for r in pairs]
 ax.barh([r['system_a']+' − '+r['system_b'] for r in pairs],values,color=['#2166ac' if v>=0 else '#b2182b' for v in values]);ax.axvline(0,color='black',lw=.7);ax.set_xlabel('Gap change D (percentage points)');save(fig,'gap_changes')
 responses=read('response_scores.csv');fig,ax=plt.subplots(figsize=(6.5,3.5))
 for s in labels:
  vs=sorted(100*float(r['loss']) for r in responses if r['system']==s);ax.step(vs,[(i+1)/len(vs) for i in range(len(vs))],where='post',label=s)
 ax.set(xlabel='Response-level precision loss (pp)',ylabel='Cumulative fraction',ylim=(0,1.02));ax.legend();save(fig,'loss_ecdf')
 fig,ax=plt.subplots(figsize=(6.5,3.4))
 for name,path in [('Primary',out),('Identical collapsed',out/'collapse_identical'),('Distinct-record mean',out/'distinct_record_mean')]:
  rr=list(csv.DictReader((path/'tables/system_scores.csv').open()));ax.plot(labels,[float(r['loss_pp']) for r in rr],marker='o',label=name)
 ax.set_ylabel('Mean precision loss (pp)');ax.legend();save(fig,'robustness')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',default='results');a=p.parse_args();generate(a.out)
