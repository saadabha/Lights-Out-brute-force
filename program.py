import itertools
import time

# Fungsi untuk mengubah status lampu (on/off)
def toggle(board, x, y):
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        board[x][y] = 1 - board[x][y]

# Fungsi untuk menekan lampu dan lampu-lampu tetangganya
def press(board, x, y):
    toggle(board, x, y)
    toggle(board, x+1, y)
    toggle(board, x-1, y)
    toggle(board, x, y+1)
    toggle(board, x, y-1)

# Fungsi untuk menerapkan kombinasi penekanan pada papan
def apply_combination(board, combination, steps):
    for i in range(len(combination)):
        if combination[i]:
            x = i // len(board[0])
            y = i % len(board[0])
            press(board, x, y)
            steps.append((x, y))

# Fungsi untuk memeriksa apakah semua lampu mati
def all_off(board):
    return all(cell == 0 for row in board for cell in row)

# Fungsi utama brute force untuk menemukan solusi
def brute_force_lights_out(board):
    n = len(board)
    m = len(board[0])
    steps = []
    for combination in itertools.product([False, True], repeat=n*m):
        temp_board = [row[:] for row in board]
        apply_combination(temp_board, combination, steps)
        if all_off(temp_board):
            return steps
        steps.clear()  # Kosongkan langkah jika tidak menemukan solusi
    return None

# Fungsi untuk membaca kondisi awal papan dari pengguna
def read_initial_board():
    print("Masukkan jumlah baris dan kolom papan lampu (n x m):")
    n = int(input("Masukkan jumlah baris: "))
    m = int(input("Masukkan jumlah kolom: "))
    print("Masukkan kondisi awal papan tiap baris (gunakan 0 untuk lampu mati dan 1 untuk lampu hidup):")
    board = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print("Jumlah kolom tidak sesuai!")
            return read_initial_board()
        board.append(row)
    return board

# Fungsi untuk mencetak kondisi papan
def print_board(board):
    print("Kondisi papan saat ini:")
    for row in board:
        print(" ".join(map(str, row)))

# # Contoh papan 5x5 dengan semua lampu menyala (1 artinya nyala, 0 artinya mati)
# initial_board = [[1] * 5 for _ in range(5)]
