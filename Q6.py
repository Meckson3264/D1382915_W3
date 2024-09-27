import math
a = int(input('輸⼊係數 a：'))
b = int(input('輸⼊係數 b：'))
c = int(input('輸⼊係數 c：'))
x1 = ((-b)+math.sqrt((b**2)-4*a*c))/2/a
x2 = ((-b)-math.sqrt((b**2)-4*a*c))/2/a

print('⽅程式的根為：x1 =',x1,', x2 =',x2)

