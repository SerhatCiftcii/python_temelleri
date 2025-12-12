

""" 
#girilen ürünleri kullanıcya göre verme 
ürünler={
    1:{"ad":"samsung s22","fiyat":15000},
    2:{"ad":"iphone 13","fiyat":20000},
    3:{"ad":"xiaomi mi 11","fiyat":12000}
}
ürün_id=int(input("ürün id giriniz:"))
print("seçilen ürün bilgileri:")
if ürün_id in ürünler:
    print(ürünler[ürün_id])
else:
    print("ürün bulunamadı"),
"""
    
    
    #1-3 ürün bilgisini id,ad,fiyat kullanıcıdan aldığınız bilgilerle dictiyonary tanımalyın
# ürn id bilgisini kullanıcıdan alıp ilgili ürünün bilgilerini ekrana yazdırın

"""# bu 1 kullanıcya 3 tane ürün girdiyor
ürünler={}
for i in range(3):
    id=int(input("ürün id giriniz:"))
    ad=input("ürün ad giriniz:")
    fiyat=float(input("ürün fiyat giriniz:"))
    ürünler[id]={"ad":ad,"fiyat":fiyat}
print("ürünleriniz:",ürünler)
 """
 
 #burdaise tek tek ürün bilgisi alınıyor
ürünler={}
id=int(input("ürün id giriniz:"))
ad=input("ürün ad giriniz:")
fiyat=float(input("ürün fiyat giriniz:"))
ürünler[id]={"ad":ad,
             "fiyat":fiyat}
print("ürünleriniz:",ürünler)
