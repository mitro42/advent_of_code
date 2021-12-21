#!/bin/bash

YEAR=2021
DAY=21


if [ ! -f $YEAR/$DAY.txt ]; then
    touch $YEAR/$DAY.txt
    cp _template.py $YEAR/$DAY.py
fi