# sayilar=[]

# for i in range(10):
#     sayilar.append(i)
# print(sayilar) # çıktı [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#yukarda yapılan işlemlerin aynısını liste comprehensionla yapalım.


sayilar=[]

for i in range(10):
    sayilar.append(i)

sayilar=[i for i in range(10)] #çıktı [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sayilar=[i*i for i in range(10)] #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] sayıların karesi hızlıca

    
print(sayilar)


isimler=["asd","kaya","Mehmet"]

for i in isimler:
    print(i.upper())
    