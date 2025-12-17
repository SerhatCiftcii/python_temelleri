"""def selamla(isim):
    return "merhaba,"+ isim
yazdir= selamla("serhat")

def toplam(a,b):
    return a + b
sonuc=toplam(10,20)
sonuc=toplam(10,40)

print(sonuc)
print(yazdir)
"""

"""def yeniHesapla(dogumYili):
    return 2025-dogumYili
sonuc2=yeniHesapla(2000)
print(sonuc2)"""



import datetime

def emeklilige_ne_kadar_var(dogum_yili):
    simdiki_yil = datetime.datetime.now().year
    yas = simdiki_yil - dogum_yili

    if yas >= 60:
        return "Emekli oldunuz"
    else:
        return f"Emekliliğe {60 - yas} yıl var"

dogum_yili = int(input("Doğum yılınızı giriniz: "))
hesapla = emeklilige_ne_kadar_var(dogum_yili)
print(hesapla)
  
    