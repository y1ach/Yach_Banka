print("--------------------------------Yach Banka--------------------------------")
Amac = input("Kurumumuzda yeni misiniz? Yeniyseniz yeni yazın, eğer değilseniz 'değilim' yazın: ")

if Amac.lower() == "yeni":
    TC = input("TC: ")
    dosya=open(f"{TC}.txt", mode="r")
    print(dosya.readline())
    print(dosya.readline())
    print(dosya.readline())
    print(dosya.readline())
    print(dosya.readline())

elif Amac.lower() == "değilim":
    TC = input("TC: ")
    Ad = input("Adınız: ")
    Soyad = input("Soyad: ")
    Banka_Sifresi = input("Banka Şifreniz: ")
    Bankadaki_Para_Miktarı = input("Ne kadar para yatırdınız? Yanına dolar/Tl/euro vb. türünü yazın: ")
    dosya=open(f"{TC}.txt", mode="a")
    dosya.write(f"Ad: {Ad}\n")
    dosya.write(f"Soyad: {Soyad}\n")
    dosya.write(f"Banka Şifresi: {Banka_Sifresi}\n")
    dosya.write(f"Bankadaki Para Miktarı: {Bankadaki_Para_Miktarı}\n")
dosya.close()