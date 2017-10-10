#
#'ab' attach binary with no blankrow, even 'a'works
#
import csv
''' 
print "Adams plugg cmd prompt"
d=raw_input("Datum: ")
t=raw_input("tid: ")
amne=raw_input("Amne: ")
sub=raw_input("Kapitel: ")
 '''
d="2017-10-09"
t="100"
amne="stat1"
sub="kap3"


with open('plugg3.csv', 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([d]+[t]+[amne]+[sub])
