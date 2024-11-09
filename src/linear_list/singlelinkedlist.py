# ================================================ #
# @Author: Fantasy_Silence                         #
# @Time: 2024-11-09                                #
# @IDE: Visual Studio Code & PyCharm               #
# @Python: 3.9.7                                   #
# ================================================ #
# @Description: 《单链表》                          #
# 链表的每个节点值设置一个指向后继节点的指针属性       #
# ================================================ #
class LinkNode:

    ## ------ 构造单链表的节点 ------ ##
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None


class SingleLinkedList:

    """
    单链表
    """

    ## ------ 构造单链表类 ------ ##
    def __init__(self) -> None:
        
        # ------ 头节点 ------ #
        self.head = LinkNode()
        self.head.next = None
    
    def createListF(self, data: list) -> None:

        """
        头插法,越先插入越靠后
        data(list): 输入的元素
        """

        # ------ 保证输入准确性 ------ #
        if type(data) != list:
            raise ValueError("data must be a list")

        # ------ 将输入的元素存入单链表 ------ #
        for i in range(0, len(data)):
            node = LinkNode(data[i])
            node.next = self.head.next
            self.head.next = node
    
    def createListR(self, data: list) -> None:

        """
        尾插法，越先插入越靠前
        data(list): 输入的元素
        """

        # ------ 保证输入准确性 ------ #
        if type(data) != list:
            raise ValueError("data must be a list")

        # ------ 将输入的元素存入单链表 ------ #
        p = self.head
        for i in range(0, len(data)):
            node = LinkNode(data[i])
            p.next = node
            p = node
        p.next = None
    
    def geti(self, i: int) -> LinkNode:

        """
        返回索引为i的节点
        i(int): 输入的索引
        """

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")

        # ------ 返回序号为i的节点 ------ #
        p = self.head.next
        j = 0
        while p is not None and j < i:
            p = p.next
            j += 1
        # 索引越界 
        if p is None:
            raise IndexError("index out of range")
        return p
    
    def append(self, element) -> None:

        """
        在链表末尾添加一个元素
        """

        # ------ 将输入的元素存入单链表 ------ #
        p = self.head
        while p.next is not None:
            p = p.next
        node = LinkNode(element)
        p.next = node
    
    def getsize(self) -> int:

        """
        返回链表的长度
        """

        size = 0
        p = self.head.next
        while p is not None:
            size += 1
            p = p.next
        return size
    
    ## ------ 获取索引为i的元素 ------ ##
    def __getitem__(self, i: int) -> LinkNode:

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")

        # ------ 返回索引为i的元素 ------ #
        p = self.geti(i)
        return p.data
    
    ## ------ 修改顺序表中索引为i的元素的值 ------ ##
    def __setitem__(self, i: int, element) -> None:

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")

        # ------ 修改索引为i的元素的值 ------ #
        p = self.geti(i)
        p.data = element
    
    def getNo(self, e) -> int:

        """
        输出第一个值为e的元素的序号
        """

        p = self.head.next
        j = 0
        while p is not None and p.data != e:
            j += 1
            p = p.next
        if p is None:
            raise ValueError("element not in list")
        else:
            return j
    
    def insert(self, i: int, e) -> None:

        """
        插入元素e作为第i个元素
        i(int): 插入元素的位置
        """

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")
        p = self.geti(i - 1)
        if p is None:
            raise IndexError("index out of range")
        
        # ------ 插入元素 ------ #
        node = LinkNode(e)
        node.next = p.next
        p.next = node
    
    def delete(self, i: int) -> None:

        """
        删除第i个元素
        """

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")
        p = self.geti(i - 1)
        if p is None or p.next is None:
            raise IndexError("index out of range")
        
        # ------ 删除元素 ------ #
        p.next = p.next.next
    
    ## ------ 输出链表 ------ ##
    def display(self) -> None:

        # ------ 保证输入准确性 ------ #
        if self.head.next == None:
            raise ValueError("list is empty")

        # ------ 输出链表 ------ #
        linked_list_str = ""
        p = self.head.next
        while p is not None:
            linked_list_str += str(p.data) + " -> "
            p = p.next
        print(linked_list_str[:-4])
