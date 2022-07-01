# viloyatlar = {
    
#     'fazliddin':'Samarqand',
#     'jaloliddin':'Qashqadaryo',
#     'zafar':'toshkent'
#     }
# print('Ismlar ro\'yhati')
# for kalit in viloyatlar.keys():
#     print(kalit.title())


# royhat = {
# 'anor':15000,
# 'olma':12000,
# 'bodring':8000,
# 'uzum':10000,
# 'apelsin':35000
# }
# buyurtma=['banan','olma','anor','ananas']

# for mijoz in buyurtma:
#     if mijoz in royhat:
#         print(f'{mijoz.title()} bizda bor uning narxi {royhat[mijoz]}-som ')
#     else :
#         print(f'bizda {mijoz.title()} qolmagan !!!')


# dostlar = {

# 'asadbek':'redmi',
# 'doniyor':'samsung',
# 'saidbek':'redmi',
# 'zafar':'xiaomi',
# 'gafur':'samsung',
# 'dilshod':'redminot'
# }
# print("")
# for doslar in sorted(dostlar):

#     print(doslar.title())


# son=float(input(">>>"))
# while son>=1:
#     print(son)
#     son=son-1



# print('istalgan sonning kubini chiqaruvchi dastur')
# savol = "istalgan son kiriting "
# savol +="dasturni toxtatish uchun esa 'toxta' buyrug'ini kiriting >>> "

# while True:
#     qiymat = input(savol)
#     if qiymat =='toxta':
#         break
#     else:
#         print(float(qiymat)**3)
# print('\ndastur yakunlandi')


# sonlar = list(range(1,21))

# for son in sonlar:
#     if son==7:
#         break
#     print(f"{son}- ning kvadrati {son**2} ga teng")
# print ('dastur tugadi')

# sonlar = list(range(1,21))

# for son in sonlar:
#     if son==7:
#         continue
#     print(f"{son}- ning kvadrati {son**2} ga teng")
# print ('dastur tugadi')

# son =list(range(1,10,2))
# son1 =list(range(0,10,2))
# print(son)
# print(son1)




# son= 0
# while True:
#     son+=1
#     if son%2 !=0:
#         continue
#     print(son)

# kitoblar = []
# print ('Yaxshi korgan kitoblaringiz royxatini kiriting ')
# n=1
# while True:
#     savol = f"{n} - kitobingizn kiriting -  "
#     kitob = input(savol)
#     kitoblar.append(kitob)
#     javob = input("yana kitob nomi qo'shasizmi (yes/no)>>>")
#     if javob=="yes":
#         n+=1
#         continue
#     else : 
#         break    
# print(kitoblar) 


# print ('Qarindoshlar yoshini o\'zida saqlovchi dastur :')
# ismlar ={}
# tsikl = True
# while tsikl :
#     ism =input('Qarindoshingizni ismini kiriting >>> ')
#     yosh = input(f"{ism}ning yoshi nechida ? >>>")
#     ismlar[ism]= int(yosh)
#     javob = input("yana qo'shasizmi ? (ha/yo'q)>>>")
#     if javob=="yo'q":
#         tsikl = False
# print("Qarindoshlar ro'yhati: ")
# for ism,yosh in ismlar.items():
#     print(f"{ism.title()}ning yoshi {yosh} da ")


# ismlar = ['alisher','saidbek','doniyor','asadbek']
# while 'doniyor' in ismlar :
#     ismlar.remove('doniyor')
# print (ismlar)





# avtomobillar = ['moskvich','nexia','cobalt','captiva','malibu']
# narxlangan_avtolar ={}

# while avtomobillar :
#     avtomobil = avtomobillar.pop()
#     narx =input(f"{avtomobil.title()}ning narxini kiriting >>>")
#     print(f"{avtomobil} narxlandi ")
#     narxlangan_avtolar[avtomobil]=int(narx)

# for nomi,qiymati in narxlangan_avtolar.items():
#     print(f"avtomobil nomi {nomi.title()}")
#     print(f"avtomobil narxi {qiymati}")

# import random as tur

# son = tur.randint(1,9)
# print(son)




# choice()bilan ishlash 

# import random as bek

# moshinalar  = ["Nexia", "Damas", "Mersades s500"]
# print (moshinalar)
# nom = bek.choice(moshinalar)
# print(nom)
# print(bek.choice(nom))


# sonlar = list (range(1,10))
# print(sonlar)
# bek.shuffle(sonlar)
# print (sonlar)



        











