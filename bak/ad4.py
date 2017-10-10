import csv 
import numpy as np
input_file = open("eggs.csv","r+")
reader_file = csv.reader(input_file)
ant_rows= len(list(reader_file))
input_file.close()

matris=[[]]
matris.append([])
matris[0].append('3')
matris[0].append('4')
print(matris[0][0])
print(matris[0][1])
print(ant_rows)
#a=np.zeros((6,3))

#print(a)
