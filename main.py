import sys
from SerialPlot import serialPlot


def main():
    com_port = str(sys.argv[1])
    baudrate = int(sys.argv[2])
    timeout = int(sys.argv[3])
    log_path = sys.argv[4]
    mp_amount = int(sys.argv[5])
    serialPlot(com_port, baudrate, timeout, log_path, mp_amount)


if __name__ == '__main__':
    main()


