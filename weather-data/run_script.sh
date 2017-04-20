#!/bin/bash

cp seperate_factors_by_date.py $1/

for file in $1/*.txt
do
    python seperate_factors_by_date.py --file $file     
done

rm $1/seperate_factors_by_date.py