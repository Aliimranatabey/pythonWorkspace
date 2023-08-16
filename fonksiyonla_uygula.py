import os
def run_command():
    komut="netsh wlan show profiles"
    sonuc=os.popen(komut).read()
    return sonuc

def write_file(sonuc,file_name,write_or_read):
    with open(file_name,write_or_read) as file:
        file.write(sonuc)

def write_file_60_second(sonuc,file_name,file_name2,write_or_read,find_keyword):
    with open(file_name,write_or_read) as file:
        lines=file.readlines()
        for line in lines:
            if find_keyword in line:
                for i in range(60):
                    with open(file_name2,write_or_read) as file2:
                        file2.write(f"{i}. Saniyede {line} \n")

def write_file_input_second(sonuc,file_name,file_name3,write_or_read,find_keyword,sure):
    with open(file_name,write_or_read) as file:
        lines=file.readlines()
        for line in lines:
            if find_keyword in lines:
                for i in range(sure):
                    with open(file_name2,write_or_read) as file2:
                        file2.write(f"{i}. Saniyede {line} \n")
                        
file_name="deneme2.txt"
file_name2="signal3.txt"
file_name3="signal4.txt"
write_or_read=input("Dosya üzerinde okuma mı yazma mı yoksa satır satır yazma mı yapmak istediğinizi belirtmek için (a , w , r) bir tanesini giriniz : ")
find_keyword=input("Hangi satırı parse etmek istiyorsanız o satırdan bir metin giriniz : ")
sure=int(input("Kac saniye boyunca dosyaya yazmak istediginizi giriniz : "))

write_file(run_command(), file_name, write_or_read)
#write_file_60_second(run_command(), file_name, file_name2, write_or_read, find_keyword)
#write_file_input_second(run_command(), file_name, file_name2, write_or_read, find_keyword, sure)