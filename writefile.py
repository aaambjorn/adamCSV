#
#'ab attachment with no blankrow even 'a'works
#
import csv
#d=raw_input("Datum: ")
#t=raw_input("tid: ")
#amne=raw_input("Amne: ")

d='help'
#t=
#amne=


with open('eggs1.csv', 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow([d] * 5 + ['Baked BBans'])
    spamwriter.writerow([d]+[d]*5)
    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam']*2)
#spamwriter = csv.writer(csvfile, delimiter=';',
                            #quotechar='|', quoting=csv.QUOTE_MINIMAL)

