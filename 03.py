#_____
# for a in range(1,11) :
#     print('Nomor urut', a)

#_____
# for a in range(0,21,2) :
#     print('Nomor urut', a)

#_____
# for a in range(1,21,2) :
#     print('Nomor urut', a)

#____
# x = ''
# for a in range(1,6):
#     for b in range(1,6):
#         x += ' * ';
#     x += '\n';

# print(x)

#____
# x = ''
# for a in range(1,6):
#     for b in range(1,a+1):
#         x += ' * '
#     x += '\n'

# print(x)

#No. 1
# p = int(input('Panjang bintang : '))
# x = ''
# for a in range(1,p+1,1):
#     for b in range(1,p-a+2):
#         x += ' * ';
#     x += '\n';

# print(x)


#No. 2
# p = int(input('Panjang bintang : '))
# x = ''
# for a in range(p*2,1,-1):
#     if (a > p ):
#         for b in range(a,p,-1):
#             x += ' * '
#         x += '\n'
    

#     else :
#         for b in range(p,a-2,-1):
#             x += ' * '
#         x += '\n'   
        

# print(x)


#No. 2
# p = int(input('Panjang bintang : '))
# x = ''
# for a in range(1,p*2,1):
#     if (a <= p ):
#         for b in range(a,p+1,1):
#             x += ' ' + str(b) + ' '
#         x += '\n'
    

#     else :
#         for b in range(1,a-p+2,1):
#             x += ' ' + str(b) + ' '
#         x += '\n'
        

# print(x)


#No. 3
# p = int(input('Panjang bintang (ganjil) : '))
# x = ''
# for a in range(p,0,-2):
#     for b in range(1,p*2-a+1,2):
#         if (a <= b ):
#             x += ' * '
#         else :
#             x += '   '

#     x += '\n'       

# print(x)


# No. 3 Lain
# p = int(input('Panjang bintang (ganjil) : '))
# x = ''
# for a in range(0,p,2):
#     for b in range(p+a,0,-2):
#         if (a*2 >= b-1 ):
#             x += ' * '
#         else :
#             x += '   '

#     x += '\n'       

# print(x)



#No. 4
# p = int(input('Panjang bintang (ganjil) : '))
# x = ''
# for a in range(0,p,2):
#     for b in range(0,p*2-a,2):
#         if (a <= b ):
#             x += ' * '
#         else :
#             x += '   '

#     x += '\n'
        
# print(x)


#No. 5
# p = int(input('Panjang bintang (ganjil) : '))
# x = ''
# for a in range(p,0,-2):
#     for b in range(1,p*2-a+1,2):
#         if (a <= b ):
#             x += ' * '
#         else :
#             x += '   '

#     x += '\n'       

# for a in range(0,p,2):
#     for b in range(0,p*2-a-1,2):
#         if (a <= b ):
#             x += ' * '
#         else :
#             x += '   '

#     x += '\n'
        
# print(x)

# Lain-lain 1
# p = int(input('Panjang bintang (ganjil) : '))
# x = ''
# for a in range(p,0,-1):
#     for b in range(1,p+1,1):
#         if (a <= b ):
#             x += ' *  '
#         else :
#             x += '  '

#     x += '\n'       

# print(x)


# Lain-lain 2
# p = int(input('Panjang bintang : '))
# x = ''
# for a in range(p,0,-2):
#     for b in range(1,p+1,1):
#         if (a > b) :       
#             x += ' '
#         else :
#             x += '* '
#     x += '\n'

# print(x)


# p = int(input('Panjang bintang : '))
# x = ''
# for a in range(p,0,-1):
#     for b in range(a,0,-1):
#         for c in range(a,0,-1):
#             x += ' '
#         x += '*'
#     x += '\n';

# print(x)
# __________________________________________________

# p = int(input('Panjang bintang (ganjil) : '))
# x = ''

# for a in range(0,p-1,2):
#     for b in range(0,p*2-a-1,2):
#         if (a <= b ):
#             x += ' * '
#         else :
#             x += '   '

#     x += '\n'

# for a in range(p,0,-2):
#     for b in range(1,p*2-a+1,2):
#         if (a <= b ):
#             x += ' * '
#         else :
#             x += '   '

#     x += '\n'       


        
# print(x)


# Catatan _
# penggunaan boolean pada Palindrome
# kata = input('Masukkan kata/kalimat : ')
# palindrome = False
# for i in range(0,len(kata)) :
#     if kata[i] == kata[-i-1]:
#         palindrome = True
#     else :
#         palindrome = False
#         break

# print(f'is word {kata} a palindrome? {palindrome}')


# reverse = kata[::-1]


# print(f'is word {kata} a palindrome? {kata[i] == kata[-i-1]}')


# list += (str(a)+' ')*5
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# list += ' '+str(len(x)-i)+' '
# print(list)
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1