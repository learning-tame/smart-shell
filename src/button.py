import RPi.GPIO as GPIO
import time
import camera

# ボタンにつながる配線
BtnPin = 26

# GPIOセットアップ
def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(BtnPin, GPIO.IN)

# Define a callback function for button callback
def click(ev=None):
  print('click')
  '''ここでボタンを押したときにしたい処理を呼ぶ'''
  camera.take_picture()
  # 連続クリックを防ぐ
  time.sleep(1)

# ボタンのクリックを待ち受ける関数
def main():
  GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=click)
  while True:
    time.sleep(1)

# 処理終了時にGPIOピンを解放する
def destroy():
  GPIO.cleanup()

# メイン処理。Ctrl+Cを押すまでボタンのクリックを待ち受ける
if __name__ == '__main__':
  setup()
  try:
    main()
  except KeyboardInterrupt:
    destroy()
