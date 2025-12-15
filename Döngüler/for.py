"""sayilar=[1,2,3,4,5,6]
isimler=["ali","mehmet","yağmur"]
isim="serhat"
# print(sayilar[0])
# print(sayilar[1])
# print(sayilar[2])
# print(sayilar[3])

# for i in sayilar:
#     print(i)
    
for i in sayilar:
    print("merhaba")

for a in isim:
    print(a)
"""

# tuple=[(1,2),(4,5),(6,7)]
# for x,y in tuple:
#     print(x,y)
    
_dict={"k1":1,
       "k2":2,
       "k3":3
       }
"""
for k in _dict:
     print(k) #key bilgisi
     print(_dict[k]) # value bilgisi 1,2,3
     
     for l in _dict.values(): # direkt value tipi döndürür key bilgiisi gelmez
         print(l)"""
for x in _dict.items():
     print(x)
