import numpy as np

#mendefinisikan array pada numpy
array1D = np.array([1,2,3,4,5])
print("nilai array1D:\n", array1D)
array2D = np.array([[1,2,3],[4,5,6]])
print("nilai array2D:\n", array2D)
matriks = np.matrix([[1,2,3],[4,5,6]])
print("isi dari matriks:\n", matriks)
arrayND = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]],[[5,5,5],[6,6,6]]])
print("nilai arrayND:\n", arrayND)
np1 = np.full((2,3),5)
print("nilai dari np1:\n",np1)

#melihat deskripsi dari data array: bentuk (size), min, max, std, var
print("ukuran dari array2D:", array2D.shape[1])
print("ukuran dari arrayND:", arrayND.shape)
print("nilai var dari array2D:", array2D.var())

#indexing dari array numpy
print("array2D:\n", array2D)
print("tes indexing array numpy:", array2D[1,:])

#mencoba operasi sederhana
matriks2 = np.matrix([[3,5,8],[1,0,6],[5,2,7]])
print("matriks:\n", matriks)
print("matriks2:\n", matriks2)
matriks3 = np.linalg.inv(matriks2)
print("hasil:\n", matriks3)
