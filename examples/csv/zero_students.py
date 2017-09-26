#!/usr/bin/env python3
#
#  zero_students.py
#
#  Usage:
#
#    $ ./zero_students.py grades.csv grades_zeroed.csv Dave
#

import csv

def main(inputfile, outputfile, *students_to_zero):
    '''Read CSV from inputfile, zero grades and write CSV to outputfile

    inputfile: filename to read
    outputfile: filename to write zeroed results to
    students_to_zero: list of student names whose marks should be zero
    '''
    # Input name/grades CSV file
    names_grades = read_grades(inputfile)

    # Zero the grades for the named students
    zero_grades(names_grades, students_to_zero)

    # Output name/grades CSV file
    write_grades(outputfile, names_grades)

def read_grades(inputfile):
    '''Read CSV file into a list of (name,grade) tuples.'''
    with open(inputfile) as fin:
        reader = csv.reader(fin)
        names_grades = []
        for name, grade in reader:
            # note that grade is also a string here
            names_grades.append((name, grade))
    return names_grades

def write_grades(outputfile, names_grades):
    '''Write list of (name,grade) tuples to outputfile'''
    with open(outputfile, "w") as fout:
        writer = csv.writer(fout)
        for name, grade in names_grades:
            row = (name, grade)
            writer.writerow(row)


def zero_grades(names_grades, students_to_zero):
    '''Set grades to zero for students names in students_to_zero'''
    N = len(names_grades)
    for n in range(N):
        name, grade = names_grades[n]
        if name in students_to_zero:
            # Set grade to zero (grade is a string)
            names_grades[n] = (name, "0")


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
