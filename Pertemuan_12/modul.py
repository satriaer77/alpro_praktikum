def buatList(jmlAngka) :
    data       = []
    for i in range(jmlAngka) :
        angka = int(input("==> Masukkan Data Angka ke- %d: "%(i+1)))
        data.append(angka)
    return data
