speed = int(input("Motor hızı (%) ="))

if speed == 0:
    print("Motor çalışmıyor")

elif speed < 31:
    print("Motor düşük hızda çalışıyor")

elif speed < 71:
    print("Motor orta hızda çalışıyor")

else:
    print("Motor yüksek hızda çalışıyor")
