while True:
    print("Note: Untuk pangkat, bilangan b adalah nilai pangkatnya.Untuk akar, bilangan b adalah nilai akarnya."
          "Untuk hasil pengakaran agak sedikit error, sehingga untuk beberapa akar sempruna dibulatkan ke angka satuannya."
          "Selamat Mencoba.")
    a = input("Masukkan bilangan 1: ")
    b = input("Masukkan bilangan 2: ")

    print("1.Penjumlahan? 2.Pengurangan? 3.Perkalian? 4.Pembagian? 5. Sisa Pembagian? 6. Pangkat? 7. Akar? (Tulis Angka)")
    answer = input()
    if answer == "1":
        print(a, "+", b, "=", float(a) + float(b))
    elif answer == "2":
        print(a, "-", b, "=", float(a) - float(b))
    elif answer == "3":
        print(a, "x", b, "=", float(a) * float(b))
    elif answer == "4":
        print(a, ":", b, "=", float(a) / float(b))
    elif answer == "5":
        print("sisa ", a, ":", b, "=", float(a) % float(b))
    elif answer == "6":
        print(a, "^", b, "=", float(a) ** float(b))
    elif answer == "7":
        print("Akar", b, "dari ", a, " adalah", float(a) ** (1 / float(b)))
    else:
        print("Invalid Input")

    c = input("Ketik 'l' untuk melanjutkan atau 'b' untuk berhenti")
    if c == "l" :
        continue
    elif c == "b":
        break
    else:
        print("Invalid Input")