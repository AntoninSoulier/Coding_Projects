from PIL import Image
import numpy as np
from scipy import signal as sig

im = Image.open("CYTech/AnalyseImage/Images/cameraman.png")
pixels = im.load()

largeur = im.width
hauteur = im.height

im.show()