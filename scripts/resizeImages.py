import os

from wand.image import Image

sourceDirectory = r"C:\Users\Administrator\Documents\GitHub\ladybug-primer\images\components"
targetDirectory = r"C:\Users\Administrator\Documents\GitHub\ladybug-primer\images\500x500"

for i in os.listdir(sourceDirectory):
    with Image(filename = os.path.join(sourceDirectory, i), resolution=(300, 300)) as img:
        img.resize(500, 500)
        img.compression_quality = 99
        img.save(filename= os.path.join(targetDirectory, i))
