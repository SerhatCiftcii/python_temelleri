
sayilar = [1,2,3,4,867,56,34]
sonuc=[]

for sayi in sayilar:
    if (sayi%2 ==0):
        sonuc.append(sayi)
        
print("sayilar listesinde sonuca 2 ye bölünenler listelendi",sonuc)


sonuc2= [sayi for sayi in sayilar if sayi%2==0] #kısa yol

print("comprehension ile yapılmış kısım:",sonuc2)
