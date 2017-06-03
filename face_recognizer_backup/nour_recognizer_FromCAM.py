import cv2, os
import numpy as np
from PIL import Image
from xml_parser import *

#image_paths = []

CROPPING_ENABLED = True
NB_TRAINING_IMGS = 10

def get_test_img_paths(path):
    test_img_paths = []
    for f in os.listdir(path) :
        if int(f.split("_")[1].split(".")[0]) >= NB_TRAINING_IMGS :
            test_img_paths.append(f)
    return test_img_paths

def get_images_and_labels(path):
    training_imgs_paths = []
    for f in os.listdir(path) :
        if int(f.split("_")[1].split(".")[0]) < NB_TRAINING_IMGS :
            training_imgs_paths.append(os.path.join(path, f))

  #  image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    # images will contains face images
    training_images = []
    # labels will contains the label that is assigned to the image
    labels = []

    if not CROPPING_ENABLED :
        for image_path in training_imgs_paths:
            image_pil = Image.open(image_path).convert('L')
            image = np.array(image_pil, 'uint8')
            training_images.append(image)   #[y: y + h, x: x + w])
            subject_id = int(os.path.split(image_path)[1].split("_")[0])
            labels.append(subject_id)
            cv2.imshow("TRAINING - %d" % subject_id, image)   #cv2.imshow("TRAINING - %d" % int(f.split("_")[1].split(".")[0]) , image)  #[y: y + h, x: x + w])
            cv2.waitKey(10)
    else :
        for image_path in training_imgs_paths:
            image_pil = Image.open(image_path).convert('L')
            image = np.array(image_pil, 'uint8')
            #training_images.append(image)   #[y: y + h, x: x + w])

            #labels.append(subject_id)

            faces = faceCascade.detectMultiScale(image)
            # If face is detected, append the face to images and the label to labels
            for (x, y, w, h) in faces:
                training_images.append(image[y: y + h, x: x + w])
                subject_id = int(os.path.split(image_path)[1].split("_")[0])
                labels.append(subject_id)
                cv2.imshow("TRAINING - %d" % subject_id , image)  #int(f.split("_")[1].split(".")[0]), image)  # [y: y + h, x: x + w])
                cv2.waitKey(10)

            cv2.imshow("TRAINING - %d" % int(f.split("_")[1].split(".")[0]) , image)  #[y: y + h, x: x + w])
            cv2.waitKey(50)

    return training_images, labels

images_path = './images'

# For face detection we will use the Haar Cascade provided by OpenCV.
#cascadePath = "haarcascade_profileface.xml"
last_names = get_LastNames()
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# For face recognition we will the the LBPH Face Recognizer
recognizer = cv2.createLBPHFaceRecognizer()
#recognizer = cv2.createEigenFaceRecognizer()

images, labels = get_images_and_labels(images_path)

cv2.destroyAllWindows()

# Perform the tranining
recognizer.train(images, np.array(labels))

# Append the images with the extension .sad into image_paths
test_img_paths = get_test_img_paths(images_path)   #[os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]
#for image_path in test_img_paths:
cap = cv2.VideoCapture(0)

while(1):
    #predict_image_pil = Image.open(os.path.join(images_path, image_path)).convert('L')
    #predict_image = np.array(predict_image_pil, 'uint8')
    _, predict_image = cap.read()

    # Our operations on the frame come here
    predict_image = cv2.cvtColor(predict_image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(predict_image)

    # Display the resulting frame
   # cv2.imshow('CAM', predict_image)

    #faces = faceCascade.detectMultiScale(predict_image)

    if len(faces) > 0:
        max_area = 0
        x = y = w = h = 0
        for (_x, _y, _w, _h) in faces:
            a = _w*_h   #cv2.contourArea(i)
            if a > max_area:
                max_area = a
                x, y, w, h = _x, _y, _w, _h
        cv2.rectangle(img=predict_image, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 0), thickness=2)
        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        # if nbr_predicted == 1:  ## nbr_actual:
        #     print "1 is Correctly Recognized with confidence {}".format(conf)
        #
        # if nbr_predicted == 2:  ## nbr_actual:
        #     print "2 is Correctly Recognized with confidence {}".format(conf)

        print "{} is Recognized with confidence {}".format(last_names[nbr_predicted], conf)

        cv2.imshow("Recognizing Face", predict_image)  # [y: y + h, x: x + w])
    #cv2.waitKey(1000)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

