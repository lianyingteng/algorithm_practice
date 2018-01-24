# 数据结构与算法 之 python实现
---
## 基础篇
### 1. 基本排序算法
* [冒泡排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code1_BubbleSort.py "Code1_BubbleSort.py")
* [选择排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code1_SelectionSort.py "Code1_SelectionSort.py")
* [插入排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code1_InsertionSort.py "Code1_InsertionSort.py")
* [随机快排](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code1_QuickSort.py "Code1_QuickSort.py")
* [归并排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code1_MergeSort.py "Code1_MergeSort.py")
* [堆排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code1_HeapSort.py "Code1_HeapSort.py")
* [桶排序](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code1_BucketSort.py "Code1_BucketSort.py")

#### 应用
* [最大间隔问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code11_MaxGap.py)  求无序数组排序之后 相邻两数的最大差值？`【桶排序思想的应用】 `
* [小和问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code11_MinSum.py)  给定一个数组，计算所有小和`【归并排序思想的应用】` 
* [荷兰国旗问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code11_NetherlandsFlag.py)  小于的放在左边、等于的放在中间、大于的放在右边`【快排划分的应用】`
* [查找无序数组前k个最小的数](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code11_heapSort.py)  该程序基于堆排序思想，建立大小为k的大根堆。`注： 该问题的最优解是下节中的BFPRT算法` 

