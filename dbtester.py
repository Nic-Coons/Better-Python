import sqlite3

with sqlite3.connect('test_database.db') as connection:

    c = connection.cursor()

c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

firstName = 'Jean-Baptiste Zorg'
lastName = 'Human'
age = 122
personData = (firstName, lastName, age)
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO Roster VALUES(?, ?, ?)", personData)

firstName = 'Korben Dallas'
lastName = 'Meat Popsicle'
age = 100
personData = (firstName, lastName, age)
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO Roster VALUES(?, ?, ?)", personData)

firstName = 'Aknot'
lastName = 'Mangalore'
age = -5
personData = (firstName, lastName, age)
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO Roster VALUES(?, ?, ?)", personData)

c.execute ("""Update Roster SET Species=? WHERE IQ=?""", ('Human', 100))
