import random

def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr

def mergeSort(arr):
    if len(arr)==1:
        return arr
    middle=int(len(arr)/2)
    left=mergeSort(arr[0:middle])
    right=mergeSort(arr[middle:len(arr)])

    merged=False
    il=0
    ir=0
    new_arr=[]
    for times in range(len(left)+len(right)):
        if left[il] > right[ir]:
            new_arr.append(right[ir])
            ir+=1
        else:
            new_arr.append(left[il])
            il+=1

        if il>=len(left):
            for x in right[ir:]:
                new_arr.append(x)
            break

        if ir>=len(right):
            for x in left[il:]:
                new_arr.append(x)
            break
    return insertionSort(new_arr)

def quickSort(arr):
    if len(arr)==0:
        return []
    if len(arr)==1:
        return arr

    arr_l=[]
    arr_r=[]
    pivot=arr[len(arr)-1]

    for it in arr[:-1]:
        if it>=pivot:
            arr_r.append(it)
        else:
            arr_l.append(it)

    left=quickSort(arr_l)
    right=quickSort(arr_r)

    return left+[pivot]+right

def radixSort(arr):
    arr_str=list(map(lambda x:str(x),arr))
    continue_loop=True
    adjust=0
    while continue_loop:
        digits={}
        counter=0
        for it in arr_str:
            index=len(it)-1-adjust
            if index<0:
                counter+=1
                continue
            if not it[index] in digits.keys():
                digits[it[index]]=[]
            digits[it[index]].append(it)
            arr_str=[]
            for i in range(10):
                if not str(i) in digits.keys():
                    continue
                for v in digits[str(i)]:
                    arr_str.append(v)
        adjust+=1
        if counter>=len(arr_str):
            break

    return list(map(lambda x:int(x),arr_str))


def countingSort(arr,max):
    aux=[0 for x in range(max)]
    for it in arr:
        aux[it]+=1
    for i in range(0,len(aux)-1):
        aux[i+1]+=aux[i]
    final=[0 for x in range(len(arr))]
    for it in arr:
        final[aux[it]-1]=it
        aux[it]-=1

    return final

def bucketSort(arr,max):
    arr=[1/x for x in arr]
    aux=[[] for x in range(max)]
    for it in arr:
        index=int(it*max)-1
        aux[index].append(it)
    for i in range(len(aux)):
        aux[i]=selectionSort(aux[i])
    final=[]
    for v in aux:
        for v2 in v:
            final.append(v2)
    return final

def shellSort(arr):
    h=int(len(arr)/2)
    while h>=0:
        change=False
        for i in range(len(arr)):
            index=i+h
            if index >=len(arr):
                continue
            if arr[i] > arr[index]:
                arr[i],arr[index]=arr[index],arr[i]
                change=True
        h=int(h/2)
        if h==0:
            if not change:
                break
            h=1


    return arr


if __name__ == '__main__':
    base=[random.randint(1,9) for x in range(10)]
    print(base)
    print(selectionSort(base))
    print(bubbleSort(base))
    print(insertionSort(base))
    print(mergeSort(base))
    print(quickSort(base))
    print(radixSort(base))
    print(countingSort(base,10))
    print(bucketSort(base,len(base)))
    print(shellSort(base))
