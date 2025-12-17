def selamlama(isim,mesaj="iyi günler"):
    print(f"{mesaj}... {isim}")
selamlama("serhat","günaydın")
selamlama("serhat")#burda mejsaı yazmassam hataya düşüyor bunun için aksini veermesekte çalışsın 
#istiyoruz bunu için varsayılan mesaj="iyigünler" yazsın diyerek defaultolarak bunu yazar

# def usAlma(taban, us):
#     print("taban: {}, üs: {}".format(taban, us))
#     return taban ** us

# sonucUs = usAlma(2, 3)
# print("sonuç:", sonucUs)


def toplam(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def islem(a,b,fn): #fn=toplam yaparsan defaulkt olarak toplar
    return fn(a,b)
sonuc=islem(1,3,toplam)
sonuc2=islem(4,1,cıkarma)
print("toplam:",sonuc,"cıkarma:",sonuc2)