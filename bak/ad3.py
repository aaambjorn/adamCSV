import csv 
import numpy as np
input_file = open("nameOfFile.csv","r+")
reader_file = csv.reader(input_file)
ant_rows= len(list(reader_file))
input_file.close()

a=np.zeros(ant_rows,5)
with open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    spamreader
    for row in spamreader:
            print ', '.join(row)


