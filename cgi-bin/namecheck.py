~/public_html/cgi-bin/namecheck.py

#!/usr/bin/python

import cgi
import cgitb
import sqlite3
cgitb.enable()

# this python script will check the database to see whether the attempted username already exists.

form = cgi.FieldStorage()

username = form['username'].value

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

try:
	//I want to pass username as a parameter from the input form on register.html
	c.execute('select * from table where name = 'username')
	// if len>0, username already exists, need to print out a red X to the div.
	// if len<0, username does not exist, need to print out a green checkmark.
except sqlite3.IntegrityError:
	pass