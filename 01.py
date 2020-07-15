# Kelas tanggal 29/06/2020

# nama = '9'
# print(int(nama)+9)

# shortcut ctrl + /
# untuk membuat coding menjadi comment


#No. 1
# x = 4
# y = 3
# z = 2
# w = ((x + y * z)/(x * y))**z
# print(w)


#No. 2
# x = int(input('Silahkan masukkan angka berapapun : '))
# print('Kuadrat dari',x,'adalah',x**2 )

# print(type(x))

# a = 485
# tahun = 0
# bulan = 0
# while a >= 360 :
#     tahun += 1;
#     a -= 360;
#     if a == 0 :
#         break;

# while a >= 30 :
#     bulan += 1;
#     a -= 30;
#     if a == 0 :
#         break;

# print(a, ' hari,', bulan, ' bulan,', tahun, ' tahun')


#No. 3
# b = int(input('Masukkan jumlah hari : '))
# tahun = b // 360
# b %= 360
# bulan = b // 30
# b %= 30
# minggu = b // 7
# b %=7 

# print(b, 'hari,', minggu, 'minggu', bulan, 'bulan,', tahun, 'tahun')

# nama = input()
# print(nama.count('a'))


# No. 4
# ab = 49
# a_b = 0.4
# tahun = 2

# Andi = (ab * a_b) / (1 + a_b) 
# Budi = ab - Andi
# Andi += 2
# Budi += 2
# print('Andi :', round(Andi))
# print('Budi :', round(Budi))

# No. 5
# x = input('Kata : ').lower()
# y = input('huruh/kata yang igin dicari : ').lower()

# x = x.split(y)
# print(len(x)-1)

#No. 6
# ab = int(input('Jarak : '))
# A = int(input('Kecepatan benda A : '))
# B = int(input('Kecepatan benda B : '))
# C = int(input('Jam berangkat : '))
# E = int(input('Menit berangkat : '))
# C += (ab / (A + B))
# E += round(C % 1,1)*60
# C += E//60
# E %= 60
# E = int(E)

# print('\njam '+ str(round(C)) + ' lewat ' + str(round(E,1)), 'menit', '\n')


# Kelas Tanggal 30/6/2020

# l = 'Nama' + 'Saya'
# print(l)

# print('a' * 5)

# print('a','b')
# print('a' + 'b', (x+y))

# print(x,y)
# x, y, z = z, y, x #swap
# print(x,y)

# from math import pi, fabs, pow, sqrt, round, ceil
# import math #ada di docs python di internet

# print(math.pi)
# print(round(8.89,1))
# print(round(8.89))

# p = 'Halo Dunia'
# print(len(p))
# print(p[1])
# print(p.index('a',2)) #index = len - 1 , index dimulai dari 0
# print(p.index('a'))

# print(p.split(' '))
# print(p.split()) # default memisahkan string menggunakan spasi

# print(p.lower())
# print(p.upper())
# print(p.capitalize())
# print(p.replace('Halo','Hai'))

# a = "Saya \
# adalah"
# print('Saya \n adalah')
# print(p[0:4])
# print(p[-1])
# print(p[-5:])

# print('saya \'tidak\' mau makan')

# nama = input()
# umur = int(input())
# x = -1*(umur%2)+5

# print('karakter nama saya pada posisi index modulus 2 dari umur saya adalah',nama[umur%2])
# print(nama[-1*(umur%2)+5:-1])


# """Yang diperhatikan dalam coding
# 1. Speed = Seberapa cepat program berjalan
# 2. Space = Seberapa besar program memakan RAM
# 3. Maintainability = Seberapa mudah memaintain sebuah program
# """

# seda # shortcut ctrl + H
# seda # untuk men search dan atau replace beberapa atau semua kata
# seda # shortcut ctrl + F2
# seda # untuk men search dan replace semua kata


# print('nama saya' , nama, 'dan umur saya', umur) #
# print('nama saya ' + nama, ' dan umur saya ' + str(umur))
# print('nama saya %s dan umur saya %d' %(nama,umur))
# print('nama saya {} dan umur saya {}' .format(nama,umur))
# print(f'nama saya {nama} dan umur saya {umur}')


# Input angka tersambung _____________
# x = input('Masukkan angka : ')
# y = []
# for i in range(0,len(x)) :
#     y.append(int(x[i]))
# print(y)

# Input angka terpisah spasi ___________
# x = input('Masukkan angka : ')
# x = x.split()
# for a in range(0,len(x)) :
#     x[a] = int(x[a])
# print(x)


# AAAAAAAAAAAAAAAA
# mmmmmmm