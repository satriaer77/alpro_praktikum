kursRupiah = 14268.80 # Kurs 1 US Dollar ke Rupiah

dollar =float(input("===> Masukkan jumlah dollar : ")) #Mengambil inputan dollar dari user dengan tipe data float
konversi = kursRupiah*dollar

print("""
        =------------------------------------------------------------=
        Jadi Konversi mata uang $""",dollar,""" ke rupiah dengan kurs  Rp.""",kursRupiah,""" per $1 adalah Rp.""",konversi,"""
        =------------------------------------------------------------=
        """)
