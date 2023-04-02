import RPi.GPIO as GPIO
import time

# 
IN1 = 18
IN2 = 23
IN3 = 24
IN4 = 25

STEP_PATTERN = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]

INTERVAL = 0.001

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def rotate(degrees, direction='CW'):
    if direction == 'CCW':
        step_pattern = list(reversed(STEP_PATTERN))
    else :
        step_pattern = STEP_PATTERN
        
    steps = int((512/360) * degrees)
    for i in range(steps):
        for j in range(len(step_pattern)):
            GPIO.output(IN1, step_pattern[j][0])
            GPIO.output(IN2, step_pattern[j][1])
            GPIO.output(IN3, step_pattern[j][2])
            GPIO.output(IN4, step_pattern[j][3])
            time.sleep(INTERVAL)

def cleanup():
    GPIO.cleanup()

degrees = 200
rotate(degrees, direction='CW')
time.sleep(3)
rotate(degrees, direction='CCW')


cleanup()            


