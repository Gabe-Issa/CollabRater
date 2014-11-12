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

name = form['user_name'].value
dob = form['user_name'].value
pn = form['user_name'].value
email = form['user_name'].value
sa = form['user_name'].value
an = form['user_name'].value
city = form['user_name'].value
state = form['user_name'].value
zc = form['user_name'].value
country = form['user_name'].value
hloe = form['user_name'].value
ce = form['user_name'].value
linked = form['user_name'].value

cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

	try:


		
		c.execute('select * from profiles where name=?;', (name,))

		if len(all_results) > 0:
			
			username = all_results[0][0]
			
			#delete existing and start over again
			
			c.execute('delete from profiles where username=?;',(username,))
			
			c.execute('insert into profiles values(?,?,?,?,?,?,?,?,?,?,?,?,?,?);', (username,name, dob,pn,email,sa,an,city,state,zc,country,hloe,ce,linked))
			conn.commit()
			
			

		else:
		
			c.execute('select * from users where sessionid=?;', (cookie_string,))
			all_results = c.fetchall()
		
			username = all_results[0][0]
		
			c.execute('insert into profiles values(?,?,?,?,?,?,?,?,?,?,?,?,?,?);', (username,name, dob,pn,email,sa,an,city,state,zc,country,hloe,ce,linked))
			conn.commit()

			

	except sqlite3.IntegrityError:
	    pass

