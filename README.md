# 📊 Customer Churn Analysis & Prediction with PySpark

Bu proje, bir şirketin müşteri verilerini kullanarak hangi müşterilerin ayrılma (churn) eğiliminde olduğunu tahmin eden uçtan uca bir makine öğrenmesi çözümüdür. **PySpark** ile eğitilen model, **Streamlit** kullanılarak interaktif bir web arayüzüne dönüştürülmüştür.

## 🚀 Proje Özeti (Project Overview)
Müşteri kaybını önlemek, yeni müşteri kazanmaktan çok daha maliyetlidir. Bu projede:
- **Büyük Veri İşleme:** PySpark kullanılarak ham veri temizlendi ve analiz edildi.
- **Model Eğitimi:** Lojistik Regresyon (Logistic Regression) algoritması kullanıldı.
- **Hassas Tahmin (Threshold Tuning):** Giden müşterileri kaçırmamak adına model eşiği **0.19** olarak optimize edildi.
- **Deployment:** Eğitilen modelin matematiksel katsayıları kullanılarak hızlı, hatasız ve Spark bağımlılığı olmayan bir web arayüzü (Streamlit) geliştirildi.

---

## 🛠️ Kullanılan Teknolojiler (Tech Stack)
- **Veri İşleme Kısmı:** PySpark (Spark SQL & MLlib)
- **Model:** Logistic Regression
- **Web Uygulaması:** Streamlit
- **Görselleştirme:** Seaborn, Matplotlib
- **Language:** Python

---

## 📈 Model Performansı (Model Performance)
Model, giden müşterileri (True Positives) yakalamaya odaklanmıştır. **0.19 eşik değeri (threshold)** ile elde edilen sonuçlar:

| Metrik | Değer |
| :--- | :--- |
| **Doğru Yakalanan Kayıplar (TP)** | 45 / 59 (%76 Başarı) |
| **Doğru Bilinen Sadıklar (TN)** | 191 / 218 |
| **Model Eşiği (Threshold)** | 0.19 |

> **Neden 0.19?** İş mantığı gereği, giden bir müşteriyi kaçırmak, sadık bir müşteriye yanlışlıkla "gidebilir" demekten daha risklidir (Recall vs Precision). Bu yüzden model daha hassas hale getirilmiştir.

---

## 💻 Uygulama Nasıl Çalıştırılır? (How to Run)

1. **Gereksinimleri Kurun:**
pip install streamlit

2.**Uygulamayı Başlatın:**
streamlit run app.py

3.**Test Edin:**
Arayüzdeki "🔴 Riskli Müşteri" senaryosunu seçerek modelin yüksek riskli profilleri nasıl ayırt ettiğini gözlemleyebilirsiniz.

📄 Dosya Yapısı (Project Structure)
proje.ipynb: Veri analizi, görselleştirme ve PySpark model eğitim süreci.

app.py: Streamlit web arayüzü ve matematiksel tahmin motoru.

requirements.txt: Gerekli kütüphaneler listesi.

NOT : Projenin kalbi olan büyük veri analizi, lojistik regresyon modelinin eğitilmesi ve threshold (eşik) optimizasyonları tamamen PySpark üzerinde tarafımca olarak geliştirilmiştir. Modelin hızlı bir şekilde canlıya alınması (Deployment) sürecinde, Streamlit arayüzünün kodlanması için yapay zekadan destek alınmıştır.

