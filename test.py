from rpi_ws281x import PixelStrip, Color
import time
import rpi_ws281x as ws


# LED strip configuration:
LED_COUNT = 50      # Number of LED pixels
LED_PIN = 18        # GPIO pin connected to the pixels (18 uses PWM!)
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10        # DMA channel to use for generating signal
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0     # Set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.SK6812_STRIP_RGBW  # Strip type for RGBW



def setPixelColor(strip, i, color):
    """Set color of individual pixel."""
    strip.setPixelColor(i, color)
    strip.show()

# Initialize the LED strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

# Set color of first LED to red
setPixelColor(strip, 0, Color(255, 0, 0, 0))  # Red

# Set color of second LED to green
setPixelColor(strip, 1, Color(0, 255, 0, 0))  # Green

# Set color of third LED to blue
setPixelColor(strip, 2, Color(0, 0, 255, 0))  # Blue

# Set color of fourth LED to white
setPixelColor(strip, 3, Color(0, 0, 0, 255))  # White