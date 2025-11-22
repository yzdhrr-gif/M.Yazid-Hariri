try:
    nilai = int(input("Masukkan nilai maksimal 12 digit: "))

    if 0 <= nilai <= 999999999999:

        # Daftar pembagi dan nama tempat nilai
        tempat_nilai = [
            (1000000000000, "triliun"),
            (100000000000, "ratus miliar"),
            (10000000000, "puluh miliar"),
            (1000000000, "miliar"),
            (100000000, "ratus juta"),
            (10000000, "puluh juta"),
            (1000000, "juta"),
            (100000, "ratus ribu"),
            (10000, "puluh ribu"),
            (1000, "ribu"),
            (100, "ratus"),
            (10, "puluh"),
            (1, "satuan")
        ]

        sisa = nilai

        for pembagi, nama in tempat_nilai:
            jumlah = sisa // pembagi
            sisa = sisa % pembagi
            if nilai >= pembagi:
                print(f"{jumlah} merupakan {nama}")

    else:
        print("Masukkan ulang, nilai harus 0 - 999999999999")

except ValueError:
    print("Input tidak valid")
