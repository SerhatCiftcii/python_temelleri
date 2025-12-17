# liste = [10,20,30]

# def toplam(sayilar):
#     sonuc=0
#     for i in sayilar:
#         sonuc+=i
#     return sonuc
# print(toplam(liste))

# bundan farklı olarak args isimli parametre var
def toplam(*args): #args aslıdnabi değişken a da olabilir adı
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc

print(toplam(10,20,30,40))