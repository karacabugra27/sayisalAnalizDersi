def f(x):  # denklemimiz
    return x ** 3 + 4 * (x ** 2) - 10


def ikiye_bolme(a, b, hatapayi, maksiterasyon):  # a v b kökler , hata payi ve iterasyon sayısı
    iterasyon = 0

    while (b - a) / 2 > hatapayi and iterasyon < maksiterasyon - 1:
        c = (a + b) / 2
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterasyon += 1

    return (a + b) / 2


a = 1
b = 2

hatapayi = 10 ** -6
maksiterasyon = 4

# ikiye bölme
kok = ikiye_bolme(a, b, hatapayi, maksiterasyon)

print("*******************************")
print("Bulunan kök:", kok)
print("*******************************")
