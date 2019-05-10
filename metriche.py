import csv

def accuracy(table1, table2):
	d1, d2 = create_dict(table1, table2)
	return calc_accuracy(d1, d2)

def create_dict(table1):
	d1 = {}
	d2 = {}
	reader1 = csv.reader(table1, 'rt')
	for row in reader:
		d1[ str(row[0])+str(row[1]) ] = str(row[2])
	reader2 = csv.reader(table2, 'rt')
	for row in reader:
		d2[ str(row[0])+str(row[1]) ] = str(row[2])
	return d1, d2

def calc_accuracy(d1, d2):
	esatti=0
	tot=0
	for k in d1.keys():
		if d1(k)==d2(k):
			esatti+=1
		tot+=1
	return (esatti/tot)*100