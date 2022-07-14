"""
# **Implementación del modelo con la Cámara Web**

* Se accede a la webcam
* Se implementa la función `eye_cropper` para optimizar cada imagen suelta para el modelo
* Pasar el fotograma recortado del ojo por el modelo para predecir si está cerrado o no
* Si la predicción da que el sujeto está cerrando los ojos durante más de un determinado número de fotogramas, entonces lo alerta con un sonido
"""

# Para la inicialización de la cámara y la visión por computador
import cv2
# Librería que define tipos de datos representadas como matrices multidimensionales
import numpy as np
# playsound ejecuta sonidos de alerta
from playsound import playsound
#PIL permite la edicion de imágenes desde Python
#Image provee funciones para cargar imagenes desde archivos
#ImageDraw provee funcionalidades de graficos en 2D en objetos de Image, creando nuevas imagenes, retoque y anotación de imagenes
from PIL import Image, ImageDraw
#El modulo "face_recognition" es necesario para la detección y reconocimiento de rostros
import face_recognition
#Importar la biblioteca Keras para el trabajo de DeepLearning que puede funcionar sobre TensorFlow
from tensorflow import keras
#Serial: Conexión con el serial del arduino
import serial

#Abrimos el puerto serial del Arduino
arduino = serial.Serial("COM4", 9600)

#Nos aseguramos de especificar la ruta del mejor modelo que hemos obtenido
eye_model = keras.models.load_model('best_model5.h5')

def eye_cropper(frame):

    #Crear una variable para las coordenadas de los rasgos faciales
    facial_features_list = face_recognition.face_landmarks(frame)

    # Se crea un array para marcar la posición de las coordenadas de los ojos
    # y añadimos las coordenadas de los ojos que no hayan sido encontrados
    try:
        eye = facial_features_list[0]['left_eye']
    except:
        try:
            eye = facial_features_list[0]['right_eye']
        except:
            return



    # Establecemos las coordenadas X y Y maximas de los ojos
    x_max = max([coordinate[0] for coordinate in eye])
    x_min = min([coordinate[0] for coordinate in eye])
    y_max = max([coordinate[1] for coordinate in eye])
    y_min = min([coordinate[1] for coordinate in eye])


    # Establecemos el rango de las coordenadas X y Y
    x_range = x_max - x_min
    y_range = y_max - y_min

    # Para asegurar que el ojo entero es capturado, calcular las coordenadas de un cuadrado que tenga
    # 50% de brecha al eje mayor y hacerlo coincidir el rango menor con el rango mayor
    if x_range > y_range:
        right = round(.5*x_range) + x_max
        left = x_min - round(.5*x_range)
        bottom = round((((right-left) - y_range))/2) + y_max
        top = y_min - round((((right-left) - y_range))/2)
    else:
        bottom = round(.5*y_range) + y_max
        top = y_min - round(.5*y_range)
        right = round((((bottom-top) - x_range))/2) + x_max
        left = x_min - round((((bottom-top) - x_range))/2)


    #Recortamos la imagen de acuerdo a las coordenadas determinadas anteriormente
    cropped = frame[top:(bottom + 1), left:(right + 1)]

    # Redimensionamos la imagen
    cropped = cv2.resize(cropped, (80,80))
    image_for_prediction = cropped.reshape(-1, 80, 80, 3)

    return image_for_prediction


# Iniciamos la Webcam
cap = cv2.VideoCapture(0)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(cap.get(cv2.CAP_PROP_FPS))

if not cap.isOpened():
    raise IOError('No se pudo abrir la webcam')

# Establecemos un contador
counter = 0

# Crear un bucle while que se ejecuta mientras la cámara esta en uso

while True:

    # Capturamos los fotogramas que son emitidos por la cámara
    ret, frame = cap.read()

    # Utilizamos cada dos fotogramas para gestionar la velocidad y el uso de la memoria
    frame_count = 0
    if frame_count == 0:
        frame_count += 1
        pass
    else:
        count = 0
        continue

    # Mandamos el frame a la función eye_cropper que nos retornará una imagen recortada para hacer la predicción
    image_for_prediction = eye_cropper(frame)
    try:
        image_for_prediction = image_for_prediction / 255.0
    except:
        continue

    # Obtenemos la predicción del modelo
    prediction = eye_model.predict(image_for_prediction)

    #Basado en la predicción, mostrar si es "Ojos Abiertos" u "Ojos Cerrados"
    if prediction < 0.5:
        counter = 0
        status = 'Abiertos'

        # Creamos un rectángulo
        cv2.rectangle(frame, (round(w / 2) - 110, 20), (round(w / 2) + 180, 80), (38, 38, 38), -1)
        cv2.putText(frame, status, (round(w / 2) - 104, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_4)
        x1, y1, w1, h1 = 0, 0, 225, 75
        # Dibujamos rectangulos de fondo negro
        cv2.rectangle(frame, (x1, x1), (x1 + w1 - 20, y1 + h1 - 20), (0, 0, 0), -1)
        # Añadimos texto
        cv2.putText(frame, 'ActivO', (x1 + int(w1 / 10), y1 + int(h1 / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                    2)
    else:
        counter = counter + 1
        status = 'Cerrados'

        cv2.rectangle(frame, (round(w / 2) - 110, 20), (round(w / 2) + 180, 80), (38, 38, 38), -1)

        cv2.putText(frame, status, (round(w / 2) - 104, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_4)
        x1, y1, w1, h1 = 0, 0, 225, 75
        # Dibujamos rectangulos de fondo negro
        cv2.rectangle(frame, (x1, x1), (x1 + w1 - 20, y1 + h1 - 20), (0, 0, 0), -1)
        # Añadimos texto
        cv2.putText(frame, 'Activo', (x1 + int(w1 / 10), y1 + int(h1 / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                    2)
        #_|arduino.write(b'N')  # b un bit

        # Si el contador es más que 3, reproducimos y mostramos la alerta de que el usuario se está durmiendo
        if counter > 3:
            x1, y1, w1, h1 = 400, 400, 400, 100

            cv2.rectangle(frame, (round(w / 2) - 160, round(h) - 200), (round(w / 2) + 160, round(h) - 120),
                          (0, 0, 255), -1)

            cv2.putText(frame, 'No te duermas!', (round(w / 2) - 136, round(h) - 146), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 0), 2, cv2.LINE_4)

            cv2.imshow('Drowsiness detection', frame)
            # Viendo si se presiona la letra k por teclado para detener la ejecución
            k = cv2.waitKey(1)
            #Sonido de alerta
            playsound(r'D:\SEMESTRE 1-2022\Visión Artificial\PROYECTO\audios\Despierta1231256.mp3')
            arduino.write(b'R')  # b un bit
            counter = 1
            continue
    cv2.imshow('Drowsiness detection', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()