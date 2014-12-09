#!/usr/bin/python
# Daniel Harris, Gabe Issa, Ethan Lipkind
import cgi
import datetime
import cgitb
cgitb.enable()
import sqlite3
import os
import uuid
import Cookie

form = cgi.FieldStorage()

usr = form['usr_name'].value
comment = form['comment'].value
score = 0
if form.getvalue('score'):
   score = form.getvalue('score')

cookie_string = os.environ.get('HTTP_COOKIE')

if cookie_string:
	my_cookie = Cookie.SimpleCookie(cookie_string)
	saved_session_id = my_cookie['session_id'].value

	conn = sqlite3.connect('accounts.db')
	c = conn.cursor()

	try:
		c.execute('select * from users where sessionID=?', (saved_session_id,))
		all_results = c.fetchall()
		commenter = all_results[0][0]

		c.execute('select * from profiles where username=?', (usr,))
		all_results = c.fetchall()

		if len(all_results) > 0:

			c.execute('insert into comments values(?,?,?,?);', (usr,commenter,comment,score))
			conn.commit()

			print "Content-type: text/html"
			print "Location:        ../home.html"
        	print # don't forget newline
			print "Content-type: application/json"
			print
			print '{"viewer": commenter, "comment": comment, "score": score}'
        		
		else:

			print "Content-type: text/html"
        		print # don't forget newline
        		print "<html>"
        		print "<body>"
			print "<a href = '../home.html'>Try Again</a>"
        		print "</body>"
        		print "</html>"

	except sqlite3.IntegrityError:
		pass
