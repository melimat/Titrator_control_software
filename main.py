import serial
import time
import csv

port = "COM6"
baudrate = 9600
log_csv_path = "log.csv"

titrator = serial.Serial(port, 9600, timeout=1)
log_file = open(log_csv_path, "a")
writer = csv.writer(log_file, dialect="excel")
writer.writerow(["Adds", "Ph"])
time.sleep(2)

while True:
    ser_bytes = titrator.readline()
    decoded_bytes = ser_bytes.decode('ascii')
    if (len(decoded_bytes) > 1):
        print(decoded_bytes)
        line_list = decoded_bytes.split(";")
        number_of_adds_list = line_list[0].split(" ")
        ph_str_list = line_list[1].split(" ")
        print("Parsed: Adds: " + number_of_adds_list[1] + " ; Ph: " + ph_str_list[2])
        adds = int(number_of_adds_list[1])
        ph = float(ph_str_list[2])
        writer.writerow([str(adds), str(ph)])



