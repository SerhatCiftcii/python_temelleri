"""sayilar = [1,2,3,6,8,9]
#bir kriter var bu kriteri map ile kullanabiliriz
kareleri=[]
for sayi in sayilar:
    kareleri.append(sayi ** 2) [1, 4, 9, 36, 64, 81]
    
print(kareleri)

def kareAl(sayi):
    return sayi**2
sonuc=list(map(kareAl,sayilar))#[1, 4, 9, 36, 64, 81]
print(sonuc)"""

# lambda ile daha kısa sı var yukarının
"""sayilar = [1,2,3,6,8,9]
sonuc=list(map(lambda sayi:sayi **2 ,sayilar))

str_sayilar=["1","2","32","21"]
sonuc = list(map(int, str_sayilar))
print(sonuc)"""

isimler=["ahmettt","mehmet","burak"]
numberPage=[1,2,7,-2,-3,23]
numberPlus=list(map(abs,numberPage))
numberPlus=list(map(int,numberPage))
numberPlus=list(map(float,numberPage))
numberPlus=list(map(int,numberPage))
for i in isimler:
    print(i,len(i))
print(numberPlus)


#buda map yada lambda olmadan appendlada liste halınde yazdırız
# sayilar2=[1,2,7,-2,-3,23]
# for i in sayilar2:
#      sonuc=(i.__abs__())
#      print(sonuc)
