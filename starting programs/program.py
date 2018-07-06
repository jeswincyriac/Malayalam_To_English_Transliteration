#  -*- coding: utf-8 -*-
import pandas
import unicodedata


#malwords = pandas.read_csv("villagesinkeralamalayalam1.txt")
#malarray=malwords.values.encode("utf-8")
#malencoded = malwords.encode("utf-8")
#print malarray
#b'\xe0\xb4\x95\xe0\xb4\x9f\xe0\xb5\x8d\xe0\xb4\x9f\xe0\xb4\xaa\xe0\xb5\x8d\xe0\xb4\xaa\xe0\xb4\xa8'.decode("utf-8")
filem = open ("villagesinkeralamalayalam1.txt","rb")
fileeng = open ("villagesinkeralaenglish1.txt","r")
out = open ("teest.txt","w")
line=filem.readline()
out.write(line)
#encodedline=line.encode("acsii")
print line
