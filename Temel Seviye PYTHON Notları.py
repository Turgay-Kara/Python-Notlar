"""____________________________________________
   | Best way to learn a language is to use it #
   | 1.Günlük kod yazın.                       #
   | 2.Interaktif çalışın.                     #
   | 3.20-25 dk çalış - ara verin.             #
   | 4.Hata yap ve çözüm bulun.                #
   | 5.Çalışma arkadaşları bulun.              #
   | 6.Anladığınızı öğretmeye çalışın.         #
   | 7.Projeler yapın.                         #
   |___________________________________________#
"""
    #PRİNT
#print('Merhaba Dünya')

#print('Türkiye'nin en kalabalık şehri istanbuldur.')
#-> Sağ taraf string olarak algılanmadı.
#-> Bunu düzeltmek için ters slash(\) koyarız.
#print('Türkiye\'nin en kalabalık şehri istanbuldur.')

#-> ya da 3 tırnaktan yararlanabiliriz.
#3 tırnak ile istediğimiz kadar boşluk bırakabilir ve ya " tırnak koyabiliriz.
#print("""Türkiye'nin en kalabalık şehri istanbuldur.""")

#print("""T
#u
#r
#g
#a
#y""")


#print("Turgay\nAdamdır.")   #-> \n paragraf anlamına gelir yani \n'den sonra bir alt satıra geçer.
#print("Turgay\tAdamdır.")   #-> \t bir TAB boşluk bırakmak için kullanılır.


#print("Hello", end="-")
#print("World")


#print("Turgay", "Kara",sep="-",end="123")     #-> sep"" arasına yazılan değeri kelimeler ARASINA koyar.
                                               #-> end"" arasına yazılan değeri cümlenin SONUNA koyar.


#-> Bu şekilde değişkenlerin yerlerini değiştirebiliriz.
#sayi1=10
#sayi2=20
#sayi1, sayi2=sayi2, sayi1
#print(sayi2)


#x = 'Bu bir değişken denemesi.' 
#print(x)


#x=30
#y=70
#print(x+y) #-> 100



#print(10*'Turgay ')
#print(7)
#print(4*3)


#print("Ben " + str(16) + " yaşımdayım.")    #-> Hem int hem str kullanılmaz. Bu yüzden sayıyı str yaptık.


#for i in range(3):
    #print('Turgay')




    #DEĞİŞKENLER ve SABİTLER (Variables and Constants)
 #değişkenler;
#a = 'turgay' #değişkenin ismi a, değeri turgay
#b = 1.34
#print(b + 3) #-> 4.34


#isim, isim2 = "turgay", "talha"
#print(isim, isim2)  #-> turgay talha


 #sabitler;
#PI = 3.14 #-> Sabitler değiştirilemez ve Değişkenin ismi BÜYÜK harfle yazılır.




    #NUMBERS
 #INTEGER(int)  #-> Tam Sayılar (-, 0, +)
#x = 34
#y = 0
#z = -34




    #FLOAT(float) #-> Noktalı Sayılar (2.34, -0.40)
"""
ortalama = 95.7
sıcaklık = -3
para = -0.31

x = para 
print(type(sıcaklık))  #-> Değişkenin tipini gösterir. -> 'int'
print(ortalama)        #-> Değerini gösterir. -> 95.7  
print(type(x))         #-> x'in yani para'nın tipini gösterir. -> 'float'
                       #-> Noktalı sayı olduğu için 'float'
"""




    #STRİNG(str) #-> "çift tırnak" ("123", "1.23", "TURGAY", "A")
#isim = "Turgay Kara"
#şifre = "şifre123e"
#yaş = "16" #->INTEGER DEĞİL BU BİR STRİNG ->çünkü " içine alınmış.
#print(type(yaş))    #-> 'str'
#print(isim[3]) #-> 3.karakteri yazar -> "g"



    #STRİNG "METOTLAR"
