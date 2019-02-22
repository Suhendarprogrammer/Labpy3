#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     21/02/2019
# Copyright:   (c) Lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print ('program menghitung laba perusahaan dengan modal 100 juta')
print ('')
print ('note')
print ('bulan pertama dan ke dua = 0%')
print ('bulan ke 3 = 1%')
print ('bulan ke 5 = 5%')
print ('bulan ke 8 = 3%')
print ('')

a=100000000
for x in range (1,9):
    if (x>=1 and x<=2):
        b=a*0
        print ('laba bulan ke -',x,'  : ',b)
    if (x>=3 and x<=4):
        c=a*0.1
        print ('laba bulan ke -',x,'  :' ,c)
    if (x>=5 and x<=7):
        d=a*0.5
        print ('laba bulan ke -',x,'  :' ,d)
    if (x==8):
        e=a*0.2
        print ('laba bulan ke -',x,'  :' ,e)
total = b+b+c+c+d+d+d+e
print ('total laba yang didapat adalah ',total)
