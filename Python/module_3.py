
# Operators:
# Arithmetic operators
print(5 + 2) # penjumlahan
print(5 - 2) # Pemngurangan
print(5 * 2) # Perkalian
print(5 / 2) # Pembagian
print(3 % 2) # Modulus (Sisa Bagi)
print(3 ** 2) # Pangkat
print(3 // 2) # Pembagian dengan pembulatan ke bawah

# ===========================================================================================================================================================

# Assignment operators

# penambahan
x = 3
x += 2
print(x)

# pengurangan
x = 3
x -= 2
print(x)

# perkalian
x = 3
x *= 2
print(x)

# pembagian
x = 3
x /= 2
print(x)

# modulus
x = 3
x %= 2
print(x)

# pangkat
x = 3
x **= 2
print(x)

# pembagian bulat kebawah
x = 3
x //= 2
print(x)

# ===========================================================================================================================================================

# Comparison operators
# Operator comparison dapat digunakan untuk membandingkan dua buah nilai, berikut merupakan contoh-contoh operator komparasi.

# persamaan
print(33==33) # output: True dikarenakan benar 33 sama dengan 33
print(33==34) # output: False dikarenakan 34 tidak sama dengan 33

# pertidaksamaan
print(34!=33) # output: True dikarenakan benar bahwa 34 tidak sama dengan 33
print(33!=33) # output: False dikarenakan 33 sama dengan 33

# lebih besar
print(34>33) # output: True dikarenakan 34 lebih besar dari 33
print(33>34) # output False dikarenakan tidak benar 33 lebih besar dari 34

# lebih kecil
print(33<34) # output True dikarenakan benar 33 lebih kecil dari 34
print(34<33) # output: False dikarenakan tidak benar 34 lebih kecil dari 33

# lebih besar atau sama dengan 
print(34>=33) # output True dikarenakan 34 lebih besar dari 33
print(33>=34) # output False dikarenakan 33 tidak lebih besar dari 34 dan tidak sama dengan 34

# lebih kecil atau sama dengan
print(33<=34) # output True dikarenakan 33 lebih kecil dari 34
print(34<=33) # output False dikarenakan 34 tidak lebih kecil dari 33 dan tidak sama dengan 34

# ===========================================================================================================================================================

# Logical operators
# Operator logical digunakan untuk menggabungkan beberapa nilai kebenaran atas suatu statemen logika

# operator and
x = 5
print(x >= 1 and x <= 10) # mengembalikan nilai True
print(x >= 1 and x <= 4) # mengembalikan nilai False

# operator or
x = 3
print (x >= 1 or x <= 2) # mengembalikan nilai True dikarenakan statemen logika pertama terpenuhi
print (x >= 5 or x <= 0) # mengembalikan nilai False dikarenakan kedua statemen logika tidak terpenuhi (bernilai False)

# operator not
x = 7
print (not(x == 7)) # mengembalikan nilai False
print (not(x >= 10)) # mengembalikan nilai True

# ===========================================================================================================================================================

# Identity operators
# is
x = ["Ani", "Budi"]
y = ["Ani", "Budi"]
a = x # menyamakan objek rujukan
print(a is x) # nilai True dikarenakan a dan x merujuk ke objek yang sama
print(a is y) # nilai False dikarenakan a dan y tidak merujuk ke objek yang sama meskipun isi di dalam keduanya sama.

# is not
x = ["Ani", "Budi"]
y = ["Ani", "Budi"]
a = x
print(a is not x) # False dikarenakan a dan x merujuk ke objek yang sama
print(a is not y) # True dikarenakan a dan y tidak merujuk ke objek yang sama

# is dengan fungsi type()
x = 10
print(type(x) is int)

x /= 3
print(type(x) is int)

x /= 3
print(type(x) is float)

# ===========================================================================================================================================================

# Membership operators

# in : Menerima sebuah sequence/set dan objek, mengembalikan True ketika objek merupakan anggota dari sequence/set, dan False ketika bukan.
x = ["Ani", "Budi", "Cici"]
y = "Cici"
z = "Dodi"
print(y in x) # True
print(z in x) # False

# not in
x = ["Ani", "Budi", "Cici"]
y = "Cici"
z = "Dodi"
print(y not in x) # False
print(z not in x) # True

# ===========================================================================================================================================================

# Program menghitung diskon dan pajak pembelian
# menghitung harga yang harus dibayarkan menggunakan 
# barang senilai 150,000, dengan diskon 30% dan pajak 10%, 

# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga # baris pertama
harga_bayar *= total_harga # baris kedua
pajak_bayar = pajak * harga_bayar # baris ketiga
harga_bayar += pajak_bayar # baris ke-4
print("Kode awal - harga_bayar=", harga_bayar)

# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga #baris pertama 
harga_bayar += harga_bayar * pajak # baris kedua
print("Penyederhanaan kode - harga_bayar=", harga_bayar)

# ImplementasiNilai Prioritas Operator dalam Python
# ()
## **
### *,/,%
#### =,-
nilai = (3 + 2) ** 2 + (4 + 4) / 2 % 4
# berikut merupakan simulasi dari urutan pengerjaan yang dilakukan Python,
# 1. Python akan mengerjakan bagian di dalam kurung paling kiri
# nilai . 5 ** 2 + (4 + 4) ) / 2 % 4
# 2. Python akan mengerjakan bagian di dalam kurung yang tersisa
# nilai = 5 ** 2 + 8 / 2 % 4
# 3. Operator pangkat akan dikerjakan oleh Python
# nilai = 25 + 8 / 2 % 4
# 4. Python akan menjalankan operator pembagian dikarenakan prioritasnya
# lebih tinggi dibanding operator penambahan
# nilai = 25 + 4 % 4
# 5. Python akan mengerjakan operator modulus dikarenakan prioritasnya juga
# lebih tinggi dibanding operator penambahan
# nilai = 25 + 0
# 6. Python akan mengerjakan operator penambahan
# nilai = 25
print(nilai = 25)

# Tugas Praktek + penyederhanaan coding
sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1
print(total_harga)