import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

titrator = serial.Serial("COM6", 9600, timeout=0)

fig = plt.figure()
#ax = plt.axes(xlim=(0,150), ylim=(0,14))
ax = fig.add_subplot(1,1,1)
#line, = ax.plot([], [], lw=2)

xar = []
yar = []


def init():
#    line.set_data([], [])
#    return line
    pass

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
        # line.set_data(xar, yar)
        #return line,
    #else:
        #return line,
        ax.clear()
        ax.plot(xar, yar)

anim = animation.FuncAnimation(fig, animate, fargs=(xar, yar),
                               frames=100, interval=1000, blit=False)
plt.show()