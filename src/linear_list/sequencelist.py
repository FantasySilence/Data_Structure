# =========================================================== #
# @Author: Fantasy_Silence                                    #
# @Time: 2024-11-09                                           #
# @IDE: Visual Studio Code & PyCharm                          #
# @Python: 3.9.7                                              #
# =========================================================== #
# @Description: 《顺序表》                                     #             
# 线性表中所有元素按照其逻辑顺序依次存储到存储器中一块连续的空间   #
# =========================================================== #
class SequeceList:

    """
    顺序表
    """

    # ------ 构造顺序表类 ------ #
    def __init__(self) -> None:
        
        # ------ 初始容量 ------ #
        self.init_capacity = 10
        self.capacity = self.init_capacity

        # ------ 顺序表的存储空间 ------ #
        self.data = [None] * self.capacity
        self.size = 0
    
    def resize(self, new_capacity: int) -> None:

        """
        改变顺序表的容量
        new_capacity(int): 新的容量  
        """

        # ------ 保证输入准确性 ------ #
        if type(new_capacity) != int or new_capacity < 0:
            raise ValueError("new_capacity must be a positive integer")
        
        # ------ 重新分配存储空间 ------ #
        old_data = self.data
        self.data = [None] * new_capacity
        self.capacity = new_capacity

        # ------ 将原先的元素存入扩容后的顺序表 ------ #
        for i in range(self.size):
            self.data[i] = old_data[i]
    
    def create_list(self, data: list) -> None:

        """
        建立顺序表
        data(list): 输入的元素
        """

        # ------ 保证输入准确性 ------ #
        if type(data) != list:
            raise ValueError("data must be a list")

        # ------ 将输入的元素存入顺序表 ------ #
        for i in range(0, len(data)):
            # 元素装满时进行扩容
            if self.size == self.capacity:
                self.resize(self.capacity * 2)
            # 添加元素
            self.data[self.size] = data[i]
            self.size += 1
    
    def append(self, element) -> None:

        """
        在末尾添加一个元素
        """

        # ------ 元素装满时进行扩容 ------ #
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        # ------ 添加元素 ------ #
        self.data[self.size] = element
        self.size += 1
    
    def getsize(self) -> int:

        """
        求顺序表的长度
        """

        return self.size
    
    ## ------ 获取索引为i的元素 ------ ##
    def __getitem__(self, i: int):

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")
        if i >= self.size:
            raise IndexError("index out of range")

        return self.data[i]

    ## ------ 修改顺序表中索引为i的元素的值 ------ ##
    def __setitem__(self, i: int, element) -> None:

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")
        if i >= self.size:
            raise IndexError("index out of range")

        self.data[i] = element
    
    def getNo(self, e) -> int:

        """
        输出第一个值为e的元素的序号
        """

        # ------ 保证输入准确性 ------ #
        if e not in self.data:
            raise ValueError("element not in list")

        for i in range(self.size):
            if self.data[i] == e:
                return i
    
    def insert(self, i: int, e) -> None:

        """
        插入元素e作为第i个元素
        i(int): 插入元素的位置
        """

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")
        if i >= self.size:
            raise IndexError("index out of range")

        # ------ 元素装满时进行扩容 ------ #
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        # ------ 插入元素 ------ #
        for j in range(self.size, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = e
        self.size += 1
    
    def delete(self, i: int) -> None:

        """
        删除第i个元素
        """

        # ------ 保证输入准确性 ------ #
        if type(i) != int or i < 0:
            raise ValueError("index must be a positive integer")
        if i >= self.size:
            raise IndexError("index out of range")

        # ------ 删除元素 ------ #
        for j in range(i, self.size - 1):
            self.data[j] = self.data[j + 1]
        self.data[self.size - 1] = None
        self.size -= 1

        # ------ 缩容 ------ #
        # 当前容量大于初始容量并且实际长度仅为当前容量的1/4时
        if self.size <= self.capacity // 4 and self.capacity > self.init_capacity:
            self.resize(self.capacity // 2)

    ## ------ 输出顺序表 ------ ##    
    def display(self) -> None:
        
        print("[",  end="")
        if self.size == 0:
            print("]", end="")
            print()
        for i in range(self.size):
            if i == self.size - 1:
                print(self.data[i], end="")
                break       
            print(self.data[i], end=", ")
        print("]",  end="")
        print()
