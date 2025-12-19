#comment isminde bir sınıf oluşturalım.
# comment sınıfı username , text, likes dislikes isminde özelliklier sahip olsun.
#5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class Comment:
    def __init__(self,username,text,likes=0,dislike=0):
        self.username=username
        self.text=text
        self.likes=likes
        self.dislikes=dislike

c1=Comment("sadık turan","güzel kurs")
c2=Comment("serhat turan","çok güzel kurs")
c3=Comment("asdas turan","idare eder kurs",50,10)
c4=Comment("sadık turan","süper bir kurs olmuş",100)

comments=[c1,c2,c3,c4]
for c in comments:
    print(f"{c.username}: {c.text}")
    print(f" likes: {c.likes} - dislekes: {c.dislikes}")
  

        