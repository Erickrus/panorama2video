from tqdm import tqdm

from PIL import Image
import imageio
import numpy as np
import sys

class Panorama2Video:
    def __init__(self):
        pass

    def process(self, inputFilename, outputFilename, reversedInd=False):
        im = Image.open(inputFilename)
        width, height = im.size
        finalWidth, finalHeight = 1080, 1920
        ratio = float(finalHeight) / float(height)
        
        clipWidth =  int(float(height) / 1920. * 1080.)
        writer = imageio.get_writer(outputFilename, fps=25)
        if not reversedInd:
            x = range(width-clipWidth+1)
        else:
            x = reversed(range(width-clipWidth+1))

        for i in tqdm(x):
            if i%16!=0:
                continue
            #print([i,0,i+clipWidth, height])
            imCropped = im.crop([i,0,i+clipWidth, height])        
            writer.append_data(np.array(imCropped))
        writer.close()

if __name__ == "__main__":
    anotherP2v = Panorama2Video()
    if len(sys.argv)==3:
        anotherP2v.process(sys.argv[1], sys.argv[2], False)
    else:
        anotherP2v.process(sys.argv[1], sys.argv[2], True)