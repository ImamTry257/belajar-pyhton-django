def fungsi():
    print('ini adalah fungsi di dalam python')

fungsi()


# fungsi dengan input argument
def luasPersegi(p,l):
    Luas = p * l
    print("Luas Persegi dengan panjang =",p,"dan lebar =",l,"adalah",Luas,"cm2")

luasPersegi(5, 873)


# fungsi dengan return value
def sayHi(message):
    awalan = "Hi, "
    return awalan + message

show = sayHi("Imam")
print(show)
