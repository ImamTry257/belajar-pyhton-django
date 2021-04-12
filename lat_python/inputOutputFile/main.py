# input output file

# membuat file text
# w = write mode / mode menulis dan menghapus file lama, jika file tidak ada, maka akan dibuat file baru
# r = read mode only / hanya bisa baca
# a = appending mode / menambahkan data di akhir baris
# r+ = write and read mode

# write
# file = open("inputOutputFile/data.text","w")
# file.write("ini adalah text yang dibuat menggunakan python")
# file.write('\nini adalah baris kedua')
# file.write('\nini adalah baris ketiga')
# file.write('\nini adalah baris keempat')
# file.close()

# membaca file text
readFile = open("inputOutputFile/data.text","r")
# print(readFile.read()) #cara 1, read(10), 10 = jumlah karakter
# cara ke 2
# print(readFile.readline())
# print(readFile.readline())

appendingFile = open("inputOutputFile/data.text","a")
appendingFile.write("\nbaris dibuat dengan menggunakan mode append")
appendingFile.close()
