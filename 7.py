kullanici_adi = input("Kullanici adi giriniz: ")
parola = input("parola giriniz: ")

if kullanici_adi == "t3" and parola == "2020":
    print("Kullanici adi ve parola dogru!")
    print("Hosgeldin", kullanici_adi)

elif kullanici_adi == "t3":
    print("parola yanlis!")

else:
    print("yanlis kullanici adi girdiniz!")
