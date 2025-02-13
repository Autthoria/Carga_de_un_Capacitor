int ValorSensor = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial) {}  // Esperar a que la comunicación serial esté lista
}

void loop() {
  ValorSensor = analogRead(A0);
  
  // Escalar valores para obtener el voltaje real
  float Voltaje = (ValorSensor * 5.0) / 1023.0;  // Convertir a voltaje real
  Serial.println(Voltaje);  // Enviar el voltaje real
  
  delay(100);  // Aumentar el delay para mejorar la resolución temporal
}
