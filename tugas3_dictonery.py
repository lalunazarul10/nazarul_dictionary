kamus ={
    "kelapa":"kaya akan mamfaatnya",
    "jeruk": "mengandung vitamin A, B1, B2, dan C yang baik untuk sistem kekebalan tubuh",
    "apel": "buah berwarna merah atau hijau",
}

kata = input("masukkan kata yang ingin anda cari artinya:")

if kata in kamus:
    print(f"Arti dari'[kelapa]'adalah:""[kaya akan mamfaatnya]}")

kata = input("masukkan kata yang ingin anda cari artinya:")

if kata in kamus:
    print(f" Arti dari'[jeruk]' adalah:""[mengandung vitamin A, B1, B2, dan C yang baik untuk sistem kekebalan tubuh]}")

kata = input("masukkan kata yang ingin anda cari artinya:")

if kata in kamus:
    print(f" Arti dari'[apel]'adalah:""[buah berwarna merah atau hijau]}")
else:
    print("maaf,arti dari kata yang anda cari'[kata]'tidak ditemukan dalam kamus,coba lagi nanti).")