#isim = "Turgay Kara"
#text1 = isim.center(10, '*')            #-> turgay = 6 karakterli, .center parantezine 10yazdık 6 turgayda var kaldı 4, bu 4 karakteri isim'in yanlarına dağıtır.
#text2 = isim.rjust(10, '*')             #-> .center'a benziyor ama turgay'ın sağına 4 karakter * yazdırır.
#text3 = isim.ljust(10, '*')             #-> .center'a benziyor ama turgay'ın soluna 4 karakter * yazdırır.
#text4 = isim.startswith("t")            #-> değişkenimiz küçük t ile mi başlıyor?
#text5 = isim.endswith("y")              #-> değişkenim küçük y ile mi bitiyor?
#text6 = isim.title()                    #-> Tüm kelimelerin baş harfini büyük yapar.
#text7 = isim.split(" ")                 #-> Parantez içine yazılan ifadeyi her gördüğünde değişkeni parçalar ve bir listeye atar.
#text8 = "-".join(isim)                  #-> Her karakter arasına istenilen elemanı yazar.
#text9 = isim.swapcase()                 #-> Büyük harfleri küçük, küçük harfleri büyük yapar.
#text10 = isim.upper()                   #-> Tüm harfleri Büyük yapar.
#text11 = isim.lower()                   #-> Tüm harfleri Küçük yapar.
#text12 = isim.capitalize()              #-> Cümlenin ilk kelimesinin baş harfini büyük yapar(Diğerlerini küçültür.)
#text13 = isim.count("a")                #-> Istenilen elemanın kaç tane olduğunu söyler. -> 1
#text14 = isim.lower().count("t")        #-> Tüm harfleri küçültür ve istenilen elemanın cümlede kaç kere geçtiğini sayar.
#text15 = isim.upper().count("T")        #-> İstenilen elemanı büyülterek istenilen elemanı sayar.
#text16 = isim.find("Kara")              #-> Bulmamıza yarar. -> 7.indexten itibaren başladığını bize söyler.
#text17 = isim.index("g")                #-> Kaçıncı indexten itibaren olduğunu bize söyler. -> 3
#text18 = isim.replace("Kara", "Beyaz")  #-> .replace("Değiştirmek istediğin.", "Yerine koyacağın.")
#text19 = '  - Hello World  '.lstrip()   #-> Sol taraftaki boşluğu sil. -> .lstrip()
#text20 = '  - Hello World  '.rstrip()   #-> Sağ taraftaki boşluğu sil. -> .rstrip()
#text21 = '  - Hello World  '.strip()    #-> Her iki taraftaki boşluğu sil. -> #.strip()
#print(text20)




    #BOOLEAN
  #Boolean (bool) #-> 2 değeri var. True ve False
"""
havagüzel = False #-> Hava güzel değil ise
yağmuryağıyor = True

print(havagüzel)    #-> False
print(type(havagüzel)) #->Değişken tipini gösterir. 'bool'
print(yağmuryağıyor) #-> True
"""



    #LİST
#List (list) #-> Liste. Birden fazla data tipi depolama
#sayılar = [1,2,3,9]
#print(type(sayılar))    #-> 'list'
#print(sayılar)


    #LİSTE METOTLARI

#hayvanlar = ["At", "Köpek", "Kedi", "Balık", "Timsah"]
#print(hayvanlar)



  #.append() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balık", "Timsah"]
#hayvanlar.append("Panda")   #-> .append() -> Listeye yeni eleman ekler.
#print(hayvanlar)



  #.remove() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balık", "Timsah"]
#hayvanlar.remove("Kedi")  #-> .remove() -> Listeden istenilen elemanı çıkartır.
#print(hayvanlar)



  #.pop() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balık", "Timsah"]
#hayvanlar.pop(2)             #-> .pop() -> Listeden istenilen elemanı çıkartır.
#print(hayvanlar)             #-> () Boş bırakılırsa son elemanı çıkartır.



  #.copy() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balık", "Timsah"]
#hayvanlar2 = hayvanlar.copy()      #-> Aktarılacak liste = kopyalanacak liste.copy()
#print(hayvanlar2)



  #.extend() METOTU
