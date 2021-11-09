#!/usr/bin/python3

#Author: Github organization/team 1ems2005/school/2INF2/FakeLotto
#Version: DEV

import cgi, cgitb

cgitb.enable()

inputlist = cgi.FieldStorage()
s=[]


if inputlist["username"]:
    user = inputlist["username"].value

print("content-type: text/html")
print()
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")

print("<p>You are logged in as", user, "</p>")

print("</body>")
print("</html>")
