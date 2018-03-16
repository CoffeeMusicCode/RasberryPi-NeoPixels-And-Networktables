import time
import logging

logging.basicConfig(level=logging.DEBUG)

# strip.numPixels()
# strip.setPixelColor(120, Color(255, 0, 0)) RED GREEN BLUE
# strip.setBrightness(255)
# strip.show()

LED_COUNT      = 134      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255       # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


def colorWipe(strip, color, wait_ms=25):
    strip.setBrightness(brightness)
    turnOff(strip)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorWipeReverse(strip, color, wait_ms=25):
    strip.setBrightness(brightness)
    turnOff(strip)
    for i in range(strip.numPixels()):
        strip.setPixelColor(LED_COUNT - i - 1, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)


def theaterChaseTwoTone(strip, wait_ms=50, iterations=15):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(2):
            for i in range(0, strip.numPixels(), 2):
                strip.setPixelColor(i+q, Color(0, 255, 0))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 2):
                strip.setPixelColor(i+q, Color(255, 255, 0))


def allSameColor(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def turnOff(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


if __name__ == '__main__':

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()

    allSameColor(strip, Color(0, 255, 0))

    while True:
        colorWipe(strip, Color(0, 255, 0))
        time.sleep(1)
        colorWipe(strip, Color(255, 255, 0))
        time.sleep(1)
        colorWipeReverse(strip, Color(0, 255, 0))
        time.sleep(1)
        colorWipeReverse(strip, Color(255, 255, 0))
        time.sleep(1)
        theaterChaseTwoTone(strip)
        time.sleep(1)
