yaslar=[5,12,18,24,45]

def yetiskinMi(x):
    if x<18:
        return False
    else:
        return True
for i in filter(yetiskinMi,yaslar):
    #foryerine
# sonuc= list(filter(yetiskinMi,yaslar))
    print("Yetişkin olanlar: ",i)
    

isimler=["çınar","yiğit","sena","ada","ali"]
sonuc= list(map(lambda n: n.upper(),isimler))
print(sonuc)

users=[
   {"username":"sadikturan",
     "tweets":["twwet1","tweet2"]   
    },
    {"username":"serhat",
     "tweets":[]   
    },
     {"username":"merhaba",
     "tweets":["twwet1"]   
    },
]
sonuc=list(filter(lambda u: len(u["tweets"])>0,users))
print(sonuc)