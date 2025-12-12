sayilar=[79,11,3,1,2,3,4,5]
harfler=['b','a','e','s','y']
sonuc=min(sayilar) #listenin en küçük elemanını verir

sonuc=min(harfler) #alfabetik olarak en küçük elemanı verir

sayilar.append(10) #liste sonuna 10 ekler

sayilar.insert(0,3) #0.indexe 3 ekler

sayilar.pop() #son elemanı siler

sayilar.remove(3) #ilk bulduğu 3 ü siler
sayilar.pop(0) #0. indexteki elemanı siler

print(sayilar)

# sıralama
sayilar.sort() #küçükten büyüğe sıralar

print("sort:",sayilar)
print("count:",sayilar.count(3)) #listede kaç tane 3 olduğunu verir
print("index:",sayilar.index(4)) #4 sayısının kaçıncı indexte olduğunu verir