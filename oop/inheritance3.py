#child siniflarının genişletilmesi


# class Person:
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age
#         print(f"person giriş yaptı: {self.name}")
        
# class Student(Person): #kalıtım ile personu aldık.
#     pass
# class Teacher(Person):
#     pass
# p1=Person("serhat","çiftçi",25)
# print(p1.name, p1.surname,p1.age)


# s1=Student("aydın","yılmaz",35)
# print(s1.name,s1.surname,s1.age)
# # t1=Teacher()
    
    
     
    #***/////***/////////////***********
    #yukardaki işlem printle uzun uzun yazmak yerine bir
    # method tanımalyıp onun içinde self hepsini hazır yazdırcaz şimdi
    #********////////////************
    
 
class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("person giriş yaptı:") 
        
    def intro(self):
        return "kullanıcı bilgileri intro: ",self.name,self.surname,self.age
        
class Student(Person): #kalıtım ile personu aldık.
     def __init__(self,name,surname,age,number,): #yukarıdaki initin değerlerini burda set edicez
        # Person.__init__(self,name,surname,age)
        super().__init__(name,surname,age) #2. super methodu şle sınıf ismini yazmıyoruz selfide yazmıyoruz kendi yazıyor super sayesinde
        
        self.number=number
        print("student türetildi") #ekstra bi init yazarsan persondaki initi, ezmiş olursun dikkat bu paratreli init beklmıyor sonr aparametreyide ekle
                                    #parametreleri gönderdikten sonra set etmek lazım(bidaha set etmek zorunda kalmadık).bu sayede bi child sınıf student için şimdi işte ezmeden (ezedebilirr bazı durumlarda dikkat böyle yazcaz bu sınıfa özel)
                                    # artık ekstra özelliklere eklemeler yapılabilir.
     def study(self):
         print (f"{self.number} numaralı öğrenci ders çalışıyor")
            

class Teacher(Person):
    def __init__(self,name,surname,age,branch): 
        Person.__init__(self,name,surname,age) # super yazarak self paramtrresini göndermeden yapılabilir
        self.branch= branch
        print("student türetildi")
    def teach(self):
        print(f"{self.name} isimli öğretmen hangi dersi veriypr {self.branch}")
 

p1=Person("serhat","çiftçi",25)
# print(p1.name, p1.surname,p1.age)
print(p1.intro()) #artık uzun uzun yazmıyoruz özel method sayesinde


s1=Student("aydın","yılmaz",35,32)
print(s1.intro())
print(s1.number)
print(s1.study())
# print(s1.name,s1.surname,s1.age)
t1=Teacher("öğretmen","yılmaz","40 yaşında","branşı mat")

print(t1.intro())
print(t1.branch)
