# The Tallyers: Saxon, Rona, and Marocs
#Software Development
#skeleton/stub :: SQLITE3 BASICS
#Oct 2026

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below, you will find a bit more scaffolding.
USAGE:
As you address each piece of functionality, 
 "talk shop" as you design it, 
 TEST it in sqlite3 shell, 
 then...
"""


def CSV_to_DB(name):
    with open (f"{name}.csv", "r") as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
    #this works because both CSV files being read have the same amount of field w/ same data types
        c.execute(f"CREATE TABLE {name} ({fields[0]} TEXT, {fields[1]} INTEGER, {fields[2]} INTEGER)")
        for row in reader:
            c.execute(f"INSERT INTO {name} VALUES ('{row[fields[0]]}', '{int(row[fields[1]])}', '{int(row[fields[2]])}')")
        
    
    
CSV_to_DB("students")
CSV_to_DB("courses")


    #tbl_name = ""
    #c.execute(f"CREATE TABLE {tble_name}")
    
# command = "CREATE TABLE students (name TEXT);"          # <-- insert tested stmt in quotes
# c.execute(command)    # run SQL statement
# c.execute("INSERT INTO students VALUES ('Saxon');") 

#==========================================================

db.commit() #save changes
db.close()  #close database