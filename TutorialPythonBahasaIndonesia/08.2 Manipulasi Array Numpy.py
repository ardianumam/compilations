import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])
print("nilai array:\n", array)

#reshaping array numpy
reshapedArray = np.reshape(array,(3,-1))
print("reshaped array:\n", reshapedArray)

#menghapus bagian dari array
deletedArray = np.delete(reshapedArray,slice(1,3),1)
print("deleted array:\n", deletedArray)

#menggabungkan array numpy
gabungan = np.concatenate((reshapedArray,deletedArray.reshape((1,3))),axis=0)
print("gabungan:\n", gabungan)

#sorting array numpy
sortedIndex = np.argsort(gabungan[:,0])
print("sorted index:\n", sortedIndex)
sortedArray = gabungan[sortedIndex]
print("hasil sortir:\n", sortedArray)

#coditional array
cond = sortedArray < 4
print("cond:\n", cond)
sortedArray[cond] = 0
print("conditioned array:\n", sortedArray)