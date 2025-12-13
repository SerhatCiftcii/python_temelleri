#valuetypes tip x hala 5 string,number(float int)
x=5
y=25
x=y
y=10

print(x,y)

#reference types (list) bu sefer a da b de üzüm oldu.2side ayn adrese gösteriyor olduğundan.
#adresi tutyoruz a ile b eşleştiğinde adresler birbriyle eşlşeip ikiside aynı adrese göstercek.list a ve list b üzerinde aynı bilgiler hedef alınıyor int ve stringde bu olmuyor.
#neden var cevabı ürün listemiz var.bu listeyi biyerden biyere kopylaamk istyoruz büyüük verilerde 2.kopyası oluşur performasn düşer.sadece bir kopyalaama işleminde adresi kopyalamak istiyruz.
#
a=["apple","banana"]
b=["apple","banana"]
a=b
b[0]="üzüm"
print(a,b)