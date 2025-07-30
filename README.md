# 📪 Kartopu API

Kartopu, FastAPI tabanlı modüler bir backend servisidir. Geliştirme süreci Docker ve GitHub Actions ile otomatize edilmiştir.

## 🚀 Özellikler

- ⚡️ FastAPI ile modern Python backend
- 🐳 Docker container yapısı
- 📦 Uvicorn ile development sunucusu
- 🔄 Geliştirme ve production profilleri (docker-compose)
- 🛠️ GitHub Actions ile otomatik Docker Hub dağıtımı

---

## 📁 Proje Yapısı

```
.
├── app/
│   ├── __init__.py
│   └── main.py         # Uygulama giriş noktası
├── Dockerfile          # Image tanımı
├── docker-compose.yml  # Profil tabanlı servis tanımı
├── requirements.txt    # Python bağımlılıkları
└── README.md           # Bu dosya
```

---

## 🔪 Geliştirme

### 1. Sanal Ortam (opsiyonel)

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 2. Docker ile Başlat

```bash
docker compose --profile dev up --build
```

- API: [http://localhost:11800](http://localhost:11800)
- Dokümantasyon: [http://localhost:11800/docs](http://localhost:11800/docs)

---

## ⚙️ Production

```bash
docker compose --profile prod up --build -d
```

- `CMD` olarak `uvicorn` çalışır (Dockerfile'a bağlı)
- Hot-reload devre dışıdır

---

## 🔐 Ortam Değişkenleri

**TODO** `.env` dosyası desteklenmektedir. `docker-compose.yml` içinde yüklenebilir.

---

## 🐙 CI/CD - Docker Hub

Bu proje GitHub Actions kullanarak her `main` push’unda Docker Hub’a image gönderir.

### Örnek workflow:

- `docker build -t ndhakara/kartopu .`
- `docker push ndhakara/kartopu`

---

## 📬 İletişim

Cihat Ertem – cihatertem\@gmail.com

---

## 📝 Lisans

MIT License
