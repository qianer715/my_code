# �鲢����  
def mergeSort(unsortedList):  
    if len(unsortedList)<2:  
        return unsortedList  
    sortedList=[]  
    left=mergeSort(unsortedList[:len(unsortedList)/2])  
    right=mergeSort(unsortedList[len(unsortedList)/2:])  
    while len(left)>0 and len(right)>0:  
        if left[0]<right[0]:  
            sortedList.append(left.pop(0))  
        else:  
            sortedList.append(right.pop(0))  
    if len(left)>0:  
        sortedList.extend(mergeSort(left))  # extend()����ֻ����һ���б���Ϊ�����������ò�����ÿ��Ԫ�ض���ӵ�ԭ�е��б���
    else:  
        sortedList.extend(mergeSort(right))  
    return sortedList  