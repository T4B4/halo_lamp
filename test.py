import rpi_ws281x as ws

# Set up the LED strip
LED_COUNT = 60
LED_PIN = 18
strip = ws.Adafruit_NeoPixel(LED_COUNT, LED_PIN, 800000, 10, False, 255, 0, ws.WS2812_STRIP_RGBW)
strip.begin()

# Set the first LED to blue
strip.setPixelColor(0, ws.Color(0, 0, 255, 0))  # Blue (no white)
strip.show()

# Set the second LED to red
strip.setPixelColor(1, ws.Color(255, 0, 0, 0))  # Red (no white)
strip.show()
