input.onButtonPressed(Button.A, function () {
    abbruch = 0
    Eingabe = 0
    while (!(abbruch)) {
        zahl2 = randint(1, 4)
        zahl1 = randint(1, 4)
        ergebnis = zahl1 + zahl2
        if (ergebnis < 5) {
            abbruch = 1
        }
    }
    I2C_LCD1602.ShowString("" + zahl1 + "+" + ("" + zahl2) + "=?", 2, 0)
    startZeit = control.millis()
    while (Eingabe == 0) {
    	
    }
    EndZeit = control.millis()
    I2C_LCD1602.ShowString("Dauer:" + ("" + (EndZeit - startZeit)) + "ms", 2, 0)
})
function COUNTDOWN () {
    I2C_LCD1602.ShowString("3", 5, 0)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    basic.pause(1000)
    I2C_LCD1602.ShowString("2", 5, 0)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    basic.pause(1000)
    I2C_LCD1602.ShowString("1", 5, 0)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    basic.pause(1000)
    I2C_LCD1602.ShowString("0", 5, 0)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
}
function start () {
    I2C_LCD1602.ShowString("Hallo", 5, 0)
    I2C_LCD1602.ShowString("Rechenkuenstler", 0, 1)
    basic.pause(2000)
    I2C_LCD1602.clear()
    I2C_LCD1602.ShowString("ich starte", 4, 1)
    basic.pause(5000)
    I2C_LCD1602.clear()
    I2C_LCD1602.ShowString("ES GEHT LOS", 4, 1)
    basic.pause(2000)
    I2C_LCD1602.clear()
}
let wert = 0
let EndZeit = 0
let startZeit = 0
let ergebnis = 0
let zahl1 = 0
let zahl2 = 0
let Eingabe = 0
let abbruch = 0
I2C_LCD1602.LcdInit(39)
basic.forever(function () {
    wert = pins.analogReadPin(AnalogPin.P2)
    if (wert < 50) {
        basic.showNumber(1)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("" + zahl1 + "+" + ("" + zahl2) + "=1", 2, 0)
        Eingabe = 1
        I2C_LCD1602.clear()
    } else if (wert < 150) {
        basic.showNumber(2)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("" + zahl1 + "+" + ("" + zahl2) + "=2", 2, 0)
        Eingabe = 2
        basic.pause(2000)
        I2C_LCD1602.clear()
    } else if (wert < 260) {
        basic.showNumber(3)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("" + zahl1 + "+" + ("" + zahl2) + "=3", 2, 0)
        Eingabe = 3
        basic.pause(2000)
        I2C_LCD1602.clear()
    } else if (wert < 520) {
        basic.showNumber(4)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("" + zahl1 + "+" + ("" + zahl2) + "=4", 2, 0)
        Eingabe = 4
        basic.pause(2000)
        I2C_LCD1602.clear()
    } else if (wert < 600) {
        basic.showNumber(5)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("" + zahl1 + "+" + ("" + zahl2) + "=5", 2, 0)
        Eingabe = 5
        basic.pause(2000)
        I2C_LCD1602.clear()
    }
})
