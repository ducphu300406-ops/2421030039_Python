def cong (a,b):
    return a + b
def tru (a,b):
    return
#vd.....
import mymath
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong 2 so la:", mymath.cong(x, y))
print("Hieu 2 so la:", mymath.tru(x, y))
print("Tich 2 so la:", mymath.nhan(x, y))
print("Thuong 2 so la:", mymath.chia(x, y))
#  tính diện tích ình tròn....
r = float(input("Nhap ban kinh: "))
print("Dien tich hinh tron:", mymath.dthtron(r))
#vd....
from mymath import cong,tru
x = int(input("nhap so thu nhat:"))
y = int(input("nhap so thu 2:"))
print("tong 2 so la:",cong(x,y))
print("Hieu 2 so la:",tru(x,y))
#b1....
def cong(a, b):
    return a + b
def tru(a, b):
    return a - b
def nhan(a, b):
    return a * b
def chia(a, b):
    return a / b
# Diện tích các hình....
def dthv(a):
    return a * a
def dthcn(a, b):
    return a * b
def cvhcn(a, b):
    return (a + b) * 2
def dthtron(r):
    return 3.14 * r * r
def dttamgiac(b, h):
    return 0.5 * b * h