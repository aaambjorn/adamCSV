import csv 
import numpy as np
input_file = open("eggs.csv","r+")
reader_file = csv.reader(input_file)
ant_rows= len(list(reader_file))
input_file.close()

ma=[]

#matris[0].append('3')
#matris[0].append('4')
#print(matris[0][0])
#print(matris[0][1])
#print(ant_rows)
#a=np.zeros((6,3))

#print(a)
a=0

with open('eggs.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        ma.append(row)
        a=a+1

print ma[3][1],ma
