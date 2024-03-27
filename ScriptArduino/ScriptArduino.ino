const int relayPins[] = {2, 3, 4, 5}; // Números de pin de los relés

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(relayPins[i], OUTPUT); // Configura los pines de los relés como salidas
  digitalWrite(2,0);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);



  }
  Serial.begin(9600); // Establece la comunicación serie a 9600 baudios
}

void loop() {
  if (Serial.available() > 1) { // Verifica si hay al menos dos bytes disponibles en el puerto serie
    char indexChar = Serial.read(); // Lee el byte que representa el índice del relé en el array
    char command = Serial.read(); // Lee el byte que representa el comando para el relé
    int index = indexChar - '0'; // Convierte el carácter a un número entero
    if (index >= 0 && index < 4) { // Verifica que el índice esté dentro del rango válido
      if (command == '1') {
        digitalWrite(relayPins[index], HIGH); // Cierra el relé correspondiente
      } else if (command == '0') {
        digitalWrite(relayPins[index], LOW); // Abre el relé correspondiente
      }
    }
  }
}
