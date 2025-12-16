# 1- çarpım tablosu hazırlayınız
"""for i in range(1,11):
    print("xxxxxxxxxxxx")
    for k in range(1,11):
        print("{}* {}= {}".format(i,k,i*k))
   """


#2 girilen bir sayının asal olup olmadığını kontrol ediniz

print("girdiğiniz sayı asal mı değilmi kontrol edelim")
sayi=int(input("bir sayı giriniz: "))

asalMi=True

if(sayi==1):
    asalMi=False
    
for i in range(2,sayi):
    if(sayi % i ==0):
        asalMi=False
        break
if asalMi:
    print("sayi asaldir")
else:
    print("asal değildir")