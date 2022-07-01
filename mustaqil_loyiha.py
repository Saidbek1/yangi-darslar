# sayt = True
# while sayt:
    
#     print ('Sotib olmoqchi bolgan kompyuter nomini kiriting❓❓❓ >>>')
#     sotib_olmoqchi_komp =input()
#     websaytdagi_narxi = int(input('Kompyuterning Websaytdagi narxini kiriting >>>'))
#     yonidagi_puli = int(input('Yoningizdagi pulingizni kiriting >>>'))
#     if websaytdagi_narxi>yonidagi_puli:
#          print(f"Bu kompyuterni sotib olish uchun sizga {websaytdagi_narxi - yonidagi_puli } yetmaydi")
#          print('Websaytdan , narxi sizga to\'g\'ri keladigan kompyuter tanlang ??? ')
#          sayt = True
#          continue
#     elif websaytdagi_narxi < yonidagi_puli:
#          print(f"Bu kompyuterni xarid qilsangiz sizda {yonidagi_puli - websaytdagi_narxi} pul qoladi ")
#          print ('davom ettirish uchun 1 ni bosing >>>')
#          print ('Xaridni bekor qilish uchun 0 ni bosing >>>')
#          davom_etish = int(input())
#          if davom_etish==1 :
#              print ('tabriklaymiz siz muvafaqiyatli savdoni amalga oshirdingiz !!! ')
#              print("Xaridni biz bilan amalga oshirganingiz uchun rahmat ! Sizga foydamiz tekkanidan mamnunmiz !!!")
             
#          elif davom_etish==0:
#              print('Xarid bekor qilindi !!! ')
#              print("Xaridni qayta amalga oshirishingiz yoki Websaytdan boshqa modeldagi kompyuter xarid qilishingiz mumkin !!! ")
#              continue
#          else :
#              print('siz noto\'g\'ri kod kiritdingiz qayta urinib ko\'ring ?')
#              continue
#          break
#     else :
#          print('Iltimos Tekshirib qaytadan kiriting')
#          break        








                                        # IKKINCHI LOYIHA CALCULATOR YARATISH



# n = 0
# m=""
# s=""
# while True :
#     print ("        Calkulator :      ")
#     a=int(input("Birinchi sonni kiriting >>> "))
#     b=int(input("Ikkinchi sonni kiriting >>> "))
#     d=" Siz Calculatordan qayta foydalanishingiz mumkin !!! "
#     print(" Qanday amalni bajarmoqchisiz ??? ")
#     print("\n 1- qo\'shish amali \n 2- ayirish amali \n 3-ko'paytirish amali\n 4- bo'lish amali\n ")
#     c=int(input("Menudagi foydalanmoqchi bo'lgan amalingizni tartib raqaminin kiriting ??? "))
#     if c==1:
#         n = a + b
#         m="+"
#         s=" qo'shish "
#     elif c==2:
#         n= a-b
#         m="-"
#         s="ayirish"
#     elif c==3:
#         n= a*b
#         m="*"
#         s= "ko'paytirish"
#     elif c==4:
#         n = a/b
#         m=":"
#         s="bo'lish" 
#     else :
#         print (" Kechirasiz noto'g'ri kod kiritdingiz Menuda bunday kod mavjud emas\n Qaytadan urinib ko'ring va o'zingizga kerakli amalni bajaring : ")
#         continue
#     print (f"Siz {s} amalini tanladingiz natija :")
#     print(f"Natija :{a} {m} {b} = {n} \n {d}")
    

# import random as bek

# print("O'yla , izla , top o'yiniga xush kelibsiz \n Salom , men 1 dan 10 gacha son o'yladim topa olasizmi ? ")
# son = bek.randint(1,10)
# i=0
# while True:
#     user_oylagan_son = int(input(" Qaysi sonni tanladingiz kiriting >>>"))
#     i+=1
#     if user_oylagan_son==son:
#         print(f"Tabriklaymiz siz {i}- urunishda topdingiz !!!")
#         user = input(" O'yinni davom ettirasizmi (ha/yo'q)")
#         if user=="ha":
#             continue
#         else :
#             break
#     elif user_oylagan_son > son:
#         print(f"Xato ! Kompyuter o'ylagan son siz o'ylagan sondan kichik ! yana urunib ko'ring ?")

