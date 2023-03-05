import cv2
import numpy as np

# 画像を読み込む
path = "images/operate-enable.png"
img = cv2.imread(path)

# 画像サイズの取得
height = img.shape[0]
width = img.shape[1]
print(f"width:{width}, height:{height}")
# 1080:2280 = 540:1140 = 270:570 = 27:57 = 9:19

# リサイズ
re1 = cv2.resize(img, dsize=None, fx=0.25, fy=0.25)

# トリミング
tr1 = img[1528:1709, 537:718]

# 赤色抽出
bgr = [66, 77, 219]
# bgr = [86, 124, 238]
# bgr = [28, 28, 124]
thresh = 50
minBGR = np.array([ 60, 70, 200 ])
maxBGR = np.array([ 100, 128, 255 ])
maskBGR = cv2.inRange(tr1, minBGR, maxBGR)
resultBGR = cv2.bitwise_and(tr1, tr1, mask=maskBGR)

# HSVに変換
imgHSV = cv2.cvtColor(tr1, cv2.COLOR_BGR2HSV)

# 画像を表示
# cv2.imshow('origin', img)
# cv2.imshow('trimming', tr1)
cv2.imshow('Result BGR', resultBGR)
cv2.imshow('Result mask', maskBGR)
# cv2.imshow('HSV', imgHSV)
cv2.waitKey(0)
cv2.destroyAllWindows()
