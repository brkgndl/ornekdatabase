import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase_app():
   # firebase ' i başlatma
    try:
        cred = credentials.Certificate("/Users/burakg/Desktop/ornekdatabase-39322-firebase-adminsdk-o9t71-be6d13e691.json")
        firebase_admin.initialize_app(cred)
        print("Firebase başlatıldı.")
        return firestore.client()
    except Exception as e:
        print(f"Firebase başlatılamadı: {e}")
        return None

def add_user_input_data(client):
    # kullanıcıdan veriyi alıp veritabanına kaydeden fonksiyon
    try:
        name = input("Kullanıcı adı: ").strip()
        age = int(input("Yaş: "))
        city = input("Şehir: ").strip()

        user_data = {
            "name": name,
            "age": age,
            "city": city
        }

        client.collection("users").add(user_data)
        print("Kullanıcı başarıyla eklendi.")
    except Exception as e:
        print(f"Kullanıcı eklenemedi: {e}")

def list_documents(client):
    # tüm kullanıcı listesini bastırma
    try:
        print("\n Kayıtlı tüm kullanıcılar listeleniyor")
        docs = client.collection("users").stream()

        for doc in docs:
            print(f"Doküman ID: {doc.id}, Veri: {doc.to_dict()}")
    except Exception as e:
        print(f"Veriler okunamadı: {e}")

def main():
    # Firebase uygulamasını başlat
    client = initialize_firebase_app()
    if not client:
        return

    # Kullanıcıdan veri al ve Firestore'a ekle
    add_user_input_data(client)

    # Verileri listele
    list_documents(client)

if __name__ == "__main__":
    main()