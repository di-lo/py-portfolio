sayi = int(input("Sayi Giriniz:"))
toplam=0
for i in range(1,sayi):
    if(sayi%i == 0):
        print(i)
        toplam +=i

if(sayi == toplam):
    print("Mukemmel Sayidir : Perfect number")
else:
    print("Mukemmel Sayi Degildir : Not a perfect number")
