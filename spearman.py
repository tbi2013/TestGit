import pandas as pd
import csv
# rs = pd.DataFrame.from_csv(r'C:/Users/tbi2013/Downloads/dump/followers.csv',encoding='utf-8')
rs = pd.read_csv(r'C:/Users/tbi2013/Downloads/dump/followers.csv',encoding='utf-8')

with open('C:/Users/tbi2013/Downloads/dump/followers.csv','r') as csvfile:

    reader = csv.reader(csvfile)
    rows = [row for row in reader]
csv_title = rows[0]
csv_title = csv_title[1:]
len_csv_title = len(csv_title)
for i in range(len_csv_title):
    for j in range(i+1,len_csv_title):
        print(str(csv_title[i]) + "_" + str(csv_title[j]) + " = " + str(rs[csv_title[i]].corr(rs[csv_title[j]])), end='\t')
    print()
