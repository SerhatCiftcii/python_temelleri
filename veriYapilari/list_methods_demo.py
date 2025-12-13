isimler=["ali","veli","ayşe"]
yaslar=[27,18,26]
isimler.append("fatma") #liste sonuna fatma ekler
isimler.insert(0,"ahmet") #0.indexe ahmet ekler -1 sondan bire ekler, len methodu ile sona ekleyebilişrsin,
isimler.remove("veli") #veli yi siler
isimler.pop() #son elemanı siler index vermekte olur 

index= isimler.index("ayşe")

print("ayşe indeksi:",index)
#AYŞE KULLANICIS VAR MI DİYE BAKALIM
sonuc="ayşe" in isimler
print("ayşe var mı:",sonuc)
#if ile yapalım birde aynısını
if "ayşe" in isimler:
    print("evet ayşe var")

isimler.reverse() #listeyi ters çevirir
yaslar.sort() #küçükten büyüğe sıralar
print("yaslar sıralı:",yaslar)
print(isimler)

#kullanıcıdan 3 tane marka bilgisi tutanm listeyi saklayınız
markalar=[]
for i in range(3):
    marka=input("marka giriniz:")
    markalar.append(marka)
print("markalar listesi:",markalar)