class Product:
    def __init__(self,name,price):
        self.name=name
        if price >0:
            self._price =price
        else:
            raise ValueError(" - değer girmezssiniz")
        
    # def set_price(self,value):
    #     if value >0:
    #         self._price =value
    #     else:
    #         raise ValueError(" - fiyata -değer girmezssiniz")
    # def get_price(self):
    #     return self._price
    
    # yukardaı alan_ile ayzılıcna private olduğu anlamına gelcek c#daki gibi private kavramı yok bu yuzden bu onlemi böyle alyıoruz birde propertilerle bu kavramları farklı yapcaz.
    
    @property #atrubute gibi çalışıyor
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
         if value >=0:
            self._price =value
         else:
             raise ValueError(" - fiyata -değer girmezssiniz")
    
# p = Product("iphone12" ,523)
# p.price=-9000 # kafamıza göre aşşağıda böyle fiyatlar atılmamalı hata vermesi gerekir yukarda bu ksıımı hatanın önüne geçmiyor set pricelada bunu çözcez
# print(p.price) #9000
# print(p.get_price()) #523
# p.set_price(-8002) #ValueError:  - fiyata -değer girmezssiniz


# propertiy için hazırlanna
p = Product("iphone12" ,523)
print(p.price) #523
p.price=-5555
print(p.price)
