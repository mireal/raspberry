from liquidcrystal_i2c import LiquidCrystal_I2C as Lc

LC_COLS, LC_ROWS = 16, 2
LCD = Lc(0x3f, 1, numlines=LC_ROWS)


def show_temp(temp, humid, light=True):
    """Shows temperature and humidity from DTH module on display.
    The light argument controls display backlight (True by default)"""
    if light:
        LCD.backlight()
    else:
        LCD.noBacklight()
    LCD.printline(0, f'Temp:  {temp}C')
    LCD.printline(1, f'Humid: {humid}%')
