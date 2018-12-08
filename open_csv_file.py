import csv
r = csv.reader(open('C:/Users/tbi2013/Downloads/Grade.csv', 'rb'))
for row in r:
print row

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
_csv.Error: field larger than field limit (131072)
