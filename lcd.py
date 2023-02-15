from liquidcrystal_i2c import LiquidCrystal_I2C as Lc

LC_COLS, LC_ROWS = 16, 2
LCD = Lc(0x3f, 1, numlines=LC_ROWS)


def light_mode(light=True):
    """The light argument controls display backlight (True by default)"""
    if light:
        LCD.backlight()
    else:
        LCD.noBacklight()


def lcd_print(row1, row2):
    """Receives 2 strings for each row and send it to LCD display."""

    LCD.printline(0, row1)
    LCD.printline(1, row2)
