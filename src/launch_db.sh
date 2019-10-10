#!/bin/bash

#TODO: first start database (Arch: sudo systemctl start mongodb)

#drop old database
mongo wyscout --eval "db.dropDatabase()"

#recursively list of all the names of collections in folder fold
fold="data"

colls=$(find $fold -type f -name "*.json")

#create all collections

for c in $colls
do
  y=${c%.json}
  #echo ${y##*/}
  #echo $c
  mongoimport -d wyscout -c ${y##*/} --file $c
done


