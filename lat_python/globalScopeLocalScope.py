# local scope variable

# nama = "Udin"

# def ubahNama(namaBaru):
#     namaBaruSkg = namaBaru
#     print("Nama saya menjadi",namaBaruSkg)

# ubahNama("supri")
# print("Nama saya menjadi",nama)


# global scope variable

nama2 = "Udin"

def ubahNama2(namaBaru2):
    global namaBaruSkg2
    namaBaruSkg2 = namaBaru2
    print("Nama saya menjadi",namaBaruSkg2)

ubahNama2("supri")
print("Nama saya menjadi",namaBaruSkg2)