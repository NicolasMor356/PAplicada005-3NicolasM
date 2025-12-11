#define BLYNK_TEMPLATE_ID "TMPL2hcN1ddQy"
#define BLYNK_TEMPLATE_NAME "CERRADURA"
#define BLYNK_AUTH_TOKEN "HRieeqcj4uz-4okmqpdxun6heqajRfDy"

#include <WiFi.h>
#include <BlynkSimpleEsp32.h>
#include <ESP32Servo.h>
#include "FS.h"
#include "SPIFFS.h"
#include <time.h>

// ========= SERVO =========
Servo servoMotor;
int servoPin = 4;

// ========= PASSWORD =========
const char* correctPassword = "1234";
String inputPass = "";

// ========= TERMINAL V2 =========
WidgetTerminal terminal(V2);

// ========= FUNCION PARA LOG CSV =========
void logEvent(String eventType) {

  Serial.println("➡ Registrando evento: " + eventType);

  // Crear archivo si no existe
  if (!SPIFFS.exists("/registro.csv")) {
    Serial.println("Creando archivo registro.csv...");
    File file = SPIFFS.open("/registro.csv", FILE_WRITE);
    if (!file) {
      Serial.println("❌ Error creando registro.csv");
      return;
    }
    file.println("DATE, TIME, EVENT");
    file.close();
  }

  // Obtener hora
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) {
    Serial.println("❌ Error obteniendo hora NTP");
    return;
  }

  char dateStr[20], timeStr[20];
  strftime(dateStr, sizeof(dateStr), "%Y-%m-%d", &timeinfo);
  strftime(timeStr, sizeof(timeStr), "%H:%M:%S", &timeinfo);

  // Guardar registro
  File file = SPIFFS.open("/registro.csv", FILE_APPEND);
  if (!file) {
    Serial.println("❌ No se pudo abrir registro.csv para escribir");
    return;
  }

  file.printf("%s, %s, %s\n", dateStr, timeStr, eventType.c_str());
  file.close();

  Serial.printf("✔ Evento guardado: %s, %s, %s\n", dateStr, timeStr, eventType.c_str());
}

// ========= ACCIONES =========
void abrirPuerta() {
  Serial.println("🔓 Abriendo puerta...");
  servoMotor.write(0);
  logEvent("OPEN");
}

void cerrarPuerta() {
  Serial.println("🔒 Cerrando puerta...");
  servoMotor.write(90);
  logEvent("CLOSE");
}

// ========= BLYNK PASSWORD INPUT (V0) =========
BLYNK_WRITE(V0) {
  inputPass = param.asStr();

  Serial.println("Contraseña ingresada: " + inputPass);

  if (inputPass == correctPassword) {
    abrirPuerta();
  } else {
    Serial.println("❌ Contraseña incorrecta");
  }
}

// ========= BOTÓN CERRAR (V1) =========
BLYNK_WRITE(V1) {
  int estado = param.asInt();
  if (estado == 1) {
    cerrarPuerta();
  }
}

// ========= MOSTRAR REGISTRO EN TERMINAL (V3) =========
void mostrarRegistroEnBlynk() {
  if (!SPIFFS.exists("/registro.csv")) {
    terminal.println("❌ No existe registro.csv");
    terminal.flush();
    return;
  }

  File file = SPIFFS.open("/registro.csv");
  if (!file) {
    terminal.println("❌ Error abriendo registro.csv");
    terminal.flush();
    return;
  }

  terminal.println("=== REGISTRO DE EVENTOS ===");

  while (file.available()) {
    String linea = file.readStringUntil('\n');
    terminal.println(linea);
  }

  terminal.println("=== FIN ===");
  terminal.flush();
  file.close();
}

BLYNK_WRITE(V3) {
  if (param.asInt() == 1) {
    mostrarRegistroEnBlynk();
  }
}

// ========= SETUP =========
void setup() {
  Serial.begin(115200);
  delay(500);

  // SPIFFS
  Serial.println("Montando SPIFFS...");
  if (!SPIFFS.begin(true)) {
    Serial.println("❌ Error montando SPIFFS");
    return;
  }
  Serial.println("✔ SPIFFS listo");

  // Servo
  servoMotor.attach(servoPin);
  cerrarPuerta(); // estado inicial

  // Conectar WiFi + Blynk
  Serial.println("Conectando a WiFi...");
  Blynk.begin(BLYNK_AUTH_TOKEN, "iPhone de Nicolas", "12345678");

  // Hora NTP
  Serial.println("Sincronizando hora NTP...");
  configTime(-5 * 3600, 0, "pool.ntp.org");

  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) {
    Serial.println("❌ No se pudo sincronizar hora");
  } else {
    Serial.println("✔ Hora sincronizada correctamente");
  }

  Serial.println("Sistema iniciado correctamente.");
}

// ========= LOOP =========
void loop() {
  Blynk.run();
}
