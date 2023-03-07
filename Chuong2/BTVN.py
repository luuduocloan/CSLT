# #BAI1
# HoTen=input("Nhap ho ten: ")
# print('Chao ban',HoTen,'!!!')

# #BAI2
# r=int(input("Nhap vao ban kinh cua duong tron: "))
# Pi=3.14
# DienTich=Pi*r**2
# ChuVi=2*r*Pi 
# print("Dien tich cua duong tron co ban kinh",r,"la =",round(DienTich,1))
# print("Chu vi cua duong tron co ban kinh",r,"la =",round(ChuVi,1))

# #BAI3
# import math
# print("Nhap hai canh ke cua tam giac vuong:")
# a=int(input())
# b=int(input())
# x=a**2+b**2
# c=math.sqrt(x)
# print('canh ke thu nhat la: ',a,',canh ke thu hai: ',b,',co canh huyen = ',round(c,2),sep="")

#BAI4
# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))
# d=float(input('d='))
# T=a+b+c+d
# TB=(a+b+c+d)/4
# print('Tong=',T,sep="")
# print('Trung binh cong=',round(TB,1),sep="")

#BAI5
# n=int(input('So tien ban dau: '))
# k=int(input('So thang gui: '))
# T=float(input('Lai suat/thang: '))
# print('Voi so tien ban dau ',n,', sau ',k,' thang gui, lai suat ',T,'/thang',sep="")

#BAI6
HT=input('Ho ten: ')
So_NC=int(input('So ngay cong: '))
DonGia_NC=int(input('Don gia ngay cong: '))
HSPC=float(input('He so phu cap: '))
TamUng=int(input('Tam ung: '))
TLuong=DonGia_NC*So_NC*HSPC
ThucLinh=TLuong-TamUng
print('Nhan vien ',HT,', Co tien Luong=',TLuong,', Tam ung=',TamUng,' va Thuc linh=',ThucLinh,sep="")
