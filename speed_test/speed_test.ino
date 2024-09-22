unsigned long startTime;
unsigned long endTime;
unsigned long currentTime;
unsigned long calculations = 0;
unsigned long totalCalculations = 0;

void setup() {
  Serial.begin(9600);
  delay(2000);  // Allow time for the serial monitor to open
  Serial.println("Starting C++ calculation test");

  // Run calculations for 3 seconds
  for (int second = 1; second <= 3; second++) {
    calculations = 1;
    startTime = millis();
    endTime = startTime + 1000;  // Run for 1 second

    while (millis() < endTime) {
      // Perform some simple calculations
      float result = (1234.56 * 7890.12) / 345.67;
      calculations++;
    }

    totalCalculations += calculations;
    Serial.print("Calculations in second ");
    Serial.print(second);
    Serial.print(": ");
    Serial.println(calculations);
  }

  // Print total calculations
  Serial.print("Total calculations in 3 seconds: ");
  Serial.println(totalCalculations);
}

void loop() {
  // Nothing to do here
}
