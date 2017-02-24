# -*- coding: UTF-8 -*-

import random

unsortedList = []

#generate an unsorted List
def generateUnsortedList(num):
	for i in range(0,num):  #[0,num-1]
		unsortedList.append(random.randint(0,100)) #返回在 [0, 100] 区间的随机数，包括 0， 100
	print unsortedList

#筛选
def maxHeapify(L,heap_size,i):
	leftChildIndex = 2*i+1
	rightChildIndex = 2*i+2
	largest = i
	if leftChildIndex<heap_size and L[leftChildIndex]>L[largest]:
		largest = leftChildIndex
	if rightChildIndex<heap_size and L[rightChildIndex]>L[largest]:
		largest = rightChildIndex
	if largest != i:
		L[i],L[largest] = L[largest],L[i]
		maxHeapify(L,heap_size,largest)

#建立大顶堆
def bulidMaxHeap(L):
	heap_size = len(L)
	if heap_size>1:
		start = heap_size/2-1
	while start>=0:
		maxHeapify(L,heap_size,start)
#堆排序
def heapSort(L):
	heap_size = len(L)
	bulidMaxHeap(L)
	i = heap_size-1
	while i>0:
		L[0],L[i] = L[i],L[0]
		heap_size = heap_size-1
		i = i-1
		maxHeapify(L,heap_size,0)
		
generateUnsortedList(20)
print heapSort(unsortedList)