#!/usr/bin/python3

#Author: Github organization/team 1ems2005/school/2INF2/FakeLotto
#Version: DEV

import cgi, cgitb
import random

cgitb.enable()

inputlist = cgi.FieldStorage()
s=[]

z1=[]
z2=[]
z3=[]

if inputlist["z11"]:
    z1.append(int(inputlist["z11"].value))
if inputlist["z12"]:
    z1.append(int(inputlist["z12"].value))
if inputlist["z13"]:
    z1.append(int(inputlist["z13"].value))
if inputlist["z14"]:
    z1.append(int(inputlist["z14"].value))
if inputlist["z15"]:
    z1.append(int(inputlist["z15"].value))
if inputlist["z16"]:
    z1.append(int(inputlist["z16"].value))
if inputlist["z21"]:
    z2.append(int(inputlist["z21"].value))
if inputlist["z22"]:
    z2.append(int(inputlist["z22"].value))
if inputlist["z23"]:
    z2.append(int(inputlist["z23"].value))
if inputlist["z24"]:
    z2.append(int(inputlist["z24"].value))
if inputlist["z25"]:
    z2.append(int(inputlist["z25"].value))
if inputlist["z26"]:
    z2.append(int(inputlist["z26"].value))
if inputlist["z31"]:
    z3.append(int(inputlist["z31"].value))
if inputlist["z32"]:
    z3.append(int(inputlist["z32"].value))
if inputlist["z33"]:
    z3.append(int(inputlist["z33"].value))
if inputlist["z34"]:
    z3.append(int(inputlist["z34"].value))
if inputlist["z35"]:
    z3.append(int(inputlist["z36"].value))
if inputlist["z36"]:
    z3.append(int(inputlist["z36"].value))

zuf=[]

while len(zuf) in range(0,6):
    tempzuf=random.randint(1,49)
    if tempzuf not in zuf:
        zuf.append(tempzuf)

treffer=0

for i in range(6):
    for j in range(6):
        if zuf[i] == z1[j]:
            treffer+=1
    for j in range(6):
        if zuf[i] == z2[j]:
            treffer+=1
    for j in range(6):
        if zuf[i] == z3[j]:
            treffer+=1

if treffer < 6:
    gewinn=treffer*3800
elif treffer >= 6:
    gewinn=18320517

print("content-type: text/html")
print()
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")

print("<p>Sie haben", treffer, "Treffer</p>")
print("<p>Ihr Gewinn liegt somit bei", gewinn, "€</p>")

print("</body>")
print("</html>")
