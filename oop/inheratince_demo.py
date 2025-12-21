#user
#moderator

class User:
    # class seviyeisinde özellik tanımalma
    active_users=0
    
    @classmethod
    def display_active_users(cls):
        return f"şaunda aktif {cls.active_users} user var."
        
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        User.active_users +=1
    def fullname(self):
        return f"ad ve soyad: {self.firstname + self.lastname}"

class Moderetor(User): # user sınıfını bazalıyor ama ekstra işler (özelik)yapıcak olan sınıf blog uygulaması için bir sııfı temsil edıyor ancak temelde user sınıfı baz aldıktan sonra blog ekleme silme vs işlerinide yapcak 
    active_moderators=0
    @classmethod
    def display_active_moderators(cls):
        return f"şaunda aktif {cls.active_moderators} Modertors user var."
    
    def __init__(self, firstname, lastname,community):
        super().__init__(firstname, lastname) # bu bilgiler ilgili user sınıfında init methoduna set edilicek communıtyde dışardan alıyoruz.
        self.community=community
        Moderetor.active_moderators +=1
    
    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan 1 post sildi"
        
u1=User("ali" ,"korkmaz")
m1=Moderetor("yağmur","korkmaz","yazılım alanı")
# isinstance bir obje bilgisini alır bu method hangi tipten türetilmiş sorusuna ceva veriri 

# print(isinstance(u1,User)) #true
# print(isinstance(u1,Moderetor)) #false userda türetiliyor çünkü
# print(isinstance(m1,Moderetor)) # true gelir
# print(u1.fullname()) 
# print(m1.fullname()) #moderatrda fullname sahip oldu

print(User.display_active_users()) #moderetordan gelen kısım userdan aldığı için modertorıda alır  2tane var der.
print(Moderetor.display_active_moderators())

print(m1.remove_post())
# sadece moderatordan almak istiyorsak  class seviyesinde bi değer tanımlarız.


    
    
