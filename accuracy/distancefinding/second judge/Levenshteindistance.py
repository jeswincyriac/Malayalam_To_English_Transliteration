import codecs
from Levenshtein import ratio

#dist =[101]
filereal = codecs.open("real.txt","r",encoding="utf-8")
fileout = codecs.open("output.txt","r",encoding="utf-8")
realword = filereal.readline()
outword = fileout.readline()
i=0
c=0
while realword != "":
    edit_dist = ratio(realword,outword)
    realword = filereal.readline()
    outword = fileout.readline()
    #dist[i] = edit_dist
    if edit_dist>.9:
        c=c+1

    i = i+1
print (c)
