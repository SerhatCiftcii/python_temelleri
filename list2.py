diller=["python","python","java","c++","c#"]
sonuc=diller
sonuc=type(diller) #list türünde olduğunu gösterir
sonuc=len(diller) #listenin eleman sayısını verir =>4
sonuc=diller[0:2]
sonuc=diller[2:]

diller[0]="html"
sonuc =diller #0. indexe html atandı
sonuc = len(diller) #listenin eleman sayısını verir =>4
sonuc= diller + ["javascript","ruby"] #listeye eleman ekleme sonuna ekler 


if "sad" in diller:
    print("evet var")
else:
    print("yok")
    
print(sonuc)

    
del diller[0] #2.indexteki elemanı siler
sonuc=diller
print(sonuc)
