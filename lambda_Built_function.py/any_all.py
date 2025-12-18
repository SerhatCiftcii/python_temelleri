sonuc=all([True,False,False]) #hepsinin true olduğununda bize true döner burda flase old. için false döndü
sonuc2=all([True,True])
#and =>karşlığı aslında all or un karşlığı any
sonuc3=any((True,False,False))#herhangi bir eleman true ise true döner
print(sonuc)
print(sonuc2)
print(sonuc3)

sayilar = [-1, 0, 1, 2, 3, 4, 9, 4]

sonuc4 = [bool(i) for i in sayilar] #[True, False, True, True, True, True, True, True]
print(sonuc4)
    
        
sayilar = [-1, 0, 1, 2, 3, 4, 9, 4]

sonuc5 = all([bool(i) for i in sayilar]) #[True, False, True, True, True, True, True, True]
print(sonuc5) #allda hepsi true olması gerek false doner o yuzden
             
             
# kisiler=["ali","ahmet","serhat"] =>bu kodda al biyere koyulamıyor allta yazdığım gibi yaparsan 
# for kisi in kisiler:
#     print(all(kisi[0]=="a"))
kisiler=["ali","ahmet","serhat"]
sonuc=all([kisi[0]=="a" for kisi in kisiler]) #false

        
