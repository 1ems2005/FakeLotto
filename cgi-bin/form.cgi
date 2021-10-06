#!/bin/python3

#Author: Github organization/team 1ems2005/school/2INF2/FakeLotto
#Date: 2021/09/23
#Version: DEV21w38-

import cgi, cgitb

cgitb.enable()

inputlist = cgi.FieldStorage()
s=[]


if "user" in inputlist:
	user = inputlist["user"].value()

print("content-type: text/html")
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8' / Python 3.7></head>");
print("<body>")

print("<p>You are logged in as", user, "</p>")

print("</body>")
print("</html>")
