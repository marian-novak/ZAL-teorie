from math import isclose
from math import fabs
from math import sqrt

print("Trojuhelnik #1: ")
x1 = float(input("x1: ")) 
y1 = float(input("y1: "))
x2 = float(input("x2: ")) 
y2 = float(input("y2: "))
x3 = float(input("x3: ")) 
y3 = float(input("y3: "))

print("Trojuhelnik #2: ")
x12 = float(input("x1: ")) 
y12 = float(input("y1: "))
x22 = float(input("x2: ")) 
y22 = float(input("y2: "))
x32 = float(input("x3: ")) 
y32 = float(input("y3: "))

strana1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
strana2 = sqrt((x3 - x2)**2 + (y3 - y2)**2)
strana3 = sqrt((x1 - x3)**2 + (y1 - y3)**2)
strana12 = sqrt((x22 - x12)**2 + (y22 - y12)**2)
strana22 = sqrt((x32 - x22)**2 + (y32 - y22)**2)
strana32 = sqrt((x12 - x32)**2 + (y12 - y32)**2)

obvod1 = strana1 + strana2 + strana3
obvod2 = strana12 + strana22 + strana32

if (strana1 + strana2 <= strana3) or (strana2 + strana3 <= strana1) or (strana1 + strana3 <= strana1) or (strana12 + strana22 <= strana32) or (strana12 + strana32 <= strana22) or (strana22 + strana32 <= strana12):
    print("Body netvori trojuhelnik")

elif (isclose(strana1,strana12) or isclose(strana1,strana22) or isclose(strana1,strana32) and isclose(strana2,strana12) or isclose(strana2,strana22) or isclose(strana2,strana32) and isclose(strana3,strana12) or isclose(strana3,strana22) or isclose(strana3,strana32)) and isclose(obvod1,obvod2):
    print("Trojuhelniky jsou shodne")

elif isclose(obvod1,obvod2):
    print("Trojuhelniky nejsou shodne, ale maji stejny obvod")

elif obvod1 > obvod2:
    print("Trojuhelnik #1 ma vetsi obvod")

elif obvod2 > obvod1:
    print("Trojuhelnik #2 ma vetsi obvod")

