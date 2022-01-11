import cv2
from PIL import Image
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
n=0
i=0
while True:

    check, image = video.read()
    n+=1
    print(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0))

    if n%75 == 0 :
        i+=1
        cv2.imwrite("Image"+str(i)+".png", image)
        img = Image.open("D:\Travail\ENSEA\Projets_ENSEA\Projet_2A\python\Image"+str(i)+".png")
        box = (x, y, x+w, y+h)
        im = img.crop(box)
        im.save("Imageredim"+str(i)+".png", "PNG")

    cv2.imshow("capture", image)
    if cv2.waitKey(1) == ord('a'):
        break
video.release()
cv2.destroyAllWindows()


