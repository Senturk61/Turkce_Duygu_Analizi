# Türkçe Duygu Analizi Web Uygulaması

Bu proje, kullanıcı tarafından girilen Türkçe metinlerin duygu durumunu (Pozitif, Negatif, Nötr) analiz eden basit bir web uygulamasıdır. Hugging Face üzerinde eğitilmiş bir BERT modeli kullanılarak geliştirilmiştir.

<img width="1920" height="893" alt="image" src="https://github.com/user-attachments/assets/79b2a63e-3af3-4cc7-a500-56ebe5cfc208" />

<img width="1920" height="875" alt="image" src="https://github.com/user-attachments/assets/a323ac99-1a9c-4dce-a842-4cb0e021cc95" />


## Özellikler

-   Girilen Türkçe cümlenin anlık olarak duygu analizini yapar.
-   Analiz sonucunu "Pozitif", "Negatif" veya "Nötr" olarak etiketler.
-   Modelin tahminine olan güven skorunu yüzde olarak gösterir.
-   Basit, temiz ve kullanıcı dostu bir arayüze sahiptir.

## Kullanılan Teknolojiler

-   **Backend:** Python, Flask
-   **Frontend:** HTML, CSS, JavaScript (Fetch API)
-   **Doğal Dil İşleme (NLP):** Hugging Face `transformers` kütüphanesi
-   **Makine Öğrenmesi Modeli:** `savasy/bert-base-turkish-sentiment-cased`

## Kurulum ve Çalıştırma

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Projeyi klonlayın:**
    ```bash
    git clone [https://github.com/Senturk61/Turkce_Duygu_Analizi.git](https://github.com/Senturk61/Turkce_Duygu_Analizi.git)
    cd Turkce_Duygu_Analizi
    ```
    *(NOT: Yukarıdaki linki kendi GitHub linkinle değiştirmeyi unutma.)*

2.  **Sanal ortam (virtual environment) oluşturun ve aktive edin:**
    ```bash
    # Windows için
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux için
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Gerekli kütüphaneleri yükleyin:**
    Proje için gerekli tüm bağımlılıklar `requirements.txt` dosyasında listelenmiştir.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Flask sunucusunu başlatın:**
    ```bash
    python app.py
    ```
    Sunucu başlatıldığında, modelin ilk defa indirilmesi birkaç dakika sürebilir.

5.  **Uygulamaya erişin:**
    Web tarayıcınızı açın ve `http://127.0.0.1:5000` adresine gidin.

## Nasıl Çalışıyor?

Uygulamanın çalışma mantığı oldukça basittir:
1.  **Frontend:** Kullanıcı, metni HTML arayüzündeki text alanına girer ve butona tıklar. JavaScript, bu metni alarak backend'e bir `POST` isteği gönderir.
2.  **Backend:** Flask sunucusu, `/analyze` adresine gelen isteği karşılar. Gelen metni, uygulama başlarken yüklenmiş olan `BERT` modeline verir.
3.  **Model:** `savasy/bert-base-turkish-sentiment-cased` modeli, metni analiz eder ve bir duygu etiketi (`positive`, `negative`, `neutral`) ile güven skorunu üretir.
4.  **Sonuç:** Backend, modelden aldığı sonucu JSON formatında tekrar frontend'e gönderir. JavaScript, bu sonucu alarak ekrandaki sonuç kutusunu günceller ve kullanıcıya gösterir.
