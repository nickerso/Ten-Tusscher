import numpy as np
import pandas as pd

# loading data file
filename = input('Enter the file name : ')
DI = input('Enter the DI :')
data_file = pd.read_csv(filename)

print(data_file[0:3])

voltage = data_file['membrane | V (millivolt)']
print(voltage[0:3])
time = data_file['time | time (millisecond)']
print(time[0:3])

max_voltage_10 = np.max(voltage[9010:10010])
max_time_10 = np.argmax(voltage[9010:10010])
place = np.where(voltage[9010:10010]<=-86)

print('max_voltage_10 is', max_voltage_10)
print('max_time_10 is', max_time_10)
print(place[0][1])

max_voltage_s2 = np.max(voltage[9010+347+int(DI):])
max_time_s2 = np.argmax(voltage[9010+347+int(DI):])

print(max_voltage_s2)
print(max_time_s2)

APD_90 = (max_voltage_s2 - voltage[9010+347+int(DI)]) * 0.1 +voltage[9010+347+int(DI)]
print(APD_90)

place = np.where(voltage[9010+347+int(DI):]<=APD_90)
print(place)

APD90_duration = place[0][1]
print(APD90_duration)
