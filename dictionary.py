# key-value    : tckimlik saklamak için kullanılabilir
#41 =>kocaeli : yada bu 2 değer gibivvsvs
#istanbul =>34

plakalar={
    "kocaeli" :41,
    "istanbul":34,
    "ankara"  :6
}
print(plakalar["kocaeli"])
print(plakalar.get("istanbul"))
plakalar["rize"]=53  #yeni key-value ekleme
print(plakalar) 

ogrenciler={
    100:{
        "yas":20,
        "ad":"ali",
        "soyad":"veli",
        "notlar":[70,60,80]
    },
    101:{
        "yas":22,
        "ad":"ayşe",
        "soyad":"fatma",
         }
}

sonuc=ogrenciler[100]
sonuc=ogrenciler[101]["ad"]
sonuc=ogrenciler.get(101).get("soyad") #fatma
sonuc=ogrenciler[100]["notlar"]
sonuc=ogrenciler[100]["notlar"][1]  #60
print(sonuc)