#a = [1, 2, 3]
#b = [5, 8, 4, 12, 10]
#a.extend(b)             #-> a listesini ve b listesini birleştir.
#print(a)



  #.sort() METOTU
#a = [1, 2, 3]
#b = [5, 8, 4, 12, 10]
#b.sort()                #-> .sort() Listedeki elemanları sıralamamıza yarar.
#print(b)                #-> Büyükten küçüğe sıralar.

#b.sort(reverse = True)  #-> reverse tersine çevirir.
#print(b)                #-> Küçükten büyüğe sıralar.

#.sort Sadece sayıları değil kelimeleri de sıralayabilir;
#hayvanlar = ["At", "Köpek", "Kedi", "Balık", "Timsah"]
#hayvanlar.sort(reverse = True)
#print(hayvanlar)         #-> hayvanlar listesini tersten(reverse) sıralar


  #max-min() fonksiyonu
#x = [1,2,3,4,5,10,50]
#print(max(x))   #-> Listedeki en büyük sayıyı gösterir.
#print(min(x))   #-> Listedeki en küçük sayıyı gösterir.

  #.count() METOTU
#x = [5, 8, 4, 12, 10, 4]
#print(x.count(4))   #-> .count() Istenilen elemanın kaç tane olduğunu söyler.


  #.index() METOTU
#y = [5, 8, 4, 12, 10]
#print(y.index(5))   #-> .index() Belirtilenn elemanın kaçıncı indexte olduğunu söyler.



  #.insert() METOTU
#b = [5, 8, 4, 12, 10]
#b.insert(1, "TURGAY")  #-> .insert() Belirtilen indexe istenilen elemanı ekler.(Belirtilen indexi silmez.)
#print(b)               #-> 1.index'e "TURGAY" elemanını ekle.



  #.clear() METOTU
#a = [1, 2, 3]
#a.clear()       #-> İstenilen listedeki tüm elemanları siler(.clear).
#print(a)



  #slicing[] METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balık", "Timsah"]
#print(hayvanlar)
#print(hayvanlar[2:4])  #-> 2. ve 4. Elemanların arasındaki elemanları print eder. 2. eleman dahil, 4. eleman dahil DEĞİL.
#print(hayvanlar[:3])    #-> [:3] sayı sağa yazılırsa 3. Elemana kadar print eder. 3. eleman dahil DEĞİL. #slicing metotunda [x:y] y hiçbir zaman dahil edilmez.
#print(hayvanlar[3:])    #-> [3:] sayı sola yazılırsa 3. Elemandan sonraki elemanları print eder. 3. eleman da dahil.
#print(hayvanlar[0:5:3]) #-> [x:y:z] -> z = Kaç karakter aralıklarla gideceğini söyler.
#--> 0.Karakterden 3.Karakter dahil olmamak üzere 2şer aralıklarla(2.dahil) print et. <--#


#hayvanlar[3] = "Arı"   #-> Listenin 3.elemanı yerine istenilen elemanı koy.
#print(hayvanlar)


#insanlar = [["Turgay", "Kara"], ["Talha", "Beyaz"], ["Eşref", "Siyah"]]
#print(insanlar[0])    #-> Turgay, Kara
#print(insanlar[0][1]) #-> Kara
#print(insanlar[2][0]) #-> Eşref
#print(len(insanlar))  #-> len -> Listenin kaç elemandan oluştuğunu söyler -> 3

#x = "Turgay"
#text = (len(x))
#print(text)






    #DEMETLER(Tuples)
 #Listelere benzer ama değiştirilemez ve [] değil, () parantezlerle oluşturulur.

#zamirler  = ("ben", "sen", "o", "biz", "siz", "onlar") #-> Değişiklik yapılamaz.
#print(zamirler[3])     #-> 3. index'i verir. -> biz

#zamirler[0] = "bne"    #-> 0. elemanı yani "ben"i, "bne ile değiştirmeye çalıştık.
 #print(zamirler)       #-> Hata verir çünkü tuple elemanları değiştirilemez(yani eklenme veya çıkartma yapılamaz.!)


