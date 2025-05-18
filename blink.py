from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

print("LED starts flashing...")
led.off()
while True:
    try:
        led.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
led.off()
print("Finished.")
