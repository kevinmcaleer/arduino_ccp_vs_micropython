import time

total_calculations = 0
calculations = 0

print("Starting MicroPython calculation test")

# Run calculations for 3 seconds
for second in range(1, 4):
    calculations = 0
    start_time = time.ticks_ms()
    end_time = start_time + 1000  # Run for 1 second

    while time.ticks_ms() < end_time:
        # Perform some simple calculations
        result = (1234.56 * 7890.12) / 345.67
        calculations += 1

    total_calculations += calculations
    print(f"Calculations in second {second}: {calculations}")

# Print total calculations
print(f"Total calculations in 3 seconds: {total_calculations}")
