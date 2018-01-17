# 数据结构与算法 之 python实现
---
## 基础篇
### 1. 基本排序算法
* [冒泡排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Code1_BubbleSort.py "Code1_BubbleSort.py")
* [选择排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Code1_SelectionSort.py "Code1_SelectionSort.py")
* [插入排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Code1_InsertionSort.py "Code1_InsertionSort.py")
* [随机快排](https://github.com/lianyingteng/algorithm_practice/blob/master/Code1_QuickSort.py "Code1_QuickSort.py")
* [归并排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Code1_MergeSort.py "Code1_MergeSort.py")
* [堆排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Code1_HeapSort.py "Code1_HeapSort.py")
* [桶排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Code1_BucketSort.py "Code1_BucketSort.py")
   
#### 应用
* [最大间隔问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Code11_MaxGap.py)  求无序数组排序之后 相邻两数的最大差值？`【桶排序思想的应用】 `
* [小和问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Code11_MinSum.py)  给定一个数组，计算所有小和`【归并排序思想的应用】` 
* [荷兰国旗问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Code11_NetherlandsFlag.py)  小于的放在左边、等于的放在中间、大于的放在右边`【快排划分的应用】`
* [查找无序数组前k个最小的数](https://github.com/lianyingteng/algorithm_practice/blob/master/Code11_heapSort.py)  该程序基于堆排序思想，建立大小为k的大根堆。`注： 该问题的最优解是下节中的BFPRT算法` <br> 

### 2. KMP、Manacher、BFPRT
* [KMP算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Code2_KMP.py) `解决字符串匹配问题`
* [Manacher算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Code2_Manacher.py) `解决最长回文子串问题`
* [BFPRT算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Code2_BFPRT.py) `查找无序数组中第k小的数`
#### 应用
* [最短扩增序列（包含两个输入序列）](https://github.com/lianyingteng/algorithm_practice/blob/master/Code21_KMP_ShortestHaveTwice.py)  `【基于KMP的next数组构建】` <br> 

### 3. 数据结构

**数组题** <br>

* [使用数组实现栈结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_Array_To_Stack.py)
* [使用数组实现队列结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_Array_To_Queue.py)
* [实现可以输出栈中最小值的栈结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_GetMinStack.py)
* [两个栈实现队列结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_Stack_To_Queue.py)
* [两个队列实现栈结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_Queue_To_Stack.py)
* [猫狗队列](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_CatDogQueue.py) 
* [设计RandomPool结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_RandomPool.py) 
* [转圈打印矩阵](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_spiralOrderPrintMatrix.py) 
* [Z字形打印矩阵](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_spiralOrderPrintMatrix.py)
* [行列排好序的矩阵中找数](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_FindNumInSortedMatrix.py)<br> 

**链表题**<br> 
* [打印两个有序链表的公共部分](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_PrintCommonPart.py)  `注： Node类中， value和next依附于实例`
* [链表是回文结构？](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_LinkedListIsPalindrome.py)
* [链表的Partition过程](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_SmallerEqualBigger.py) 
* [复制含有随机指针节点的链表](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_CopyListWithRandom.py)
* [寻找两个单链表第一个相交的结点](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_FindFirstIntersectNode.py)
* [反转单(双)向链表](https://github.com/lianyingteng/algorithm_practice/blob/master/Code3_ReverseList.py)

**堆结构的应用** <br>
* [**随时找到数据流的中位数**](https://github.com/lianyingteng/algorithm_practice/blob/master/Code4_MedianHolder.py) `P462`
* [切金条问题：**最小分割代价**](https://github.com/lianyingteng/algorithm_practice/blob/master/Code4_LessMoney.py)
* [**如何使得项目获得收益最大化**](https://github.com/lianyingteng/algorithm_practice/blob/master/Code4_IPO.py) `设计python的类的继承`
