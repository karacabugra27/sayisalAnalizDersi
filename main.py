def faktoriyel(n):
    fakt = 1
    for i in range(1, n + 1):
        fakt *= i
    return fakt


def cos(x, sinir):  # x : cosinüsün değeri  sinir : kaçıncı dereceden istediğimiz
    index = 0  # terimlerin indexini tutar
    sonuc = 0  # sonuc

    while index <= sinir - 1:
        if index % 2 == 0:
            isaret = 1
        else:
            isaret = -1

        terim = isaret * x ** (index * 2) / faktoriyel(2 * index)
        sonuc += terim
        index += 1
    return sonuc


pi = 22 / 7

print("tek terim kesme hatasi : ", (0.80902 - cos(pi / 5, 2)))
print("-------------------------------------------------")
print("iki terim kesme hatasi : ", (0.80902 - cos(pi / 5, 4)))
