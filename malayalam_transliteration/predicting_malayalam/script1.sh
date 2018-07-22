#!/bin/sh
sed  's/ /\n/g' tempe.txt > temp.txt
awk '{print($1"$")}' temp.txt > english.txt
rm temp.txt
