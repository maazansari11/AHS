import cv2 as cv
import json
import numpy as np
import pandas as pd
# from json import JSONEncoder
import pickle

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

class JsonObject:
	row = []
	min_x = []
	min_y = []
	max_x = []
	max_y = []
	is_inner_contour = []
	def __init__(self,row,min_x,min_y,max_x,max_y,is_inner_contour):
		self.row = row
		self.min_x = min_x
		self.min_y = min_y
		self.max_x = max_x
		self.max_y = max_y
		self.is_inner_contour = is_inner_contour

	def __int__(self,dict):
		self.dict = dict


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

# dict.index =
# 	me.age = 35
# 	me.dog = Object()
# 	me.dog.name = "Apollo"
list_of_numbers = [90, 26, 67, 47, 8]
list_of_contour_rect_coordinates = pd.read_csv('list.csv',header=None,delimiter=',')
tuples = [tuple(x) for x in list_of_contour_rect_coordinates.values]
index_of_inner_contours = []
print(tuples)
img = np.zeros(shape =[2000,2000,3], dtype=np.uint8)
def plot_rectangles(img,tuples,color):

	# dict = JsonObject()


	# print(me.toJSON())
	for rectangle in tuples:
		_is_inner_contour = False
		if tuples.index(rectangle) in index_of_inner_contours :
			_is_inner_contour = True
		row_rect = 'row'+str(tuples.index(rectangle))
		row_rectangle = JsonObject(rectangle[0],rectangle[1],rectangle[2],rectangle[3],rectangle[4],tuples.index(rectangle) in index_of_inner_contours)
		# dict[row_rect].index_of_rect = rectangle[0]
		# dict[row_rect].min_x = rectangle[1]
		# dict[row_rect].min_y = rectangle[2]
		# dict[row_rect].max_x = rectangle[3]
		# dict[row_rect].max_y = rectangle[4]
		# dict[row_rect].is_inner_contour = tuples.index(rectangle) in index_of_inner_contours

		# dict.toJSON()
	# dict.toJSON()
		# dict[str(rectangle[0])] = {'index':str(rectangle[0]) , 'min_x':str(rectangle[1]) , 'min_y':str(rectangle[2]) , 'max_x':str(rectangle[3]) , 'max_y':str(rectangle[4]), 'is_inner_contour': str(tuples.index(rectangle) in index_of_inner_contours)}
# for index in dict['is_inner_contour']:
# 		print('dict ' + str(dict))
# print(json.dumps())

# if index in list: True else: Falses

def list_inner_contour():
	for rectangle in tuples:
		index_of_rectangle = tuples.index(rectangle)
		i = 0
		while i < len(tuples):
			if i != index_of_rectangle:
				if rectangle[1] > 	tuples[i][1] and rectangle[2] > tuples[i][2] \
					and rectangle[3] < 	tuples[i][3] and rectangle[4] < tuples[i][4]:
					index_of_inner_contours.append(index_of_rectangle)
			i+=1

	return True
def slice_on_custom_list_of_indices(tuples,list_of_indices):
	sliced_tuple = []
	for index in list_of_indices:
		sliced_tuple.append(tuples[index])
	return sliced_tuple
list_inner_contour()
plot_rectangles(img,tuples,(0,255,0))
tuple_of_inner_contours = slice_on_custom_list_of_indices(tuples,index_of_inner_contours)
plot_rectangles(img,tuple_of_inner_contours,(0,0,255))

# object = dict()
# json_object = jsonpickle.encode(object)
# json_file = json.dumps(dict)
with open('A1.json','w') as f:
	f.write(dict)

# json_file = json.dumps(dict)
# print(index_of_inner_contours)
# print(dict['index'])
# cv.imshow('rectangles',img)
# cv.waitKey(0)
#for list in tuples:

	# for number in list:
	# 	index = list.index(number)
	# 	print(number)
	# 	# if index < len(list_of_numbers)-1:
		# 	if int(number) > list_of_numbers[index+1]:
		# 		number_to_replace = list_of_numbers[index + 1]
		# 		list_of_numbers[index + 1] = number
		# 		list_of_numbers[index] = number_to_replace

