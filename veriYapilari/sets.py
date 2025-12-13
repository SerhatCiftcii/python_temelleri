#list =>indexlenebilir bir yapı 5. numarakı liste onemliyse ekleme silme olması gerekıyorsa
#tuple => değişmeyen elemanlar için daha performanslı ekleme silme güncelmme olmaz ama dikat et
# dictioanry =>key-value bilgisi saklıyorsak kullanırız
#set=> key bilgisi vermede dictioary gibi yazıyourz. sırası önemli değilse var olanı değiştirebiliriz unuınq kotrolu hızlı olablir

meyveler={"elma","kiraz","kavun","üzüm"}
sonuc=meyveler
# sonuc=meyveler[0] #setler indexlenemz ve sıralanamaz sort gibi sıralama olmuyor 
# for x in meyveler: =>forla döner ama
#     print(x)
meyveler.add("kiraz")
meyveler.update(["vişne","kavun"])
meyveler.remove("üzüm")
if "kirazz" in meyveler:
    print("var")
else:
    print("yok")
    
    meyveler.discard("karpuz") #birde fazla veriyi tek alma
    meyveler.pop()#indexleme olmadığı için silinene yazıyor ve hangisini siliceği bilinmiyor
sebzeler={"bezelye","kurufasulye"}
print(meyveler.union(sebzeler))