#Tek elemanlı bir tuple oluşturmak için:
#a = (5)
#print(a)    #-> 5 çıkar. Yani tuple oluşmadı.

#a = (4,)
#print(a)    #-> (4,) çıktı. Tek elemanlı tuple oluşturduk.


#Bir kaç tane demeti birleştirebiliriz:
#sayılar = (1, 2, 3, 4, 4)
#print(zamirler + sayılar)


#tuple'a bu şekilde de ekleme yapabiliriz:(üstteki daha pratik)
#tuple1=('Turgay', 'Kara')
#tuple1=tuple1+('udemy',)    #-> , olmazsa ERROR
#print(tuple1)

 #Tuple'dan, List'e dönüştürme
#list1 = [1,2,3]
#list2 = (1,2,3)
#list2 = list(list2)
#print(type(list2))

 #List'den Tuple'a dönüştürme
#list1 = tuple(list1)
#print(type(list1))


#print(zamirler[0:3])       #-> Tuple'larda indexleme işlemleri geçerlidir.

#print(len(zamirler))       #-> .len eleman uzunluğunu gösterir.

#print(sayılar.count(4))    #-> .count -> Istenilen elemanın kaç tane olduğunu söyler.

#print(sayılar.index(2))    #-> .index -> Istenilen elemanın kaçıncı indexte olduğunu gösterir.




    #SÖZLÜKLER(Dictionary)(dict)
 #Anahtar ve değerlerden oluşan bir çok elemanı içerisinde bulunduran veri tipi
"""
kimlik = {
        "isim":"Turgay",
        "soyisim":"Kara",
        "TC_NO":12367845689,
        "yer":["Kastamonu", "Merkez"],
        "bilgiler":{"email":"adsfs@gmail.com",
                    "kardeşi sayısı":2
                    }
        }
kimlik["yıl"] = 2005    #-> Kimliğin içine yıl ekledik.

print(kimlik["isim"])
print(kimlik["yıl"])
print(kimlik)
print(len(kimlik))  #-> Eleman sayısını gösterir. -> 4

print(kimlik.keys())       #-> Sözlükteki anahtarları gösterir.
print(kimlik.values())     #-> Sözlükteki değerleri gösterir.
print(kimlik.items())      #-> Anahtalaarı ve Değerleri yanyana gösterir.
print(kimlik.get("yer"))   #-> İstenilen anahtarın değerini gösterir.
print(kimlik.update({"Anne_adi":"Ayfer"}))  #-> Listeye yeni Anahtar(key) ve Değer(value) ekledik.
print(kimlik.copy())       #-> Kimliği kopyalar.
kimlik.pop("isim")         #-> Sözlükten istenilen değeri çıkarır.
kimlik.clear()             #-> Sözlükteki tüm elemanları siler.
print(kimlik)
"""

    #.get() METOTU
"""
ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız: ")
print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))
#->Birinci argüman sorgulamak istediğimiz sözlük öğesidir.
#->İkinci argüman ise bu öğenin sözlükte bulunmadığı durumda kullanıcıya hangi mesajın gösterileceğini belirtir.
"""

#

"""
soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın: ")
if soru == "istanbul":
    print("gök gürültülü ve sağanak yağışlı")
elif soru == "ankara":
    print("açık ve güneşli")
elif soru == "izmir":
    print("bulutlu")
else:
    print("Bu şehre ilişkin havadurumu bilgisi bulunmamaktadır.")
"""
#Bunun yerine .get() metotunu kullanabiliriz.
"""
soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın: ")
cevap = {"istanbul": "gök gürültülü ve sağanak yağışlı",
         "ankara": "açık ve güneşli", "izmir": "bulutlu"}
print(cevap.get(soru, "Bu şehre ilişkin havadurumu bilgisi bulunmamaktadır."))
"""





    #KÜMELER(Sets)
 #-> Süslü parantez kullanılır. {}, #-> Farklı elemanlardan oluşan bir veri tipi, Aynı elemanı 1'den fazla basmaz.
