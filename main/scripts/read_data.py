import csv

def make_objects(infile):
    in_file = open(infile, 'r')
    in_reader = csv.reader(in_file)
    for row in in_reader:
        print(row)