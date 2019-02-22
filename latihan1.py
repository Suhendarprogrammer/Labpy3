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
import random
jumlah = int(input('Masukkan nilai n : '))
print('*****Nilai Random*****')
for i in range (jumlah):
    i = random.uniform(0.0 , 0.5)
    print(i)
print('=======DONE=======')
