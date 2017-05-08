
import os, cv2

path_BGR = r"./images0"  # r"/home/aitsaid/Pictures/Webcam/Noureddine_Ait_Said_BGR_cropped"
path_GRAYSCALE = r"./images"   #r"/home/aitsaid/Pictures/Webcam/Noureddine_Ait_Said_GRAYSCALE_cropped"

i = 0
for f in os.listdir(path_BGR):
    img = cv2.imread(os.path.join(path_BGR, f), cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(os.path.join(path_GRAYSCALE, "002_%d.jpg"%i), img)
    i += 1
    print f

