print ("=========================================")
print ("      Aplikasi Penggajian Pegawai")
print ("=========================================")

nama = str(input("nama pegawai :"))
tingkatan = str(input("Jabatan :"))
awal = int(input("tahun Masuk :"))
akhir = int(input("Lama Kontrak Hingga :"))
gajipokok = int(input("gaji :"))
jam = int(input("jumlah jam kerja :"))
hari = int(input("jumlah hari kerja :"))
anak = int(input("jumlah anak yang ditanggung :"))
kerja = 5+jam 
gajiperbulan = (gajipokok/hari*jam)+(anak*50000)
gajipertahun = gajiperbulan*12
gajitotal = gajipertahun*(akhir-awal)

if tingkatan == "A":
	print("jabatan = CEO")
elif tingkatan == "B":
	print("Jabatan = Manager")
elif tingkatan == "C":
	print("Jabatan = Superviser")
elif tingkatan == "D":
	print("Jabatan = Karyawan")
elif tingkatan == "E":
	print("Jabatan = Cleaning Service")
else:
	print("tingkatan tidak tersedia")

if anak < 1:
  print ("Jomblo akut")
elif anak == 1:
  print ("Baru Menikah")
elif anak > 1:
  print("Sudah Menikah")
  
print ("\n\n=============================")
print ("\nNama pegawai					: ",nama)
print ("mulai kerja					: ",awal)
print ("akhir kerja					: ",akhir)
print ("jam kerja					:  9 s/d ",kerja)
print ("perbulan					: Rp. ",gajiperbulan)
print ("pertahun					: Rp. ",gajipertahun)
print ("total gaji diterima adalah			: Rp. ",gajitotal)
print ("")