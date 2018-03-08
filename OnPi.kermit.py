import time
import logging

from neopixel import *
from networktables import *

logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server='192.168.1.8')
nt = NetworkTables.getTable("RasberryPi")

# strip.numPixels()
# strip.setPixelColor(120, Color(255, 0, 0)) RED GREEN BLUE
# strip.setBrightness(255)
# strip.show()

LED_COUNT      = 22      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 1       # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


def colorWipe(strip, color, brightness, wait_ms=25):
    strip.setBrightness(brightness)
    turnOff(strip)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorWipeReverse(strip, color, brightness, wait_ms=25):
    strip.setBrightness(brightness)
    turnOff(strip)
    for i in range(strip.numPixels()):
        strip.setPixelColor(LED_COUNT - i - 1, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def updateDetaunts(strip, d1, d2, toggle, brightness=1):
    strip.setBrightness(brightness)
    for i in range(11):
        if (i < d1):
            strip.setPixelColor(i + 1, Color(0, 0, 255))
        else:
            strip.setPixelColor(i + 1, Color(0, 0, 0))
    for i in range(11):
        if (i < d2):
            strip.setPixelColor(i + 11, Color(255, 0, 0))
        else:
            strip.setPixelColor(i + 11, Color(0, 0, 0))
    if (toggle == 0):
        strip.setPixelColor(0, Color(0, 255, 0))
        strip.setPixelColor(21, Color(0, 0, 0))
    if (toggle == 1):
        strip.setPixelColor(0, Color(0, 0, 0))
        strip.setPixelColor(21, Color(0, 255, 0))
    strip.show()


def turnOff(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


if __name__ == '__main__':

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()

    colorWipe(strip, Color(0, 100, 0), 255, 50)
    time.sleep(0.25)
    colorWipeReverse(strip, Color(0, 100, 0), 255, 50)
    time.sleep(0.25)
    colorWipe(strip, Color(0, 100, 0), 255, 50)
    time.sleep(0.25)

    while True:
        state = nt.getString('state', 'Disabled')
        toggle = int(nt.getNumber('toggle', 2))
        d1 = int(nt.getNumber('detaunt1', 0.0))
        d2 = int(nt.getNumber('detaunt2', 0.0))
        print(d1, d2, state, toggle)
        if state == 'Disabled':
            updateDetaunts(strip, d1, d2, toggle, 100)
        if state == 'Auto':
            colorWipeReverse(strip, Color(100, 100, 0), 255, 50)
            time.sleep(0.25)
            colorWipe(strip, Color(100, 100, 0), 255, 50)
        if state == 'TeleOp':
            colorWipeReverse(strip, Color(0, 100, 0), 255, 50)
            time.sleep(0.25)
            colorWipe(strip, Color(0, 100, 0), 255, 50)
        time.sleep(0.25)
