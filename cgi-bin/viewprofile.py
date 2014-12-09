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
			print "<head>"
			print "<title>CollabRater</title>"
			print "<script src='http://code.jquery.com/jquery-1.11.1.min.js'></script>"

			print "<script>"
			print "$(document).ready(function(){"
			print "var profile = '" + usr + "';"
			print "document.getElementById('deleteme').value = (profile);"
			print "});"
			print "</script>"

			print "<script>"
			print "var user = '" + usr + "';"
			print "$(document).ready(function(){"
			print "$('#commentandscore').click(function(){"
			print "$.ajax("
			print "{"
			print "url: 'comment.py',"
			print "type: 'GET',"
			print "data: {"
			print "profile: user,"
			print "comment: $('#comment').val(),"
			print "score: $('input[name=score]:checked').val()"
			print "},"
			print "dataType: 'json',"
			print "success: function(dat){"
			print "console.dir(dat);"
			print "$('#comments').append('<h3>' + dat.viewer + '</h3><p>' + dat.comment + '</p><p>Rating: ' + dat.score + '</p>');"
			print "},"
			print "}"
			print ");"
			print "});"
			print "});"
			print "</script>"

			print "</head>"

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
			print "<br><label>Please rate this potential employee between 1 and 7:</label><br>"
			print "<label>1</label><input type='radio' name='score' value='1'>"
			print "<label>2</label><input type='radio' name='score' value='2'>"
			print "<label>3</label><input type='radio' name='score' value='3'>"
			print "<label>4</label><input type='radio' name='score' value='4'>"
			print "<label>5</label><input type='radio' name='score' value='5'>"
			print "<label>6</label><input type='radio' name='score' value='6'>"
			print "<label>7</label><input type='radio' name='score' value='7'>"
			print "<br><br><label>Enter your comment:</label><br><textarea rows='10' cols='50' type='text' name='comment' id='comment'></textarea><br>"
			print "<button id='commentandscore'>Submit</button>"
			print "<div id='comments'>"
			for index in range(len(all_comments)):
				print "<h3>" + all_comments[index][1] + "</h3><p>" + all_comments[index][2] + "</p><p>Rating: " + all_comments[index][3] + "</p>"
			print "</div>"
			print "<form method='post' id = 'deletecomments' action='deletecomments.py'>"
			print "<label>Delete all your comments on this page: </label><input name = 'usr_name' type='text' id='deleteme' style= 'display: none'/>"
			print "<input type='submit' value='Delete' id='deletecommentsbutton'/>"
			print "</form>"

			print "</body>"
			print "</html>"

		else:

			print "Content-type: text/html"
			print # don't forget newline
			print "<html>"
			print "<head><title>CollabRater</title></head>"
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

