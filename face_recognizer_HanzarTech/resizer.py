import os, cv2
#
# i = 0
# for f in os.listdir("fromcam") :
#     os.rename(os.path.join("fromcam/" , f ) , os.path.join("fromcam/" , "subj01_{}.jpg".format(i)))
#     i += 1
#     print f

# haarcascade_profileface.xml
cascadePath = "haarcascade_profileface.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

cv2.namedWindow("h")
#cv2.namedWindow("cropped")


for f in os.listdir("fromcam") :
    img = cv2.imread("fromcam/{}".format(f))

    #faces = faceCascade.detectMultiScale(img)

    #cv2.imshow("h", img)
    #print f , "   ->>  "
    #for (x, y, w, h) in faces:
    #    cv2.rectangle(img=img, pt1=(x, y) , pt2=(x+w, y+h), color=(255, 0, 0), thikness=3)
    cv2.imwrite("fromcam/{}_cropped.jpg".format(f), img) #[y: y + h, x: x + w])

    cv2.waitKey()

    #cv2.waitKey(1000)


cv2.waitKey()
