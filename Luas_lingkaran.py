luas_lingkaran = lambda r: 3.14 * r ** 2

print("======== LUAS LINGKARAN ========")

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} = {luas:.2f}")