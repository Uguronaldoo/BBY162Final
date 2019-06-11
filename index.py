global ad
ad= "index.txt"

def listeleme() :
    with open(ad ,"r") as dosya:
        bilgiler = dosya.readlines()
        i =1
        for bilgi in bilgiler:
            print(i,".",bilgi)
            i+= 1
def eserekleme():

        with open (ad,"a") as dosya:
         dosya.write(input("Yazar ismi")+":")
         dosya.write(input("Eser ismi")+",")
         dosya.write(input("Tarih"))
def aramayapma():

    with open(ad,"r") as dosya:

        aranan = input("Aramak istediğiniz kelimeyi giriniz: ")

        aranan_varmi =dosya.read().find(aranan)

    if aranan_varmi != -1:
        print(aranan)

    else:

        print("Aradığınız Kelime bulunmamaktadır.")

while 1:
    print("Eserleri listelemek için: 1'e basınız.")

    print("Yeni eser girişi için: 2'ye basınız.")

    print("Eser adına, yazar adına ya da tarihe göre arama yapmak için: 3'e basınız.")

    secenek = int(input("İşlem yapmak için bir seçenek seçiniz:"))

    if secenek ==1 :
        listeleme()
    if secenek ==2:
        eserekleme()
    if secenek ==3 :
       aramayapma()