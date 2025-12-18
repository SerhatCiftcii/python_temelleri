sayilar =[34,5,2,7,12]
sonuc=sum(sayilar)
sonuc=sum(sayilar,10)#üstünede 10 ekler

urunler = [
    {"title":"iphone" , "price":6000},
    {"title":"iphone 11" , "price":3000},
    {"title":"iphone12" , "price":4000}
]
sonuc=sum([urun["price"] for urun in urunler])
print(sonuc)
yuvarla= round(10.2)
yuvarla= round(10.5)#10
yuvarla= round(10.6)
yuvarla= round(1.424242,3)# ondalık kısmı kabetmemk için virgukden sonrakı basamığı alıyor.


print(yuvarla)
#rounded yuvarlama 