msq ="  Python is fun"
sonuc=msq.upper()
sonuc=msq.lower()
sonuc=msq.title() #her kelimenin ilk harfi büyük olur
sonuc=msq.capitalize() #sadece ilk harf büyük olur
sonuc=msq.replace("Python","Java") #kelime değiştirme
sonuc=msq.split() #boşluklardan ayırır liste haline getir
sonuc =msq.islower() #Hepsi küçük mü diye bakar
sonuc =msq.strip() #başında ve sonundaki boşlukları siler
sonuc=msq.split() #boşluklardan ayırır liste haline getir => ['Python', 'is', 'fun']
sonuc=msq.find("is") #kaçıncı indexten başladığını verir
sonuc=msq.startswith("P") #P ile mi başlıyor
sonuc="-".join(msq) #her karakterin arasına - ekler
sonuc=msq.index("P") #kaçıncı indexten başladığını verir
sonuc=msq.replace(' ',"") #boşlukları siler
sonuc=msq.count()
print(sonuc)
