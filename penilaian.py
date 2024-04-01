print("-------------------GRADE CALCULATION------------------")
print("")
print("")
print("")
nama=(input("Silahkan masukkan nama = "))
nim=(input("Silahkan masukkan NIM  = "))
print("")
print("")

absen=int(input("Masukkan nilai absen = "))
uts=int(input("Masukkan nilai UTS   = "))
uas=int(input("Masukkan nilai UAS   = "))

nilai_batas=44
jumlah=absen+uts+uas
rata=jumlah/3

print("")
print("Jumlah nilai         =",jumlah)
print("Nilai rata rata      =",rata)
print("")
  
if rata >= 95 <= 100:
    print("Nilai anda adalah = A")
elif rata >= 90 <= 94:
    print("Nilai anda adalah = A-")
elif rata >= 85 <= 89:
    print("Nilai anda adalah = B+")    
elif rata >= 80 <= 84:    
    print("Nilai anda adalah = B")
elif rata >= 75 <= 79:
    print("Nilai anda adalah = B+")  
elif rata >= 70 <= 74:
    print("Nilai anda adalah = C+") 
elif rata >= 65 <= 69:
    print("Nilai anda adalah = C")   
elif rata >= 60 <= 64:
    print("Nilai anda adalah = C-")    
elif rata >= 55 <= 59:
    print("Nilai anda adalah = D+")  
elif rata >= 50 <= 54:
    print("Nilai anda adalah = D")  
elif rata >= 45 <= 49:
    print("Nilai anda adalah = D-") 
elif rata <= 44:
    print("Nilai anda adalah = E")

if rata >= nilai_batas:
    print("~SELAMAT ANDA LULUS MATA KULIAH INI~")
if rata <= nilai_batas:
    print("~MAAF ANDA TIDAK LULUS MATA KULIAH INI,")
    print("SILAHKAN COBA LAGI TAHUN DEPAN~")