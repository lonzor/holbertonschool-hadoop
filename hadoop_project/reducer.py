#!/usr/bin/env python3
"""
Reducer for MapReduce
"""
import sys


vert = ['id', 'company', 'Salary']
top = []

for x in sys.stdin:
    x = x.strip()
    hori = dict(zip(vert, [y for y in x.replace('\t', ',').split(',')]))
    try:
        earnings = float(hori['Salary'])
        top.append(hori)
    except:
        continue

top = list(reversed(sorted(top, key=lambda z: float(z['Salary']))))[:10]

print('id\tSalary\tcompany')

for r in top:
    pers_id = r['id']
    earnings = float[r['Salary'])
    comp = r['company']
    output = (f'{pers_id}\t{earnings}\t{comp}')
    print output
