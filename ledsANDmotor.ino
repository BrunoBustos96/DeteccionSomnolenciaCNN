// Declaracion de variables
#define ledRojo 7
#define ledVerde 8
// Asumiendo una conexión al motor conectado al pin 12 y GND
#define motor 12 
char orden = 'C';

void setup() {

    // Definicion de salidas
    pinMode(ledRojo, OUTPUT);
    pinMode(ledVerde, OUTPUT);
    pinMode(motor, OUTPUT);

    // Apagamos todo por seguridad
    digitalWrite(ledRojo, LOW);
    digitalWrite(ledVerde, LOW);
    digitalWrite(motor, LOW);

    Serial.begin(9600);

}

void loop() {

    char aux = Serial.read();

    // A manera de evitar que se manden cientos de alertas
    // Solo se hara cuando se reciba una orden diferente a la anterior
    if (aux != orden) {

        // Si se recibe 'R' se enciende el led rojo y el motor
        if (aux == 'R') {

            digitalWrite(ledRojo, HIGH);
            digitalWrite(ledVerde, LOW);
            digitalWrite(motor, HIGH);
            orden = 'R';
            Serial.println("Presionaste R, enciendo led rojo y motor.");

        // Si se recibe 'N' se enciende el led verde
        } else if (aux == 'N') {

            digitalWrite(ledRojo, LOW);
            digitalWrite(ledVerde, HIGH);
            digitalWrite(motor, LOW);
            orden = 'N';
            Serial.println("Presionaste N, encendiendo led verde.");

        // Si se recibe 'C' se apaga todo
        } else if (aux == 'C') {

            digitalWrite(ledRojo, LOW);
            digitalWrite(ledVerde, LOW);
            digitalWrite(motor, LOW);
            orden = 'C';
            Serial.println("Presionaste C, apagando todo.");

        }

    }

}
