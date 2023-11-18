def f(x):  # fonksiyon
    return 4 * (2.71828) ** (-0.5 * x) - x


def ft(x):  # fonksiyonun türevi
    return -2 * (2.71828) ** (-0.5 * x) - 1


def newtonraphson(x, iterasyon):
    for i in range(1, iterasyon + 1):
        bolme = f(x) / ft(x)
        x = x - bolme
        print(i, ". sonuc =", x)
        print("*******************************")


x0 = 2
itr = 4

newtonraphson(x0, itr)
