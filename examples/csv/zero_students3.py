#!/usr/bin/env python3
#
#    $ ./zero_students2.py grades.csv grades_zeroed.csv Dave ...
#
# Zero grades of named students.

import sys
import csv

_, inputfile, outputfile, *students_to_zero = sys.argv

def zero_grade(name, grade):
    if name in students_to_zero:
        grade = "0"
    return (name, grade)

with open(inputfile) as fin, open(outputfile, "w") as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    writer.writerows((zero_grade(name, grade) for name, grade in reader))
