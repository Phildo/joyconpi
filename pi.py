import RPi.GPIO as GPIO

DIR_PIN_U = 5
DIR_PIN_D = 19
DIR_PIN_L = 13
DIR_PIN_R = 6

BTN_PIN_0 = 16

class Pi():

    def __init__(self):
        pass

    def initialize(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIR_PIN_U, GPIO.IN)
        GPIO.setup(DIR_PIN_D, GPIO.IN)
        GPIO.setup(DIR_PIN_R, GPIO.IN)
        GPIO.setup(DIR_PIN_L, GPIO.IN)
        GPIO.setup(BTN_PIN_0, GPIO.IN)

        self.dir_u = False
        self.dir_d = False
        self.dir_l = False
        self.dir_r = False
        self.btn_0 = False

        self.locked = False

    def tick(self):
        self.locked = True
        self.dir_u = GPIO.input(DIR_PIN_U)
        self.dir_d = GPIO.input(DIR_PIN_D)
        self.dir_r = GPIO.input(DIR_PIN_R)
        self.dir_l = GPIO.input(DIR_PIN_L)
        self.btn_0 = GPIO.input(BTN_PIN_0)
        out = ""
        if self.dir_u:
            out += "u"
        if self.dir_d:
            out += "d"
        if self.dir_r:
            out += "r"
        if self.dir_l:
            out += "l"
        if self.btn_0:
            out += "b"
        if out is not "":
            print(out)
        self.locked = False

    def destruct(self):
        GPIO.cleanup()

