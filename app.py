from rasp_lcd import lcd_init, lcd_string, LCD_LINE_1, LCD_LINE_2
import RPi.GPIO as GPIO
import time
from temp_ import tempC_str

def main():
    try:
        lcd_init()
        lcd_string("Hello, World!", LCD_LINE_1)
        lcd_string("LCD with Raspberry Pi", LCD_LINE_2)
        time.sleep(1)

        while True:
            lcd_string("Temperature is:", LCD_LINE_1)
            lcd_string(tempC_str()+"^C", LCD_LINE_2)
            time.sleep(2)
              # Display for 3 seconds

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

if __name__=='__main__':
    main()