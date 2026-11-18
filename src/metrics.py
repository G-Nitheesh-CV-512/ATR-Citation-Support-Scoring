from fractions import Fraction
from itertools import combinations
from .cohort import SYSTEMS

def mean(values):
    values=list(values)
    if not values:raise ValueError('Empty cohort')
    return sum(values,Fraction(0))/len(values)

def pairwise(scores):
    rows=[]
    for a,b in combinations(SYSTEMS,2):
        g0=scores[a][0]-scores[b][0];g1=scores[a][1]-scores[b][1];d=g1-g0
        assert d==(scores[b][0]-scores[b][1])-(scores[a][0]-scores[a][1])
        sign=lambda x:(x>0)-(x<0)
        status='strict_reversal' if g0*g1<0 else ('tie_transition' if sign(g0)!=sign(g1) else 'unchanged')
        rows.append(dict(system_a=a,system_b=b,gap_C0_pp=float(g0*100),gap_C1_pp=float(g1*100),
            gap_change_pp=float(d*100),gap_C0_exact=str(g0),gap_C1_exact=str(g1),gap_change_exact=str(d),ordering=status))
    return rows
