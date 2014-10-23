#!/usr/bin/python

#Daniel Harris, Gabe Issa, Ethan Lipkind

import Cookie

import cgi

import os


# set the cookie to expire


#need to check the syntax of the expiration setting

cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
    my_cookie = Cookie.SimpleCookie(cookie_string)
    saved_session_id = my_cookie['session_id'].value

my_cookie['session_id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

#don't forget to print my cookie

print "Content-type: text/html"
print my_cookie
print "Location:        http://elipkind.rochestercs.org/"
print # don't forget newline
print "<html>"
print "<body>"
print "<h1>Logged Out</h1>"
print "<p><a href='../index.html'>Return To Main Page</a></p>"
print "</body>"
print "</html>"





