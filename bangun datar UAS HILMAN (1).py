import math

def persegi():
    sisi = float(input("masukan panjang sisi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def persegi_panjang():
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def segitiga():
    alas = float(input("masukan alas: "))
    tinggi = float(input("masukan tinggi: "))
    sisi1 = float(input("masukan sisi 1: "))
    sisi2 = float(input("masukan sisi 2: "))
    luas = 0.5 * alas * tinggi
    keliling = alas + sisi1 + sisi2
    return luas, keliling

def lingkaran():
    r = float(input("masukan jari jari: "))
    luas = math.pi * r * r
    keliling = 2 * math.pi * r
    return luas, keliling

# ------ PROGRAM UTAMA ------

bangun_datar = [
    "persegi",
    "persegi panjang",
    "segitiga",
    "lingkaran"
]

while True:
    print("\n===== APLIKASI BANGUN DATAR =====")
    for i in range(len(bangun_datar)):
        print(f"{i + 1}. {bangun_datar[i]}")
    print("5. keluar")

    pilihan = int(input("pilih bangun datar (1-5): "))

    if pilihan == 1:
        luas, keliling = persegi()
    elif pilihan == 2:
        luas, keliling = persegi_panjang()
    elif pilihan == 3:
        luas, keliling = segitiga()
    elif pilihan == 4:
        luas, keliling = lingkaran()
    elif pilihan == 5:
        print("terima kasih telah menggunakan aplikasi.")
        break
    else:
        print("pilihan tidak valid!")
        continue

    print(f"luas     : {luas}")
    print(f"keliling : {keliling}")
