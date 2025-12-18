# import pandas as pd

# # 1. Data uji (5 sampel)
# data_uji = pd.DataFrame({
#     "Jam Belajar": [8, 6, 9, 5, 7],
#     "Nilai Sebelumnya": [80, 70, 85, 60, 75],
#     "Ekstrakurikuler": [1, 0, 1, 0, 1],
#     "Jam Tidur": [7, 6, 8, 6, 7],
#     "Latihan Soal": [5, 4, 6, 3, 5],
#     "Nilai Akhir Asli": [87, 78, 91, 72, 83]
# })

# # 2. Rumus Regresi Manual
# # Y^ = 11.23 + 1.85*X1 + 0.63*X2 + 3.17*X3 + 0.44*X4 + 1.56*X5
# def prediksi_manual(baris):
#     return (
#         11.23 +
#         1.85 * baris["Jam Belajar"] +
#         0.63 * baris["Nilai Sebelumnya"] +
#         3.17 * baris["Ekstrakurikuler"] +
#         0.44 * baris["Jam Tidur"] +
#         1.56 * baris["Latihan Soal"]
#     )

# # 3. Hitung prediksi & tampilkan hasil
# print("=== Prediksi Nilai Akhir Mahasiswa (Regresi Manual) ===")
# for i in range(len(data_uji)):
#     pred = prediksi_manual(data_uji.iloc[i])
#     actual = data_uji.iloc[i]["Nilai Akhir Asli"]
#     print(f"Data ke-{i+1}: Prediksi = {pred:.2f} | Aktual = {actual}")




# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error

# # 1. Data uji (dataset kecil dari soal kamu)
# data = pd.DataFrame({
#     "Jam Belajar": [8, 6, 9, 5, 7],
#     "Nilai Sebelumnya": [80, 70, 85, 60, 75],
#     "Ekstrakurikuler": [1, 0, 1, 0, 1],
#     "Jam Tidur": [7, 6, 8, 6, 7],
#     "Latihan Soal": [5, 4, 6, 3, 5],
#     "Nilai Akhir": [87, 78, 91, 72, 83]
# })

# # 2. Pisahkan fitur (X) dan target (y)
# X = data[["Jam Belajar", "Nilai Sebelumnya", "Ekstrakurikuler", "Jam Tidur", "Latihan Soal"]]
# y = data["Nilai Akhir"]

# # 3. Bangun model regresi linier
# model = LinearRegression()
# model.fit(X, y)

# # 4. Tampilkan hasil model
# print("=== Hasil Model LinearRegression ===")
# print(f"Intercept (β₀): {model.intercept_:.2f}")
# for nama, coef in zip(X.columns, model.coef_):
#     print(f"Koefisien {nama}: {coef:.2f}")

# # 5. Buat prediksi untuk data yang sama
# y_pred = model.predict(X)

# print("\n=== Hasil Prediksi vs Aktual ===")
# for i in range(len(y)):
#     print(f"Data ke-{i+1}: Prediksi = {y_pred[i]:.2f} | Aktual = {y.iloc[i]}")

# # 6. Evaluasi akurasi (optional)
# mae = mean_absolute_error(y, y_pred)
# print(f"\nMean Absolute Error (MAE): {mae:.2f}")