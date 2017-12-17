#!/usr/bin/python
#coding:utf-8
import sys
import cgi
form = cgi.FieldStorage()

sys.stdout.write("Status: 200\r\nContent-type: text/html\r\n\r\n")

print "<html>"
print "<meta charset=\"utf-8\">"
print "<h2>"
print "we can access both get and post info from stdin by cgi module"
print "</h2>"
print "<h1>"


print "form[\"username\"]:"
print form["username"]
print "<br>"
print "form.getvalue('username'):"
print form.getvalue('username')

print "</h1>"
print "</html>"