#     elif user_oylagan_son < son :
#         print(f"Xato ! Kompyuter o'ylagan son siz o'ylagan sondan katta ! yana urunib ko'ring ?")



# print("Assalomu aleykum yangi o'yin o'ynaymiz 1 dan 20 gacha son tanlang kompyuter necha urinishda siz o'ylagan onni topar ekan ??? ")
# yuqori = 1
# past = 20
# user_son = int(input("1 dan 20 gacha son kiriting >>> "))
# i=0
# while True:
#     son = bek.randint(yuqori , past)
#     print(son , " - kompyuter tanlagan son")
#     tanlov = input("Agar kompyuter tanlagan son siz tanlagan songa teng bo'lsa 't' ni bosing \nAgar kompyuter tanlagan son siz tanlagan sondan katta bo'lsa '+' ni bosing \nAgar kompyuter tanlagan son siz tanlagan sondan kichik bo'lsa '-' ni bosing!!! ")
#     i+=1
#     if tanlov=="t":
#         print(f" Tabriklaymiz Siz kiritgan sonni kompyuter {i}- urunishda topdi !!!")
#         print("yana o'ynaysizmi agar o'ynamoqchi bo'lsangiz <ha> , agar o'ynamasangiz <yo'q> deb javob bering")
#         soz = input(">>>")
#         if soz=="ha":
#             continue
#         elif soz=="yo'q":
#             break
#         else:
#             print("Menuda yo'q so'zni kiritdingiz !!!")
#             break
#     elif tanlov == "+":
#         yuqori = son
#     elif tanlov=="-":
#         past = son
#     else :
#         print("Siz menuda yo'q so'zni kiritdingiz !!! ")
#         break


# import random
# def menu():
#     while True:
#         print("Assalomu aleykum o'yinimizga xush kelibsiz bu o'yin matematikadan hisob kitob bo'yicha ishlash o'yini")
#         print ("         o'zingizga kerakli bo'limni tanlang   ")
#         print ("<<<<<<Qiyinlik darajasi>>>>>>\n <1> Oson\n<2> O'rtacha\n <3> Qiyin\n<4> Ortga")
#         daraja = int(input("1 dan 4 gacha son kiriting ? >>>"))
#         if daraja<=4 or daraja>=1:
#             return daraja
            
# def oyin(menu):



# def regestratsiya( gmail  ,kod , IDraqam ,  ism = " ", familiya=" ",  ): 
#     royhat = {

#             'gmail':gmail,
#             'kod':kod,
#             'IDraqam':IDraqam,
#             'ism':ism,
#             'familiya':familiya }
#     print ("Assalomu aleykum hush kelibsiz saytga kirish uchun quyidagi formani to'ldiring ? ")
#     for kalit,qiymat in royhat:
        

#      return royhat


# def kirish(regestratsiya):
    
#     print("Assalomu aleykum hush kelibsiz saytga kirish uchun quyidagi formani to'ldiring ? ")
#     a=int(input("<1> Ro'yhatdan o'tish\n <2> Kirish"))
#     if a==1:
        
# def regestratsiya( username  ,kod , IDraqam ,  ism = " ", familiya=" ",  ):



# """login registartion"""

# user[
#     {"username" : "test" , "id":'4545445',"password":'4444'
#     }
# ]
# print ("\n\n Assalomu aleykum ro'yhatdan o'tish bo'limiga hush kelibsiz \n \n Menudan o'zingizga kerak bo'limni tanlang")
# def main():
#     def login():
#         username = input("Foydalanuvchi nomi : ")
#         password = input("Foydalanuvchi kodi : ")
#         for users in user:
#             if users['username'] == username and users['password']==password:
#                 print ("Tariklaymiz siz akkauntga kirdingiz ")
#             else:
#                 print ("Xato login va parolni o'ylab kiriting ? ")
#             login()
#     def create():
#         username = input ("Yangi login kiriting : ")
#         password = input ("Yangi parol kiriting : ")
#         id_raqam = input("Yangi ID kiriting ")
# main()

