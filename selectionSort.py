# -*- coding: UTF-8 -*-

import random

unsortedList = []

#generate an unsorted List
def generateUnsortedList(num):
	for i in range(0,num):  #[0,num-1]
		unsortedList.append(random.randint(0,100)) #返回在 [0, 100] 区间的随机数，包括 0， 100
	print unsortedList

#选择排序
def selectionSort(unsortedList):
	list_length = len(unsortedList)
	for i in range(0,list_length-1):
		for j in range(i+1,list_length):
			if unsortedList[i]>unsortedList[j]:
				unsortedList[i],unsortedList[j] = unsortedList[j],unsortedList[i]
	return unsortedList
	
generateUnsortedList(20)
print selectionSort(unsortedList)