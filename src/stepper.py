import RPi.GPIO as GPIO
import time

class Stepper():

  def __init__(self):
    # GPIOピン番号設定
    self.IN1 = 18
    self.IN2 = 23
    self.IN3 = 24
    self.IN4 = 25

    # 28BYJ-48ステッピングモーター(2相ユニポーラ式)用のシーケンス設定
    self.STEP_PATTERN = [[1,0,0,1],
                    [1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1]]

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.IN1, GPIO.OUT)
    GPIO.setup(self.IN2, GPIO.OUT)
    GPIO.setup(self.IN3, GPIO.OUT)
    GPIO.setup(self.IN4, GPIO.OUT)

  '''_
  ステッピングモーターを回転する
  Arguments
  degrees(int): 回転する角度
    direction(str): 回転する方向。CW or CCW
    interval(float): 回転する度に停止する時間。これが短いほど速く回転する
  Returns
  '''
  def rotate(self, degrees, direction='CW', interval=0.001):
    # 回転方向に応じてシーケンスパターンを設定
    if direction == 'CCW':
      step_pattern = list(reversed(self.STEP_PATTERN))
    else :
      step_pattern = self.STEP_PATTERN

    # 指定した角度分回転する
    steps = int((512/360) * degrees)
    for i in range(steps):
      for j in range(len(step_pattern)):
        GPIO.output(self.IN1, step_pattern[j][0])
        GPIO.output(self.IN2, step_pattern[j][1])
        GPIO.output(self.IN3, step_pattern[j][2])
        GPIO.output(self.IN4, step_pattern[j][3])
        # interval分停止する
        time.sleep(interval)

  '''
  GPIOピンの解放
  '''
  def cleanup(self):
    GPIO.cleanup()

  '''_summary_
  開いて、閉じる
  '''
  def open(self):
    degrees = 200 # 回転角度=速度
    interval = 0.001 # 回転の度の停止時間=小さいほど速い。小さすぎると上手く動かない。0.001以上は必要
    # 正回転
    self.rotate(degrees, direction='CW', interval=interval)
    # 一時停止
    time.sleep(1)
    # 逆回転
    self.rotate(degrees, direction='CCW',  interval=interval)

    # self.cleanup()

# usage
# stepper = Stepper()
# print(1)
# stepper.open()
# print(2)
# stepper.cleanup()
# print(3)