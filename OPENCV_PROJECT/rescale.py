import cv2 as cv

# img = cv.imread('image/s.jpg')

# cv.imshow('shane', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



capture = cv.VideoCapture('vidio/1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, scale=.10)
    frame_resize2 = rescaleFrame(frame, scale=.5)
    frame_resize3 = rescaleFrame(frame, scale=.8)
    frame_resize4 = rescaleFrame(frame, scale=.15)
    frame_resize5 = rescaleFrame(frame, scale=.20)

    

    cv.imshow('Video', frame)
    cv.imshow('Video Resize', frame_resize)
    cv.imshow('Video Resize2', frame_resize2)
    cv.imshow('Video Resize3', frame_resize3)
    cv.imshow('Video Resize4', frame_resize4)
    cv.imshow('Video Resize5', frame_resize5)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)