mahasiswa1 =  {
        "Alex" : {
        "NIM"  : 210341110085,
        "Nama" : "Alexandra",
        "Kelas": "IF A",
        "Asal" : "France"
        },
        "Stv" : {
        "NIM"  : 210341110001,
        "Nama" : "Steve",
        "Kelas": "IF A",
        "Asal" : "Hungary"
            }

        }

"""
mahasiswa = {
        
        ["NIM" : 210341110085,
        "Nama" : "Alexandra",
        "Kelas": "IF A",
        "Asal" : "France"],

        ["NIM"  : 210341110001,
        "Nama" : "Steve",
        "Kelas": "IF A",
        "Asal" : "Hungary"],

        ["NIM"  : 210341110053,
        "Nama" : "Joshua",
        "Kelas": "IF B",
        "Asal" : "Germany"],
        
        }
"""


mahasiswa = {
        
        "NIM"  : [210341110085,210341110001,210341110053],
        "Nama" : ["Alexandra","Steve","Joshua"],
        "Kelas": ["IF A","IF A","IF B"],
        "Asal" : ["France","Hungary","Germany"]

              
        }


dataMhs = {
        "1900" : ["Rani","Surabaya","SMA 1",17]
        "1901" : []
        "1908" : []
        }


print(mahasiswa["NIM"][1])

print(mahasiswa1["Stv"]["Nama"])
