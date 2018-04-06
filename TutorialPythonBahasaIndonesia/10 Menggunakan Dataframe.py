import pandas as pd

#membaca dari file dengan pandas
path = 'file_campuran.txt'
data = pd.read_csv(path, delimiter=',')
print("data:\n", data, ", shape:", data.shape)

#indexing pada dataframe
print("umur andi:\n", data.iloc[0,2])
print("nama-nama:\n", data['Nama'])

#menghapus data
deletedData = data.drop('No', axis=1)
print("deletedData:\n", deletedData)

#membuat dataframe sendiri
newDF = pd.DataFrame([['Amy',24,'Riau']], columns=('Nama','Umur','Asal'))
print("newDF:\n", newDF)

#menggabungkan dua dataframe
gabungan = pd.concat([deletedData,newDF], ignore_index=True)
print("gabungan:\n", gabungan)

#menghapus data terduplikat
noDup = gabungan.drop_duplicates()
print("data noDup:\n", noDup)

#normalisasi range [0,1] --> rumus = (nilai-min)/(max-min)
min = noDup['Umur'].min()
max = noDup['Umur'].max()
normalizedData = noDup.copy()
normalizedData['Umur'] = (noDup['Umur']-min)/(max-min)
print("hasil normalisasi:\n",normalizedData)