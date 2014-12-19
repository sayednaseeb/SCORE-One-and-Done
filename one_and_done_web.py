#!/usr/bin/python
import csv
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
reader =  form['filename1']
print "Content-Type: text/html\n\n"
reader = csv.reader(open('filename1', 'r'))
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
#print "The list after being vetted is: %d" % len(data)
#calculate Circle A
for row in data:
	if row[2] == 'New Case' or row[2] == 'One-Time':
		circleA.append(row)
numA = len(circleA)
#print "The length of circle A is: %d" % numA

#calculate Circle B
for row in data:
	if row[2] == 'Follow-On' or row[2] == 'Close Out':
			circleB.append(row[0])
numB = len(list(set(circleB)))		
#print "The length of circle B is %d" % numB

#find total number of unique clients
uniqueClients = len(list(set(emails))) - 1
#print "The number of total unique clients is %d" % uniqueClients

#intersection 
intersection = numA + numB - uniqueClients
#print "The intersection is %d" % intersection

oneDoneClient = numA - intersection

#one and done rate
rate = (float(oneDoneClient)/float((oneDoneClient) + numB)) * 100
#print "The one and done rate for this chapter is: {0:.2f}%".format(rate)

print "Content-type: text/html"
print "---------- REPORT ----------"
print "ONE AND DONE CLIENTS: %d \n(Circle A minus slashed area)" % (numA - intersection)
print "\nREPEAT BUSINESS CLIENTS: %d \n(Circle B)" % numB
print "\nTOTAL CLIENTS MENTORED IN PERIOD: %d" % (oneDoneClient + numB)
print "\nOne and Done % of All Clients: {0:.2f}%".format(rate)
print "\nRepeat Business % of All Clients: {0:.2f}%".format(100-rate)
print "----------------------------"
 
