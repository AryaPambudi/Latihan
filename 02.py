# input() input default berupa str
# int(input()) input berupa int
# input().lower() input dengan str huruf kecil semua
# input().upper() input dengan str huruf besar semua
# list(input()) input dengan str berupa list



#No. 1
# x = int(input('Masukkan angka : '))

# if x % 2 == 0 :
#     print('Angka', x, 'tergolong bilangan GENAP!');
# else :
#     print('Angka', x, 'tergolong bilangan GANJIL!');


#No. 2

# a = int(input('Masukkan Massa(kg) : '))
# b = int(input('Masukkan Tinggi(cm)) : '))
# imt = a / ((b/100)**2)

# if imt > 39.9 :
#     print('IMT =', str(imt) + ', OBESITAS!')
# elif imt > 30.0 :
#     print('IMT =', str(imt) + ', BB SANGAT BERLEBIH!')
# elif imt > 25.0 :
#     print('IMT =', str(imt) + ', BB BERLEBIH!')
# elif imt > 18.5 :
#     print('IMT =', str(imt) + ', BERAT BADAN IDEAL!')
# else :
#     print('IMT =', str(imt) + ', BERAT BADAN KURANG!')



#________________________________KELAS_____________________

#list

# mobil = ['Toyota', 'Honda', 'Isuzu']
# print(type(mobil))
# print(mobil[0])
# print(mobil[1])
# print(mobil[2])

# print(mobil[0:2])
# print(mobil[:2])
# print(mobil[1:])

# #list.append() menambahkan hanya 1 (satu) element saja di posisi paling belakang
# mobil.append('BMW')
# print(mobil)

# #list.pop() mengambil dan menghapus element paling belakang atau sesuai index 
# merk = mobil.pop(1)
# print(mobil)
# print(merk)

# #list.index() mengetahui index dari element tertentu
# print(mobil.index('Toyota'))

# #list.copy() membuat copy list
# mobil_copy = mobil.copy()
# print(mobil_copy)
# mobil_copy.pop()
# print(mobil)
# print(mobil_copy)

# #list.insert(index,element) memasukkan element pada index tertentu
# mobil.insert(15,'Mercy')
# print(mobil)

# #list.sort() mengurutkan (reverse = True / reverse = False)
# mobil.sort(reverse=False)
# print(mobil)

# #list.remove() menghapus element tertentu pada list
# mobil.remove('Toyota')
# print(mobil)

# #list.reverse() membalik urutan list
# mobil.reverse()
# print(mobil)

# #list.count(element) menghitung banyaknya element pada list
# mobil.append('Toyota')
# print(mobil.count('Toyota'))

# #list.extend([]) menambahkan satu atau lebih element pada list
# mobil.extend(['A', 'B', 'C'])
# print(mobil)

# #list[index][index] menyebutkan element pada list didalam list
# mobil.append(['A', 'B', 'C'])
# print(mobil)
# print(mobil[-1][0])

# #tuple () adalah list yang tidak bisa dirubah
# angka = (1,2,3,4,5)
# print(type(angka))
# print(angka.index(1))

# #mengubah tuple () menjadi list []
# angka = [angka]
# print(type(angka))

#set {}
#pada data set tidak dapat memanggil index
#memanggil set akan menampilkan element secara acak
# bilangan = {1,2,3,1,5,4,3}
# print(type(bilangan))
# print(bilangan)

# #set.add() menambahkan hanya satu element
# bilangan.add((5,4,3))
# print(bilangan)

# #set.update([]) menambahkan satu atau lebih element
# bilangan.update([10])
# bilangan.update([7,9,11])
# bilangan.update('andy')
# print(bilangan)

# #set.discard() menghapus element tertentu
# bilangan.discard((5,4,3))
# print(bilangan)

# #set.pop() menghapus element tertentu
# bilangan.pop()
# print(bilangan)

# #set.clear() menghapus semua element dalam
# bilangan.clear()
# print(bilangan)

# a = list('absde')
# b = list('bcfga')
# print(a,b)

# a_set = set(a)
# b_set = set(b)

# print(a_set, b_set)

# #set1.intrsection(set2) irisan dari set1 dan set2
# print('irisan atau intersection: ', a_set.intersection(set_b))

# #set1.difference(set2) selisih set1 dari set2
# print('irisan atau difference: ', a_set.difference(set_b))
# print('irisan atau difference: ', b_set.difference(set_a))

# #set1.union(set2) gabungan dari set1 dan set2
# print('irisan atau union: ', a_set.union(set_b))

# #set1.symmetric_difference(set2) gabungan dari selisih set1 dan set2
# print('symmetric difference',set1.symmetric_difference(set2))


# p = [1,2,4,7,9,19]
# q = [5,12,16,17,7,9,19,6]
# r = [19,6,3,8]

# p = set(p)
# q = set(q)
# r = set(r)

# print('Gabungan P dan Q : ', p.union(q)) # p.union(q) sama dengan p|q
# print('Gabungan P dan R : ', p.union(r))
# print('Gabungan Q dan R : ', q.union(r))
# print('Irisan dari Gabungan P dan Q dengan Q dan R : ', 
# (p.union(q)).intersection(q.union(r))) # (p.union(q)).intersection(q.union(r)) sama dengan (p|q)&(q|r)

# zip
# angka = [1,2,3,4,5]
# huruf = ['a', 'b', 'c', 'd', 'e']

# print(dict(zip(huruf,angka)))
# print(list(zip(huruf,angka)))


# index dalam list

# kata = 'aku'
# print(kata[1])
# print(kata.index('k'))


# Membuat list dengan looping for dan syarat if
# Angka Genap
# angka = list(a for a in range(1,100+1) if (a%2) == 0 )
# print(angka)

# _______________________________________________________________
# Fungsi reduce()
# reduce() hanya untuk dua variabel saja
# Faktorial 2

# from functools import reduce

# number = [1,2,3,4]
# n = reduce(lambda a, b: a*b, number)
# print(n)


# kata = ['ini', 'ibu', 'budi']
# a = reduce(lambda a, b: a+' '+b, kata)
# print(a)
# ________________________________________________________________

# Quiz 1
# from functools import reduce
# x = int(input('Masukkan angka awal :'))
# y = int(input('Masukkan angka akhir : '))

# Cara 1
# angka = reduce(lambda a, b : a + b, map(lambda a : a*2 ,filter(lambda a : (a%2) == 0 , list(a for a in range(x,y+1)))))
# Cara 2
# angka = reduce(lambda a, b : a + b, map(lambda a : a*2 ,list(a for a in range(x,y+1) if (a%2) == 0 )))
# print(angka)
# ____________________________________________________________________________