import cv2

# Carrega o classificador Haar Cascade pré-treinado para detecção de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicia a captura de vídeo a partir da webcam (o '0' refere-se à primeira webcam conectada)
cap = cv2.VideoCapture(0)

print("Pressione 'Q' para sair.")

while True:
    # Lê o frame atual da webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Converte o frame para escala de cinza, pois o classificador trabalha com imagens em tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    scaleFactor_param = 1.1
    minNeighbors_param = 5

    # Detecta as faces no frame em escala de cinza
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scaleFactor_param,
        minNeighbors=minNeighbors_param,
        minSize=(30, 30) # Tamanho mínimo do objeto a ser detectado
    )

    # Exibe os parâmetros na tela
    cv2.putText(frame, f'scaleFactor: {scaleFactor_param}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f'minNeighbors: {minNeighbors_param}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Desenha um retângulo ao redor de cada face detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # (0, 255, 0) é a cor verde

    # Exibe o frame resultante em uma janela chamada 'Detector de Face'
    cv2.imshow('Detector de Face', frame)

    # Aguarda a tecla 'q' ser pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura da webcam e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()
