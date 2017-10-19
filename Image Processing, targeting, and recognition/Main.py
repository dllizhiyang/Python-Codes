'''
import cv2
import numpy as np
minPlateRatio = 2.5 # 车牌最小比例
maxPlateRatio = 5   # 车牌最大比例
# 图像处理
def imageProcess(gray):
    # 高斯平滑
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
    # Sobel算子，X方向求梯度
    sobel = cv2.convertScaleAbs(cv2.Sobel(gaussian, cv2.CV_16S, 1, 0, ksize=3))
    # 二值化
    ret, binary = cv2.threshold(sobel, 150, 255, cv2.THRESH_BINARY)
    # 对二值化后的图像进行闭操作
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 4))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, element)
    # 再通过腐蚀->膨胀 去掉比较小的噪点
    erosion = cv2.erode(closed, None, iterations=2)
    dilation = cv2.dilate(erosion, None, iterations=2)
    # 返回最终图像
    return dilation
# 找到符合车牌形状的矩形
def findPlateNumberRegion(img):
    region = []
    # 查找外框轮廓
    contours_img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("contours lenth is :%s" % (len(contours)))
    # 筛选面积小的
    for i in range(len(contours)):
        cnt = contours[i]
        # 计算轮廓面积
        area = cv2.contourArea(cnt)
        # 面积小的忽略
        if area < 2000:
            continue
        # 转换成对应的矩形（最小）
        rect = cv2.minAreaRect(cnt)
        # print("rect is:%s" % {rect})
        # 根据矩形转成box类型，并int化
        box = np.int32(cv2.boxPoints(rect))
        # 计算高和宽
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        # 正常情况车牌长高比在2.7-5之间,那种两行的有可能小于2.5，这里不考虑
        ratio = float(width) / float(height)
        if ratio > maxPlateRatio or ratio < minPlateRatio:
            continue
        # 符合条件，加入到轮廓集合
        region.append(box)
    return region
def detect(img):
  # 转化成灰度图
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # 形态学变换的处理
  dilation = imageProcess(gray)
  # 查找车牌区域
  region = findPlateNumberRegion(dilation)
  print(len(region))
  # 默认取第一个
  #box = region[0]
  #在原图画出轮廓
  cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
  # 找出box四个角的x点，y点，构成数组并排序
  ys = [box[0, 1], box[1, 1], box[2, 1], box[3, 1]]
  xs = [box[0, 0], box[1, 0], box[2, 0], box[3, 0]]
  ys_sorted_index = np.argsort(ys)
  xs_sorted_index = np.argsort(xs)
  # 取最小的x，y 和最大的x，y 构成切割矩形对角线
  min_x = box[xs_sorted_index[0], 0]
  max_x = box[xs_sorted_index[3], 0]
  min_y = box[ys_sorted_index[0], 1]
  max_y = box[ys_sorted_index[3], 1]
  # 切割图片，其实就是取图片二维数组的在x、y维度上的最小minX,minY 到最大maxX,maxY区间的子数组
  img_plate = img[min_y:max_y, min_x:max_x]
  return img_plate
if __name__ == '__main__':
        imagePath = 'd:\\CarImage\\car_04.jpg' # 图片路径
        img = cv2.imread(imagePath)
        img = detect(img)
        cv2.imshow("img",img)
        cv2.waitKey(0)

'''

################################### Working code###############################################
# -*- coding: utf-8 -*-
# @Author: hyzhangyong
# @Date:   2016-06-23 16:21:54
# @Last Modified by:   hyzhangyong
# @Last Modified time: 2016-06-24 00:00:47
import sys
import cv2
import numpy as np

def preprocess(gray):
	# # 直方图均衡化
	# equ = cv2.equalizeHist(gray)
	# 高斯平滑
	gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
	# 中值滤波
	median = cv2.medianBlur(gaussian, 5)
	# Sobel算子，X方向求梯度
	sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0, ksize = 3)
	# 二值化
	ret, binary = cv2.threshold(sobel, 170, 255, cv2.THRESH_BINARY)
	# 膨胀和腐蚀操作的核函数
	element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
	element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 7))
	# 膨胀一次，让轮廓突出
	dilation = cv2.dilate(binary, element2, iterations = 1)
	# 腐蚀一次，去掉细节
	erosion = cv2.erode(dilation, element1, iterations = 1)
	# 再次膨胀，让轮廓明显一些
	dilation2 = cv2.dilate(erosion, element2,iterations = 3)
	cv2.imshow('dilation2',dilation2)
	#cv2.waitKey(0)
	return dilation2

