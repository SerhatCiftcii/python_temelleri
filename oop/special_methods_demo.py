class NewDict(dict):
    def __repr__(self):
        print("repr metoundan mesaj var")
        return super().__repr__()
    def __missing__(self,key):
        print("olmayan key bilgisi istenıyor")
        
    def __getitem__(self, key):
        print("bir elemanı çağırıyorsunuz")
        return super().__getitem__(key)
    def __setitem__(self, key, value):
        print("listeye eleman eklenıyor")
        return super().__setitem__(key, value)
        
data= NewDict({"First":"Serhat","Last":"Çiftçi"})

print(data["First"])

data["age"]

data["First"]="Çınar"
print(data)