# import random
# from secrets import choice
# print("Assalomu aleykum quduq , qaychi o'yiniga hush kelibsiz ! ")
# k_yut = 0
# u_yut =0
# durr =0
# variant = [ 'quduq' ,'qaychi' ,'qogoz']
# print (variant)
# for j in range(1,6) :
#     user_var = input("Variant tanlang >>>")
#     komp_use = choice(variant)
#     if user_var==komp_use:
#         print(f"Durrang !!!\n Kopmyuter {komp_use} : {user_var}  foydalanuvchi")
#         durr+=1
#     elif komp_use=="quduq" and user_var=="qaychi":
#         print(f"Siz yutqazdingiz !!! \n Kompyuter  {komp_use}: {user_var}  Foydalanuvchi\n ")
#         k_yut+=1
#     elif komp_use =="quduq" and user_var=="qogoz":
#         print (f"Siz yutdingiz !!! \n Kompyuter  {komp_use}: {user_var}  Foydalanuvchi\n ")
#         u_yut+=1
#     elif komp_use=="qaychi" and user_var=="quduq":
#         print (f"Siz yutdingiz !!! \n Kompyuter  {komp_use}: {user_var}  Foydalanuvchi \n")
#         u_yut+=1
#     elif komp_use=="qaychi" and user_var=="qogoz":
#         print(f"Siz yutqazdingiz !!! \n Kompyuter  {komp_use}: {user_var}  Foydalanuvchi\n ")
#         k_yut+=1
#     elif komp_use=="qogoz" and user_var=="quduq":
#         print(f"Siz yutqazdingiz !!! \n Kompyuter  {komp_use}: {user_var}  Foydalanuvchi\n ")
#         k_yut+=1
#     elif komp_use=="qogoz" and user_var=="qaychi":
#         print (f"Siz yutdingiz !!! \n Kompyuter  {komp_use}: {user_var}  Foydalanuvchi \n")
#         u_yut+=1
#     else :
#         print("Siz noto'g'ri kalit so'z kiritdingiz qayta kiriting!!!")
#         break
# if k_yut > u_yut:
#     print (f"\n\nSIZ UMUMIY HISOB BO'YICHA YUTQAZDINGIZ\n <<<Umumiy hisob>>>\nqaychi kompyuter {k_yut} : {u_yut} foydalanuvchi \n durranglar soni {durr}")
# elif k_yut==u_yut:
#      print (f"\n\nUMUMIY HISOB BO'YICHA DURRANG\n <<<Umumiy hisob>>>\nqaychi kompyuter {k_yut} : {u_yut} foydalanuvchi \n durranglar soni {durr}")
# else :
#     print (f"\n\nSIZ UMUMIY HISOB BO'YICHA YUTDINGIZ\n <<<Umumiy hisob>>>\nqaychi kompyuter {k_yut} : {u_yut} foydalanuvchi \n durranglar soni {durr}")





def mehmonxona ():
    """menu tanlov """
    print("<<<<<Assalomu aleykum mehmonxonamizning online sahifasiga hush kelibsiz>>>>>\nquyidagi menudan o'zingizga mos bo'limni tanlang ?")
    a=int(0)
    print(f"<1> Xona bron qilish\n<2> Mehmonxona haqida ma'lumot olish\n<3> Admin kabinetiga kirish\n<4> Dasturni to'xtatish")
    a=int(input(">>>"))
    
    def bir ():
        
            print ("---Xona bron qilish---")
            print (f"<1> Lux xonalar\n<2> Standart xonalar\n<0> Ortga")
            b=int(input(">>>"))
            if b==1:
                print ("---Lux xonalar haida ma'lumot---")
                print(f"<1> Lux xonalar haqida ma'lumot\n<2> Lux xonalar narxlari\n <0> Ortga")
                c=int(input(">>>"))
                if c==1:
                    print("Lux xona - 1 , 2 , 3 xonali xonalarimiz mavjud siz bu xonani band qilish orqali juda ko'p qulayliklarga ega bo'lasiz xona o'z ichiga 'play station',televizor ,tekin 3 mahal ovqatni o'z ichiga oladi ")
                elif c==2:
                    print("Sizga nechi xona kerak 1,2,3 xona xonalarimiz narxi 1 xonali arzonroq 2 xonali qimmatroq 3 xonali qimmat ")
                    print("<1> 100 $ \n<2> 200$ \n<3> 250 $")
                    i=int(input(">>>"))
                    if i==1:
                        print ("Siz bir xonani tanladingiz  ")



    


























