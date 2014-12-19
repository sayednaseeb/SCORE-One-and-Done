import csv
import cgi
import os
rootdir = 'C:/Users/Heather/score'

for files in os.walk(rootdir):
    for file in files:
        filename = file
#		try:
#			filename = "chapter_" + str(i) + ".csv"
#		except IOError:
#			print "oops! That file doesn't exist."

reader = csv.reader(open('%s' % filename, 'r'))
writer = csv.writer(open('Output.txt', 'w'))
writer = open("newfile.txt", "a")
data = []
emails = []
circleA = []
circleB = []


writer.write("filename is: %s" % filename)

#remove non-sessions
for row in reader:
		if not(row[1] == '0' and row[2] == 'Close Out'):
			data.append(row)
			emails.append(row[0])

#calculate Circle A
for row in data:
	if row[2] == 'New Case' or row[2] == 'One-Time':
		circleA.append(row)
numA = len(circleA)
print "The length of circle A is: %d" % numA
writer.write("\nThe length of circle A is: %d\n" % numA)

#calculate Circle B
for row in data:
	if row[2] == 'Follow-On' or row[2] == 'Close Out':
			circleB.append(row[0])
numB = len(list(set(circleB)))		
print "The length of circle B is %d" % numB
writer.write("\nThe length of circle B is %d\n" % numB)

#find total number of unique clients
uniqueClients = len(list(set(emails)))
print "The number of total unique clients is %d" % uniqueClients
writer.write("\nThe number of total unique clients is %d\n" % uniqueClients)

#intersection 
intersection = numA + numB - uniqueClients
#print "The intersection is %d" % intersection

print numA - intersection

#one and done rate
rate = (float(numA - intersection)/float(numA + numB)) * 100
print "The one and done rate for this chapter is: {0:.2f}%".format(rate)
writer.write("\nThe one and done rate for this chapter is: {0:.2f}%\n".format(rate))
