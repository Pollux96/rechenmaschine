def on_button_pressed_a():
    global abbruch, Eingabe, zahl2, zahl1, ergebnis
    abbruch = 0
    Eingabe = 0
    while not (abbruch):
        zahl2 = randint(1, 4)
        zahl1 = randint(1, 4)
        ergebnis = zahl1 + zahl2
        if ergebnis < 5:
            abbruch = 1
    I2C_LCD1602.show_string("" + str(zahl1) + "+" + ("" + str(zahl2)) + "=?", 2, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def COUNTDOWN():
    I2C_LCD1602.show_string("3", 5, 0)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.pause(1000)
    I2C_LCD1602.show_string("2", 5, 0)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.pause(1000)
    I2C_LCD1602.show_string("1", 5, 0)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.pause(1000)
    I2C_LCD1602.show_string("0", 5, 0)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
def start():
    I2C_LCD1602.show_string("Hallo", 5, 0)
    I2C_LCD1602.show_string("Rechenkuenstler", 0, 1)
    basic.pause(2000)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("ich starte", 4, 1)
    basic.pause(5000)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("ES GEHT LOS", 4, 1)
    basic.pause(2000)
    I2C_LCD1602.clear()
wert = 0
ergebnis = 0
zahl1 = 0
zahl2 = 0
Eingabe = 0
abbruch = 0
I2C_LCD1602.lcd_init(39)

def on_forever():
    global wert, Eingabe
    wert = pins.analog_read_pin(AnalogPin.P2)
    if wert < 50:
        basic.show_number(1)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("" + str(zahl1) + "+" + ("" + str(zahl2)) + "=1", 2, 0)
        Eingabe = 1
        I2C_LCD1602.clear()
    elif wert < 150:
        basic.show_number(2)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("" + str(zahl1) + "+" + ("" + str(zahl2)) + "=2", 2, 0)
        Eingabe = 2
        basic.pause(2000)
        I2C_LCD1602.clear()
    elif wert < 260:
        basic.show_number(3)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("" + str(zahl1) + "+" + ("" + str(zahl2)) + "=3", 2, 0)
        Eingabe = 3
        basic.pause(2000)
        I2C_LCD1602.clear()
    elif wert < 520:
        basic.show_number(4)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("" + str(zahl1) + "+" + ("" + str(zahl2)) + "=4", 2, 0)
        Eingabe = 4
        basic.pause(2000)
        I2C_LCD1602.clear()
    elif wert < 600:
        basic.show_number(5)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("" + str(zahl1) + "+" + ("" + str(zahl2)) + "=5", 2, 0)
        Eingabe = 5
        basic.pause(2000)
        I2C_LCD1602.clear()
basic.forever(on_forever)
