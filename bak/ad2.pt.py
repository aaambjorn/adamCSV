#
#första gången
#
import csv
#d=raw_input("Datum: ")
#t=raw_input("tid: ")
#amne=raw_input("Amne: ")

#d=
#t=
#amne=


with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


