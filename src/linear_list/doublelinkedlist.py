# ======================================================== #
# @Author: Fantasy_Silence                                 #
# @Time: 2024-11-09                                        #
# @IDE: Visual Studio Code & PyCharm                       #
# @Python: 3.9.7                                           #
# ======================================================== #
# @Description: 《双链表》                                  #
# 每个节点设置设置两个指针属性，分别指向前驱节点和后继节点      #
# ======================================================== #
class LinkNode:

    ## ------ 构造双链表的节点 ------ ##
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
        self.prior = None


class DoubleLinkedList:

    """
    双链表
    """

    ## ------ 构造双链表类 ------ ##
    def __init__(self) -> None:
        
        self.dhead = LinkNode()
        self.dhead.next = None
        self.dhead.prior = None
    
    def createListF(self, data: list) -> None:

        """
        头插法,越先插入越靠后
        data(list): 输入的元素
        """

        # ------ 保证输入准确性 ------ #
        if type(data) != list:
            raise ValueError("data must be a list")

        # ------ 将输入的元素存入双链表 ------ #
        for i in range(0, len(data)):
            node = LinkNode(data[i])
            node.next = self.dhead.next
            if self.dhead.next is not None:
                self.dhead.next.prior = node
            self.dhead.next = node
            node.prior = self.dhead
    
    def createListR(self, data: list) -> None:

        """
        尾插法，越先插入越靠前
        data(list): 输入的元素
        """

        # ------ 保证输入准确性 ------ #
        if type(data) != list:
            raise ValueError("data must be a list")

        # ------ 将输入的元素存入双链表 ------ #
        p = self.dhead
        for i in range(0, len(data)):
            node = LinkNode(data[i])
            p.next = node
            node.prior = p
            p = node
    
    def geti(self, i: int) -> LinkNode:

        """
        返回索引为i的节点
        i(int): 输入的索引
        """

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")

        # ------ 返回序号为i的节点 ------ #
        p = self.dhead.next
        j = 0
        while p is not None and j < i:
            p = p.next
            j += 1
        # 索引越界 
        if p is None:
            raise IndexError("index out of range")
        return p
    
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
        if p.next is not None:
            p.next.prior = node
        p.next = node
        node.prior = p
    
    def delete(self, i: int) -> None:

        """
        删除第i个元素
        """

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")
        p = self.geti(i)
        if p is None:
            raise IndexError("index out of range")
        
        # ------ 删除元素 ------ #
        p.prior.next = p.next
        if p.next is not None:
            p.next.prior = p.prior

    ## ------ 输出链表 ------ ##
    def display(self) -> None:

        linked_list_str = ""
        p = self.dhead.next
        while p is not None:
            linked_list_str += str(p.data) + " <-> "
            p = p.next
        print(linked_list_str[:-5])
