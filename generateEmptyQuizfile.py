import sqlite3

conn = sqlite3.connect('empty.quizfile')
c = conn.cursor()
c.execute("CREATE TABLE questions (num INTEGER, contents TEXT, answA TEXT, answB TEXT, answC TEXT, answD TEXT, correct TEXT)")
conn.commit()
conn.close()
print("Generated empty.quizfile. Open with DB Browser for SQlite.")
input("Press ENTER to exit...")