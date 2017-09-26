#!/usr/bin/env python3
#
#    $ ./zero_students2.py grades.csv grades_zeroed.csv Dave ...
#
# Zero grades of named students.

import sys
import csv

_, inputfile, outputfile, *students_to_zero = sys.argv

with open(inputfile) as fin, open(outputfile, "w") as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    for name, grade in reader:
        if name in students_to_zero:
            grade = "0"
        writer.writerow((name, grade))
