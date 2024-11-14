import tkinter as tk
from tkinter import font as tf
import tkinter.messagebox as mb
import random
import time

window = tk.Tk()
window.title("카드게임")

def flip(i):
    global score
    if stat[i] != 2:
        card[i].config(text=str(list[i]), bg="red")
        stat[i] = 1
        if flipped[0] == 100:
            flipped[0] = i
        else:
            flipped[1] = i
        if flipped[0] != 100 and flipped[1] != 100:
            if list[flipped[0]] == list[flipped[1]]:
                match(flipped[0])
                match(flipped[1])
                flipped[0] = 100
                flipped[1] = 100
                score += 100
                socre.config(text = f"Score: {score}")
                if stat.count(2) >= 16:
                    mb.showinfo("Clear", f"Your score is {score}")
                return
            else:
                hide(flipped[0])
                hide(flipped[1])
                flipped[0] = 100
                flipped[1] = 100
                score -= 25
                socre.config(text = f"Score: {score}")

def hide(i):
    global flipped
    if stat[i] != 2:
        card[i].after(1000, lambda: card[i].config(text= "?", bg = "blue"))
        stat[i] = 0

def match(i):
    global flipped
    card[i].after(1000, lambda: card[i].config(text = "", bg = "green", activebackground = "green"))
    stat[i] = 2

list = ["☆", "☆", "☆", "☆", "★", "★", "★", "★", "♡", "♡", "♡", "♡", "♥", "♥", "♥", "♥"]
random.shuffle(list)
card = [None] * 16
flipped = [100] * 2
stat = [0] * 16
score = 0

buttonsize = (3, 1)
font = tf.Font(size=60)

i = 0

while i < 16:
    card[i] = tk.Button(window, text = "?", width=buttonsize[0], height=buttonsize[1], command = lambda idx = i: flip(idx), bg = "blue", activebackground = "blue", font=font)
    card[i].grid(row = i // 4, column = i % 4)
    i += 1

socre = tk.Label(window, text = f"Score: {score}")
socre.grid(row = 5, column= 0)

window.mainloop()