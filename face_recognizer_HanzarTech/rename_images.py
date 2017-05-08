import os
import cv2

i = 0
path = "./images0"
for f in os.listdir(path) :
    #img = cv2.imread(os.path.join(path , f ) , cv2.IMREAD_GRAYSCALE)
    #cv2.imwrite(os.path.join(path , "001_%d.jpg"%i ), img)
    os.rename(os.path.join(path , f ) , os.path.join(path , "002_%d.jpg"%i ))
    #os.remove(os.path.join(path , f ))
    i += 1
    print f

