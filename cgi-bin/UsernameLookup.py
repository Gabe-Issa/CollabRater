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

usr = form['user_name'].value

cookie_string = os.environ.get('HTTP_COOKIE')

my_cookie = Cookie.SimpleCookie(cookie_string)
saved_session_id = my_cookie['session_id'].value


conn = sqlite3.connect('accounts.db')
c = conn.cursor()

try:

	c.execute('select * from profiles where username=?', (usr,))
	all_results = c.fetchall()

	if len(all_results) = 0:
		print "Content-type: application/json"
		print
		print '{"name": "Profile does not exist."}'