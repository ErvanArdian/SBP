
alternatives = [
    [7, 7, 9, 7, 1, 9, 1, 6],
    [4, 3, 5, 3, 3, 10, 7, 4],
    [5, 5, 7, 4, 9, 2, 6, 1],
    [9, 5, 10, 9, 7, 8, 6, 7],
    [10, 1, 9, 2, 10, 6, 10, 2],
    [6, 7, 2, 7, 10, 2, 8, 7],
    [10, 9, 10, 2, 6, 7, 10, 4],
    [7, 6, 6, 4, 7, 2, 3, 9],
    [4, 9, 9, 1, 6, 1, 6, 1],
    [9, 8, 2, 4, 5, 3, 2, 5],
    [4, 4, 2, 5, 4, 10, 6, 5],
    [10, 6, 9, 9, 10, 10, 2, 6],
    [6, 8, 8, 5, 4, 9, 2, 3],
    [8, 6, 3, 3, 6, 7, 8, 7],
    [4, 9, 3, 5, 10, 5, 10, 6],
    [6, 2, 7, 6, 5, 6, 5, 9],
    [8, 4, 1, 8, 3, 10, 7, 4],
    [4, 1, 8, 5, 10, 5, 2, 6],
    [9, 8, 9, 5, 1, 3, 10, 6],
    [3, 1, 10, 4, 7, 5, 10, 8]
]

weights = [0.2904, 0.2133, 0.1708, 0.0441, 0.1399, 0.0293, 0.0624, 0.0498]

# 1. Menentukan Solusi Rata-rata (AV)
average_solution = [sum(col) / len(col) for col in zip(*alternatives)]

# 2. Menghitung Jarak Positif / Negatif dari Rata-rata (PDA / NDA)
PDA = []
NDA = []

for row in alternatives:
    pda_row = []
    nda_row = []
    for val, avg in zip(row, average_solution):
        if val >= avg:
            pda_row.append(val - avg)
            nda_row.append(0)
        else:
            pda_row.append(0)
            nda_row.append(avg - val)
    PDA.append(pda_row)
    NDA.append(nda_row)

# 3. Menentukan Jumlah Terbobot dari PDA / NDA (SP / SN)
SP = [sum(p * w for p, w in zip(pda_row, weights)) for pda_row in PDA]
SN = [sum(n * w for n, w in zip(nda_row, weights)) for nda_row in NDA]

# 4. Normalisasi Nilai SP / SN (NSP / NSN)
SP_max = max(SP)
SN_max = max(SN)
NSP = [sp / SP_max for sp in SP]
NSN = [1 - (sn / SN_max) for sn in SN]

# 5. Menghitung Nilai Skor Penilaian (AS)
AS = [(nsp + nsn) / 2 for nsp, nsn in zip(NSP, NSN)]

# 6. Perangkingan
ranking = sorted(range(len(AS)), key=lambda i: AS[i], reverse=True)

# 7. Menghitung Skor Positif dan Negatif
positif_negatif_scores = [(NSP[i] - 0.5, NSN[i] - 0.5) for i in range(len(NSP))]

# 8. Menghitung Faktor Kombinasi (CF)
CF = [AS[i] - 0.5 for i in range(len(AS))]

# Output Skor Alternatif dan Faktor Kombinasi
print("Skor Alternatif:")
for i in range(len(positif_negatif_scores)):
    print(f"A{i+1}: Positif {positif_negatif_scores[i][0]:.4f}, Negatif {positif_negatif_scores[i][1]:.4f}")

print("\nCombination Factor (CF):")
for i in range(len(CF)):
    print(f"A{i+1}: {CF[i]:.4f}")

# Menentukan Alternatif Terbaik
best_alternative_index = ranking[0]
print(f"\nAlternatif terbaik adalah A{best_alternative_index + 1} dengan nilai CF {CF[best_alternative_index]:.4f}")
