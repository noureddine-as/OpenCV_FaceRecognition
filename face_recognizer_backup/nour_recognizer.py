import cv2, os
import numpy as np
from PIL import Image

#image_paths = []



def get_test_img_paths(path):
    test_img_paths = []
    for f in os.listdir(path) :
        if int(f.split("_")[1].split(".")[0]) > 19 :
            test_img_paths.append(f)
    return test_img_paths

def get_images_and_labels(path):
    training_imgs_paths = []
    for f in os.listdir(path) :
        if int(f.split("_")[1].split(".")[0]) <= 19 :
            training_imgs_paths.append(os.path.join(path, f))

  #  image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []

    for image_path in training_imgs_paths:
        image_pil = Image.open(image_path).convert('L')
        image = np.array(image_pil, 'uint8')
        images.append(image)   #[y: y + h, x: x + w])
        subject_id = int(os.path.split(image_path)[1].split("_")[0])
        labels.append(subject_id)
        cv2.imshow("TRAINING - %d" % int(f.split("_")[1].split(".")[0]) , image)  #[y: y + h, x: x + w])
        cv2.waitKey(50)
    return images, labels

images_path = './images'

# For face detection we will use the Haar Cascade provided by OpenCV.
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# For face recognition we will the the LBPH Face Recognizer
recognizer = cv2.createLBPHFaceRecognizer()
#recognizer = cv2.createFisherFaceRecognizer()

images, labels = get_images_and_labels(images_path)

cv2.destroyAllWindows()

# Perform the tranining
recognizer.train(images, np.array(labels))

# Append the images with the extension .sad into image_paths
test_img_paths = get_test_img_paths(images_path)   #[os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]
for image_path in test_img_paths:
    predict_image_pil = Image.open(os.path.join(images_path, image_path)).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')
    nbr_predicted, conf = recognizer.predict(predict_image)   ##[y: y + h, x: x + w])
    nbr_actual = int(os.path.split(image_path)[1].split("_")[0])   #.replace("subject", ""))
    if nbr_actual == nbr_predicted:
        print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
    else:
        print "{} is Incorrect Recognized as {}".format(nbr_actual, nbr_predicted)
    cv2.imshow("Recognizing Face", predict_image)  # [y: y + h, x: x + w])
    cv2.waitKey(1000)

    # faces = faceCascade.detectMultiScale(predict_image)
    # for (x, y, w, h) in faces:
    #     nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
    #     nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
    #     if nbr_actual == nbr_predicted:
    #         print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
    #     else:
    #         print "{} is Incorrect Recognized as {}".format(nbr_actual, nbr_predicted)
    #     cv2.imshow("Recognizing Face", predict_image) #[y: y + h, x: x + w])
    #     cv2.waitKey(1000)

