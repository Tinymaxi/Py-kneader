from gpiozero import LED
from gpiozero import Button
from signal import pause
from time import sleep
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from melody import *
from finishing_time import *
from dht11 import *
import os


oled_reset = digitalio.DigitalInOut(board.D4)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 1

# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)


Red_LED = LED(23)
Relais = LED(17)
button = Button(26)


Relais.on()
Red_LED.on()

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))



# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a bleck background
draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

# Load default font.
#font = ImageFont.load_default()
font = ImageFont.truetype('/home/pi/slkscr.ttf', 8)



# Draw Some Text
text = "Finishing time at"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, 8),
    text,
    font=font,
    fill=255,
)

text = (finishing_time(9000))
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, 16),
    text,
    font=font,
    fill=255,
)

text = x
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, 24),
    text,
    font=font,
    fill=255,
)



text = "Press the button"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, 32),
    text,
    font=font,
    fill=255,
)

text = "to start the sequence"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, 40),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()

   
def start_kneading_sequence():
    def squence(Relais,Text1,Text2,Text3,time):
        # Clear display.
        oled.fill(0)
        oled.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (oled.width, oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a white background
        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

        # Draw a smaller inner rectangle
        draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1), outline=0, fill=0,)

        # Draw Some Text
        text = Text1
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 15),
            text,
            font=font,
            fill=255,
        )

        text = Text2
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 23),
            text,
            font=font,
            fill=255,
        )

        text = Text3
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 31),
            text,
            font=font,
            fill=255,
        )
        # Display image
        oled.image(image)
        oled.show()

        Relais
        sleep(time) #Kneading Time 720
        
    squence(Relais.on(),"Button pressed!","kneading","very hard",5) # Kneading sequence Time 720
    squence(Relais.off(),"taking a first break","relax with","Max",5) # First break Time 900
    squence(Relais.on(),"just a","quick first","knead",5) # First quick knead Time 60
    squence(Relais.off(),"second","break","",5) # Second break Time 900
    squence(Relais.on(),"second","quick","kneading",5) # Second quick knead Time 60
    squence(Relais.off(),"taking","the last","break",5) # First half final break Melody for switching on the oven Time 300
    squence(Relais.off(),"switch","the oven on!","",5) # fFirst half final break  Time 1
    #  Playing Melody to make shore someone switches the oven on.
    setup()
    play(crazy_frog_melody, crazy_frog_tempo, 0.30, 0.900)
    squence(Relais.off(),"Final break","I hope the","oven is on!",5) # Second half final break Time 300
    squence(Relais.on(),"nealy finished","just a second","",5) # Last quick knead Time 60
    
    ##### Kneading done ################################
    
    # Clear display.
    oled.fill(0)
    oled.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white background
    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

    # Draw a smaller inner rectangle
    draw.rectangle((10, 10, oled.width - 10 - 1, oled.height - 10 - 1), outline=255, fill=0,)

    # Draw Some Text
    text = "Finished!"
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width // 2 - font_width // 2, (oled.height // 2 - font_height // 2)),
        text,
        font=font,
        fill=255,
    )
    
         
    # Display image
    oled.image(image)
    oled.show()

    Relais.off() ### Kneading finished
    Red_LED.off()
    
      
    def start_beaking_sequence():           
        # Clear display.
        oled.fill(0)
        oled.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (oled.width, oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a white background
        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

        # Draw a smaller inner rectangle
        draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1), outline=0, fill=0,)

        # Draw Some Text
        text = "Ready"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 15),
            text,
            font=font,
            fill=255,
        )

        text = "Steady"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 23),
            text,
            font=font,
            fill=255,
        )

        text = "bake!"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 31),
            text,
            font=font,
            fill=255,
        )
        # Display image
        oled.image(image)
        oled.show()

        
        sleep(5) # 1200 for the 250 C beaking time

        #Playing Melody to make shore someone turns down the temperature.
        setup()
        play(popcorn_melody, popcorn_tempo, 0.50, 1.000)

        sleep(5)   # Final Baking stage until finished 1800.
        play(final_countdown_melody, final_countdown_tempo, 0.30, 1.2000)
        
        # Clear display.
        oled.fill(0)
        oled.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (oled.width, oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a white background
        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

        # Draw a smaller inner rectangle
        draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1), outline=0, fill=0,)

        # Draw Some Text
        text = "Well done"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 15),
            text,
            font=font,
            fill=255,
        )

        text = "finished"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 23),
            text,
            font=font,
            fill=255,
        )

        text = "En Guätä'"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, 31),
            text,
            font=font,
            fill=255,
        )
        # Display image
        oled.image(image)
        oled.show()
      
        def turnoff():
            if Button.is_pressed: #Check to see if button is pressed
                time.sleep(1) # wait for the hold time we want. 
                if Button.is_pressed: #check if the user let go of the button
                    os.system("shutdown now") #shut down the Pi -h is or -r will reset
                    
        button.when_pressed = turnoff
    
    button.when_pressed = start_beaking_sequence 



button.when_pressed = start_kneading_sequence