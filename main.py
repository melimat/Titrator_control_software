import serial
import time
import csv
import matplotlib.pyplot as plt


x_array = []
y_array = []
micropipette_amount = 200

port = "COM6"
baudrate = 9600
log_csv_path = "log.csv"

titrator = serial.Serial(port, baudrate, timeout=1)
log_file = open(log_csv_path, "w", newline="")
writer = csv.writer(log_file, dialect="excel")
writer.writerow(["Adds", "Ph"])
time.sleep(2)

while True:
    ser_bytes = titrator.readline()
    decoded_bytes = ser_bytes.decode('utf-8')
    print(ser_bytes)
    if (len(decoded_bytes) > 1):
        print(decoded_bytes)
        line_array = decoded_bytes.split(";")
        adds_str_array = line_array[0].split(":")
        ph_str_array = line_array[1].split(":")
        ph_str_array_second = ph_str_array[1].split("\r\n")
        print(adds_str_array[1])
        print(ph_str_array_second[0])
        adds = int(adds_str_array[1])
        ph = float(ph_str_array_second[0])
        x_array.append(adds*micropipette_amount)
        y_array.append(ph)
        print(adds)
        print(ph)
        writer.writerow([adds, ph])
        time.sleep(0.1)




