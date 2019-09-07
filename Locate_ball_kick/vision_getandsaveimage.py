import time                                        #import time for Nao
from PIL import Image                              #import image from pillow
import config                                      #import configuration module to interact with nao
from naoqi import ALProxy                               #to work with proxy
def showNaoImage(IP, PORT,camera_id):                 #
  camProxy = config.loadProxy("ALVideoDevice")           #Service which give capability to use videodevice of Nao
  camProxy.kCameraSelectID=18
  print camProxy.getParam(camProxy.kCameraSelectID)
  camProxy.setParam(camProxy.kCameraSelectID,camera_id)
  resolution =  1   # VGA
  colorSpace = 11   # RGB
  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
  naoImage = []
  naoImage = camProxy.getImageRemote(videoClient) 
  camProxy.unsubscribe(videoClient)
  print (naoImage)
  
  # Now we work with the image returned and save it as a PNG  using ImageDraw
    # package.

    # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]
  
  # Create a PIL Image from our pixel array.
  im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
  
   # Save the image.
  im.save("camImage.png", "PNG")
  im.show()

if __name__ == '__main__':
  IP = "192.168.43.11"  # Replace here with your NaoQi's IP address.
  PORT = 9559
  showNaoImage(IP, PORT)
