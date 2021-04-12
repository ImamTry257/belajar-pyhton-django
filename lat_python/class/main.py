class mahasiswa():

    __nilai = 10 # variable private , tdk bisa diakses dari luar kelas

    def __init__(self, input_nama):
        self.nama = input_nama # variable public

    def belajar(self, info):
        print(self.nama,', ayo belajar',info)
    
    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,"tidak lulus")
        else:
            print(self.nama,"lulus")


mahasiswa = mahasiswa("musa")

print(mahasiswa.nama)

mahasiswa.nama = "ucup"
# print(mahasiswa.nama)

mahasiswa.belajar("python")
mahasiswa.uts(7 )
mahasiswa.check_status()
