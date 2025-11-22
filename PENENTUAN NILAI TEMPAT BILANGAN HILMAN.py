try:
    angka_input = int(input("Masukkan angka: "))

    if 0 <= angka_input <= 999999999999:

    
        jutaan = angka_input // 1000000
        sisa_jutaan = angka_input % 1000000

        ratusan_ribu = sisa_jutaan // 100000
        sisa_ratusan_ribu = sisa_jutaan % 100000
       
        puluhan_ribu = sisa_ratusan_ribu // 10000
        sisa_puluhan_ribu = sisa_jutaan % 10000
  
        ribuan = sisa_puluhan_ribu // 1000
        sisa_ribuan = sisa_jutaan % 1000

        ratusan = sisa_ribuan // 100
        sisa_ratusan = sisa_jutaan % 100

        puluhan = sisa_ratusan // 10
        sisa_puluhan = sisa_jutaan % 10
       
        satuan = sisa_puluhan // 1

        
        H = "\033[92m"   # hijau
        R = "\033[0m"    # reset

        print(H + "\nHasil Pemecahan Angka:" + R)
        print(H + "---------------------------------------------" + R)

        if angka_input >= 1000000:
            print(H + f"Jutaan         : {jutaan}" + R)

        if angka_input >= 100000:
            print(H + f"Ratusan Ribu   : {ratusan_ribu}" + R)

        if angka_input >= 10000:
            print(H + f"Puluhan Ribu   : {puluhan_ribu}" + R)

        if angka_input >= 1000:
            print(H + f"Ribuan         : {ribuan}" + R)

        if angka_input >= 100:
            print(H + f"Ratusan        : {ratusan}" + R)

        if angka_input >= 10:
            print(H + f"Puluhan        : {puluhan}" + R)

        if angka_input >= 1:
            print(H + f"Satuan         : {satuan}" + R)

        print(H + "---------------------------------------------" + R)
        print(H + "Pemecahan angka selesai!" + R)

    else:
        print("Silakan masukkan angka yang sesuai.")

except ValueError:
    print("Input salah. Silakan masukkan angka yang benar.")
