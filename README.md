# Detección de Somnolencia usando Redes Neuronales Convolucionales

Proyecto final para el [Bootcamp en Visión Computacional para los Objetivos de Desarrollo Sostenible Hackcities](https://github.com/EdwinTSalcedo/Bootcamp-Computer-Vision-for-the-SDGs)

![image](https://user-images.githubusercontent.com/78177589/178857695-c6ab6e2a-e4f6-42d1-b69d-2e1378dd4ce2.png)


## DeteccionSomnolenciaCNN
El Backend del proyecto final de HackCities fue desarrollado en Pycharm y Colaboratory utilizando liberías de Procesamiento de Imágenes y Aprendizaje Profundo.

## Motivación
Los accidentes de tránsito son un grave problema  en nuestro país, y aunque los efectos del alcohol y el cambio de carril sean las principales causas de dichos accidentes, la tercera más relevante es la somnolencia de los conductores, problema que puede ser atacado con una solución que implemente visión computacional en dispositivos de bajo costo. 

Dentro de los Objetivos de Desarrollo Sostenible, este proyecto se concentra principalmente en 2: ODS 3 "Salud y bienestar", buscando mejorar la seguridad vial de peatones y conductores; y el ODS 11 "Industria, innovación e infraestructura", buscando proponer soluciones innovadoras en nuestro entorno que puedan tener un impacto económico positivo.

## Link al video
[![Link al video](https://upload.wikimedia.org/wikipedia/commons/archive/d/da/20151123111600%21Google_Drive_logo.png)](https://drive.google.com/file/d/1hifv4_kZ9eyYGI8D0iQLE_9xXUThOXyc/view)

## Capturas de pantalla e imágenes importantes
#### Definición del problema
##### Objetivos de desarrollo sostenible objetivo:
![image](https://user-images.githubusercontent.com/78177589/178859934-7fbe2711-d946-4d9d-865d-269c9f5bd158.png)
![image](https://user-images.githubusercontent.com/78177589/178859946-a13b74f3-8b81-4f80-97ff-9f81db75fc6e.png)

##### Objetivos
![image](https://user-images.githubusercontent.com/78177589/178860273-2d7602f2-f813-4180-b1d7-1b1cbe859a22.png)
##### Modelo de entrenamiento CNN
![image](https://user-images.githubusercontent.com/78177589/178860309-76d00c10-e220-4e77-a3ef-11e0e1f67b26.png)
##### Métricas
![image](https://user-images.githubusercontent.com/78177589/178860374-f5d59d15-d461-4785-8280-d7e7d8e68c00.png)
##### Resultados experimentales
* Ojos abiertos
![image](https://user-images.githubusercontent.com/78177589/178860602-b846a1bf-1de0-4abd-b33f-8b4bcc8a9903.png)
* Ojos cerrados
![image](https://user-images.githubusercontent.com/78177589/178860631-d3e9e9df-8ece-44ea-b918-7a1cc85c07c5.png)
* Alerta
![image](https://user-images.githubusercontent.com/78177589/178860768-7b9bd603-2b8d-4ff1-b442-a50d154e0d51.png)




## Tecnologías utilizadas

- Arduino mega  
- 2 leds (rojo y verde)  
- Motor de 5Vdc  
- Cables

## Frameworks utilizados

- Numpy  
- Pandas  
- OpenCV  
- TensorFlow  
- Keras  
- face_recognition

## Funcionalidades más importantes
- Extracción del área de los ojos para una clasificación más precisa  
- Modelo de Redes Neuronales Convolucionales de varias capas con una precisión alta (>90%)  
- Clasificación en tiempo real de somnolencia con etiquetas
- Adición de un prototipo que alerta de manera sensorial, auditiva y visual en el modelo en vivo en caso de somnolencia

## Instalación
* Es importante tener instaladas, fuera de las librerías típicas de Ciencia de Datos (Numpy, MatPlotLib, Pandas), librerías como OpenCV, TensorFlow, Keras, face_recognition, playsound (A través del comando pip)
* Se recomienda tener la cámara web activa en un entorno Desktop
* Se recomienda tener la GPU activa (En Colaboratory)

* En algunos sistemas operativos puede ser necesario instalar homebrew, cmake, dlib antes de instalar face_recognition, OpenCV y Playsound  
**Para la aplicación en vivo se recomienda un IDE de escritorio (Pycharm, Spyder) corriendo un entorno virtual con todas las librerías necesarias**

## Créditos
- Israel Algodón (25 %)
- Bruno Bustos  (25 %)
- Tracy Loza (50 %)

* Funciones de detección adaptadas de: https://towardsdatascience.com/drowsiness-detection-using-convolutional-neural-networks-face-recognition-and-tensorflow-56cdfc8315ad

* GitHub del autor del artículo: https://github.com/dustin-stew

* Estructura de las Redes Neuronales Convolucionales inspiradas de: https://github.com/EdwinTSalcedo/Bootcamp-Computer-Vision-for-the-SDGs/blob/master/notebooks/Laboratorio%2011_%20Redes%20Neuronales%20Convolucionales.ipynb

* Base para el uso de imágenes en Colab a través de OpenCV: https://github.com/EdwinTSalcedo/Bootcamp-Computer-Vision-for-the-SDGs/blob/087b9e0474e5497a03c6c8073e79721d24da3ce1/notebooks/Laboratorio%201_%20Introducci%C3%B3n%20a%20Colab,%20OpenCV%20y%20Numpy.ipynb

* Github del autor de los últimos 2 Notebooks: https://github.com/EdwinTSalcedo

* Métricas del modelo decididas a partir de: https://towardsdatascience.com/a-look-at-precision-recall-and-f1-score-36b5fd0dd3ec

* Objetivos de desarrollo sostenible decididos a partir de la información proveída por Natalia Guerreros Lima en: https://github.com/EdwinTSalcedo/Bootcamp-Computer-Vision-for-the-SDGs/blob/f2dd3b0eb4edb18d308a472bb5904c74b8eefe09/slides/ODS%20primera%20parte.pdf

# Secciones adicionales (Los resultados experimentales son más profundizados en el video y en nuestras imágenes importantes)
## Trabajos Relacionados

![image](https://user-images.githubusercontent.com/78177589/178857156-aa829a4f-ed59-4a7a-b5aa-47b83d545d80.png)
![image](https://user-images.githubusercontent.com/78177589/178857174-033d1d6b-f057-4c82-b740-70ad376138ac.png)
![image](https://user-images.githubusercontent.com/78177589/178857225-a1464ccb-5814-4f0b-8d27-81dc79b0234b.png)
![image](https://user-images.githubusercontent.com/78177589/178857244-4ec666e8-3277-4dd9-8557-5a37f1c7509a.png)
![image](https://user-images.githubusercontent.com/78177589/178857268-d88addc4-5813-4160-a340-abc73ad29378.png)
![image](https://user-images.githubusercontent.com/78177589/178857291-e915522b-2f61-4921-a226-bcfc886a5eb6.png)
![image](https://user-images.githubusercontent.com/78177589/178857318-596bc8e4-80b6-4702-87f3-22ae812dc200.png)

Garcés M., Salgado J., Cruz J., Cañon W. (2015), Sistemas de Detección de Somnolencia en Conductores: inicio, desarrollo y futuro. https://dialnet.unirioja.es/descarga/articulo/5432283.pdf 
Gupta, V. (22 de octubre de 2018). Learn OpenCV. https://www.learnopencv.com/face-detection-opencv-dlib-and-deep-learning-c-python/ 
Ramzan M, Ullah H, Mahmood S., Amina I., Ilyas M. (1 mayo 2019), A Survey on State-of-the-Art Drowsiness Detection Techniques. https://ieeexplore.ieee.org/abstract/document/8704263 
Sanchez E., Limaquispe M., (junio 2018), Sistema de Detección de somnolencia mediante Inteligencia Artificial en Conductores de Vehículos para Alertar la Ocurrencia de Accidentes de Tránsito. https://repositorio.unh.edu.pe/bitstream/handle/UNH/2327/TESIS-2018-INGENIERIA%20ELECTRONICA-LIMAQUISPE%20MIGUEL.pdf?sequence=1&isAllowed=y

## Métodos

Los pasos a seguir durante este proyecto fueron inspirados en: [A How-to-Model Guide for Neuroscience](https://www.eneuro.org/content/7/1/ENEURO.0352-19.2019), combinando con funcionalidades de un sistema completo aprendidas durante el presente [Bootcamp](https://github.com/EdwinTSalcedo/Bootcamp-Computer-Vision-for-the-SDGs), ya que:

1. Se definió un objetivo
2. Se revisó la literatura
3. Se determinaron los ingredientes básicos de un posible modelo (Explorando las alternativas aprendidas durante el bootcamp)
4. Se definió una posible hipótesis (Proponiendo encontrar un modelo que supere el 90% de accuracy)

Dentro de la implementación del modelo:   


  5. Se seleccionaron las herramientas a ser implementadas, donde se consideraron enfoques alternativos  
  6. Se planificó el modelo, la arquitectura y la aplicación en vivo utilizados durante el proyecto  
  7. Se implementó el modelo en Colaboratory de Google y Jupyter Notebooks  
  8. Se completó el modelo modificando posibles hiperparámetros  
  9. Se testeó y evaluó el modelo en vivo alcanzando muy buenas métricas y combinandolo con un sistema de retroalimentación multisensorial  

Para finalmente:     

  10. Publicarlo en este Bootcamp

![image](https://user-images.githubusercontent.com/78177589/178867188-975fe1fb-ed6a-4bbb-93c9-32e0eaceb10c.png)


## Licencia

The MIT License

Copyright (c) 2022 SplitVision

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
