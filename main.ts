input.onButtonPressed(Button.A, function () {
    abbruch = 0
    I2C_LCD1602.ShowString("3", 5, 0)
    basic.pause(1000)
    I2C_LCD1602.ShowString("2", 5, 0)
    basic.pause(1000)
    I2C_LCD1602.ShowString("1", 5, 0)
    basic.pause(1000)
    I2C_LCD1602.ShowString("0", 5, 0)
    while (!(abbruch)) {
        zahl2 = randint(1, 5)
        zahl1 = randint(1, 5)
        ergebnis = zahl1 + zahl2
        if (ergebnis < 6) {
            abbruch = 1
        }
    }
    I2C_LCD1602.ShowString("" + zahl1 + "+" + zahl2 + "=?", 2, 0)
})
let wert = 0
let ergebnis = 0
let zahl1 = 0
let zahl2 = 0
let abbruch = 0
I2C_LCD1602.LcdInit(39)
I2C_LCD1602.ShowString("Hallo", 5, 0)
I2C_LCD1602.ShowString("Rechenkuenstler", 0, 1)
basic.pause(2000)
I2C_LCD1602.clear()
I2C_LCD1602.ShowString("ich starte", 4, 1)
basic.pause(5000)
I2C_LCD1602.clear()
I2C_LCD1602.ShowString("es Geht los", 4, 1)
basic.forever(function () {
    wert = pins.analogReadPin(AnalogPin.P2)
    if (wert < 50) {
        basic.showNumber(1)
    } else if (wert < 150) {
        basic.showNumber(2)
    } else if (wert < 260) {
        basic.showNumber(3)
    } else if (wert < 500) {
        basic.showNumber(4)
    } else if (wert < 600) {
        basic.showNumber(5)
    }
})
