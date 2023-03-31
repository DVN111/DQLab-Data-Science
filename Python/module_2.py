#2. ======================Python Variables & Data Types===============================
# variable harus dimulai dengan (A-Z,a-z,_)
# variable gaboleh diawali angka(0-9) 
# bersifat case sensitive
# python otomatis tau tipe data yang ada pada literals

# 1. null
null = None

#2 boolean (bool)
booleanTrue = True
booleanFalse = False

#3 integer
nint = 1 

#4 float
nfloat = 1.0 

#5 string
tulisan ="ayam"

#====================================================================

# Sequence Type

# 1. Tipe data sequence List [x,y] kalo string tinggal ['x','y'] 
# tipe list memiliki data berurutan dari indeks ke-0
# Bersifat mutable(datanya bisa dirubah setelah dideklarasikan)
# Penerapannya : 
contoh_list = [1,'dua',3,4.0,5]
print(contoh_list[3])
contoh_list = [1,'dua',3,4.0,5]
contoh_list[3] = 'empat' # Ngubah nilai elemen ke4(index ke-3) jadi 'empat'
print(contoh_list[3])

#2 Tipe data sequence Tuple (x,y) kalo string tinggal ('x','y')
# tipe tuple memiliki data yangberurutan dari indeks ke-0
# Bersifat immutable(datanya TIDAK BISA dirubah setelah dideklarasikan)
# Penerapannya:
contoh_tuple = ("Januari","Februari","Maret","April")
print(contoh_tuple[0])
contoh_tuple = ("Januari","februari","Maret","April")
contoh_tuple[0] = 'Desember' #ini bakan error TypeError

#====================================================================

# Set Type 
# Set(set) {x,y} 
# mirip dengan sequence tapi 
# gak ngijinin ada nilai yang sama, misal : ada 2 cici dibawah, ini bakal kebaca 1 cici aja 
contoh_set = {'Dewi','Budi','Cici','Linda','Cici'}
print(contoh_set)

#Frozen set ({})
# sama aja cmn kalo frozen set gabisa diubah immutable setelah deklarasi
contoh_frozen_set = ({'Dewi','Budi','Cici','Linda','Cici'})
print(contoh_frozen_set)

#====================================================================

# Mapping Type (dictionary)
'''
Setiap elemen pada tipe data dictionary 
dideklarasikan dengan format:
"kunci" : "nilai"
'''

person = {'nama':'John Doe','pekerjaan':'Programmer'}
print(person['nama'])
print(person['pekerjaan'])

#====================================================================

# Tugas Praktek
# membuat variable bertipe dictionary (mirip api)
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000} 

# Membuat variable list untuk menyimpan variable dictionary sebelumnya
daftar_belanja = [sepatu, baju, celana]

#Tugas Praktek 2
#menghitung total harga jual dengan potongan harga beserta pajak sebesar 10% dari nilai jual.

# Data yang dinyatakan ke dalam dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
# Hitunglah harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"] 
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
# Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana
# Hitung harga kena pajak
total_pajak = total_harga * 0.1
# Cetak total_harga + total_pajak
print(total_harga + total_pajak)