#sayı = {1, 3, 3, 34, 543, 5324, 5, 43}
#print(sayı)     #-> 2tane 3 yazmamıza rağmen 1 tanesini gösterir.


#sayı.add(100)       #-> Eleman eklemek için kullanılır.
#print(sayı)


#sayı.discard(3)     #-> Istenilen elemanı çıkartamk için kullanılır.
#print(sayı)


#sayı.remove(34)     #-> Yine eleman çıkartmak için kullanılır ama () içi boş bırakılırsa hata verir.
#print(sayı)


#yeni_sayi = {32, 3, 25, 432, 4, 325, 4}
#sayı.update(yeni_sayi)     #-> Kümeleri birleştirdik.
#print(sayı)

"""
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}

print(a.difference(b))      #-> a ve b kümelerindeki farkları gösterir. -> 1, 2, 3
print(a.intersection(b))    #-> istenilen kümelerdeki kesişen elemanları gösterir. -> 4
print(a.union(b))           #-> istenilen kümeleri birleştirerek tek bir küme haline getirir. Kesişen elemanlar varsa 1 kere geçirir. -> 1, 2, 3, 4, 5, 6, 7
print(len(a))               #-> istenilen kümedeki eleman sayısını gösterir.
"""



    #TYPE METHOTU ve Örnekler:
 #type Method #-> Bir değişkenin tipini anlamak için kullanılır.
 #type(x)


#a = 1           #-> int'dan
#a = "1"         #-> str'e      ->1
#print(type(a))

#b = 1           #-> int'dan
#b = float(1)    #-> float'a    -> 1.0  -> floata çevirildiği için int'ın sonuna .0 koyar
#print(type(b))

#c = "1"         #-> str'den
#c = int("1")    #-> int'a      -> 1
#print(type(c))

#d = str(1)      #-> str'den
#d = float(1)    #-> float'a    -> 1.0
#print(type(d))

#e = 1.6         #-> float'dan
#e = int(1.6)    #-> int'a      -> 1   -> float'ı integer'a çevirirken YUVARLAMAZ, KESER.
#print(type(e))

#f = 1.6         #-> float'dan
#f = str(1.6)    #-> str'e      -> 1.6
#print(type(f))



#x = [1, 2, 3, 3, 4, 5]
#print(tuple(x))  #-> Listeyi, Tuple'a çevirdik.
#print(set(x))    #-> Listeyi, Set haline getirdik. Çakışan elemanları bir kere yazar ve süslü parantez halinde yazar.
#print(dict(a = 7, a = 9)) #-> Sözlük haline getirdi ve Süslü paranteze aldı, eşittir(=) işaretlerini iki nokta(:) yaptı.


#t = (5,4,2,6,8)
#y = (list(t))   #-> y = t'nin Liste hali
#print(type(y))


#print(round(4.56)) #-> round() ->Herhangi bir sayıya Yuvarlama yapmak için kullanılır. -> 5


#x = 35e3           #-> 3ünün de tipi float
#y = 12E4           #-> olarak çıkar, çünkü;
#z = -87.7e1000     #-> e = 10 üzeri demektir


"""
x = -0.30
y = 1234
z = "z harfi"
print(type(x))  #-> 'float' -> Noktalı Sayı
print(type(y))  #-> 'int'   -> Tam Sayı
print(type(z))  #-> 'str'   -> Kelime
"""


#print("Benim doğum yılım 2005")    #-> 'str'
#print("Benim doğum yılım" + 2005) #ERROR #-> Hem İnteger hem String kullandığımız için ERROR verir.
#print("Benim doğum yılım " + str(2005))





  #KARŞILAŞTIRMA OPERATÖRLERİ
 # <   #-> Küçük müdür?
 # >   #-> Büyük müdür?
 # <=  #-> Küçük müdür veya eşit midir?
 # >=  #-> Büyük müdür veya eşit midir?
 # ==  #-> Eşit midir?
 # =   #-> variable/değişken tanımlanırken kullanılır.
 # !=  #-> Eşit değilse.