### 2. KMP、Manacher、BFPRT
* [KMP算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code2_KMP.py) `解决字符串匹配问题`
* [Manacher算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code2_Manacher.py) `解决最长回文子串问题`
* [BFPRT算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code2_BFPRT.py) `查找无序数组中第k小的数`
#### 应用
* [最短扩增序列（包含两个输入序列）](https://github.com/lianyingteng/algorithm_practice/blob/master/Part0_Sort/Code21_KMP_ShortestHaveTwice.py)  `【基于KMP的next数组构建】`

### 3. 数据结构

**数组结构** <br>

* [使用数组实现栈结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_Array_To_Stack.py)
* [使用数组实现队列结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_Array_To_Queue.py)
* [实现可以输出栈中最小值的栈结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_GetMinStack.py)
* [两个栈实现队列结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_Stack_To_Queue.py)
* [两个队列实现栈结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_Queue_To_Stack.py)
* [猫狗队列](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_CatDogQueue.py) 
* [设计RandomPool结构](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_RandomPool.py) 
* [转圈打印矩阵](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_spiralOrderPrintMatrix.py) 
* [Z字形打印矩阵](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_spiralOrderPrintMatrix.py)
* [行列排好序的矩阵中找数](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code3_FindNumInSortedMatrix.py)
* [岛屿问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code4_IsLands.py)
* [找到无序数组局部最下位置](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code4_findLessValueIndex.py)  `二分也可用于数组无序的情况`
* [找到有序数组中第一个大于或等于k的数](https://github.com/lianyingteng/algorithm_practice/blob/master/Part1_Array/Code4_BinarySearch.py) `二分`



**链表结构**<br> 

* [打印两个有序链表的公共部分](https://github.com/lianyingteng/algorithm_practice/blob/master/Part2_LinkedList/Code3_PrintCommonPart.py)  `注： Node类中， value和next依附于实例`
* [链表是回文结构？](https://github.com/lianyingteng/algorithm_practice/blob/master/Part2_LinkedList/Code3_LinkedListIsPalindrome.py)
* [链表的Partition过程](https://github.com/lianyingteng/algorithm_practice/blob/master/Part2_LinkedList/Code3_SmallerEqualBigger.py) 
* [复制含有随机指针节点的链表](https://github.com/lianyingteng/algorithm_practice/blob/master/Part2_LinkedList/Code3_CopyListWithRandom.py)
* [寻找两个单链表第一个相交的结点](https://github.com/lianyingteng/algorithm_practice/blob/master/Part2_LinkedList/Code3_FindFirstIntersectNode.py)
* [反转单(双)向链表](https://github.com/lianyingteng/algorithm_practice/blob/master/Part2_LinkedList/Code3_ReverseList.py)



**树结构** <br>

* [折纸问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part3_Tree/Code4_PaperFolding.py)
* [**二叉树的先序、中序、后序遍历**](https://github.com/lianyingteng/algorithm_practice/blob/master/Part3_Tree/Code4_PreInPosRecur.py) `重点是非递归实现`
* [较为直观打印二叉树](https://github.com/lianyingteng/algorithm_practice/blob/master/Part3_Tree/Code4_PrintTree.py)
* [在二叉树中找到一个节点的后继节点](https://github.com/lianyingteng/algorithm_practice/blob/master/Part3_Tree/Code4_GetNextNode.py)
* [**前缀树**](https://github.com/lianyingteng/algorithm_practice/blob/master/Part3_Tree/Code5_TrieTree.py)



**堆结构** <br>

* [**随时找到数据流的中位数**](https://github.com/lianyingteng/algorithm_practice/blob/master/Part4_HeapStructure/Code4_MedianHolder.py) `P462`
* [切金条问题：**最小分割代价**](https://github.com/lianyingteng/algorithm_practice/blob/master/Part4_HeapStructure/Code4_LessMoney.py)
* [**如何使得项目获得收益最大化**](https://github.com/lianyingteng/algorithm_practice/blob/master/Part4_HeapStructure/Code4_IPO.py) `涉及python的类的继承`



**图结构** <br>

* [图的定义](https://github.com/lianyingteng/algorithm_practice/blob/master/Part5_Graph/Code5_DefineGraph.py)
* [图的宽度优先遍历](https://github.com/lianyingteng/algorithm_practice/blob/master/Part5_Graph/Code5_BFS.py)
* [图的深度优先遍历](https://github.com/lianyingteng/algorithm_practice/blob/master/Part5_Graph/Code5_DFS.py)
* [拓扑排序算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Part5_Graph/Code5_TopologySort.py)
* [最小生成树 - Kruskal算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Part5_Graph/Code5_Kruskal.py) `加边法`
* [最小生成树 - Prim算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Part5_Graph/Code5_Prim.py) `加点法`
* [求单源最短路径 - Dijkstra算法](https://github.com/lianyingteng/algorithm_practice/blob/master/Part5_Graph/Code5_Dijkstra.py)


**其他重要知识** <br>

* [**并查集结构**](https://github.com/lianyingteng/algorithm_practice/blob/master/Code4_UnionFindSet.py)


### 4. 算法基础

**递归** <br>

`函数的递归过程是函数自己调用自己的过程。 基本思想：把一个规模大的问题，转化成若干个规模小的子问题，并且大问题和其子问题的解决策略是一致的（同一种方法）。 递归函数必须有明确的结束条件！`

* [求阶乘](https://github.com/lianyingteng/algorithm_practice/blob/master/Part6_Recursion_DP/Code7_r_Factorial.py)
* [汉诺塔问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part6_Recursion_DP/Code7_r_Hanio.py)
* [**打印一个字符串所有子序列**](https://github.com/lianyingteng/algorithm_practice/blob/master/Part6_Recursion_DP/Code7_r_PrintAllSubSequence.py)
* [**全排列**](https://github.com/lianyingteng/algorithm_practice/blob/master/Part6_Recursion_DP/Code7_r_PrintAllPermutation.py)
* [斐波那契系列问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part6_Recursion_DP/Code7_Fibonacci.py)


**动态规划** <br>

`动态规划是一种分阶段求解决策问题的数学思想。 三个重要的概念： 最优子结构、 边界、 状态转移公式。 动态规划利用自底向上的递推方式，实现时间和空间上的额最优化。`

* [斐波那契系列问题](https://github.com/lianyingteng/algorithm_practice/blob/master/Part6_Recursion_DP/Code7_Fibonacci.py)