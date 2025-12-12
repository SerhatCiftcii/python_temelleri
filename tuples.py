_list=[1,2,3]
_tuple=(1,2,3)
_tuple2=(4,5,6)
print(type(_list))  #list türünde olduğunu gösterir
print(type(_tuple))  #tuple türünde olduğunu gösterir

print(_list[0])  #listenin 0.indexini verir
print(_tuple[0])  #tuple ın 0.indexini verir
# _list[0]=10  #listenin 0.indexine 10 atar
# print(_list)
# _tuple[0]=10  #hata verir çünkü tuple ler değiştirilemez
# print(_tuple)
print(_tuple2 + _tuple)  #liste ve tuple ı birleştirir liste + tuple olur
print(len(_list))  #listenin eleman sayısını verir
