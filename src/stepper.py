import RPi.GPIO as GPIO
import time

# GPIOピン番号設定
IN1 = 18
IN2 = 23
IN3 = 24
IN4 = 25

# 28BYJ-48ステッピングモーター(2相ユニポーラ式)用のシーケンス設定
STEP_PATTERN = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

'''_
ステッピングモーターを回転する
Arguments
degrees(int): 回転する角度
  direction(str): 回転する方向。CW or CCW
  interval(float): 回転する度に停止する時間。これが短いほど速く回転する
Returns
'''
def rotate(degrees, direction='CW', interval=0.001):
  # 回転方向に応じてシーケンスパターンを設定
  if direction == 'CCW':
    step_pattern = list(reversed(STEP_PATTERN))
  else :
    step_pattern = STEP_PATTERN

  # 指定した角度分回転する
  steps = int((512/360) * degrees)
  for i in range(steps):
    for j in range(len(step_pattern)):
      GPIO.output(IN1, step_pattern[j][0])
      GPIO.output(IN2, step_pattern[j][1])
      GPIO.output(IN3, step_pattern[j][2])
      GPIO.output(IN4, step_pattern[j][3])
      # interval分停止する
      time.sleep(interval)

'''
GPIOピンの解放
'''
def cleanup():
  GPIO.cleanup()

degrees = 200 # 回転角度=速度
interval = 0.001 # 回転の度の停止時間=小さいほど速い。小さすぎると上手く動かない。0.001以上は必要
# 正回転
rotate(degrees, direction='CW', interval=interval)
# 一時停止
time.sleep(1)
# 逆回転
rotate(degrees, direction='CCW',  interval=interval)

cleanup()
