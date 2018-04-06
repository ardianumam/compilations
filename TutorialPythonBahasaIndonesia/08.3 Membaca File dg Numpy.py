import numpy as np

#membaca file dengan numpy
path = 'file_angka.txt'
data1 = np.loadtxt(path, delimiter=',')
data2 = np.loadtxt(path, delimiter=',', skiprows=2)
print("data1:\n", data1)
print("data2:\n", data2)