sayi = int(input("dort basamakli sayi giriniz: "))

b1 = sayi%10

b2 = sayi//10
b2 = b2%10

b3 = sayi//100
b3 = b3%10

b4 = sayi//1000
b4 = b4%10

print("birler basamagi", b1)
print("onlar basamagi", b2)
print("yuzler basamagi", b3)
print("binler basamagi", b4)
