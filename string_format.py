""" 
ad= "Serhat"
soyad="çiftçi"
age=25
# print("BenımAdım"+ ad + " " + soyad + " " + str(age)) # int i str ye çevirmek gerekir agin başına ******str***** koymadan hata alıyorduk.
# print("BenımAdım{} {} {}".format(ad,soyad,age))# int ve string hata vermez bu kullanımda {} parantez içine değişkenleri sırayla yazarız
# print(f"BenımAdım {ad} {soyad} {age}") #f string kullanımı en kolay ve pratik yöntem
# number=200/700
# print("number {n:1.3}".format(n=number))

#yeni methof f string
print(f"benım adım {ad} soyadım {soyad} yaşım {age} ")
"""
website="www.sadikturan.com"
kursAdi="Python Kursu: Baştan Sona Python Programlama Rehberiniz"
#1-'kursAdi' karakter dizinde kaç karakter bulunuyor.
sonuc=len(website)
print(sonuc)

#2-'website' içinde kaç tane 'a' karakteri vardır.
sonuc=website.count("a")
print(sonuc)
#web site içindeki wwww karaterini alın sadece
sonuc =website[0:3]
print(sonuc)

#kursadi içinde ilk 15 ve son 15 karakteri alın
sonuc=kursAdi[:16]
print(sonuc)

#KURSADİ karakterlini terse çevirme
sonuc=kursAdi[::-1]
print(sonuc)
sonuc2="".join(reversed(kursAdi))
print("reversedsonuc2",sonuc2)
#'Hello World' ifadesini w harfini W ile değiştirin
sonuc3= "Hello world".replace("w","W")
print(sonuc3)
""" burda hata var kaldı çünkü str helloyu yontem2 olarak yazıyoruz ama [] bu işlemi str tipinde yapamıyoruz.sliceing ile yapıcaz onuda allta yapcam
yontem2='Hello world'
str[6]="W"
print("yontem2: ",str(yontem2))
""" 
yontem2='Hello world'
yontem2=yontem2[:6] + "W" + yontem2[7:]
print("yontem2: ",yontem2)


#8-abc ifadesini yan yana e defa yazdırın
ifade ="abc"*3
print(ifade)

