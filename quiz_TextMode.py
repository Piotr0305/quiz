import sqlite3

score = 0

conn = sqlite3.connect('used.quizfile')
c = conn.cursor()
a = c.execute("SELECT * from questions")

for i in a:
    print(i[1])
    print("A) "+i[2])
    print("B) "+i[3])
    print("C) "+i[4])
    print("D) "+i[5])
    out = input("A, B, C, D> ")
    if out == i[6]:
        print("Correct answear.")
        print("")
        score = score + 1
    else:
        print("Wrong ansewear.")
        print("")

print("Your score: "+str(score))
print("")
input("Press ENTER to exit...")