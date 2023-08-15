import os
import re
import time

def read_signal_strength():
    # Belirtilen dosyayı oku ve sinyal gücü bilgisini al
    with open('deneme.txt', 'r') as dosya:
        icerik = dosya.read()

    signal_pattern = r"Signal\s*:\s*(\d+)%"
    match = re.search(signal_pattern, icerik)

    if match:
        signal_strength = match.group(1)
        return signal_strength
    else:
        return "Sinyal bilgisi bulunamadı."

def main():
    os.getcwd()
    os.chdir('C:\\Users\\TP-link\\Desktop\\yazilarsss')

    print("Her saniye bir dosya üretilecektir. Kaç saniye, yani kaç ayrı dosya girişi olmasını istiyorsanız giriniz.")
    saniye = int(input("Verdiğiniz Değer: "))

    for i in range(saniye):
        signal_strength = read_signal_strength()

        # Her saniye için ayrı bir dosya oluştur ve içeriği yaz
        with open(f'signal_output_{i+1}.txt', 'w') as dosya:
            dosya.write(f"Saniye {i+1}: Sinyal Gücü: {signal_strength}%")

        time.sleep(1)  # 1 saniye beklet

if __name__ == "__main__":
    main()
    
#Bu örnekte, kodunuz read_signal_strength adında bir işlev ile sinyal gücü bilgisini 
#okumak için ayrılmıştır. Ana mantık ise main adlı bir işlev içine taşınmıştır.
#Bu sayede kodumuzu daha anlaşılır ve tekrar kullanılabilir hale getirmiş olduk.





