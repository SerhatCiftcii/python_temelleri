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
    pass
class Teacher(Person):
    pass

 

p1=Person("serhat","çiftçi",25)
# print(p1.name, p1.surname,p1.age)
print(p1.intro()) #artık uzun uzun yazmıyoruz özel method sayesinde

s1=Student("aydın","yılmaz",35)
# print(s1.name,s1.surname,s1.age)
# t1=Teacher()