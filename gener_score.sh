#!/bin/sh

# usage: sh gener_score.sh 

python proc_xls.py daily_score.xlsx > score.txt

python gen_score_day.py score.txt > o.txt

cp score.txt ./score_history/"score"`date -v-1d +-%y-%m-%d`".txt"

open o.txt 

