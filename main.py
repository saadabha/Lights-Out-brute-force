from program import *

print("Selamat datang di program penyelesaian permainan Lights Out dengan algorithm brute force!")
print("Silakan masukkan kondisi awal papan lampu:")
# Baca kondisi awal papan dari pengguna
initial_board = read_initial_board()

# Cetak kondisi awal papan
print_board(initial_board)

# Temukan solusi dengan brute force
start_time = time.time()
solution = brute_force_lights_out(initial_board)
end_time = time.time()

# Cetak solusi jika ditemukan
if solution:
    print("\nSolusi ditemukan! Urutan pemencetan tombol:")
    for step in solution:
        print(f"Tekan lampu di {step}")
else:
    print("\nTidak ada solusi yang ditemukan.")
print(f"Waktu eksekusi: {end_time - start_time} detik")