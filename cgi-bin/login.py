#!/usr/bin/python

# Daniel Harris, Gabe Issa, Ethan Lipkind - CSC 210

import cgi, Cookie, os, sqlite3

# to facilitate debugging
import cgitb
cgitb.enable()

conn = sqlite3.connect('users.db')
c = conn.cursor()


cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
    my_cookie = Cookie.SimpleCookie(cookie_string)
    saved_session_id = my_cookie['sessionID'].value

    c.execute('select * from users where sessionID=?', (saved_session_id,))
    all_results = c.fetchall()
    if len(all_results) > 0:
        saved_name = all_results[0][0]
        print "Content-type: text/html"
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<h1>Welcome back " + saved_name + "</h1>"
        print "</body>"
        print "</html>"
    else:
        print "Content-type: text/html"
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<h1>Error imposter wrong session_id</h1>"
        print "</body>"
        print "</html>"

else:
    form = cgi.FieldStorage()
    username = form['username'].value
    
    # check whether my_name is in accounts.db
    c.execute('select * from users where username=?;', (username))
    all_results = c.fetchall()
    if len(all_results) > 0:
        import uuid
        session_id = str(uuid.uuid4())

        c.execute('update users set sessionID=? where name=?',
                  (sessionID, username))
        conn.commit()

        cook = Cookie.SimpleCookie()
        cook['sessionID'] = sessionID

        print "Content-type: text/html"
        print cook
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<h1>Hello, " + username +". You're now logged in.</h1>"
        print "<h2>sessionID: " + sessionID + "</h2>"
        print "</body>"
        print "</html>"
    else:
        print "Content-type: text/html"
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<p>Sorry, incorrect username/password combination.  Please try again.</p>"
        print "<a href=\"form.html\">Or, register here.</a>"
        print "</body>"
        print "</html>"