import os
komut="netsh wlan show interfaces"
sonuc=os.popen(komut).read()
print(sonuc)

with open("deneme1.txt","w") as file:
    file.write(sonuc)


with open("deneme1.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        if "Signal" in line:
            for i in range(60):
                with open("signal.txt","a") as file2:           
                    file2.write(f"{i+1}. Saniyede {line} \n")

print("Signal bilgisini kaç saniye boyunca almak istediğinizi saniye cinsinden giriniz ... ")
giris=int(input("Saniye : "))

with open("deneme1.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        if "Signal" in line:
            for i in range(giris):
                with open("signal2.txt","a") as file2:
                    file2.write(f"{i+1}. Saniyede {line} \n")