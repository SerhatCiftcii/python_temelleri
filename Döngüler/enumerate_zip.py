markalar=["opel","bmw","mercedes"]
# index=0
# for marka in markalar:
#     index=index+1
#     print(f"{index}-{marka}")
    
    #üstte yapılanın basit hali enumarete
"""#enumerate
obj1=enumerate(markalar)
print(type(obj1))
print(list(obj1))

for i in enumerate(markalar):
    print(i)
    
    for index,value in enumerate(markalar):
        print(index,value)"""
 
        
#zip 

liste1=[1,2,3,4,5]
liste2=["a","b","c","r","e","f"] #fin karşılığı olmd. için yazmaz

print(list(zip(liste1,liste2)))
