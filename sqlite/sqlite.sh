#!/bin/bash

sqlite3 # opening sqlite prompt
.open sample.db # opening the sample database or createsa opens if not exists.
.mode csv # import mode is set to csv
.import city.csv table1 # import csv file to sqllite db table with tablename
.tables # to view tables list
