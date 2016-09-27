import re
import math
import textwrap
import os
import configparser
from PIL import Image, ImageFont, ImageDraw
from imgurpython import ImgurClient

config = configparser.ConfigParser()
config.read('authorization.ini')
client = ImgurClient(config['Imgur']['client_id'], config['Imgur']['client_secret'])

def write_matoran(string, id=0, dir='translations'):
  """
  Outputs a JPEG containing Matoran text given a string
  """

  message = ''.join(re.findall('[a-zA-Z0-9.:,;\'"(!?) ]', string))
  wrap = textwrap.wrap(message, width=24)

  font = ImageFont.truetype("Matoran.ttf", 24)
  h = font.getsize(message)[1]

  max = 0
  for line in wrap:
    if font.getsize(line)[0] > max:
      max = font.getsize(line)[0]

  size = (min(max, 500) + 10, len(wrap) * h + 7)

  image = Image.new('RGBA', size, color='white')
  draw = ImageDraw.Draw(image)

  offset = 2

  # use a truetype font
  for line in textwrap.wrap(message, width=24):
    draw.text((5, offset), line, fill='black', font=font)
    offset += h

  del draw

  if not os.path.exists(dir):
    os.makedirs(dir)

  image.save('translations/' + str(id) + '.jpg', 'JPEG')

def upload_matoran(img_path):
  data = client.upload_from_path(img_path)
  return data['link']
