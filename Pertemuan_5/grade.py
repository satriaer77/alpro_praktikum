#Fungsi Cek Grade
def cekGrade(ass,md,fn) :
    total = ass+md+fn
    score = total/3

    print(""" 
        
    Nilai Assignment    = %d        | Nilai Rata-Rata (%d + %d + %d)/3 = %d / 3
    Nilai Mid Test      = %d        |                                  = %f
    Nilai Final Test    = %d
    --------------------------+
    Total               = %d 
            """%(ass,ass,md,fn,total,md,score,fn,total))

    if score <= 100 and score > 90:
        return "%f dengan grade S"%(score)
    elif score <= 90 and score > 85:
        return "%f dengan grade A"%(score)
    elif score <= 85 and score >75:
        return "%f dengan grade B"%(score)
    elif score <= 75 and score > 50:
        return "%f dengan grade C"%(score)
    elif score <= 50 and score > 0:
        return "%f dengan grade D"%(score)
    else :
        return "Salah karena lebih dari 100 atau kurang dari 0"
#End Fungsi Cek Grade

#-----------------------------------------------------------#


try :
    assignment  = int(input("==> Masukkan Nilai Assignment  : "))
    mid         = int(input("==> Masukkan Nilai Mid Test    : "))
    final       = int(input("==> Masukkan Nilai Final Test  : "))

except :
    print("Yang anda masukkan bukan angka")

else :
    print("""

    =========================================

    +---------------------------------------+
     Jadi skor anda %s 
    +---------------------------------------+
    """ % (cekGrade(assignment,mid,final)))
