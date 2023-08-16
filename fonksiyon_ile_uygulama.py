import os
import time

def run_command():
    return """There is 1 interface on the system:
        Name                   : Wi-Fi
        Description            : Intel(R) Wi-Fi 6 AX201 160MHz
        GUID                   : c97928cb-1a41-4d89-be5b-af0b903f08a4
        Physical address       : 40:ec:99:6e:ed:8a
        State                  : connected
        SSID                   : TT_C15
        BSSID                  : 8c:59:73:cd:c2:42
        Network type           : Infrastructure
        Radio type             : 802.11n
        Authentication         : WPA2-Personal
        Cipher                 : CCMP
        Connection mode        : Auto Connect
        Channel                : 10
        Receive rate (Mbps)    : 144.4
        Transmit rate (Mbps)   : 117
        Signal                 : 91% 
        Profile                : TT_C15 

        Hosted network status  : Not available"""
        
def write_output_to_file(output,filename):
    with open(filename,"w") as file:
        file.write(output)

def parse_signal_strength(output):
    signal_line=None
    lines=output.strip().split("\n")
    for line in lines:
        if "signal Strength" in line:
            signal_line=line
            break
        
    if signal_line:
        signal_strength=signal_line.split(":")[1].strip()
        return f"Signal Strength: {signal_strength}"
    else:
        return "Signal Strength: {signal_strength}"
    
def main():
    duration=int(input("Çalışma süresini saniye cinsinden giriniz : "))
    start_time=0
    
    while start_time<duration:
        output = run_command()
        write_output_to_file(output,"output.txt")
        signal_info=parse_signal_strength(output)
        print(signal_info)
        write_output_to_file(signal_info,"signal_info.txt")
        start_time+=1
        for second in range(1,duration+1):
            with open(f"output_{second}.txt","w") as file:
                file.write(output)
            start_time+=1
if __name__=="__main__":
    main()
    
    
# def find_line_with_keyword(file_path,keyword):
#     with open('deneme.txt','r') as dosya:
#         lines=dosya.readlines()
#         for line_number,line in enumerate(lines,start=1):
#             if file_path in line:
#                 return line_number,line.strip()

# def main():
#     komut="netsh wlan show interfaces"
#     sonuc=os.popen(komut).read()
#     print(sonuc)
#     with open('deneme.txt','w') as dosya:
#         dosya.write(sonuc)
        
#     # Belirtilen dosyayı oku ve sinyal gücü bilgisini al
#     with open('deneme.txt', 'r') as dosya:
#         icerik = dosya.read()
    
#     line_number,line_with_keyword=find_line_with_keyword('deneme.txt', 'Signal')
    
#     print(line_number,".Satır : ",line_with_keyword)
    
#     with open('deneme2.txt','w') as dosya:
#         dosya.write(line_number,".Satır : ",line_with_keyword)
#     print("**********************")
#     print("Sure girilmeden yapılan")
#     print("**********************")    
#     for i in range(61):
#         with open('deneme2.txt','w') as dosya:
#             dosya.write(line_number,".Satır : ",line_with_keyword)
    
#     print("**********************")
#     print("Sure girilerek yapılan")
#     print("**********************")
#     sure=int(input("Bir süre giriniz : "))
#     for i in range(sure):
#         with open('deneme3.txt','w') as dosya:
#             dosya.wrie(line_number,".Satır : ",line_with_keyword)
            

# if __name__ == "__main__":
#     main()