sayilar= [0,5,8,32,23,35,26,53,98]
# for i in sayilar:
#     print(i)
    
#sayilar listesindeki hangi sayilar 5'in katıdır.
"""for sayi in sayilar:
    if(sayi % 5 ==0 ):
        print("5in katı olan sayılar: ",sayi)"""
        
#SAYİLAR listesindeki sayıların toplamı kaçtır?
"""toplam=0
for sayiTopla in sayilar:
    toplam=toplam+sayiTopla
print("sayiların toplamı: ",toplam)"""

#sayilar listesindeki çift sayıların karesini alınız.

"""for sayi in sayilar:
    if(sayi%2==0):
        print("sayının karesi",sayi,sayi**2)"""
        
#urunler lisetsindeki tüm ürünlerin 2.karaterlerini ekrana yazdırma.
# urunler=["elma","muz","kahve"]  
# for urun in urunler:
#     print("urunlerin2.karakteri: ",urun[1])  

#urunler listesinde kahveden kaç adet geçmiştir. 

"""urunler=["elma","muz","kahve","kahve"] 
for kacTane in urunler:
    if(kacTane in "kahve"):
        print("vasa yazdır",kacTane) # 2 adaet varsa yazdır çıktır şimdi indexe göre yapalım"""

urunler=["elma","muz","kahve","kahve","kahve"] 
count=0
for urun in urunler:
    index=urun.find("kahve")
    if(index>-1):
        count +=1
print(count)