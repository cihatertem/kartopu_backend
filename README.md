# 📪 Kartopu API

Kartopu, FastAPI tabanlı modüler bir backend servisidir. Geliştirme süreci Docker ve GitHub Actions ile otomatize edilmiştir.

## 🚀 Özellikler

- ⚡️ FastAPI ile modern Python backend
- 🐳 Docker container yapısı
- 🦾 Alembic ile veritabanı otomasyonu
- 📦 Uvicorn ile development sunucusu
- 🔄 Geliştirme ve production profilleri (docker-compose)
- 🛠️ GitHub Actions ile otomatik Docker Hub dağıtımı

---

## 📁 Proje Yapısı

```
.
├── alembic
│   ├── env.py            # Alembic ayar dosyası
│   ├── README
│   ├── script.py.mako    # Sqlmodel bu dosyada import edilmeli
│   └── versions          # Alembic revision versiyonları burada
├── alembic.ini
├── app
│   ├── crud
│   │   ├── category.py
│   │   ├── __init__.py
│   │   ├── post.py
│   │   ├── tag.py
│   │   └── user.py
│   ├── db
│   │   ├── __init__.py
│   │   └── session.py
│   ├── helpers
│   │   ├── auth.py
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── __init__.py
│   ├── main.py           # Uygulama giriş noktası
│   ├── models
│   │   ├── category.py
│   │   ├── __init__.py
│   │   ├── post.py
│   │   ├── tag.py
│   │   └── user.py
│   ├── routers
│   │   ├── category.py
│   │   ├── __init__.py
│   │   ├── post.py
│   │   ├── tag.py
│   │   └── user.py
│   └── schemas
│       ├── category.py
│       ├── __init__.py
│       ├── post.py
│       ├── tag.py
│       └── user.py
├── docker-compose.yml    # Profil tabanlı servis tanımı
├── Dockerfile            # Image tanımı
├── example.env           # Ortam değişkenleri örnek dosya
├── README.md             # Bu dosya
└── requirements.txt      # Python bağımlılıkları
```

---

## 🔪 Geliştirme

### 1. Sanal Ortam (opsiyonel)

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 2. Docker ile Başlat/Durdur

#### Başlat

```bash
docker-compose up --build
docker-compose up --build -d (Opsiyonel terminalden bağımsız çalıştırır)
```

- API: [http://localhost:11800](http://localhost:11800)
- Dokümantasyon: [http://localhost:11800/docs](http://localhost:11800/docs)

#### Durdur

```bash
docker-compose down
docker-compose down -v (Opsiyonel volumeleri de siler)
```

---

- `CMD` olarak `uvicorn` çalışır (Dockerfile'a bağlı)
- Hot-reload devre dışıdır. (Compose dosyasında ise aktif.)

---

## Alembic

### DEV ortamı

```bash
alembic init -t async alembic
```

komutu ile host/lokal geliştirme ortamında Alembic başlangıcı yapılır.

```bash
docker-compose exec backend alembic revision --autogenerate -m "XXX"
```

Revision oluşturma işlemleri init sürecinden farklı olarak servisler çalışırken compose ile yapılır.

```bash
docker-compose exec backend alembic upgrade head
```

Veritabanı/model değişiklikleri yine compose ile servisler çalışırken uygulanır.

---

## 🔐 Ortam Değişkenleri

`.env` dosyası desteklenmektedir. `docker-compose.yml` içinde yüklenebilir.
Örnek için `example.env`
Prod ortamında swarm secret/environment kullanılacak

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

```

```
