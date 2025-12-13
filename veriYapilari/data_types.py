int
#float
#string ,str
#bool

"""
x=10
y=10.5
toplam=x+y
print("Toplam:",toplam)
print(str(x)+str(y))  #1010.5   
"""


""" 
# kullancıya konsoldan veri girdirme
x=input("Bir sayı giriniz:")  #input fonksiyonu her zaman string veri tipi döner,eğer int olsun dersek2.yontem direkt
# x=int(input("Bir sayı giriniz:"))  #2.yöntem direkt int e çevirme
y=input("Bir sayı giriniz:")
print("Toplam StringDeğer:",x+y)  

print("Toplam:",int(x)+int(y))  # string birleştirme yapar  örn: 23 girilirse 2323 olur
"""

#True==1, False==0

""" 
    pi=3.14
    Daire çevrresi : 2pir
    alanı : pir^2
    yarı çapı verilen  bir dairenın çevresini ve alanını hesaplayınız.
"""
""" 
pi=3.14
x=float(input("yarı çapı giriniz"))
if x<0:
    print("Negatif değer giremezsiniz, yada sayı giriniz")
    exit()
else:
        print("Hesaplama yapılıyor...")
cevre=2*pi*x
alan=pi*(x**2)
print("Dairenin çevresi:",int(cevre)) 
print("Dairenin alanı:",alan)#burda float default olarak gelir.
"""

#bir aracın km cinsinden gittiği yol mil olarak yazdırma mil=km/1.609

km=float(input("Km cinsinden yolu giriniz:"))
mil =float(km) /1.609
mil=round(mil,2) #virgülden sonra 2 basamak göster
print("Gidilen mesafe mil cinsinden:",mil)



