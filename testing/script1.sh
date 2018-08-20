#!/bin/sh
sed  's/ /\n/g' tempm.txt > temp.txt
awk '{print($1"$")}' temp.txt > malayalam.txt
rm temp.txt
