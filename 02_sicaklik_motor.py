temperature = int(input("Sıcaklık (°C) = "))

if temperature <= 30:
    print("Motor kapalı")

elif temperature <= 60:
    print("Motor düşük hızda çalışıyor")

elif temperature <= 80:
    print("Motor orta hızda çalışıyor")

else:
    print("Motor yüksek hızda çalışıyor")
