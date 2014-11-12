
#!/usr/bin/python

import cgi
import cgitb
import sqlite3
cgitb.enable()

# this python script will check the database to see whether the attempted username already exists.

form = cgi.FieldStorage()
stuff = form['stuff'].value
f = open('data.txt', 'a')
f.write(stuff)
f.write('\n')
f.close()

all_contents = open('data.txt').read()

print "Content-type: text/html"
# don't forget the extra newline!
print
print all_contents

# this is what the user typed in
#usrname = form['usrname'].value

#conn = sqlite3.connect('accounts.db')
#c = conn.cursor()

#try:
	#I want to pass username as a parameter from the input form on register.html
#	c.execute('select * from users where username=?', (usrname,))
#	all_results = c.fetchall()
	
#	if len(all_results) > 0:
#		print "Content-type: application/json"
#		print #extra line
#		#  username already exists, need to print out a red X to the div.
#		print '{"result": "Used Username"}'
#	else:
#		print "Content-type: application/json"
#		print #extra line
#		# username does not exist yet, need to print out a green checkmark.
#		print '{"result": "Accepted Username"}'
#except sqlite3.IntegrityError:
#	pass