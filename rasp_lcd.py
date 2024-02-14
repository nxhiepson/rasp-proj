import RPi.GPIO as GPIO
import time

# Define LCD pin numbers
RS = 7
E = 8
D4 = 25
D5 = 24
D6 = 23
D7 = 18

# Define some device constants
LCD_WIDTH = 16  # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RS, GPIO.OUT)
    GPIO.setup(E, GPIO.OUT)
    GPIO.setup(D4, GPIO.OUT)
    GPIO.setup(D5, GPIO.OUT)
    GPIO.setup(D6, GPIO.OUT)
    GPIO.setup(D7, GPIO.OUT)

    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    GPIO.output(RS, mode)

    # High bits
    GPIO.output(D4, False)
    GPIO.output(D5, False)
    GPIO.output(D6, False)
    GPIO.output(D7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()

    # Low bits
    GPIO.output(D4, False)
    GPIO.output(D5, False)
    GPIO.output(D6, False)
    GPIO.output(D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()

def lcd_toggle_enable():
    time.sleep(E_DELAY)
    GPIO.output(E, True)
    time.sleep(E_PULSE)
    GPIO.output(E, False)
    time.sleep(E_DELAY)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

if __name__ == "__main__":
    try:
        lcd_init()

        while True:
            lcd_string("Hello, World!", LCD_LINE_1)
            lcd_string("LCD with Raspberry Pi", LCD_LINE_2)
            time.sleep(3)  # Display for 3 seconds

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
