import random

def tas_kagit_makas_firat_seven():

    #Oyun Bilgilendirme
    print("\nTaş, Kağit, Makas oyununa hoş geldiniz!✨🧨✨\nIlk iki turu kim kazanirsa oyunun galibi olacaktir. \nOyun bitiminde tekrar oynamak isterseniz. Lutfen tekrar oynayalim tusuna basiniz.")

    #Oyun içeriği
    secim = ["tas", "kagit", "makas"]

    tur_sayisi = 0
    oyuncu_galip_taraf = 0
    bilgisayar_galip_taraf = 0

    while True:
        #Kullanıcı ve bilgisayarın sayaçları sıfırlama
        tur_sayisi = 0
        oyuncu_galip_taraf = 0
        bilgisayar_galip_taraf = 0

        while oyuncu_galip_taraf < 3 and bilgisayar_galip_taraf < 3:
            print(f"\n{tur_sayisi + 1}. Tur:")
            
            #Kullanıcı oyun secimi
            oyuncu_secim = input("\nTaş, Kağit, Makas secimi yapiniz: ").lower()

            #Geçersiz secenek girerse
            if oyuncu_secim not in secim:
                print("Seçeneklerde olmayan bir değer girdiniz. Lütfen tekrar deneyiniz.")
                continue

            bilgisayar_secim = random.choice(secim)
            print(f"Bilgisayarın Seçimi: {bilgisayar_secim}")

            #Kazanan oyuncu ve bilgisayarın karşılaştırılması
            if (oyuncu_secim == "tas" and bilgisayar_secim == "makas") or (oyuncu_secim == "makas" and bilgisayar_secim == "kagit") or (oyuncu_secim == "kagit" and bilgisayar_secim == "tas"):
                print("Kazandınız!")
                oyuncu_galip_taraf += 1
            elif oyuncu_secim == bilgisayar_secim:
                print("Berabere!")
            else:
                print("Kaybettiniz!")
                bilgisayar_galip_taraf += 1

            tur_sayisi += 1

            #2 Galibiyet alan oyunu kazanır
            if oyuncu_galip_taraf == 2 or bilgisayar_galip_taraf == 2 :
                if oyuncu_galip_taraf==2:
                    print("\nOyuncu Oyunu Kazandı ��������� \n Oyun Sona Erdi")
                elif bilgisayar_galip_taraf==2:
                    print("\nBilgisayar Oyunu Kazandı ��������� \n Oyun Sona Erdi")
                break

            #Oyun bitirme kontrolü
            if oyuncu_galip_taraf>=2:
                print("\nOyuncu Oyunu Kazandı 🎇🎉✨✨")
                oyuncu_galip_taraf += 1
            else:
                print("\nBilgisayar Oyunu Kazandı 😥😣😏")
                bilgisayar_galip_taraf += 1

            #Oyuna tekrar etmek için kontrol sağlama
            cevap = input("\nTekrar oynamak ister misiniz? (e/h): ").lower()
            bilgisayar_cevap = random.choice(["e","h"])
            print(f"Bilgisayar oyuna devam etmek istiyor mu? {bilgisayar_cevap.lower()}")

            if cevap != "e" or bilgisayar_cevap != "e":
                print("Oyun sona erdi. Teşekkürler!")
                break
            
            """
            
            #Oyuna tekrar etmek isteyen kullanıcı kontrolü
            if bilgisayar_galip_taraf==2:
                #cevap = input("\nTekrar oynamak ister misiniz? (e/h): ").lower()
                if cevap!= "e":
                    print("\nOyun bitti. İyi oynamadınız! ��")
                    break

            #Oyuna Bilgisayar tekrar etmek istiyormu
            if bilgisayar_galip_taraf==2:
                #bilgisayar_cevap = random.choice(["e","h"]).lower()
                if bilgisayar_cevap!= "e":
                    print("\nBilgisayar oyuna devam etmek istemiyor.. \n Güle Güle Tekrar bekleriz! 🤣 ��")
                    break
                    

            """
tas_kagit_makas_firat_seven()