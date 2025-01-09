import cv2
from ultralytics import YOLO

# Modeli yükle
model_path = "C:/Users/user/Desktop/best.pt"  # Modelinizin yolu
model = YOLO(model_path)

# Kamerayı başlat
cap = cv2.VideoCapture(0)  # 0, varsayılan kamerayı kullanır

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

# Gerçek zamanlı tahmin döngüsü
while True:
    ret, frame = cap.read()  # Kameradan bir kare al
    if not ret:
        print("Kare alınamadı, çıkılıyor...")
        break

    # Modeli çalıştır ve tahmin al
    results = model.predict(source=frame, conf=0.5, show=False)  # Tahmin eşiğini ayarlayın

    # Tahminleri görüntüye çizin
    annotated_frame = results[0].plot()

    # Görüntüyü ekranda göster
    cv2.imshow("Gercek Zamanli Tahmin", annotated_frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
