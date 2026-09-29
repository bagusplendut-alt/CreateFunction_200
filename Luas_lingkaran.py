import math
luas_lingkaran = lambda r: math.pi * r ** 2

print("======== LUAS LINGKARAN ========")

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} = {luas:.2f}")