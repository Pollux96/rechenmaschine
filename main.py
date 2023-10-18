def on_button_pressed_a():
    global abbruch, Eingabe, zahl2, zahl1, ergebnis, startZeit, EndZeit
    abbruch = 0
    Eingabe = 0
    COUNTDOWN()
    while not (abbruch):
        zahl2 = randint(1, 4)
        zahl1 = randint(1, 4)
        ergebnis = zahl1 + zahl2
        if ergebnis < 5:
            abbruch = 1
    I2C_LCD1602.show_string("" + str(zahl1) + "+" + ("" + str(zahl2)) + "=?", 2, 0)
    startZeit = control.millis()
    while Eingabe == 0:
        pass
    EndZeit = control.millis()
    I2C_LCD1602.show_string("Dauer:" + ("" + str((EndZeit - startZeit))) + "ms", 2, 0)
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
wert = 0
EndZeit = 0
startZeit = 0
ergebnis = 0
zahl1 = 0
zahl2 = 0
Eingabe = 0
abbruch = 0
I2C_LCD1602.lcd_init(39)
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

def on_forever():
    global wert, Eingabe
    wert = pins.analog_read_pin(AnalogPin.P2)
    if wert < 50:
        basic.show_number(1)
        Eingabe = 1
    elif wert < 150:
        basic.show_number(2)
        Eingabe = 2
    elif wert < 260:
        basic.show_number(3)
        Eingabe = 3
    elif wert < 520:
        basic.show_number(4)
        Eingabe = 4
    elif wert < 600:
        basic.show_number(5)
        Eingabe = 5
basic.forever(on_forever)
