import aedat
import math
import os
import PIL.Image

print(os.getcwdb())
decoder = aedat.Decoder("CYTech/PFE/malo-gesture.aedat4")
print(decoder.id_to_stream())

for packet in decoder:
    print("stream_id", packet["stream_id"], end=": ")
    if("events" in packet):
        print("{} polarity events".format(len(packet["events"])))
    elif("frame" in packet):
        print("{} x {} frame".format(packet["frame"]["width"], packet["frame"]["height"]))
    elif("imus" in packet):
        print("{} IMU samples".format(len(packet["imus"])))
    elif("triggers" in packet):
        print("{} trigger events".format(len(packet["triggers"])))

'''
index = 0
for packet in decoder:
    if("frame" in packet):
        image = PIL.Image.fromarray(packet["frame"]['pixels'], mode=packet["frame"]["format"],)
        image.save(f"{index}.png")
        index += 1
'''