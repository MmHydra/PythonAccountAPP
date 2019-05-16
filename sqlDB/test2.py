import sqlite3

result1 = "Shovchko"
result2 = "Second_Name"
conn = sqlite3.connect('sqlTest')

c = conn.cursor()

text_query = "INSERT INTO user (" + result2 + ") VALUES ('" + result1 + "')"
print(text_query)
c.execute(text_query)

conn.commit()

conn.close()
