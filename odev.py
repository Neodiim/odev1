def frekans_analizi(metin):

    metin = metin.lower()
    harfler = [harf for harf in metin if harf.isalpha()]

    frekanslar = {}
    toplam_harfler = len(harfler)


    for harf in harfler:
        if harf in frekanslar:
            frekanslar[harf] += 1
        else:
            frekanslar[harf] = 1


    for harf, sayi in frekanslar.items():
        frekanslar[harf] = (sayi / toplam_harfler) * 100

    return frekanslar


metin = input("Lütfen bir metin girin: ")

print("\nİlk 100 karakterlik metnin harf frekansları:")
sonuc_100 = frekans_analizi(metin[:100])
for harf, frekans in sonuc_100.items():
    print(f"{harf}: %{frekans:.2f}")

print("\nİlk 1000 karakterlik metnin harf frekansları:")
sonuc_1000 = frekans_analizi(metin[:1000])
for harf, frekans in sonuc_1000.items():
    print(f"{harf}: %{frekans:.2f}")


print("\nİlk 10000 karakterlik metnin harf frekansları:")
sonuc_10000 = frekans_analizi(metin[:10000])
for harf, frekans in sonuc_10000.items():
    print(f"{harf}: %{frekans:.2f}")
