import json
import os
import re

class Json ():
        user_json = json.load(open("/home/akako/pixelByPixel/user.json"))
        world_json = json.load(open("/home/akako/pixelByPixel/world_generator/world_gen.json"))
        world_folder = world_json["world_folder"]
        world_size = world_json["world_size"]
        chunck_size = world_json["chunck_size"]

worldMap={}

x = 0
y = 1
i = 1

for file in sorted(os.listdir(Json.world_folder), key=lambda x: (int(re.sub('\D','',x)),x)):
        if x == Json.world_size and y < Json.world_size:
                x = 1
                y += 1
        elif x == Json.world_size and y == Json.world_size:
                x = 1
                y = 1
        else:
                x += 1
        #print((x,y), file)
        worldMap[(x,y)] = file
tile_size = Json.user_json["pixel_size"]
screen_width = 800
screen_height = 800
"""
for file_list_2 in file_list:
        for file in file_list_2:
                for in_file in json.load(open(world_folder+file)):
                        for index, pixel in enumerate(in_file):
                                if x == chunck_size and y < chunck_size:
                                        x = 1
                                        y += 1
                                elif x == chunck_size and y == chunck_size:
                                        x = 1
                                        y = 1
                                else:
                                                x += 1
                                worldMap[(x,y)]=pixeltile_size = Json.user_json["pixel_size"]
screen_width = 800
screen_height = 800
"""
