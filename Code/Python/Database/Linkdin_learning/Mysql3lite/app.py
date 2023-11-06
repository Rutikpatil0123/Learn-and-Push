import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE MOVIES(Title TEXT, Director TEXT, Year INT)''')

# cursor.execute('''INSERT INTO movies VALUES('Zingat', 'Nagraj', 2019)''')

# famousFilms = [('Avengers', 'Nolan', 2019), ('Age of ultron','Nolan',2021), ('Avengers2', 'Nlaon', 2023)]

# cursor.executemany('Insert INTO Movies Values (?,?,?)', famousFilms)

cursor.execute("SELECT * FROM MOVIES")

release_year = (2023,)

cursor.execute("Select * from Movies Where year =?", release_year)

print(cursor.fetchall())

connection.commit()

connection.close()
