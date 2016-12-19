import numpy as np
import pandas as pd

# loading data file
filename = input('Enter the file name : ')
DI = input('Enter the DI :')
data_file = pd.read_csv(filename)


voltage = data_file['membrane | V (millivolt)']

time = data_file['environment | time (millisecond)']


max_voltage_10 = np.max(voltage[9010:10010])
max_time_10 = np.argmax(voltage[9010:10010])
place = np.where(voltage[9010:10010]<=-86)


max_voltage_s2 = np.max(voltage[9010+347+int(DI):])
max_time_s2 = np.argmax(voltage[9010+347+int(DI):])



APD_90 = (max_voltage_s2 - voltage[9010+347+int(DI)]) * 0.1 +voltage[9010+347+int(DI)]

place = np.where(voltage[9010+347+int(DI):]<=APD_90)


APD90_duration = place[0][1]
print(APD90_duration)
