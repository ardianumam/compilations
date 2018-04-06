class pasien:
    jumlah = 0
    def __init__(self,nama,berat,tinggi):
        self.nama = nama
        self.berat = berat
        self.tinggi = tinggi
        pasien.jumlah = pasien.jumlah + 1

    def hitungBMI(self):
        print("nama pasien:", self.nama)
        BMI = self.berat/(self.tinggi**2)
        print("BMI:", BMI)
        if (BMI<18.5):
            print("kekurangan berat badan.")
        elif (BMI>=18.5 and BMI<24.9):
            print("berat badan ideal.")
        elif (BMI>=24.9 and BMI<29.9):
            print("kelebihan berat badan level 1")
        else:
            print("obesitas.")
    def beratIdeal(self):
        bbIdeal = (self.tinggi*100 - 100) - (10/100 * (self.tinggi*100 - 100))
        print("berat badan ideal seharusnya:", bbIdeal)
        print("-----------------------------------")

pasien1 = pasien("Edward",60,1.70)#instantiation
pasien1.hitungBMI()
pasien1.beratIdeal()
pasien2 = pasien("Joko",90,1.65)
pasien2.hitungBMI()
pasien2.beratIdeal()
print("jumlah pasien yang sudah diinput: ", pasien.jumlah)