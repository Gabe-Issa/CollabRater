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

	if len(all_results) > 0:

		c.execute('select * from users where sessionID=?', (saved_session_id,))
		viewer_info = c.fetchall()
		viewer = viewer_info[0][0]
		adminstatus = viewer_info[0][3]

		if adminstatus:

			c.execute('select * from comments where username=?', (usr,))
			all_comments = c.fetchall()

			print "Content-type: text/html"
			print # don't forget newline
			print "<html>"
			print "<body>"
			print "<a href = '../home.html'>Return to Main Page</a>"
			print "<h1>" + all_results[0][1] + "\'s profile: (Username " + usr + ")</h1>"
			print "<p>Date of Birth: " + all_results[0][2] + "</p>"
			print "<p>Phone Number: " + all_results[0][3] + "</p>"
			print "<p>E-mail: " + all_results[0][4] + "</p>"
			print "<p>Street Address: " + all_results[0][5] + "</p>"
			print "<p>Apartment: " + all_results[0][6] + "</p>"
			print "<p>City: " + all_results[0][7] + "</p>"
			print "<p>State: " + all_results[0][8] + "</p>"
			print "<p>Zipcode: " + all_results[0][9] + "</p>"
			print "<p>Country: " + all_results[0][10] + "</p>"
			print "<p>Education: " + all_results[0][11] + "</p>"
			print "<p>Employer: " + all_results[0][12] + "</p>"
			print "<p>LinkedIn: " + all_results[0][13] + "</p>"
			print "<br>"
			print "<label>Comment:</label> <input name='comment' id ='comment'/>"
			print "<button id ='comment'>Post</button>"			
			for index in range(len(all_comments)):
				print "<h3>" + all_comments[index][1] + "</h3><p>" + all_comments[index][2] + "</p>"
			print "</body>"
			print "</html>"

		else:
			
			print "Content-type: text/html"
			print # don't forget newline
			print "<html>"
			print "<body>"
			print "<h1>" + all_results[0][1] + "\'s profile: (Username " + usr + ")</h1>"
			print "<p>Date of Birth: " + all_results[0][2] + "</p>"
			print "<p>Phone Number: " + all_results[0][3] + "</p>"
			print "<p>E-mail: " + all_results[0][4] + "</p>"
			print "<p>Street Address: " + all_results[0][5] + "</p>"
			print "<p>Apartment: " + all_results[0][6] + "</p>"
			print "<p>City: " + all_results[0][7] + "</p>"
			print "<p>State: " + all_results[0][8] + "</p>"
			print "<p>Zipcode: " + all_results[0][9] + "</p>"
			print "<p>Country: " + all_results[0][10] + "</p>"
			print "<p>Education: " + all_results[0][11] + "</p>"
			print "<p>Employer: " + all_results[0][12] + "</p>"
			print "<p>LinkedIn: " + all_results[0][13] + "</p>"
			print "<br>"
			print "<a href = '../home.html'>Return to Main Page</a>"
			print "</body>"
			print "</html>"

	else:

		print "Content-type: text/html"
		print # don't forget newline
		print "<html>"
		print "<body>"
		print "<h1>Sorry, the username: " + usr + " could not be found in our profiles database </h1>"
		print "<a href = '../home.html'>Return to Main Page</a>"
		print "</body>"
		print "</html>"

except sqlite3.IntegrityError:

	pass
