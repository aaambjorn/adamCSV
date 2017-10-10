from pandas import read_csv


#df = pd.DataFrame([['hello', 'hello world'], ['abcd', 'defg']])
 
#print df

df1=read_csv("plugg3.csv", delimiter=';',header=None)

df3=df1.loc[df1[0] == "2017-10-09"]

print len(df3)
print sum(df3[1] )
