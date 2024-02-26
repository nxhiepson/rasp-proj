from gpiozero import CPUTemperature
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
 
# LCD size
lcd_columns = 16
lcd_rows = 2
 
# LCD to RPi Pin
lcd_rs = digitalio.DigitalInOut(board.D27)
lcd_en = digitalio.DigitalInOut(board.D22)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)
 
 
# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)
 
# Clear LCD screen 
lcd.clear()
cpu = CPUTemperature()
while True:
     cpuTemp = cpu.temperature
     cpuSTR = str(round(cpuTemp))
     lcd.message = "CPU Temp:" +  cpuSTR + "'C" 
     sleep(1)
