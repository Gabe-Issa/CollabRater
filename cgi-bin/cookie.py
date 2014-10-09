!/usr/bin/python

# Philip Guo - CSC 210
# put in public_html/cgi-bin/ and set the proper execute permissions

import cgi, Cookie, os, sqlite3

# to facilitate debugging
import cgitb
cgitb.enable()

conn = sqlite3.connect('accounts.db')
c = conn.cursor()


cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
    my_cookie = Cookie.SimpleCookie(cookie_string)
    saved_session_id = my_cookie['session_id'].value

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
    my_name = form['my_name'].value
    
    # check whether my_name is in accounts.db
    c.execute('select * from users where name=?;', (my_name,))
    all_results = c.fetchall()
    if len(all_results) > 0:
        import uuid
        session_id = str(uuid.uuid4())

        c.execute('update users set sessionID=? where name=?',
                  (session_id, my_name))
        conn.commit()

        cook = Cookie.SimpleCookie()
        cook['session_id'] = session_id

        print "Content-type: text/html"
        print cook
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<h1>Hello, " + my_name +". You're now logged in.</h1>"
        print "<h2>session_id: " + session_id + "</h2>"
        print "</body>"
        print "</html>"
    else:
        print "Content-type: text/html"
        print # don't forget newline
        print "<html>"
        print "<body>"
        print "<h1>Sorry unregistered user</h1>"
        print "</body>"
        print "</html>"