from vklib import VK

'''
 Copyright (C) 2022  Arseniy Meserakov

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; version 3.

 uvk is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

def login(number, passwd):
  client=VK("6146827qVxWRF1CwHERulrKBnqe", "client_secret")
  client.auth(number, passwd)
  client.wall.post(client.id, "UVK Client for Ubuntu touch test")