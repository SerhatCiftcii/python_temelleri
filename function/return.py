# def toplam():
#     return (f"toplam: {10+20}")

# print(toplam())

#****************

# def toplam():
#     return 10+20
# sonuc=toplam()+50

# print(sonuc)

#*************

# def yasHesapla():
#     return 2025-2000
# sonuc1=yasHesapla()
# print(sonuc1)

#*************

# def simdi():
#     import datetime
#     return datetime.datetime.now().year
# def yasHesapla():
#     return simdi()-2000
# sonuc1=yasHesapla()
# print(sonuc1)

#************

def saat():
    import datetime
    return  datetime.datetime.now().hour
print(saat())

def selamla():
    if (saat()<12):
        return  "Günaydın"
    else:
        "iyi akşamlar"
print(selamla())        
