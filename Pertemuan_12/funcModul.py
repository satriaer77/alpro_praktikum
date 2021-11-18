def tambahElemenList(no,jmlAngka) :
    data       = []
    for i in range(jmlAngka) :
        angka = int(input("==> Masukkan Data%d Angka ke- %d: "%(no,i+1)))
        data.append(angka)
    return data

