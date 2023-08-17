import os
import time
komut="netsh wlan show interfaces"
sonuc=os.popen(komut).read()
print(sonuc)

with open("test.txt","w") as file:
    file.write(sonuc)


with open("test.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        if "Signal" in line:
            for i in range(60):
                with open("normalUygulaSIGNAL.txt","a") as file2:
                    time.sleep(1)
                    print(time.asctime()+"-"+line)
                    file2.write(f"{time.asctime()} - {line}")

print("Signal bilgisini kaç saniye boyunca almak istediğinizi saniye cinsinden giriniz ... ")
giris=int(input("Saniye : "))

with open("test.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        if "Signal" in line:
            for i in range(giris):
                with open("normalUygulaSIGNAL2.txt","a") as file2:
                    time.sleep(1)
                    print(time.asctime()+"-"+line)
                    file2.write(f"{time.asctime()} - {line}")