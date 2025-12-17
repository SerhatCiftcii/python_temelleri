#kendisine gönderilen bir kelimeyi belirten kez ekranda gösteren fonk
"""def gonder(txt,kelime):
    return txt*kelime
sonuc= gonder("merhaba\n",5)
print(sonuc)
"""
 
#2 dikdörtgenın alan ve çevresini hesaplayam fonk yazınız
"""pi=3
def hesapla(uzunKenar,kısaKenar):
    alan=kısaKenar*uzunKenar
    cevre=2*(kısaKenar+uzunKenar)
    return(f"alan:{cevre} alan:{alan} ")
print(hesapla(5,7))"""
    

# yazı tura uygulamsını fonk kullanarak yapınız(random modülü)
"""import random
def yaziTuraAt():
    sayi= random.random()
    print(sayi)
    if sayi>0.5:
        return "tura"
    else:
        return "yazı"
print(yaziTuraAt())"""
    
#kednisine gönderilken 2 sayıyı arasındakı tüm asal sayılşarı bulan fonk yazınız.

def asalSayilariBulma(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if (sayi>1):
            for i in range(2,sayi):
                if(sayi % i == 0):
                    break
            else:
                print(sayi)
asalSayilariBulma(10,11)



# import datetime

# def emeklilige_ne_kadar_var(dogum_yili):
#     simdiki_yil = datetime.datetime.now().year
#     yas = simdiki_yil - dogum_yili

#     if yas >= 60:
#         return "Emekli oldunuz"
#     else:
#         return f"Emekliliğe {60 - yas} yıl var"

# dogum_yili = int(input("Doğum yılınızı giriniz: "))
# hesapla = emeklilige_ne_kadar_var(dogum_yili)
# print(hesapla)