# AND
a = True
b = False
c = a and b

# print(a,"and",b,"=",c)


# OR
a = True
b = False
c = a or b

# print(a,"or",b,"=",c)

# XOR, jika salah satu data true, maka akan true
a = True
b = False
c = a ^ b

# print(a,"xor",b,"=",c)

# masukkan nilai kurang dari 3 atau lebih dari 10
# inputUser = input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10 :")

# checkAngkaKurangDari3 = (int(inputUser) < 3)
# checkAngkaLebihDari10 = (int(inputUser) > 10) 

# print(checkAngkaKurangDari3 or checkAngkaLebihDari10)

# masukkan nilai lebih dari 3 dan kurang dari 10
inputUser = input("Masukkan angka yang bernilai lebih dari 3 atau kurang dari 10 :")

checkAngkaLebihDari3 = (int(inputUser) > 3)
checkAngkaKurangDari10 = (int(inputUser) < 10) 

print(checkAngkaLebihDari3 and checkAngkaKurangDari10)


