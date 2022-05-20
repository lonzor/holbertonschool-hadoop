#!/usr/bin/env python3
"""
gets rows of a csv file and prints
"""
import sys


vert = ['id', 'company', 'title', 'totalyearlycompensation',
        'location', 'yearsofexperience', 'yearsatcompany',
        'basesalary', 'stockgrantvalue', 'bonus']

for x in sys.stdin:
    x = x.strip()
    hori = dict(zip(vert, [y.strip() for y in x.split(',')]))
    try:
        pers_id = hori['id']
        comp = hori['company']
        yearly_earn = hori['totalyearlycompensation']
        output = (f'{pers_id}\t{comp}, {yearly_earn}')
        print output
    except:
        continue
