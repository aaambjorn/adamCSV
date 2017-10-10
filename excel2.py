import xlsxwriter as ex
import csv
#http://xlsxwriter.readthedocs.io/tutorial03.html
#matris som läses in i excel
ma=[]

with open('plugg3.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        ma.append(row)

workbook=ex.Workbook('a.xlsx')

ws1=workbook.add_worksheet()
row = 1
col = 0
for d,t,amne,kap in (ma):
    ws1.write(row, col, d)
    ws1.write(row, col + 1, t )
    ws1.write(row, col + 2,amne)
    ws1.write(row, col + 3,kap)
    row=row+1

workbook.close()
