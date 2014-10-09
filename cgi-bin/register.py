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

name = form['username'].value
age = form['password'].value

conn = sqlite3.connect('people.db')
c = conn.cursor()

try:
    c.execute('insert into users values(?,?);', (name, int(age)))
    conn.commit()
except sqlite3.IntegrityError:
    pass


print "Content-type: text/html"
# don't forget the extra newline!
print

print "<html>"
print "<head><title>My webpage</title></head>"
print "<body>"
print "<h1>Hello world</h1>"
print "<h2>The time is: " + str(datetime.datetime.now()) + "</h2>"
print "<h2>Your name is: " + name + "</h2>"
print "<h2>Your age is: " + age + "</h2>"
print "<pre>"

for row in c.execute('select * from users where age > 10 order by age'):
    print 'Name:', row[0], '| Age:', row[1]

print "</pre>"
print "</body>"
print "</html>"
