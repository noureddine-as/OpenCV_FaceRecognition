import cv2

class ImageDbManager():
    def __init__(self, id, lastName, cascadePath="haarcascade_frontalface_default.xml", NB_TRAINING_IMGS = 10):
        self.id = id
        self.cpt = 0
        self.WIN_TITLE = "Adding " + str(id) + " - " + lastName
        self.NB_TRAINING_IMGS = NB_TRAINING_IMGS
        self.IMG_FOLDER = "images"
        self.faceCascade = cv2.CascadeClassifier(cascadePath)
        cv2.namedWindow(self.WIN_TITLE)

    def insert_cpt(self, imge):
        cv2.rectangle(imge, (30,30), (185, 60), (255, 0,0) , 3)
        cv2.putText(imge, "Taken photos " + str(self.cpt) , (45,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0))

    def run(self):
        cap = cv2.VideoCapture(0)
        while 1:
            _, img = cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            self.insert_cpt(img)
            cv2.imshow(self.WIN_TITLE , img)

            k = cv2.waitKey(1) & 0xFF
            if k == ord('s') :
                _, img = cap.read()
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = self.faceCascade.detectMultiScale(img)
                if len(faces) > 0:
                    cv2.imwrite('{}/{}_{}.jpg'.format(self.IMG_FOLDER, str(self.id), self.cpt) , img)
                    self.cpt += 1
                    print(self.cpt)

            if k == ord('q') and (self.cpt >= self.NB_TRAINING_IMGS) :
                break
        cv2.destroyWindow(self.WIN_TITLE)

#if __name__ == "__main__":
#    mgr = ImageDbManager(id=44 , lastName="Hello")
#    mgr.run()