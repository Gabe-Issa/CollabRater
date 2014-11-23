#!/usr/bin/python

# Daniel Harris, Ethan Lipkind, Gabe Issa - CSC 210

import cgi, Cookie, os, sqlite3

import cgitb
cgitb.enable()

form=cgi.FieldStorage()
# ajax "data" will be the the comment input field with id = "comment"

conn=sqlite3.connect('accounts.db')
c=conn.cursor()

cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
    my_cookie = Cookie.SimpleCookie(cookie_string)
    saved_session_id = my_cookie['session_id'].value

    c.execute('select * from users where sessionID=?', (saved_session_id,))
    all_results = c.fetchall()

	username=form['username'].value
	commenter= all_results[0][0]
	comment=form['comment'].value

	try:
		c.execute('insert into comments values(?, ?, ?);',(username, commenter, comment,))
		conn.commit()
	except sqlite3.IntegrityError:
		pass
else:
	print "Content-type: text/html"
    print # don't forget newline
	print "<html>"
	print "<body>"
	print "<p>Error, no cookie</p>"
	print "</body>"
	print "</html>"
