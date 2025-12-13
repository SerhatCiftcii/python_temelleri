opelObj={
    "marka":"Opel",
    "model":"Corsa",
    "yil":2025
}
sonuc=opelObj["marka"]
print(opelObj.get("yil"))
print(sonuc)

for x in opelObj:
    print(x) #=>şaun marka,mode,yil olarak sadece model bilgileri var valueler yok
    
for x in opelObj:
    print(opelObj[x])

    """kolay olan yontem 
    for x in opelObj.values():
        print(x)
    """
    """key ile value bilgilerini aynıu anda göremk istiyrouz
    for x,y in opelObj.items()
    print(x,y)
    """
#bu direkt renk olan modeli siler popitem sonu siler.
# opelObj["renk"]="kırmızı"
# print(opelObj)

# print(opelObj.popitem()) #son  siler
#araamk istedğimiz değer liste içinde var mı

# del opelObj["marka"]
# print(opelObj)

obj=opelObj #referans 2side aynı şeyi tutar aslında opelobj .copy dersek opelobj etkilemez.
obj["marka"]="mazda"
print(obj)
print(opelObj)

opelObj.update({
    
"marka":"updateedilen değer"
}
   )
print(opelObj)