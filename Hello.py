# menentukan tujuan dengan kriteria yang bertentangan
# Menghitung skor MOORA untuk setiap alternatif dengan menggunakan rasio antara 
# nilai alternatif tersebut dengan solusi ideal positif dan solusi ideal negatif.
import streamlit as st # mengimpor library streamlit dengan alias st, agar aplikasi web yang kita rangkai interaktif
from streamlit_echarts import st_echarts # untuk visualisasi echart atau grafik interaktif pada saat program berhasil dijalankan
import json # Memanipulasi data menggunakan format json
import numpy as np # agar dapat mengekseskusi kode np
# numpy juga digunakan untuk operasi matermatika dan manipulasi array multideminsional

def moora_method(data_matrix, weights): # Mendefinisikan fungsi moora_method yang menerima matriks data data_matrix dan bobot weights, agar dapat menghitung skor MOORA berdasarkan matriks data dan bobot
    normalized_matrix = data_matrix / np.linalg.norm(data_matrix, axis=0)
    weighted_matrix = normalized_matrix * weights
    score = np.sum(weighted_matrix, axis=1)
    return score

def main(): # penjabaran data
    st.title("Sistem Pendukung Keputusan Melalui Metode MOORA")

    # Form input data oleh user, menampilkan numerik
    criteria1 = st.number_input("Kriteria 1:")
    criteria2 = st.number_input("Kriteria 2:")
    criteria3 = st.number_input("Kriteria 3:")

    weights = { # multikriteria
        'Kriteria 1': st.slider('Bobot Kriteria 1', 0.0, 1.0, 0.3), # widget slider interaktif horizontal
        'Kriteria 2': st.slider('Bobot Kriteria 2', 0.0, 1.0, 0.3),
        'Kriteria 3': st.slider('Bobot Kriteria 3', 0.0, 1.0, 0.3),
    }

    if st.button("Hitung"): # tombol Hitung untuk perhitungan saat tombol di klik
        # Masukkan data ke dalam matriks agar dapat ditampilkan nantinya
        data_matrix = np.array([criteria1, criteria2, criteria3])

        # Memberikan bobot pada setiap kriteria pada data
        weights_values = np.array(list(weights.values()))

        # Mengubah data_matrix menjadi data_matrix.reshape(-1, 1)
        # -1 baris, 1 kolom
        scores = moora_method(data_matrix.reshape(-1, 1), weights_values) # moora_method digunakan untuk memasukkan data ke dalam matriks dan
        # memberikan bobot pada setiap kriteria, serta menghitung skor dengan fungsi

        # Menampilkan hasil eksekusi
        st.subheader("Hasil MOORA")
        st.write("Skor Kriteria:")
        st.write(scores)

        # Menspesifikasi visualisasi ECharts dinamis berdasarkan skor yang dihitung
        vis_spec = {
            "title": {"text": "Hasil MOORA - Skor Kriteria"},
            "xAxis": {"type": "category", "data": ["Kriteria 1", "Kriteria 2", "Kriteria 3"]},
            "yAxis": {"type": "value"},
            "series": [{"data": scores.tolist(), "type": "bar"}]
        }

        # Memvisualisasikan hasil dengan ECharts
        st_echarts(options=vis_spec)

if __name__ == '__main__': # Menjalankan fungsi main jika skrip dijalankan sebagai program utama
    main()
