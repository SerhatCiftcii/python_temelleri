sayilar=[1,5,7,45,23,32]
harfler= ["a","v","h","s"]
isimler=["ahmeta","aslanasd","berennn"]
sonuc=min(sayilar)
sonuc=max(sayilar)#45
# print(sonuc)
sonuc2=min(harfler)
# print(sonuc2)

sonuc3=min(isimler)
# print(sonuc3)

sonuc4=min([len(isim) for isim in isimler])
# print(sonuc4)

sonuc=max(isimler, key=lambda n: len(n))
# print(sonuc)

urunler=[
    {"title":"iphone x","price":50000},
    {"title":"iphone 12","price":60000},
    {"title":"iphone 13","price":70000},
]
sonuc= min(urunler,key=lambda urun: urun["price"] ) #en düşük fiyatlandırma 
print(sonuc)