"""
#ör:
print(5 > 3)  #->True
print(5 > 7)  #->False

print(7 >= 7) #-> True
print(7 >= 9) #-> False

print(6 != 5)  #-> True
"""

  #MANTIKSAL OPERATÖRLER
 # True and True   #-> True
 # True and False  #-> False
 # False and True  #-> False
 # False and False #-> False

 # True or True    #-> True
 # True or False   #-> True
 # False or True   #-> True
 # False or False  #-> False

 # not True        #-> False
 # not False       #-> True
"""
 #ör:
print(5 < 10 or 10 > 5)    #-> True
print(5 == 5 or 5 < 2)      #-> True
print(6 == 5 or 5 < 1)     #-> False
"""

    #AİTLİK OPERATÖRÜ
 #Aitlik operatörü, bir karakter dizisi ya da sayının,
 #Herhangi bir veri tipi içinde bulunup bulunmadığını sorgulamamızı sağlayan operatördür.

#Python’da bir tane aitlik operatörü bulunur. Bu operatör de in operatörüdür.
#Bu operatörü şöyle kullanıyoruz:
"""
a = "abcd"
print("a" in a)     #-> True
print("f" in a)     #-> False

print("e" not in a) #-> True
print("b" not in a) #-> False
"""

    #ATAMA OPERATÖRLERİ
  # += operatörü
#a = 23
#a = a + 5
#print(a)    #-> a = 28


  # -= operatörü
#a = 23
#a = a - 5
#print(a)


  # /= operatörü
#a = 30
#a = a / 3
#print(a)


  # *= operatörü
#a = 20
#a = a*2
#print(a)


  # %= operatörü
#a = 40
#a = a % 3   #-> 40/3 -> Kalan= 1
#print(a)    #-> 1


  # **= operatörü
#a = 12
#a = a**2    #-> 12üssü 2
#print(a)    #-> 144


  # //= operatörü
#a = 9
#a = a//2    #-> Kalanını atar.
#print(a)    #-> 4





  #ARİTMETİK
 # Toplama  x+y
 # Çıkarma  x-y
 # Çarpma   x*y
 # Bölme    x/y
 # (Tam Sayı sonuçlu) Bölme  x//y #-> 5/2=2   #-> Noktanın sağını atar.
 # Mod Alma x%y      #-> Bölmenin Kalanını verir.
 # Üs alma  x**y     #-> x üssü y

  #DİKKAT: İŞLEM ÖNCELİĞİ !!!
"""
x = 3
y = 5
print(x+y)  #-> 8
print(x-y)  #-> -2
print(x*y)  #-> 15
print(x/y)  #-> 0.6
print(x//y) #-> 0
print(x%y)  #-> 3
print(x**y) #-> 243
"""




     #INPUT
  #input()
"""
isim = input("Adın ne?\n")
print("Merhaba " + isim)
yaş = input("Yaşın kaç?\n")
print("Sen " + yaş + " yaşındasın")
print(type(yaş))
"""



