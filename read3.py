import csv 
from dateutil.relativedelta import relativedelta
import datetime

date1 = datetime.datetime.strptime("2015-01-30", "%Y-%m-%d").strftime("%d-%m-%Y")
print(date1)

today = datetime.date.today()
print(today)
addMonths = relativedelta(months=3)
future = today + addMonths
print(future) 

input_file = open("plugg3.csv","r+")
reader_file = csv.reader(input_file)
ant_rows= len(list(reader_file))
input_file.close()

ma=[]

print("rader: ", ant_rows)


with open('plugg3.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        ma.append(row)


print ma[0],'\n',ma[0][1] #rad kolumn start 0....rad ...0...kolumn \n ny rad tror jag
#print ma

def column(matrix, i):
    return [row[i] for row in matrix]
def columnFloat(matrix, i):
    return [float(row[i]) for row in matrix]

datum=column(ma,0)
tid=columnFloat(ma,1)
print tid
print datum
print sum(tid)


