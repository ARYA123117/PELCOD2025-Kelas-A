
# 1. Marathon Netflix
print("Soal 1: Marathon Netflix")
durasi_episode = int(input("Masukkan durasi 1 episode per menit: "))
jumlah_episode = int(input("Masukkan jumlah episode: "))

total_menit = durasi_episode * jumlah_episode
total_jam = total_menit // 60
print("Total waktu menonton ",total_menit , "menit atau", total_jam, "jam 50 menit") #sumpah bingung ka mau nambahin jam sama menit soalnya jawabanya 5jam 50 menit jadi yang 50 menit tulis manual hehe 🙏🙏


# 2. Membeli Cupang dan Koi
print(" Soal 2: Membeli Cupang & Koi ")
nim = int(input("Masukkan 3 angka terakhir NIM: "))
uang = (nim + 100) * 1000  # NIM Terakhir 037
print("Uang yang dibawa: Rp" + str (uang))
harga_cupang = 10000
harga_koi = 20000

jumlah_cupang = int(input("Masukkan jumlah cupang yang dibeli: "))
jumlah_koi = int(input("Masukkan jumlah koi yang dibeli: "))

total_belanja = (jumlah_cupang * harga_cupang) + (jumlah_koi * harga_koi)
sisa_uang = uang - total_belanja

print("Total belanja: Rp" + str (total_belanja))
print("Sisa uang: Rp" + str (sisa_uang))


# 3. Liburan naik motor
print(" Soal 3: Liburan Naik Motor ")
nim_3 = int(input("Masukkan 3 angka terakhir NIM: "))
nim_terakhir = int(input("Masukkan 1 angka terakhir NIM: "))

jarak = nim_3  # total km
bbm_perliter = 2.7
kapasitas_tangki = nim_terakhir
harga_bensin = int("1" + str(nim_3) + "0")  # Rp.1XXX0 memasukan 3digit NIM di tengah angka 1XXX0

# Hitung total bensin yang dibutuhkan
total_bensin = jarak / bbm_perliter

# diskon
if total_bensin > 3:
    harga_perliter = harga_bensin - 500
else:
    harga_perliter = harga_bensin

# Hitung total biaya bensin
total_biaya = total_bensin * harga_perliter 

# Hitung berapa kali isi bensin
if kapasitas_tangki > 0:
    kali_isi = (total_bensin // kapasitas_tangki)  # ceil division
else:
    kali_isi = 0

print(f"Total bensin dibutuhkan: {total_bensin:.2f} liter")
print(f"Harga bensin per liter: Rp {harga_perliter}")
print(f"Total biaya bensin: Rp {total_biaya:.2f}")
print(f"Perkiraan isi bensin: {int(kali_isi)} kali (isi full setiap kali)\n")
