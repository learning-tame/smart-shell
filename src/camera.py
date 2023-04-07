import picamera

PICTURE_WIDE = 800
PICTURE_HEIGHT = 600

SAVE_DIR = '/home/pi/Pictures/'

def take_picture():
  # camera setup
  cam = picamera.PiCamera()
  cam.resolution = (PICTURE_WIDE, PICTURE_HEIGHT)

  # save file
  file_name = 'test.jpg'
  save_file = SAVE_DIR + file_name

  cam.capture(save_file)
  cam.close()

# usage
# take_picture()