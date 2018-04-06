jenisKelamin = 'pria'
umur = 22
asal = "Yogyakarta"

if (jenisKelamin=="pria"):
    print("semua peserta laki-laki harus kumpul di lapangan jam 10")
    if (umur>25):
        print("silahkan berbaris di sebelah kanan.")
    else:
        print("silahkan berbaris di sebelah kiri.")
elif (jenisKelamin=="wanita"):
    print("harap tetap tinggal di kelas.")
else:
    print("kamu belum mengisikan jenis kelamin di form perdaftaran.")
