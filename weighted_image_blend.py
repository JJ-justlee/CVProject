import cv2

#cv2.COLOR_BGR2GRAY(make number of pixel be correct)
#ex) image1 = cv2.imread('./data/empireStateBuilding.jpg', cv2.COLOR_BGR2GRAY)
image1 = cv2.imread('./data/empireStateBuilding.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('./data/heartCloud.jpg', cv2.IMREAD_GRAYSCALE)

# 두 번째 이미지를 첫 번째 이미지와 동일한 크기로 조정
image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

image = cv2.addWeighted(image1, 0.7, image2_resized, 0.3, 0.0)

cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()