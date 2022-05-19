import time
import os

while True:
    print("""**********************************
    Hesap Makinesi

    İşlemler ;

    1. Toplama işlemi

    2. Çikarma işlemi

    3. Çarpma İşlemi

    4. Bölme İşlemi

    **********************************
    """)
    a = int(input("Birinci Sayı :"))
    b = int(input("İkinci Sayı :"))

    işlem = input("İşlemi giriniz :")

    if işlem == "1":
        print("{} + {} = {} olarak bulunur.".format(a,b,a+b))
    elif işlem == "2":
        print("{} - {} = {} olarak bulunur.".format(a,b,a-b))
    elif işlem == "3":
        print("{} * {} = {} olarak bulunur.".format(a,b,a*b))
    elif işlem == "4":
        print("{} / {} = {} olarak bulunur.".format(a,b,a/b))
    else:
        print("Geçersiz İşlem Girdisi Lütfen 1 , 2 , 3 veya 4 işlemlerinden bir tanesini giriniz.")
    devam = input("Devam Etmek İstiyor Musunuz?")
    if devam == "E":
        os.system("cls")
        continue
    else:
        print("Program Kapanmiştir.")
        time.sleep(4)
        quit()

