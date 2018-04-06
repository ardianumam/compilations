#number
a = 10
b = 3
c = a/b
print("hasil penjumlahannya adalah:", c)

#string
nama = 'Anton'
print("nama kamu adalah: ", nama)

#list
list1 = ['agus', 'anton', 'budi', 'tina']
print("list1 isi ketiga: ", list1[2])
print("isi list1 pertama sampai ketiga: ", list1[0:3])
print("panjang list1 adalah:", list1.__len__())
list1.append(100)
print("list1 baru: ", list1)
list1.remove('anton')
print("list1: ", list1)
del list1[0]
print("list1: ", list1)

#dictionary
dictionary1 = {'nama': 'anton', 'umur': '17', 'tinggi': 170}
print("nama: ", dictionary1['nama'], ", umur:", dictionary1['umur'])
dictionary1['nama']='Edward'
print("nama: ", dictionary1['nama'], ", umur:", dictionary1['umur'])
dictionary1['hobi']="badminton"
print("hobi: ", dictionary1['hobi'])
del dictionary1['tinggi']
#print("tinggi: ", dictionary1['tinggi'])
print("isi semua dict1: ", dictionary1)

#tuple
tuple1 = (1,2,3,4,5,6)
print("nilai tuple 1:", tuple1[0:3])

#array --> saya sarankan menggunakan package numpy


