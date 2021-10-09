"""
Program Konversi Suhu
"""

celsius = float(input(" ==>  Masukkan Suhu celsius : ")) #Mengambil data dari inputan user dengan tipe data float
 
konversiFarenheit = (9/6 * celsius)+32 #Konversi Suhu Celsius ke Farenheit

print("""
        =------------------------------------------------------------=
        Jadi Suhu """,celsius,""" derajat C ---> F adalah """,konversiFarenheit,"""derajat F
        =------------------------------------------------------------=
        """)
