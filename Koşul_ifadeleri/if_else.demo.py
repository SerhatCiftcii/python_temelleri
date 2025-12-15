
"""
ad = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

kiloIndeks = kg / (hg ** 2)


if((kiloIndeks >= 0) and (kiloIndeks <=18.4)):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf: ")
elif((kiloIndeks > 18.4) and (kiloIndeks <=24.9)):
    print(f"{ad} kilo indeksin:{kiloIndeks}  ve kilo değerlendirmen normal: ")
elif((kiloIndeks > 24.9) and (kiloIndeks <=29.9)):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu: ")
elif((kiloIndeks >= 29.9) and (kiloIndeks <=34.9)):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez: ")
else:
    print("bilgileri doğru giriniz") 
"""

#bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesefade ne kadar 
# yakıt masrafı olduğunu hesaplanan uygulama.

"""benzinliFiyat = 6.69
dizelFiyat = 5.86

ortalamaYakitTuketimi = float(input("100 km'deki ortalama yakıt tüketimi (lt): "))
gidilecekYol = float(input("Gidilecek yol (km): "))
yakitTipi = input("Yakıt tipi (benzin/dizel): ").lower()

toplamYakitTuketimi=gidilecekYol * (ortalamaYakitTuketimi / 100)

if yakitTipi == "benzin":
    toplamYakitUcreti = toplamYakitTuketimi * benzinliFiyat
elif yakitTipi == "dizel":
    toplamYakitUcreti = toplamYakitTuketimi * dizelFiyat
else:
    print("Hatalı yakıt tipi girdiniz!")
    exit()

print("Toplam yakıt tüketimi:", toplamYakitTuketimi, "litre")
print("Toplam yakıt ücreti:", toplamYakitUcreti, "TL")
"""

