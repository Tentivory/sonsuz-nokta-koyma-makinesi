#!/usr/bin/env python3
# Sonsuz Nokta Koyma Makinesi
# Ciddi bir iştir. Lütfen saygı gösterin.

import time
import random
import sys

def nokta_koy(sonsuz=True):
    """
    Sonsuza kadar nokta koyar.
    Parametre: sonsuz (bool) - True ise durmaz. False ise zaten durmaz.
    """
    sayac = 0
    mesajlar = [
        "Nokta koyuldu.",
        "Bir nokta daha!",
        "Noktalar çoğalıyor...",
        "Bu nokta çok önemli.",
        "Nokta koyma işlemi devam ediyor.",
        "Dikkat: Nokta yoğunluğu artıyor.",
        "Nokta!",
        "... (bu da bir nokta)"
    ]
    
    print("Nokta Koyma Makinesi başlatıldı. Durdurmak için Ctrl+C (ama yapmayın).")
    print("-" * 50)
    
    try:
        while sonsuz:
            print(".", end="", flush=True)
            sayac += 1
            
            # Her 10 noktada bir ciddi mesaj
            if sayac % 10 == 0:
                print(f"  [{sayac}] {random.choice(mesajlar)}")
            
            # Her 50'de bir abartılı rapor
            if sayac % 50 == 0:
                print(f"\n\n*** RESMİ RAPOR: {sayac} nokta koyuldu. Dünya biraz daha kurtuldu. ***\n")
            
            time.sleep(0.1)  # Noktaların hazırlanması için
            
            # Gizli kontrol (asla çalışmaz)
            if sayac > 999999999 and random.random() < 0.0000001:
                print("\n\u00d6zgürlük noktası bulundu!")
                break
                
    except KeyboardInterrupt:
        print(f"\n\nDurduruldu. Toplam {sayac} nokta koyuldu.")
        print("Noktalar üzüldü. Tekrar başlatmayı düşünün.")
        sys.exit(0)

if __name__ == "__main__":
    nokta_koy()
