#kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehleiyet alabilme durumunu kontroletme

bilgiAl=int((input("yaşınızı giriniz: ")))
eğitim=input("eğitimi giriniz. lise/üni :").lower()
if(bilgiAl>=18 and (eğitim=="lise")or eğitim=="üniversite"):
    print("ehliyet alabilir")
elif(bilgiAl<18):
    print(f"{eğitim} ehliyet alamaz ")
else:
    print("lütfen doğru bilgiler giriniz")