# -*- coding: utf-8 -*-
"""
def NO():
    z = "print from NO"
    global var_1 
    var_1 = 0
    print z
    
    print "recall FO()"
    print
    print "recall BO()"
    
    
    return var_1, FO() ,BO()
def FO():
    z = "print from FO"
    global var_1
    a = 1+ var_1
    print z
    print a
    return a
def BO():
    z = "print from BO"
    a = 2
    print z
    return a
var_1 = 99  
NO()
#FO()
#BO()
"""
#(все размеры в указаны в мм.)
a = 380 #размер аппарата в глубину (от фронтальной панели к задней части устройства)
b = 320 #ширина аппарата (отлевого до правого края устройства)
c = 135 #высота устройства
d = 180 #высота коничекой колбы на 500 мл
cd = c+d#общая высота устроства с колбой
e = 45#высота лампы
f = 10#коэф запаса по всем сторонам, в мм

cube_width = b+f*2
cube_deep = a+f*2
cube_hight = c+d+e+f*2

print
print "\t \t Размеры установки равны:"
print "\t", "ширина: ", b, "\t", "глубина: ", a, "\t", "высота: ", c+d+e,"\n"
print "\tРазмеры получаемого габаритного куба с запасом равны:"
print "\t", "ширина: ", cube_width, "\t", "глубина: ", cube_deep, "\t", "высота: ", cube_hight,"\n"


"""

user_input_number = float(raw_input("enter number: "))
print user_input_number+10
def user_input_1():
    user_inp = float(raw_input("enter number: "))
"""
print "первая пластина", 2000-(400+15+15)-(340*2)-(400*2)
print "вторая пластина", 2000-(400+15+15)-(340*2)-(400*2)