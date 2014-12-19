import cgitb
cgitb.enable(display=0, logdir="")

print "Content-Type: text/html"
print

print "<Title> CGI Script output</title>"
print "<h1>This is my first CGI sript</h1>"
print "Hello, world!"

form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
	print "<h1>ERROR</h1>"
	print "Please fill in the name and addr fields."
	return
	
print "<p>name: %s</p" % form["name"].value
print "<p>addr: %s</p>" % form["addr"].value
