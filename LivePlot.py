import threading
from tkinter import *
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

titrator = serial.Serial("COM6", 9600, timeout=0)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

xar = []
yar = []

def start_titration():
    titrator.write(("START\r\n").encode())

def stop_titration():
    titrator.write(("STOP\r\n").encode())

def gui():
    main_window = Tk()
    start_button = Button(master=main_window, text="START", command=start_titration)
    stop_button = Button(master=main_window, text="STOP", command=stop_titration)
    start_button.grid(row=0, column=0)
    stop_button.grid(row=0, column=1)
    main_window.mainloop()
t1 = threading.Thread(target=gui)


def animate(i, xar, yar):
    raw_data = titrator.readline()
    decoded_data = raw_data.decode("utf-8")
    print(decoded_data)
    if(len(decoded_data) > 1):
        line_array = decoded_data.split(";")
        adds_str_array = line_array[0].split(":")
        ph_str_array = line_array[1].split(":")
        ph_str_array_second = ph_str_array[1].split("\r\n")
        adds = float(adds_str_array[1])
        ph = float(ph_str_array_second[0])
        print(str(adds) + " - " + str(ph));
        xar.append(adds*200)
        yar.append(ph)
        ax.clear()
        ax.plot(xar, yar)

def animation():
    anim = animation.FuncAnimation(fig, animate, fargs=(xar, yar),
                               frames=100, interval=1000, blit=False)
    plt.show()
t2 = threading.Thread(target=animation)
t1.start()
t2.start()

