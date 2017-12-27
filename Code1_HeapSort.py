import random
import copy

def heapify(arr, index, length):
        left = 2 * index + 1
        while left < length:
                largest =  left + 1 if left+1 < length and arr[left+1] > arr[left] else left
                largest = largest if arr[largest] > arr[index] else index####
                if largest == index: #####
                        break

                arr[largest], arr[index] = arr[index], arr[largest]
                index = largest
                left = 2 * index + 1
                

def heapInsert(arr, index): # -1 // 2 ！=0 == -1
        parent_i = 0 if (index - 1)//2 < 0 else (index - 1)//2
        while arr[index] > arr[parent_i]:
                arr[index], arr[parent_i] = arr[parent_i], arr[index]
                index = parent_i
                parent_i = 0 if (index - 1)//2 < 0 else (index - 1)//2 
        

def heapSort(arr):
        if arr == None or len(arr) < 2:
                return None

        length = len(arr)
        for i in range(length):
                heapInsert(arr, i)

        length -= 1
        arr[0], arr[length] = arr[length], arr[0]

        while length > 0:
                heapify(arr, 0, length)
                length -= 1
                arr[0], arr[length] = arr[length], arr[0]

def generateRandomArray(maxLen, maxVal):
        arr = []
        length = int(maxLen * random.random() + 1)
        for _ in  range(length):
                arr.append(int(maxVal * random.random() + 1))
        return arr



if __name__ == '__main__':

        interNum = 5000
        maxLen = 100
        maxVal = 100
        succeed = True

        while interNum > 0:
                interNum -= 1

                arr = generateRandomArray(maxLen, maxVal)
                arrCopy = copy.copy(arr)

                arr.sort()
                heapSort(arrCopy)

                if arr != arrCopy:
                        succeed = False
                        break
        print(arrCopy)

        print('nice!' if succeed == True else 'Fucking Fucked!')
                

        

        
