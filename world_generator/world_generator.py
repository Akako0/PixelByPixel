from multiprocessing import Process
import numpy as np
from PIL import Image
import random, json, os

#user data
user_data = json.load(open  ("/home/akako/pixelByPixel/user.json"))
threads = [None] # * user_data["threads_number"]

#world data
world_gen_data = json.load(open("/home/akako/pixelByPixel/world_generator/world_gen.json"))
player_chunck_size = world_gen_data["chunck_size"]
world_folder = world_gen_data["world_folder"]
world_size = world_gen_data["world_size"] **2
real_world_size = world_gen_data["world_size"]

# other values
player_file_template = world_folder+"P"
chuncks_per_threads = world_size / len(threads)
chunck2chunck_list = []

os.system('clear')
threads = [None] * user_data["threads_number"]

def thread_work (num_of_players2Process, _):
    for player_index in range(int(num_of_players2Process)):
        image_rgb = []

        #Creating a list of pixel of player_chunck_size size
        for pixel_row in range(player_chunck_size):
            image_rgb.append([])
            for _ in range(player_chunck_size):
                #Adding RGB tuple to a pixel
                pixel_color = random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)
                image_rgb[pixel_row].append(pixel_color)
        #Make an image with list of row add pixels [[(0,0,0), (0,0,1)], [(0,0,2),(0,0,3)]] for a 2x2 image
        # Convert the pixels into an array using numpy
        array = np.array(image_rgb, dtype=np.uint8)
    
        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image.save(player_file_template+str(player_index)+".png")


for i in range(user_data["threads_number"]):
    _ = None
    threads[i] = Process(target=thread_work, args=(chuncks_per_threads,i))

if input('generation ready, press ENTER to continue, N,enter for cancel: ').lower() == "n":
    print("ok, cancel.")
    quit()
if len(os.listdir(world_folder))>1:
    if input("existing world found, files will be deleted, press ENTER to continue, N,enter to cancel").lower() == "n":
        quit()
    for f in os.listdir(world_folder):
        os.remove(os.path.join(world_folder, f))

for i in range(len(threads)):
    threads[i].start()
print("working on it (this could take a while)...")
