import streamlit as st
import math


COEFFICIENTS = [
    0.0653872021755002, 
    0.00006646381318777323, 
    0.39936885567369096, 
    0.4214680872656263, 
    1.2479228890706007
]
INTERCEPT = -19.60367907430692


st.set_page_config(page_title="Müşteri Kayıp (Churn) Analizi", page_icon="📊", layout="centered")
st.title("📊 Müşteri Kayıp (Churn) Tahmin Modeli")
st.markdown("""
Bu uygulama, Lojistik Regresyon modeli kullanarak bir müşterinin şirketi terk etme (churn) riskini hesaplar. 
Model eşiği (Threshold) **0.19** olarak belirlenmiştir.
""")


st.sidebar.header("1. Hızlı Test Senaryosu Seçin")
st.sidebar.info("Modelin nasıl çalıştığını görmek için hazır profilleri kullanabilirsiniz.")

senaryo = st.sidebar.selectbox(
    "Müşteri Profili:",
    ["Manuel Giriş Yap", "🔴 Riskli Müşteri (Churn Eğilimi)", "🟢 Sadık Müşteri (Güvenli)"]
)

# Senaryolara göre varsayılan değerleri ayarlama
if senaryo == "🔴 Riskli Müşteri (Churn Eğilimi)":
    d_age, d_purch, d_acc, d_years, d_sites = 55, 12000.0, 0, 7.0, 13
elif senaryo == "🟢 Sadık Müşteri (Güvenli)":
    d_age, d_purch, d_acc, d_years, d_sites = 30, 5000.0, 1, 3.0, 4
else:
    d_age, d_purch, d_acc, d_years, d_sites = 40, 8000.0, 0, 5.0, 8

# --- 4. KULLANICI GİRİŞLERİ ---
st.sidebar.markdown("---")
st.sidebar.header("2. Parametreleri Düzenleyin")

age = st.sidebar.number_input("Yaş (Age)", 18, 100, value=int(d_age))
total_purchase = st.sidebar.number_input("Toplam Satın Alım", 0.0, 100000.0, value=float(d_purch))
account_manager = st.sidebar.selectbox("Müşteri Temsilcisi (0: Yok, 1: Var)", [0, 1], index=int(d_acc))
years = st.sidebar.number_input("Şirketle Çalışılan Yıl", 0.0, 50.0, value=float(d_years))
num_sites = st.sidebar.number_input("Kullanılan Site Sayısı", 0, 50, value=int(d_sites))

# --- 5. HESAPLAMA VE GÖRSELLEŞTİRME ---
if st.button("Risk Analizini Başlat", use_container_width=True):
    # Formül hesaplaması
    z = INTERCEPT + (
        COEFFICIENTS[0] * age +
        COEFFICIENTS[1] * total_purchase +
        COEFFICIENTS[2] * account_manager +
        COEFFICIENTS[3] * years +
        COEFFICIENTS[4] * num_sites
    )
    
    risk_orani = 1 / (1 + math.exp(-z))
    risk_yuzdesi = risk_orani * 100

    st.markdown("---")
    
    # Görsel Metrik Gösterimi
    st.metric(label="Hesaplanan Churn (Kayıp) İhtimali", value=f"%{risk_yuzdesi:.2f}")
    
    # İlerleme Çubuğu (Progress Bar)
    ilerleme_degeri = min(int(risk_yuzdesi), 100) # 100'ü geçmesin diye
    st.progress(ilerleme_degeri)

    # 0.19 EŞİĞİ KARARI
    if risk_orani >= 0.19:
        st.error(f"🚨 **YÜKSEK RİSK!** Model bu müşterinin ayrılabileceğini öngörüyor (Risk: %{risk_yuzdesi:.1f})")
        st.warning("Eylem: Müşteri temsilcisi atanmalı ve sadakat kampanyası sunulmalı.")
    else:
        st.success(f"✅ **GÜVENLİ.** Müşterinin sadık kalma ihtimali yüksek (Risk: %{risk_yuzdesi:.1f})")

       
with st.expander("📊 Model Performansı ve Teknik Detaylar (İncele)"):
    st.markdown("""
    **Test Verisi Sonuçları (Confusion Matrix - 0.19 Threshold):**
    * **Doğru Yakalanan Kayıplar (TP):** 45 *(Gidenlerin %76'sı başarıyla tespit edildi)*
    * **Doğru Bilinen Sadık Müşteriler (TN):** 191
    * **Yanlış Alarmlar (FP):** 27 *(Riski minimize etmek için göze alınan sapma)*
    """)