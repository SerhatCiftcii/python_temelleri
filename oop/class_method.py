class User:
   
    active_users =0
    @classmethod
    def display_active_users(cls):
       return f"{cls.active_users}tane aktif kullanıcı var"
    #ALLTAKİLER NORMAL#yapıcı metot(init) ve  #instancemethod(nesneye özel)
    @classmethod
    def from_string(cls,data_str):
        first,lastname,age=data_str.split(",")
        return cls(first,lastname,age)
    
    def __init__(self,first,lastname,age):
        print(self)
        self.first=first
        self.lastname=lastname
        self.age=age
        User.active_users +=1
        
    def full_name(self):
        return f"{self.first} {self.lastname}"
    
    def logout(self):
        User.active_users -=1
        return f"{self.full_name()} uygulamadan çıkış yaptı. Kalan kullanıcı sayısı: {User.active_users}"
print(User.display_active_users())
userA=User("ahmet ","yılmaz",33)
userB=User("sERHAT ","CDC",35)

print(User.active_users) # 2 tane instance tanımalnınca 2 oldu 



ali= User.from_string("ali,korkmaz,20")
print(ali.first)