def findPlateNumberRegion(img):
	region = []
	# 查找轮廓
	image, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#hierarchy
	# 筛选面积小的
	for i in range(len(contours)):
		cnt = contours[i]
		# 计算该轮廓的面积
		area = cv2.contourArea(cnt)

		# 面积小的都筛选掉
		if (area < 2000):
			continue

		# 轮廓近似，作用很小
		epsilon = 0.001 * cv2.arcLength(cnt,True)
		approx = cv2.approxPolyDP(cnt, epsilon, True)

		# 找到最小的矩形，该矩形可能有方向
		rect = cv2.minAreaRect(cnt)
		print ("rect is: ")
		print (rect)

		# box是四个点的坐标
		box = cv2.cv2.boxPoints(rect)
		box = np.int0(box)

		# 计算高和宽
		height = abs(box[0][1] - box[2][1])
		width = abs(box[0][0] - box[2][0])
		# 车牌正常情况下长高比在2.7-5之间
		ratio =float(width) / float(height)
		print (ratio)
		if (ratio > 5 or ratio < 2):
			continue
		region.append(box)

	return region

def detect(img):
	# 转化成灰度图
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# 形态学变换的预处理
	dilation = preprocess(gray)

	# 查找车牌区域
	region = findPlateNumberRegion(dilation)

	# 用绿线画出这些找到的轮廓
	for box in region:
		cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
	ys = [box[0, 1], box[1, 1], box[2, 1], box[3, 1]]
	xs = [box[0, 0], box[1, 0], box[2, 0], box[3, 0]]
	ys_sorted_index = np.argsort(ys)
	xs_sorted_index = np.argsort(xs)

	x1 = box[xs_sorted_index[0], 0]
	x2 = box[xs_sorted_index[3], 0]

	y1 = box[ys_sorted_index[0], 1]
	y2 = box[ys_sorted_index[3], 1]

	img_org2 = img.copy()
	img_plate = img_org2[y1:y2, x1:x2]
	cv2.imshow('number plate', img_plate)
	cv2.imwrite('number_plate.jpg', img_plate)

	cv2.namedWindow('img', cv2.WINDOW_NORMAL)
	cv2.imshow('img', img)

	# 带轮廓的图片
	cv2.imwrite('contours.png', img)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	imagePath = 'D:\CarImage\car_05.jpg'
	img = cv2.imread(imagePath)
	detect(img)
############################## Working Code############################################


'''
import cv2
import numpy as np
# 定义蓝底车牌的hsv颜色区间
lower_blue = np.array([100, 50, 50])
higher_blue = np.array([140, 255, 255])
minPlateRatio = 2.5 # 车牌最小比例
maxPlateRatio = 5   # 车牌最大比例
# 找到符合车牌形状的矩形
def findPlateNumberRegion(img):
    region = []
    # 查找外框轮廓
    contours_img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("contours lenth is :%s" % (len(contours)))
    # 筛选面积小的
    for i in range(len(contours)):
        cnt = contours[i]
        # 计算轮廓面积
        area = cv2.contourArea(cnt)
        # 面积小的忽略
        if area < 2000:
            continue
        # 转换成对应的矩形（最小）
        rect = cv2.minAreaRect(cnt)
        # print("rect is:%s" % {rect})
        # 根据矩形转成box类型，并int化
        box = np.int32(cv2.boxPoints(rect))
        # 计算高和宽
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        # 正常情况车牌长高比在2.7-5之间,那种两行的有可能小于2.5，这里不考虑
        ratio = float(width) / float(height)
        if ratio > maxPlateRatio or ratio < minPlateRatio:
            continue
        # 符合条件，加入到轮廓集合
        region.append(box)
    return region
if __name__ == '__main__':
    img = cv2.imread('D:\CarImage\car_04.jpg')
    # 转换成hsv模式图片
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 找到hsv图片下的所有符合蓝底颜色区间的像素点，转换成二值化图像
    in_range_array = cv2.inRange(hsv_img, lower_blue, higher_blue)
    # 进行闭操作，链接车牌区域
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 3))
    closed = cv2.morphologyEx(in_range_array, cv2.MORPH_CLOSE, element)
    # 进行开操作，去除细小噪点
    eroded = cv2.erode(closed, None, iterations=2)
    dilation = cv2.dilate(eroded, None, iterations=2)
    # 查找并筛选符合条件的矩形区域
    region = findPlateNumberRegion(dilation)
    # 标识出所有符合条件的矩形区域
    if len(region) != 0:
        for i in range(len(region)):
            box = region[i]
            rect_img = findRectImg(box, tmp_img)
            rect_imgs.append(rect_img)
            cv2.drawContours(img, [box], 0, (0, 255, 0), 1)
    cv2.imshow("img", img)

'''
