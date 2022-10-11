from vklib import VK

def post_wall_message(text):
  print(vk.wall.post(message=text))