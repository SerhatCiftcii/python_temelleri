ad= 'serhat'
print(type(ad))  #<class 'str'>
age=25
print(type(age))  #<class 'int'>

result = "benim adim " +ad+" yaşım"+ " " +str(age)
print(result[-1]) #son karakteri yazdırır
print(result[2])
print("karakter uzunluğu:",(len(result)) )  #karakter sayısını verir
print(result)  
print(result[0:4])
print(result[:4])
print(result[4:]) #-1 normalde en sonu alır ama bu kısımda en son : sağ taaraf bu şekilde boş olur en son için
print(result[-4:-1])
print(result[-1])
print(result[0:7:2]) # 0 dan 7 e kadar 2 şer atlayarak yazdırır