"""C0/C1 adapted controls. Original-cohort B0 is intentionally unavailable."""
from collections import defaultdict
from fractions import Fraction

def original_b0(*args,**kwargs):
    raise NotImplementedError('DEN-01/DUP-01/AGG-01 unresolved; no faithful original B0 implementation')

def credits(units):
    groups=defaultdict(list)
    for u in units:
        if u['label'] not in ('full','partial','none') or u['collective'] not in ('Yes','No','Citations Contradict Each Other'):
            raise ValueError('Unresolved judgment; cannot score')
        groups[u['statement_index']].append(u)
    out=[]
    for group in groups.values():
        if len({u['collective'] for u in group})!=1:raise ValueError('Inconsistent collective judgments')
        has_full=any(u['label']=='full' for u in group)
        for u in group:
            full=int(u['label']=='full')
            partial=int(u['label']=='partial' and u['collective']=='Yes' and not has_full)
            out.append({**u,'full_credit':full,'conditional_partial_credit':partial})
    return out

def conditional_precision(units,denominator):
    if denominator<=0 or denominator!=len(units):raise ValueError('Positive aligned denominator required')
    c=credits(units)
    return Fraction(sum(u['full_credit']+u['conditional_partial_credit'] for u in c),denominator)

def strict_precision(units,denominator):
    if denominator<=0 or denominator!=len(units):raise ValueError('Positive aligned denominator required')
    credits(units) # same validity contract
    return Fraction(sum(u['label']=='full' for u in units),denominator)
