# def multiply(a):
#     return a ** 2
# print(multiply(4))

# sonuc= (lambda a: a**2)(3) # return keywordu yazmadan lambdafonk ile yapıyoruz 4ün karesi

#2.hali
multiply = lambda a: a**2
sonuc = multiply(5)



toplama= lambda a,b,c: a+b+c
sonuc= toplama(1,4,7)


terCevir = lambda s: s[::-1]
sonuc=terCevir("serhat")

def myFunc(n):
    return lambda a: a*n
multiply2 = myFunc(2)
multiply3 = myFunc(3)
sonuc = multiply2(10) #10*2
print(sonuc)

