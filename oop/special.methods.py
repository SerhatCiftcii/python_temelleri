liste=[1,2,3]
print(len(liste))
s="hello"
class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik=baslik
        self.yonetmen=yonetmen
        self.sure=sure
    def __str__(self):
        return f"{self.baslik}, {self.yonetmen} tarafından yönetiliyor"
    def __repr__(self):
       return f"{self.baslik}, {self.yonetmen} tarafından yönetiliyor"
    def __len__(self):
        return self.sure
    def __del__(self):
        return print("film objesi silindi")
# print(len(f))

print(type(liste))
print(type(s))


f =Film("film","yonetmen",120)
print(str(liste))
print(str(f))
print(len(f))
del f