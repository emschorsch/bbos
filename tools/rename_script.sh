#!/bin/bash

mysqlconn="mysql -u bbos -pbbos -h localhost" #-S /usr/local/mysql/bin/mysql -h localhost"
olddb=gameday
newdb=gameday2

$mysqlconn -e "CREATE DATABASE $newdb"
params=$($mysqlconn -N -e "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='$olddb'")

for name in $params; do
      $mysqlconn -e "RENAME TABLE $olddb.$name to $newdb.$name";
done;

# $mysqlconn -e "DROP DATABASE $olddb"
