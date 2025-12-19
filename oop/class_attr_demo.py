class Pet:
  
    def __init__(self,isim,cins):
        self.cinsler=["kedi", "köpek","kuş"]
        if cins not in self.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir." )
        self.isim=isim
        self.cins=cins
        print(f"{isim} {cins}")
pasa=Pet("pasa","kedi")
boncuk=Pet("boncuk","köpek")
# mavis=Pet("mavis","aslann") #aslan bir evcil hayvan değildir value eroorr

boncuk.cinsler.append("balık")

print(boncuk.cinsler)
print("pasa",pasa.cinsler)
boncuk.cinsler="aslan" # bu hata vermez python biiz zorlama appende eklersen eşler
print(boncuk.cinsler)