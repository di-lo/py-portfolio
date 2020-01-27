

def besinkatlari():

    x = int(input("Bir sayi giriniz: "))

    liste = []       

    for i in range(x):

        if i % 5 == 0:

            liste.append(i)



    return liste



print(besinkatlari())
