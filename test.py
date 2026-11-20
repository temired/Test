// CO2-Ampel mit ESP32
// Unter 1000 ppm: gruen, bis 1400 ppm: gelb, darueber: rot

const int LED_ROT   = 25;
const int LED_GELB  = 26;
const int LED_GRUEN = 27;

const int GRENZE_GELB = 1000;  // ppm
const int GRENZE_ROT  = 1400;  // ppm

void setup() {
  Serial.begin(9600);
  pinMode(LED_ROT, OUTPUT);
  pinMode(LED_GELB, OUTPUT);
  pinMode(LED_GRUEN, OUTPUT);
}

// Platzhalter: liefert spaeter den echten Wert vom MH-Z19B (UART)
int leseCO2() {
  return 850;
}

void zeigeAmpel(int co2) {
  digitalWrite(LED_ROT, LOW);
  digitalWrite(LED_GELB, LOW);
  digitalWrite(LED_GRUEN, LOW);

  if (co2 < GRENZE_GELB) {
    digitalWrite(LED_GRUEN, HIGH);
  } else if (co2 <= GRENZE_ROT) {
    digitalWrite(LED_GELB, HIGH);
  } else {
    digitalWrite(LED_ROT, HIGH);
  }
}

void loop() {
  int co2 = leseCO2();
  Serial.print("CO2: ");
  Serial.print(co2);
  Serial.println(" ppm");

  zeigeAmpel(co2);
  delay(10000);  // alle 10 Sekunden messen
}
