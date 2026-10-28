<your team heading here>

DISCOVERIES:
----------------------------------------------------
* Add a semicolon for SQL queries
* Can't cat the .db file created by the python file
* Need quotes around values when inserting into the table
* just .mode shows you the current mode
* .mode table example with students:
+-------------+------+----+
|    name     | age  | id |
+-------------+------+----+
| alison      | 23   | 10 |
| armin       | 22   | 3  |
| erykah      | 11   | 4  |
| tiesto      | 99   | 5  |
| TOKiMONSTA  | 33   | 7  |
| jphlip      | 27   | 8  |
| tINI        | 23   | 9  |
| kruder      | 66   | 1  |
| dorfmeister | 77   | 2  |
| bassnectar  | 13   | 6  |
| thluffy     | 1024 | 11 |
+-------------+------+----+
* .mode box example with students with age limit
sqlite> SELECT * FROM students WHERE age < 30;
┌────────────┬─────┬────┐
│    name    │ age │ id │
├────────────┼─────┼────┤
│ alison     │ 23  │ 10 │
│ armin      │ 22  │ 3  │
│ erykah     │ 11  │ 4  │
│ jphlip     │ 27  │ 8  │
│ tINI       │ 23  │ 9  │
│ bassnectar │ 13  │ 6  │
└────────────┴─────┴────┘

====================================================
where
where
QUESTIONS/COMMENTS/CONCERNS:
----------------------------------------------------
Q: a question
Q: another question
C: You can't keep running python file because the table already exists! We found it helpful to delate the db file or comment out the line that makes the table.
C: Do not write SQL commands lowercase because Rona says it looks ugly
====================================================
