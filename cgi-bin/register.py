#!/usr/bin/python

# Daniel Harris, Gabe Issa, Ethan Lipkind - CSC 210
# put in public_html/cgi-bin/ and set the proper execute permissions

import cgi
import datetime

# to facilitate debugging
import cgitb
cgitb.enable()

import sqlite3

form = cgi.FieldStorage()

username = form['username'].value
password = form['password'].value


conn = sqlite3.connect('users.db')
c = conn.cursor()

try:
    c.execute('insert into users values(?,?);', (username, password, null)))
    conn.commit()
except sqlite3.IntegrityError:
    print "Content-type: text/html"
	# don't forget the extra newline!
	print
	print "<html>"
	print "<head><title>CollabRater</title></head>"
	print "<body>"
	print "<p>Username already exists!</p>
	print <a href="../form.html">Try a different username.</a>
	print "</body>"
	print "</html>"

print "Content-type: text/html"
# don't forget the extra newline!
print

print "<html>"
print "<head><title>CollabRater</title></head>"
print "<body>"
print "<h1>Welcome!</h1>"
print "<h2>Log-in time: " + str(datetime.datetime.now()) + "</h2>"
print "<p>Your name is: " + username + "</p>"
print "<p>Your password is: " + password + "</p>"

print "</body>"
print "</html>"
