#!/bin/sh
sed  's/ /\n/g' input.txt > temp.txt
awk '{print($1"$")}' temp.txt > malayalam.txt
rm temp.txt
