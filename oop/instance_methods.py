class Person:
    #yapıcı metot
    def __init__(self,name,surname,year):
        #attributes(object attrubutes, yada instance attributes)
        self.namee=name
        self.surname=surname
        self.year = year
        
     #instancemethod(nesneye özel)
    def intro(self):
        return f"benım adım {self.namee} ve soyadım {self.surname} doğum yılım :{self.year}"
    def calculate_age(self):
        import datetime
        hesapla=datetime.datetime.now().year - self.year
        return "yaşım:", hesapla
     
       
    
#obje veya instance
p1= Person("serhat","çiftçi",2000)
p2=Person("adım..","soyadımmsad",1985)
print(p1.intro()) #bize introyu heemen getircek
print(p2.intro())
p3=Person("serhat","cfc",1990)
print(p3.calculate_age())






