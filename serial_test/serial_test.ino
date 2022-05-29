char buf[1];
void setup() {
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(buf, 1);
    Serial.print("ACK ");
    Serial.println(buf[0]);
  }
}
