# -*- coding: UTF-8 -*-

import random

unsortedList = []

#generate an unsorted List
def generateUnsortedList(num):
	for i in range(0,num):  #[0,num-1]
		unsortedList.append(random.randint(0,100)) #������ [0, 100] ���������������� 0�� 100
	print unsortedList
	
#��������
def quickSort(unsortedList):  
    if len(unsortedList)<2:  
        return unsortedList  
    less=[]  
    greater=[]  
    middle=unsortedList.pop(0)  
    for item in unsortedList:  
        if item<middle:  
            less.append(item)  
        else:  
            greater.append(item)  
    return quickSort(less)+[middle]+quickSort(greater) 