# -*- coding: UTF-8 -*-

import random

unsortedList = []

#generate an unsorted List
def generateUnsortedList(num):
	for i in range(0,num):  #[0,num-1]
		unsortedList.append(random.randint(0,100)) #返回在 [0, 100] 区间的随机数，包括 0， 100
	print unsortedList

#插入排序
def insertionSort(unsortedList):
	list_length = len(unsortedList)
	if list_length<2:
		return unsortedList
	for i in range(1,list_length):
		key = unsortedList[i]
		j = i-1
		while j>=0 and key<unsortedList[j]:
			unsortedList[j+1] = unsortedList[j]
			j = j-1
		unsortedList[j+1] = key 
	return unsortedList
generateUnsortedList(20)
print insertionSort(unsortedList)