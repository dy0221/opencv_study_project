import serial
import numpy as np

tx_buffer = np.zeros(4)

tx_buffer[0] = 0xff
tx_buffer[1] = 0xff
x = 300
y = 600

check = x^y
print(type(tx_buffer[0]))

