import sys

name = "Emre"
k_sifre = "1234"
max_attempts = 3
attempts = 0
choice = None
balance = 1000

while attempts < max_attempts:
    entered_name = input("Lütfen isminizi girin: ")
    entered_password = input("Lütfen 4 haneli kart şifrenizi giriniz: ")

    if entered_password == k_sifre and entered_name == name:
        print(f"Sisteme hoş geldiniz sevgili, {name}") 

        while True:
            print("Lütfen hangi işlemi yapmak istiyorsaniz onu seçin:")
            print("1. Para Yatirma")
            print("2. Para Çekme")
            print("3. Bakiye öğrenme")
            print("4. Para Gönderme")
            print("5. Çıkış")

            choice = input("Seçim ekrani (1, 2, 3, 4, 5): ")

            if choice == "1":
                deposit_amount = float(input("Hesabiniza yatirmak istediğiniz tutari belirleyin: "))

                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"Yatirilan tutar: {deposit_amount}")
                    print(f"Güncel bakiyeniz: {balance}")
                    sys.exit()

                else:
                    print("Geçersiz miktar. Lütfen pozitif bir miktar girin.")
                break

            if choice=="2":
                withdrawl=float(input("Para çekmek istediğiniz tutari girin: "))
                if withdrawl > 0:
                    balance-=withdrawl
                    print(f"Çekmek istediğiniz tutar: {withdrawl}")
                    print(f"Güncel bakiyeniz: {balance}")
                    sys.exit()
                
                else:
                    print("Geçersiz miktar. Lütfen pozitif bir miktar girin.")
                break   

            if choice=="3":
                print(f"Hesabinizin güncel bakiyesi: {balance}")
                sys.exit()      

            if choice=="4":
                send_name=input("Para göndermek istediğiniz ismi giriniz: ")
                send_money=float(input("Göndermek istediğiniz tutari giriniz: "))

                if send_money > 0:
                    balance-= send_money
                    print(f"Gönderdiğiniz tutar: {send_money}")
                    print(f"İşlem sonrasi bakiye: {balance}")
                    sys.exit()

                else:
                  print("Geçersiz miktar. Lütfen pozitif bir miktar girin.")
                break   

            if choice=="5":
                print("İsteğiniz üzere hesabinizdan ve sistemden çikiş yapiliyor")
                sys.exit()

    else:
        print("Hatali şifre veya isim girişi yaptiniz! Lütfen tekrar dener misin?")
        attempts += 1

    if attempts == max_attempts:
        print("Çok fazla hatali giriş yaptiniz, daha sonra tekrar deneyin!")
        sys.exit()