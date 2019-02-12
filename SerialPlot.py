import serial
from tkinter import *
import matplotlib.figure as figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

com_port = "COM6"
baudrate = 9600
timeout = 0

xar = []
yar =[]

titrator = serial.Serial(com_port, baudrate, timeout=timeout)
def start_function():
    titrator.write(("START\r\n").encode())

def stop_function():
    titrator.write(("STOP\r\n").encode())

def animate(i, xar, yar):
    raw_data = titrator.readline()
    decoded_data = raw_data.decode("utf-8")
    print(decoded_data)
    if (len(decoded_data) > 1):
        line_array = decoded_data.split(";")
        adds_str_array = line_array[0].split(":")
        ph_str_array = line_array[1].split(":")
        ph_str_array_second = ph_str_array[1].split("\r\n")
        adds = float(adds_str_array[1])
        ph = float(ph_str_array_second[0])
        print(str(adds) + " - " + str(ph));
        xar.append(adds * 200)
        yar.append(ph)
        ax.clear()
        ax.plot(xar, yar)

root = Tk()
root.title("Titrator controller")
frame = Frame(root)
frame.configure(bg="white")
frame.pack(fill=BOTH, expand=1)

fig = figure.Figure(figsize=(2, 2))
fig.subplots_adjust(left=0.1, right=0.8)
ax = fig.add_subplot(1, 1, 1)



canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_plot = canvas.get_tk_widget()

start_button = Button(frame, text="START", command=start_function)
stop_button = Button(frame, text="STOP", command=stop_function)

canvas_plot.grid(row=0,
                 column=0,
                 rowspan=5,
                 columnspan=10,
                 sticky=W+E+N+S)

start_button.grid(row=5, column=2, columnspan=2)
stop_button.grid(row=5, column=3, columnspan=2)

for w in frame.winfo_children():
    w.grid(padx=5, pady=5)
for i in range(0, 5):
    frame.rowconfigure(i, weight=1)
for i in range(0, 5):
    frame.columnconfigure(i, weight=1)

fargs = (xar, yar)
ani = animation.FuncAnimation(fig, animate, fargs=fargs, interval=1000)

root.mainloop()