
import xlsxwriter as ex

a="ddd"
workbook=ex.Workbook('.xlsx')

ws1=workbook.add_worksheet()
ws1.write('A2','a')
ws1.write(0,1,"s")
ws1.write(0,0,"QQ")
ws1.write(3,0,a)


workbook.close()




