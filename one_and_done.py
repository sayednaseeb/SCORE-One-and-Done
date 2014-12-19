import csv
import collections 
input_file = csv.DictReader(open("Input1.csv"))
input_file.fieldnames = "tblClients.Email", "tblSession.CounselingHours", "tblSession.CaseType"
deleted = []
circleA = []
circleB = []
uniqueEmails = []

def add_rows():
	for row in input_file:
		client_email = row["tblClients.Email"]
		hours = row["tblSession.CounselingHours"]
		caseType = row["tblSession.CaseType"]
		return "%s       %s       %s" % (client_email, hours, caseType)

def delete_noncases():
		if hours == "0" and caseType == "Close Out":
			deleted.append(row)
		return 	
	
def create_CircleA():
	for row in input_file:
		client_email = row["tblClients.Email"]
		hours = row["tblSession.CounselingHours"]
		caseType = row["tblSession.CaseType"]
		if caseType == "New Case" or caseType == "One-Time":
			circleA.append(row)
	return circleA.length

def create_CircleB():
	for row in input_file:
		client_email = row["tblClients.Email"]
		hours = row["tblSession.CounselingHours"]
		caseType = row["tblSession.CaseType"]
		if caseType == "Follow-On" or caseType == "Close Out":
			circleB.append(row)
			
