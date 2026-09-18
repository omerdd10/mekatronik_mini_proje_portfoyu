temperature = int(input("Sıcaklık ?:"))

if temperature <= 30:
    print("LED: Kapalı")

elif temperature <= 60:
    print("LED: Yanıp sönüyor.")

elif temperature <= 80:
    print("LED: Açık")

else:
    print("LED: Açık")
    print("UYARI! SICAKLIK ÇOK YÜKSEK")
