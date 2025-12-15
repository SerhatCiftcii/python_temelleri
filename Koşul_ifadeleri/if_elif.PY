
# x=int(input("x değeri giriniz: "))
# y=int(input("y değeri giriniz: "))
# if(x>y):
#     print("x yden büyüktür")
# elif(x<y):
#     print("y daha büyüktür")
# elif(x==y):
#     print("x yeye eşittir")
# else:
#     print("yanlış değerler girdiniz")


# string değer girince a  gibi bi değer else ye hiç girmiyor çözüm olarak

try:
    x = int(input("x değeri giriniz: "))
    y = int(input("y değeri giriniz: "))

    if x > y:
        print("x y'den büyüktür")
    elif x < y:
        print("y daha büyüktür")
    else:
        print("x y'ye eşittir")

except ValueError:
    print("Lütfen sadece sayısal değer giriniz")

    