import cv2 as cv

# img = cv.imread('image/s.jpg')

# cv.imshow('shane', img)

capture = cv.VideoCapture('vidio/1.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)