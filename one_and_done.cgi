#!C:\Python25\Python.exe
#!/usr/bin/python
import csv
import cgi
form = cgi.FieldStorage()
reader =  form['filename']
print "Content-Type: text/html\n\n"
#reader = csv.reader(open('inputfile', 'r'))
#writer = csv.writer(open('Output.csv', 'w'))
data = []
emails = []
circleA = []
circleB = []

#remove non-sessions
for row in csv.reader(open('/tmp/' + reader, 'wb'), delimiter=','):
		if not(row[1] == '0' and row[2] == 'Close Out'):
			data.append(row)
			emails.append(row[0])

#calculate Circle A
for row in data:
	if row[2] == 'New Case' or row[2] == 'One-Time':
		circleA.append(row)
numA = len(circleA)
print "The length of circle A is: %d" % numA

#calculate Circle B
for row in data:
	if row[2] == 'Follow-On' or row[2] == 'Close Out':
			circleB.append(row[0])
numB = len(list(set(circleB)))		
print "The length of circle B is %d" % numB

#find total number of unique clients
uniqueClients = len(list(set(emails)))
print "The number of total unique clients is %d" % uniqueClients

#intersection 
intersection = numA + numB - uniqueClients
#print "The intersection is %d" % intersection

print numA - intersection

#one and done rate
rate = (float(numA - intersection)/float(numA + numB)) * 100
print "The one and done rate for this chapter is: {0:.2f}%".format(rate)
