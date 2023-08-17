# %% module block
import os
import time

# %% function block
def run_command():
    komut="netsh wlan show interfaces"
    sonuc=os.popen(komut).read()
    return sonuc

def write_file(sonuc,file_name,write):
    with open(file_name,write) as file:
        file.write(sonuc)

def write_file_60_second(sonuc,file_name,file_name2,line_write,read,find_keyword):
    with open(file_name,read) as file:
        lines=file.readlines()
        for line in lines:
            if find_keyword in line:
                for i in range(60):
                    with open(file_name2,line_write) as file2:
                        time.sleep(1)
                        file2.write(f"{time.asctime()} - {line}")
                        print(time.asctime()+"-"+line)

def write_file_input_second(sonuc,file_name,file_name3,line_write,read,find_keyword,sure):
    with open(file_name,read) as file:
        lines=file.readlines()
        for line in lines:
            if find_keyword in line:
                for i in range(sure):
                    with open(file_name3,line_write) as file2:
                        time.sleep(1)
                        file2.write(f"{time.asctime()} - {line}")
                        print(time.asctime()+"-"+line)
  
# %% main block
file_name="testFonksiyon.txt"
file_name2="fonksiyonIleUygulaSIGNAL.txt"
file_name3="fonksiyonIleUygulaSIGNAL2.txt"
write="w"
read="r"
line_write="a"
find_keyword="Signal"
sure=int(input("Kac saniye boyunca dosyaya yazmak istediginizi giriniz : "))

write_file(run_command(), file_name, write)
write_file_60_second(run_command(),file_name,file_name2,line_write,read,find_keyword)
# write_file_input_second(run_command(), file_name, file_name3, line_write,read, find_keyword, sure)