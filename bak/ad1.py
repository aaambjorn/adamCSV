#
#'ab attachment with no blankrow even 'a'works
#
import csv
#d=raw_input("Datum: ")
#t=raw_input("tid: ")
#amne=raw_input("Amne: ")

#d=
#t=
#amne=


with open('eggs.csv', 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spak'] * 5 + ['Baked BBans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


