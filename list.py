msg="python  hoşgeldiniz".split()  #boşluklardan ayırır liste haline getir 0indexte python 1.indexe hoşgeldiniz gelir
print(msg[0])
print(msg[0][0]) #split liste halinde ilk p sonra da p nin 0.nı indexini alır


sayilar=[1,2,3,4,5]
print(sayilar[0])
print(sayilar[0]+sayilar[1])

isimler=["ali","veli","ayşe"]
print(type(isimler)) #list türünde olduğunu gösterir

listAali=["ali",17,True] #farklı türde veriler liste içinde olabilir
print(type(listAali))

ogrenciler=[["ali",17],[ "veli",18],[ "ayşe",16]]
print(ogrenciler[0]) #ilk öğrenciyi verir
print(ogrenciler[0][0]) #ilk öğrencinin ismini verir


# for isim in isimler:
#     print(isim)