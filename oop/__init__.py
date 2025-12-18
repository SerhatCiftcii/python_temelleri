# hep aynı parametreler geliyor p1 ve p2 için şuanlık biz farklı paratereler le p1 ve p2 istiyoruz onun örneğide altta
"""class Product:
    def __init__(self):#self aslında p1 ve p2 temsil ediyor
        self.name="samsungs10"
        self.price=500
     #  return "product nesnesi" int return edemez str eder
        print("nesne oluşturuldu")
p1=Product()
p2=Product()
print(p1.name,p2.name," fiyat:",p1.price)"""


class Product:
    def __init__(self,_name,_price=123,isActive=True):#self aslında p1 ve p2 temsil ediyor
        self.name=_name
        self.price=_price
        self.isActive=isActive
     #  return "product nesnesi" int return edemez str eder
        print("nesne oluşturuldu")
p1=Product("p1 Serhatın name",52000,True)
p2=Product(_name="p2 fiyati eklenmemiş name",isActive=False)
print(p1.name,p1.price,p1.isActive)
print(p2.name,p2.price,p2.isActive)

