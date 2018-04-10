"""
TUGAS BESAR 2 STRATEGI ALGORITMA
CONVEX HULL
ALBERT SAHALA THEODOROE (13516022)
"""

import time
import matplotlib.pyplot as plt
from math import sqrt
from random import uniform
result = []

def random_point(n):
	# Random titik dalam koordinat x dan y
	return[(uniform(-10, 10), uniform(-10, 10)) for i in range(n)]

def points_distance(point1,point2):
	# Menghitung jarak dua titik dengan rumus matematika
	return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def line_point_distance(point,line):
	(x0,y0) = line[0]
	(x1,y1) = line[1]
	(x2,y2) = point

	# Menghitung jarak titik dengan garis menggunakan rumus matematika
	return ((y1-y0)*x2 - (x1-x0)*y2 + x1*y0 - y1*x0) / points_distance((x0,y0),(x1,y1))

def upper_convex_hull(upper_points, line):
	global result
	max_point = []
	if(len(upper_points) > 0):
		max_point = upper_points[0]
		for point in upper_points:
			if(line_point_distance(point,line) > line_point_distance(max_point,line)):
				max_point = point

		result.append(max_point)
		initial_line = (line[0],max_point)
		next_line = (max_point,line[1])
		if (max_point in upper_points):
			upper_points.remove(max_point)

		max_point1 = []
		max_point2 = []

		for point in upper_points:
			if(line_point_distance(point,initial_line) > 0):
				max_point1.append(point)
		for point in upper_points:
			if (line_point_distance(point,next_line) > 0):
				max_point2.append(point)

		upper_convex_hull(max_point1,initial_line)
		upper_convex_hull(max_point2,next_line)

def lower_convex_hull(lower_points, line):
	global result
	min_point = []
	if(len(lower_points) > 0):
		min_point = lower_points[0]
		for point in lower_points:
			if(line_point_distance(point,line) < line_point_distance(min_point,line)):
				min_point = point

		result.append(min_point)
		initial_line = (line[0],min_point)
		next_line = (min_point,line[1])
		if (min_point in lower_points):
			lower_points.remove(min_point)

		min_point1 = []
		min_point2 = []

		for point in lower_points:
			if(line_point_distance(point,initial_line) < 0):
				min_point1.append(point)
		for point in lower_points:
			if(line_point_distance(point,next_line) < 0):
				min_point2.append(point)

		lower_convex_hull(min_point1,initial_line)
		lower_convex_hull(min_point2,next_line)

def convex_hull(points):
	global result
	points.sort()
	upper_points = []
	lower_points = []

	result.append(points[0])
	result.append(points[-1])
	line = (points[0],points[-1])
	points.remove(points[0])
	points.remove(points[-1])

	if(len(points) > 0):
		for point in points:
			if(line_point_distance(point,line) > 0):
				upper_points.append(point)
			elif (line_point_distance(point,line) < 0):
				lower_points.append(point)
	upper_convex_hull(upper_points,line)
	lower_convex_hull(lower_points,line)

def to_x(m):
	list_x = []
	for point in m:
		list_x.append(point[0])
	return list_x

def to_y(m):
	list_y = []
	for point in m:
		list_y.append(point[1])
	return list_y

def shape():
	global result
	result.sort()
	line = (result[0],result[-1])
	list_a = []
	list_b = []

	for point in result:
		if(line_point_distance(point,line) > 0):
			list_a.append(point)
		elif(line_point_distance(point,line) < 0):
			list_b.append(point)

	list_a.sort()
	list_b.sort(reverse = True)

	list_of_result = []

	list_of_result.append(result[0])
	list_of_result = list_of_result + list_a
	list_of_result.append(result[-1])
	list_of_result = list_of_result + list_b
	list_of_result.append(result[0])

	result = list_of_result

def main():
	start = time.time()
	global result
	n = int(input("Masukkan Jumlah Titik : "))
	points = random_point(n)
	x = to_x(points)
	y = to_y(points)
	print(n, "titik yang membentuk Convex Hull : ",points)

	plt.plot(x,y,"ro",markersize = 2)

	convex_hull(points)
	xr = to_x(result)
	yr = to_y(result)

	plt.plot(xr,yr,"bo",markersize = 4)
	shape()
	

	absis = to_x(result)
	ordinat = to_y(result)

	plt.plot(absis,ordinat,"r-")
	finish = time.time()
	print("Lama Waktu Eksekusi :",finish-start,"seconds")

	plt.show()

if __name__ == '__main__':
	main()






