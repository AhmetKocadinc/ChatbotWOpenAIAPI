import openai
import streamlit as st

# OpenAI API anahtarını gir
openai.api_key = "YOUR_API_KEY"

# Sağlıkla ilgili anahtar kelimeler listesi
saglik_kelime_listesi = [
    "kanser", "diyabet", "hipertansiyon", "koroner arter hastalığı", "astım", "KOAH", 
    "Alzheimer", "Parkinson", "MS", "AIDS", "HIV", "obezite", "depresyon", "anksiyete bozukluğu", 
    "bipolar bozukluk", "şizofreni", "migren", "epilepsi", "enfeksiyon", "gripal enfeksiyon", 
    "tüberküloz", "hepatit", "romatizma", "sedef hastalığı", "cilt kanseri", "prostat kanseri", 
    "meme kanseri", "bağırsak kanseri", "kalp yetmezliği", "felç", "tansiyon", "anemi", "mide bulantısı",
    
    "aile hekimliği", "pediatri", "kadın doğum", "geriatri", "psikiyatri", "diş hekimliği", 
    "kardiyoloji", "onkoloji", "nöroloji", "ortopedi", "dermatoloji", "fizyoterapi", 
    "diyetisyenlik", "eczacılık", "hemşirelik", "yoğun bakım", "acil servis", "ameliyat", 
    "ilaç tedavisi", "rehabilitasyon",

    "kan testi", "biyopsi", "MR", "CT", "röntgen", "ultrason", "EKG", "kolonoskopi", 
    "endoskopi", "PET tarama", "laparoskopi", "tansiyon ölçümü", "aşılar", "DNA testi", 
    "kan şekeri testi", "karaciğer fonksiyon testi", "hormon testi", "göz muayenesi",

    "tansiyon aleti", "glikometre", "insülin pompası", "kalp pili", "ventilatör", "defibrilatör", 
    "diş protezi", "gözlük", "kontakt lens", "protez bacak", "koltuk değneği", "MR cihazı", 
    "BT cihazı", "ultrason cihazı", "termometre", "nebülizatör",

    "diyet", "keto diyeti", "Akdeniz diyeti", "veganizm", "vejetaryen beslenme", "protein", 
    "karbonhidrat", "yağlar", "vitaminler", "mineraller", "antioksidanlar", "probiyotikler", 
    "su tüketimi", "kalori hesabı", "lifli besinler", "diyet takviyeleri", "sporcu beslenmesi", 
    "oruç", "organik gıda", "GDO",

    "stres yönetimi", "meditasyon", "mindfulness", "yoga", "psikoterapi", "CBT", "depresyon", 
    "travma sonrası stres bozukluğu", "psikoz", "uykusuzluk", "uyku bozukluğu", "panik atak", 
    "sosyal anksiyete", "madde bağımlılığı", "alkol bağımlılığı", "ruh sağlığı", "öz saygı", 
    "zihinsel sağlık",

    "aerobik", "kardiyo", "ağırlık antrenmanı", "koşu", "yüzme", "bisiklet", "pilates", 
    "güçlendirme egzersizleri", "esneme", "vücut geliştirme", "fitness", "HIIT", "duruş bozukluğu", 
    "kalori yakma", "vücut kitle indeksi",

    "sağlık sigortası", "koruyucu sağlık", "sağlıkta eşitlik", "hijyen", "bağışıklık sistemi", 
    "alerji", "genetik", "yaşlanma", "uyku", "yaşam kalitesi", "kronik hastalık", 
    "enfeksiyon kontrolü", "iyileşme", "reçetesiz ilaçlar", "zatürre", "doğum kontrolü", 
    "tıbbi yardım", "akupunktur", "alternatif tıp",

    "antibiyotikler", "antidepresanlar", "antihistaminikler", "ağrı kesiciler", "kortikosteroidler", 
    "insülin", "aşılar", "kemoterapi ilaçları", "antiviral ilaçlar", "steroidler", "tansiyon düşürücüler", 
    "kolesterol düşürücüler", "kan sulandırıcılar", "diyabet ilaçları", "uyku hapları", 
    "antipsikotik ilaçlar", "anestezi",

    "halk sağlığı", "epidemiyoloji", "pandemi", "karantina", "aşılama", "sağlık bakanlığı", 
    "Dünya Sağlık Örgütü", "kamu sağlığı kampanyaları", "sağlık reformu", "sağlık sigortası poliçeleri", 
    "klinik araştırmalar", "sağlıkta dijitalleşme", "teletıp", "tıbbi yapay zeka", 
    "uzaktan sağlık hizmetleri"
]
# Chatbot fonksiyonu
def chatbot_sorusu(soru):
    # Soruda sağlıkla ilgili anahtar kelimeler var mı diye kontrol edelim
    if any(kelime in soru.lower() for kelime in saglik_kelime_listesi):
        yanit = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": soru}],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return yanit.choices[0].message['content'].strip()
    else:
        return "Üzgünüm, sadece sağlık konularında yardımcı olabilirim."

# Streamlit arayüzü
st.title("Sağlık Chatbotu")

# Sohbet geçmişini tutmak için bir session state
if 'sohbet_gecmisi' not in st.session_state:
    st.session_state.sohbet_gecmisi = []

# Kullanıcıdan soruyu alma
soru = st.text_input("Sorunuzu girin:")

# Soruyu gönder ve cevap al
if st.button("Gönder"):
    if soru:
        cevap = chatbot_sorusu(soru)
        # Soru ve cevabı sohbet geçmişine ekle
        st.session_state.sohbet_gecmisi.append({"soru": soru, "cevap": cevap})

# Sohbet geçmişini ekranda göster
if st.session_state.sohbet_gecmisi:
    for sohbet in st.session_state.sohbet_gecmisi:
        st.write(f"**Siz**: {sohbet['soru']}")
        st.write(f"**Chatbot**: {sohbet['cevap']}")
