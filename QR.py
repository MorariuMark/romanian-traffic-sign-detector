import cv2
from pyzbar.pyzbar import decode
import webbrowser
import time

# Inițializăm camera web (0 este de obicei camera integrată)
cap = cv2.VideoCapture(0)

# Folosim un set pentru a nu deschide același link de mai multe ori la rând
linkuri_accesate = set()

print("Programul rulează. Apasă 'q' pentru a ieși.")

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Detectăm codurile QR din cadrul curent
    for code in decode(frame):
        # Decodăm datele (link-ul)
        url = code.data.decode('utf-8')
        
        # Verificăm dacă este un link nou pentru a evita deschiderea infinită
        if url not in linkuri_accesate:
            print(f"Detectat: {url}")
            
            # Verificăm dacă textul pare să fie un URL
            if url.startswith("http"):
                webbrowser.open(url)
                linkuri_accesate.add(url)
                # Mică pauză pentru a nu copleși browserul
                time.sleep(2)
        
        # Desenăm un dreptunghi în jurul codului detectat pentru feedback vizual
        pts = code.polygon
        if len(pts) > 0:
            import numpy as np
            pts = np.array([pts], np.int32)
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)

    # Afișăm fereastra video
    cv2.imshow('QR Scanner - Apasa Q pentru inchidere', frame)

    # Închidere la apăsarea tastei 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Eliberăm resursele
cap.release()
cv2.destroyAllWindows()