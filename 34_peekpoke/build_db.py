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
    data_list = []
    with open (f"{name}", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            clean_row = {}
            for col_name, value in row.items():
                if col_name is not None:
                    clean_row[col_name.strip()] = value.strip()
                    
            data_list.append(clean_row)
            
    return data_list
        
    #this works because both CSV files being read have the same amount of field w/ same data types
        #c.execute(f"CREATE TABLE {name} ({fields[0]} TEXT, {fields[1]} INTEGER, {fields[2]} INTEGER)")
        #for row in reader:
            #c.execute(f"INSERT INTO {name} VALUES ('{row[fields[0]]}', '{int(row[fields[1]])}', '{int(row[fields[2]])}')")

#==========================================================

command = "CREATE TABLE IF NOT EXISTS students(name TEXT, age INTEGER, id INTEGER)"          # <-- insert tested stmt in quotes
c.execute(command)    # run SQL statement
studentInfo = CSV_to_DB('students-beeg.csv')

for row in studentInfo:
    name = row['name']
    age = row['age']
    student_id = row['id']
    command = "INSERT INTO students (name,age,id) VALUES (?,?,?)"
    c.execute(command, (name, age, student_id))
    
command = "CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER)"          # <-- insert tested stmt in quotes
c.execute(command) 
courseInfo = CSV_to_DB('courses-beeg.csv')
for row in courseInfo:
    code = row['code']
    mark = row['mark']
    course_id = row['id']
    command = "INSERT INTO courses (code,mark,id) VALUES (?,?,?)"
    c.execute(command, (code,mark,course_id))
    
# print("STUDENTS TABLE")
# c.execute("SELECT * FROM students")
# students_data = c.fetchall()
# for row in students_data:
#     print(row)
# 
# print("COURSES TABLE")
# c.execute("SELECT * FROM courses")
# courses_data = c.fetchall()
# for row in courses_data:
#     print(row)
    
# print("Students over age 50")
# c.execute("SELECT * FROM students WHERE age > 50")
# courses_data = c.fetchall()
# for row in courses_data:
#     print(row)
    
# print("given ID example")
# ID = "0"
# print(ID)
# for row in courseInfo:
#     if row['id'] == ID:
#         print(row['code'] + ": " + row['mark'])
        
print("given name example")
name = "nikola"
print(name)
for row in studentInfo:
    if row['name'] == name:       
        ID = row['id']
for row in courseInfo:
    if row['id'] == ID:
        print(row['code'] + ": " + row['mark'])

command = "CREATE TABLE IF NOT EXISTS course_info(code primary key, mark TEXT, credits INTEGER, department TEXT)"
c.execute(command)    # run SQL statement
for row in courseInfo:
    code = row['code']
    mark = row['mark']
    course_id = row['id']
    command = "INSERT INTO course_info (code,mark,id) VALUES (?,?,?)"
    c.execute(command, (code,mark,course_id))
    

#==========================================================

db.commit() #save changes
db.close()  #close database