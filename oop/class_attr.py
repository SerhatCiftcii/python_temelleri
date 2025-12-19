class User:
    # class seviyesinde tanımlanmış olan  değer bu Userdan ulaşıyoruz. 
    active_users =0
    #ALLTAKİLER NORMAL#yapıcı metot(init) ve  #instancemethod(nesneye özel)
    def __init__(self,first,lastname,age):
        self.first=first
        self.lastname=lastname
        self.age=age
        User.active_users +=1
        
    def full_name(self):
        return f"{self.first} {self.lastname}"
    
    def logout(self):
        User.active_users -=1
        return f"{self.full_name()} uygulamadan çıkış yaptı. Kalan kullanıcı sayısı: {User.active_users}"
print(User.active_users) #0 dı
userA=User("ahmet ","yılmaz",33)
userB=User("sERHAT ","CDC",35)
print(userA.full_name)
print(User.active_users) # 2 tane instance tanımalnınca 2 oldu 

print(userA.logout())
print(User.active_users)

# print(userA.full_name())
# print(userB.full_name())


