import tkinter as tk
import datetime as dt
import math


def create_clock_face(canva):
    canva.create_oval(10, 10, 290, 290, outline='black', fill='blue', width=0)
    canva.pack()
    canva.create_oval(148, 148, 150, 150, outline='black', fill='black', width=0)
    canva.pack()

    #create hour & minute

    for i in range(360):
        if i % 6 == 0 and i != 0 and i != 360 and i != 90 and i != 270:
            angle = math.radians(i)
            x1 = 150 + 125*math.cos(angle)
            y1 = 150 - 125*math.sin(angle)
            x2 = 150 + 130 * math.cos(angle)
            y2 = 150 - 130 * math.sin(angle)
            canva.create_line(x1, y1, x2, y2, fill='gray', width=3)
        else:
            angle = math.radians(30*i)
            x1 = 150 + 120 * math.cos(angle)
            y1 = 150 - 120 * math.sin(angle)
            x2 = 150 + 130 * math.cos(angle)
            y2 = 150 - 130 * math.sin(angle)
            canva.create_line(x1, y1, x2, y2, fill='white', width=3)


def create_hands(canva):
    second = dt.datetime.now().second
    sec_angle = -1*math.radians(second*6 - 90)
    x1 = 150
    y1 = 150

    x2 = 150 + 100*math.cos(sec_angle)
    y2 = 150 - 110*math.sin(sec_angle)

    canva.create_line(x1, y1, x2, y2, fill='yellow', width=1)

    hour = dt.datetime.now().hour
    minute = dt.datetime.now().minute
    hour_angle = -1*math.radians(hour*30 - 90 + (minute/2))

    x2 = 150 + 70*math.cos(hour_angle)
    y2 = 150 - 80*math.sin(hour_angle)
    canva.create_line(x1, y1, x2, y2, fill='green', width=3)

    min_angle = -1*math.radians(minute*6 - 90)
    x2 = 150 + 100*math.cos(min_angle)
    y2 = 150 + 110*math.sin(min_angle)

    canva.create_line(x1, y1, x2, y2, fill='crimson', width=3)


def main(canva):
    canva.delete('all')
    create_clock_face(canva)
    create_hands(canva)
    canva.after(1000, main, canva)


if __name__=='__main__':
    window = tk.Tk()
    window.title("comedur")
    canva = tk.Canvas(master=window, width=300, height=300, background='white', borderwidth=0)
    main(canva)
    tk.mainloop()