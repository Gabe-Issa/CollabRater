#!/usr/bin/python
# Daniel Harris, Gabe Issa, Ethan Lipkind
import cgi
import datetime
import cgitb
cgitb.enable()
import sqlite3
import os
import uuid

form = cgi.FieldStorage()

name = form['name'].value
dob = form['dateofbirth'].value
pn = form['phonenumber'].value
email = form['email'].value
sa = form['streetaddress'].value
an = form['apartment'].value
city = form['city'].value
state = form['state'].value
zc = form['zipcode'].value
country = form['country'].value
hloe = form['education'].value
ce = form['employer'].value
linked = form['linkedin'].value

cookie_string = os.environ.get('HTTP_COOKIE')

if cookie_string:
	my_cookie = Cookie.SimpleCookie(cookie_string)
    saved_session_id = my_cookie['session_id'].value

	conn = sqlite3.connect('accounts.db')
	c = conn.cursor()

	try:
		
		c.execute('select * from users where sessionID=?;', (saved_session_id,))
		all_results = c.fetchall()
		usr = all_results[0][0]
		
		c.execute('select * from profiles where username=?;', (usr,))
		all_results = c.fetchall()

		if len(all_results) > 0:
			
			#delete existing and start over again
			
			c.execute('delete from profiles where username=?;',(usr,))
			
			c.execute('insert into profiles values(?,?,?,?,?,?,?,?,?,?,?,?,?,?);', (usr,name, dob,pn,email,sa,an,city,state,zc,country,hloe,ce,linked))
			conn.commit()
			
			

		else:
		
			c.execute('insert into profiles values(?,?,?,?,?,?,?,?,?,?,?,?,?,?);', (usr,name, dob,pn,email,sa,an,city,state,zc,country,hloe,ce,linked))
			conn.commit()

			

	except sqlite3.IntegrityError:
		pass

