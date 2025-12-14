x=10
sonuc=5 < x <15
print(sonuc) #true


# sonuc1=(x>5)and (x<15)
# print("sonuc1:",sonuc1) #true

hak = 3

while hak > 0:
    devam = input("Devam etmek istiyor musunuz? (e/h): ")

    if devam == "e":
        hak -= 1
        print(f"Kalan hak: {hak}")
    else:
        print("Çıkış yapıldı")
        break

if hak == 0:
    print("Haklar bitti, yandınız!")
