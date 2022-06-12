import sqlite3
import turtle
import ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

score = 0

conn = sqlite3.connect('used.quizfile')
c = conn.cursor()
a = c.execute("SELECT * from questions")
t = turtle.Turtle()
t.pu()
t.speed(0)

for i in a:
    t.setpos(-200,50)
    t.write(i[1])
    t.setpos(-200,0)
    t.write("A) "+i[2])
    t.setpos(-200,-20)
    t.write("B) "+i[3])
    t.setpos(-200,-40)
    t.write("C) "+i[4])
    t.setpos(-200,-60)
    t.write("D) "+i[5])
    out = turtle.textinput("","A, B, C, D")
    if out == i[6]:
        Mbox("Info","Correct answear.",0)
        score = score + 1
    else:
        Mbox("Info","Wrong answear.",0)
    t.clear()

Mbox("End","Your score: "+str(score),0)