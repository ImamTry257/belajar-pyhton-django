data = ["ayam", "pisang", "pepaya", "sepatu", "baju"]

# for dt in data:
#     print(dt)
#     print(len(dt))


data2 = ["jago", "goreng", "lezat", "ukuran 42", "koko"]

for i,dat in enumerate(data):
    print(i,". ",dat)


for dat1,dat2 in zip(data,data2):
    print(dat1," :",dat2)