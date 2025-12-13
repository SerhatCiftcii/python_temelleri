# telefonlar = ["iPhone 13", "Samsung S22", "Xiaomi Mi 11", "Oppo Reno 6"]
# print(telefonlar)
# sonuc=telefonlar
# print(len(sonuc))   #listenin eleman sayısını verir =>4
# sonuc=telefonlar[1:3]  #1. indexten 3.indexe kadar alır 3.index dahil değil =>['Samsung S22', 'Xiaomi Mi 11']
# print(sonuc)

# telefonlar[0]="iPhone 14"
# sonuc=telefonlar  #0. indexe iPhone 14 atandı
# print(sonuc)

# if "Samsung S22" in telefonlar:
#     print("Evet var")
# else:
#     print("Yok")

# telefonlar.append("Huawei P50")  #liste sonuna eleman ekler
# sonuc=telefonlar + ["OnePlus 9"]  #listeye eleman ekleme sonuna ekler
# del telefonlar[-1]  
# sonuc=telefonlar  #son indexteki elemanı siler
# print(sonuc)

ogrenciA=["Yiğit",2010,[70,60,90]]
ogrenciB=["Sena",2012,[80,80,70]]
ogrenciC=["Ahmet",2009,[60,80,70]]
ogrenciler=[ogrenciA,ogrenciB,ogrenciC]

for ogrenci in ogrenciler:
   
    print([ogrenci[0],ogrenci[2],sum(ogrenci[2])/3])  #öğrenci ismi ve not ortalaması