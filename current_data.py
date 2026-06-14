from machine import Pin, ADC
import time

led = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN)

adc = ADC(26)  # GP26 / ADC0

V_REF = 3.3
ADC_MAX = 65535
R_SHUNT = 1000.0  # 1 kΩ

filename = "current_data.csv"

# Open CSV file on Pico
with open(filename, "w") as file:
    file.write("time_ms,button,led,shunt_voltage_V,current_mA\n")

    start = time.ticks_ms()

    # Record for 10 seconds
    while time.ticks_diff(time.ticks_ms(), start) < 10000:
        button_state = button.value()

        # LED turns on when button is pressed
        led.value(button_state)

        raw = adc.read_u16()
        shunt_voltage = raw * V_REF / ADC_MAX

        current_A = shunt_voltage / R_SHUNT
        current_mA = current_A * 1000

        t = time.ticks_diff(time.ticks_ms(), start)

        line = "{},{},{},{:.4f},{:.3f}\n".format(
            t,
            button_state,
            led.value(),
            shunt_voltage,
            current_mA
        )

        file.write(line)
        print(line, end="")

        time.sleep_ms(1)

print("Finished recording.")
print("Saved as current_data.csv")