"""
 #İF-ELİF-ELSE KOMUTU
KatedilenMesafe = input("Ne kadar mesafe kat ettiniz?\n")
KalanMesafe = input("Ne kadar mesafeniz kaldı?\n")
if KatedilenMesafe > KalanMesafe:  #-> Bir koşulu kontrol etmek için if kullanılır ve sonuna : koyulur.
    print("Yolun yarısını geçtiniz.")
elif KatedilenMesafe < KalanMesafe:#-> Eğer 'if' komutundaki değer yanlış ise çalışacak komut elif tir.
    print("Yolun yarısını geçmediniz.")
else:                              #-> Eğer 2 koşul da çalışmazsa devreye else girer.
    print("Yolun yarısındasınız.")
"""
#
"""
kullanici_adi = "TurgayKara"
sifre = "12345"

ad = input("Kullanıcı Adınızı giriniz : ")
sifre_gir = input("Şifrenizi giriniz : ")

if ad == kullanici_adi and sifre == sifre_gir:
    print("Sisteme başarıyla giriş yaptınız.")
elif kullanici_adi != ad:
    print("Kullanıcı adınızı yanlış girdiniz.")
else:
    print("Şifrenizi yanlış girdiniz.")
"""
#
"""
result = input("Başvuru Sonucunu Giriniz : ")
if "olumlu" in result.lower():
    print("İşe alındınız!")
elif "olumsuz" in result.lower():
    print("İşe alınmadınız!")
else:
    print("Lütfen geçerli bir değer giriniz!")
"""
#
"""
print("Merhaba, bu program sayınızın 50'den >, < ya da = olduğunu söyler. :)")
number = int(input("Sayı giriniz: "))
if (number == 50):
    print("Sayı 50.")
elif (number < 50):
    print("Sayı 50'den küçük.")
else:
    print("Sayı 50'den büyük.")
"""
#
"""
gender = input("Cinsiyet bilginizi giriniz (E/K): ")
if gender.upper() == "E":
    BirtOfDate = int(input("Doğum yılınızı giriniz: "))

    if 2020 - BirtOfDate == 20 or 2020 - BirtOfDate > 20 and 2020 - BirtOfDate <= 28:
        print("Askere gidebilirsiniz.")
    elif 2020 - BirtOfDate != 20:
        print("Askere gidemezsiniz.")
    else:
        print("Yaşınız hesaplanamadı.")
elif gender.upper() == "K":
    print("Kadınlar askere alınamıyor.")
else:
    print("Lütfen bir cinsiyet giriniz.")
"""
#
"""
for keep in range(1,11):
    if keep == 6:
        break
    print(keep)
"""
#
"""
for keep in range(1,11):
    if keep == 6:
        continue
    print(keep)
"""
#
"""
sayı = int(input("Bir sayı giriniz : "))
if sayı >= 0:       #-> Burdaki if,(2)
    if sayı == 0:       #-> Burdaki if,(1)
        print("Sayı sıfırdır.")
    else:               #-> Burdaki else içindir.(1)
        print("Sayı pozitiftir.")
else:               #-> Burdaki içindir.(2)
    print("Sayı negatiftir.")
"""





    #FOR-WHİLE DÖNGÜSÜ
 #-> Bir durumun sürekli tekrar etmesine denir.
#for Harfler in "CODING SUMMIT":     #-> : koymayı unutma.!
    #print(Harfler)

#for i in range(3):       #-> 'range' komutu her zaman 0'dan başlar.
    #print(i)             #-> 0 1 2


#for keep in range(5):
    #print("Hello")


#for keep in range(1,10+1):
    #print(keep)


#for keep in range(1,10,2):      #->1'den 10'a kadar 2'şer olarak yaz.
    #print(keep)                 #->1, 3, 5, 7, 9

    
#for keep in range(10,0,-1):
    #print(keep)


#list1 = [1,2,3,4,5,6,7,8,9,10]
#for keep in list1:
    #print(keep)


#dict1 = {"Name":"Ali","Surname":"Yıldırım"}
#for keep in dict1.items():
    #print(keep)


#list2 = []
#for keep in range(1,1000):
    #list2.append(keep)
#for keep in list2:
    #print(keep)


#number = int(input("Satır Sayısı Giriniz : "))
#for keep in range(1,number+1):
    #print("*"*keep)


#for keep in range(10,0,-1):
    #print(keep)


#while True:
    #print("Merhaba")   #-> Döngü True olduğu için sonsuza kadar devam eder.

