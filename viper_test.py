import time

@micropython.viper
def loop():
    for _ in range(1_000_000):
        a = 1+1

start_time = time.ticks_ms()
for _ in range(1, 4):
    loop()

end_time = time.ticks_ms()

print(f"\n 1,000,000 loops in {end_time-start_time} ms")