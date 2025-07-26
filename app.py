# Gerekli kütüphaneleri ve modülleri içeri aktarıyoruz
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# Flask web uygulamasını başlatıyoruz
app = Flask(__name__)

# Uygulama başlarken modeli bir kereliğine belleğe yüklüyoruz
# Bu, her istekte modeli tekrar yüklemek yerine performansı artırır
print("Duygu analizi modeli yükleniyor... Bu işlem biraz zaman alabilir.")
sentiment_pipeline = pipeline("sentiment-analysis", model="savasy/bert-base-turkish-sentiment-cased")
print("Model başarıyla yüklendi. Sunucu istekleri kabul etmeye hazır.")

# Ana sayfa ('/') için bir yol (route) tanımlıyoruz
# Kullanıcı http://127.0.0.1:5000 adresine girdiğinde bu fonksiyon çalışır
@app.route('/')
def home():
    # 'templates' klasöründeki 'index.html' dosyasını kullanıcıya gönderir
    return render_template('index.html')

# Analiz işlemi için '/analyze' yolunu tanımlıyoruz
# Sadece POST isteklerini kabul eder
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Tarayıcıdan gönderilen JSON verisini alıyoruz
    data = request.get_json()
    
    # Gelen verinin boş olup olmadığını kontrol ediyoruz
    if not data or 'text' not in data or not data['text'].strip():
        return jsonify({'error': 'Lütfen analiz için bir metin girin.'}), 400
    
    text_to_analyze = data['text']
    
    # Metni duygu analizi modeline gönderiyoruz
    result = sentiment_pipeline(text_to_analyze)[0]
    
    # Modelin çıktısını ('positive', 'negative', 'neutral')
    # bizim istediğimiz formata ('Pozitif', 'Negatif', 'Nötr') çeviriyoruz.
    # *** SORUNU ÇÖZEN DÜZELTME BURADA ***
    label_map = {
        'positive': 'Pozitif',
        'negative': 'Negatif',
        'neutral': 'Nötr'
    }
    
    # Tarayıcıya göndereceğimiz cevabı hazırlıyoruz
    response = {
        'text': text_to_analyze,
        'sentiment': label_map.get(result['label'].lower(), 'Bilinmiyor'), # .lower() ekleyerek büyük/küçük harf sorununu da engelleriz
        'confidence_score': result['score']
    }
    
    # Hazırladığımız cevabı JSON formatında geri gönderiyoruz
    return jsonify(response)

# Bu dosya doğrudan çalıştırıldığında sunucuyu başlat
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
