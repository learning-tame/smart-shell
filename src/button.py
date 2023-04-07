import RPi.GPIO as GPIO
import time
import camera
import stepper

class Button():

  # ダブルクリックかをチェックする
  def is_douoble_click(self):
    current_time = time.time()
    if current_time - self.last_click_time < 0.5:
      self.last_click_time = 0
      return True
    else:
      self.last_click_time = current_time
      return False

  # GPIOセットアップ
  def setup(self):
    # ボタンにつながる配線
    self.BtnPin = 26
    self.st = stepper.Stepper()
    self.last_click_time = 0

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.BtnPin, GPIO.IN)

  # Define a callback function for button callback
  def click(self, ev=None):
    if self.is_douoble_click():
      print('double click')
    else:
      print('click')
      '''ここでボタンを押したときにしたい処理を呼ぶ'''
      # 写真撮る
      camera.take_picture()
      # 連続クリックを防ぐ
      time.sleep(1)
      # モーターが動く
      self.st.open()

  # ボタンのクリックを待ち受ける関数
  def main(self):
    GPIO.add_event_detect(self.BtnPin, GPIO.FALLING, callback=self.click, bouncetime=500)
    while True:
      time.sleep(1)

  # 処理終了時にGPIOピンを解放する
  def destroy(self):
    GPIO.cleanup()

# メイン処理。Ctrl+Cを押すまでボタンのクリックを待ち受ける
if __name__ == '__main__':
  button = Button()
  button.setup()
  try:
    button.main()
  except KeyboardInterrupt:
    # st.cleanup()
    button.destroy()