"""
x = 1
while x < 5:
    print("hello, user!")
    x = x + 1
else:
    print("The loop has stopped!")
"""
#
"""
sayaç = 10
while sayaç >= 0:
    print("Sayaç = " + str(sayaç))
    sayaç = sayaç - 1
print("Sayaç bitti.")
"""
#
"""
x = 0
while x <= 10:
    print("Bizim sayımız = " , x)
    x = x + 1
else:
    print("Sayınız 10dan büyük.")
"""
#
"""
sayilar = [1,2,3,4,5,6,7]
print(2 in sayilar)
for sayi in sayilar:
    print("Sayınız = ", sayi)
    if sayi == 5:
        break       #-> Döngü 5'e gelince bitsin.
else:
    print("Döngü bitti.")
"""
#
"""
 #iç içe döngü
sayı = [1,2,3,4,5,6,7]
sayı2 = [1, 2, 3]
for sayi in sayı:    #-> İfadeyi sayilar içindeki eleman kadar döndürür.
    for x in sayı2:
        print(x)
else:
    print("Döngü bitti.")
"""

#for x in range(1,20,2): #-> 1den 20ye kadar 2şer artacak şekilde dön.
    #print(x)


#print(list(range(1,20))) #-> 1den başlayarak 20ye kadar liste şeklinde sayar.


#gelirler = [3000, 4000, 5000, 6000, 7000, 10000]
#for gelir in gelirler:
    #print(gelir * 2)





    #RANDOM METOTU
"""
import random #-> Bazı variable'lar içinden rastgele seçmemizi sağlar.
renkler = ["mavi", "beyaz", "kirmizi", "sari"]
for x in range(100):    #-> 100 defa Print et.
    print(random.choice(renkler))   #-> .choice -> Seçmek istediğimiz için kullanıyoruz.
                                    #-> random.choice(renkler) -> renkler'in içinden rastgele seç.
"""





    #FONKSİYONLAR (Functions)
#def fonksiyonOrnegi():
    #print("Coding Summit'e hoşgeldiniz")
#fonksiyonOrnegi()


#def KaçYaşındasın(yaş):
    #print("Ben ", yaş, " yaşımdayım.")
#KaçYaşındasın(15)  #-> Ben  15  yaşımdayım.





    #FORMAT
#isim = "Turgay"
#soyisim = "Kara"
#print(f"{isim} {soyisim} bir insandır.")


#isim = "Turgay"
#soyisim = "Kara"
#print("Benim ismim {} soyadım {} ".format(isim, soyisim))     #-> .format() süslü parantezin içine istenileni yazar.


#isim = "Turgay"
#soyisim = "Kara"
#print("{0} {1} bir  insandır.".format(isim, soyisim))


#isim = "Turgay"
#soyisim = "Kara"
#print("{C1} {C2} bir  insandır.".format(C1 = isim, C2 = soyisim))


#a=10
#b=15
#print("{} > {}".format(a,b), a < b)    #-> True
#print("{} > {}".format(b,a), b < a)    #-> False


 #format örnekleri
"""
name = "Turgay"
surname = "Kara"
age = 20
job = "Full-Stack deweloper"
city = "İstanbul"
salery = 12000
print(f"Ben {name} {surname}\n{age} yaşımdayım.\n{city} şehrinde yaşıyorum.\nAyda {salery} dolar kazanıyorum.")
"""

#numberone = 20
#numbertwo = 12
#print(f"Toplam : {numberone + numbertwo}\nÇıkartma : {numberone - numbertwo}\nÇarpma : {numberone * numbertwo}\nBölme : {numberone / numbertwo}")



#def kare_al(x):
    #print(x**2)
#kare_al(5)  #-> 5'in karesini alır.



#def alan(r, pi = 3.14):
    #print(pi*r**2)
#alan(12)    #-> Pi tanımlı olduğu için Sadece yarı çapı yazarak alanı bulduk.





    #RETURN
  #Bir sonuç döndürmesi istenen fonksiyonlarda fonksiyonun çalıştıktan sonra bir değer döndürmesi için return anahtar kelimesi kullanılır.
"""
def alan(r, pi = 3.14):
    return pi*r**2
alan1 = alan(6)
alan2 = alan(8)
print(alan1 + alan2)
"""



#def asdasd():
    #pass

#if 3 > 1:
    #pass    #-> Bu satırda Sonradan bir düzeltme yapacaksanız pass komutu işinize yarayacaktır.
