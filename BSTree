class BSTree():
     #-------------二叉搜索树的子节点--------
    class _BSTNode():                     # 初始化
         __slots__ = "data","lchild","rchild","parent"
         def __init__(self,d):
             self.data = d
             self.lchild = None
             self.rchild = None
             self.parent = None
     #-------------end----------------

    def __init__(self):
        self.root = None

    def search(self, e):  # 查找函数
        node = self.root  # 将node设为根节点
        while node != None and e != node.data:  # 当node即根节点不为空且查询节点不等于node即根节点时
            if e < node.data:  # 查询节点小于node即根节点时
                node = node.lchild  # 将node的左节点赋值给node
            else:                   # 否则，将node的右节点赋值给node
                node = node.rchild
        if node != None and e == node.data:  # 当 node的值等于查询节点时
            print("Found!!!")
            print("node is",e)
            return node  # 返回node
        else:  # 否则，调用插入函数将该节点插入对应位置
            self.insert(e)
            print("未找到该节点,已添加！")

    def insert(self,e):                  # 插入函数
        newnode = self._BSTNode(e)
        parent = None                    # 父节点置为空
        x = self.root                    # 将x设为根节点
        while x:
            parent = x                   # 将x赋给父节点
            if newnode.data < x.data:    # 比较，若插入节点的值小于x的值
                x = x.lchild             # 将x的左节点赋值给x
            else:
                x = x.rchild             # 否则，将x的右节点赋值给x
        newnode.parent = parent          # 插入节点的父节点为父节点即为x
        if parent == None:               # 若父节点为空，插入节点即为根节点
            self.root = newnode
        elif newnode.data < parent.data: # 若插入节点的值小于父节点的值，将插入节点赋值给父节点的左节点
            parent.lchild = newnode
        else:                            # 否则，将插入节点赋值给父节点的右节点
            parent.rchild = newnode

    def preOrderTraverse(self, node):         #先根遍历
        if node == None:
            return
        print(node.data,end=" ")
        self.preOrderTraverse(node.lchild)
        self.preOrderTraverse(node.rchild)

    def inOrderTraverse(self, node):           #中根遍历
        if node == None:
            return
        self.inOrderTraverse(node.lchild)
        print(node.data,end=" ")
        self.inOrderTraverse(node.rchild)

    def postOrderTraverse(self, node):          #后根遍历
        if node == None:
            return
        self.postOrderTraverse(node.lchild)
        self.postOrderTraverse(node.rchild)
        print(node.data,end=" ")


    def depth(self, node):
        # 二叉树为空树，层数就是0
        if node is None:
            return 0
        # 左子树的深度
        dl = self.depth(node.lchild)
        # 右子树的深度
        dr = self.depth(node.rchild)
        return max(dl, dr) + 1

    def minium(self):                #查找最小值
        x= self.root                 #将x设为根节点
        while x.lchild != None:
            x = x.lchild
        return x.data

    def maxnum(self):                #查找最大值
        x = self.root                #将x设为根节点
        while x.rchild != None:
            x = x.rchild
        return x.data

    def print_tree(self, root):
        '''
         打印一棵二叉树，二叉树节点值为0~9 10个整数或者26个大小写英文字母
         使用/\模拟左右分支,如下所示
                 e
              /     \
             c       g
            / \     / \
           b   d   f   h
          /
         a
         但是在打印满二叉树时，最多打印三层，对于深度为4的二叉树，存在节点冲突，无法打印
        '''
        if root is None:
            return
         # 基本思想：
         # 查询二叉树高度，预留足够的打印区域
        current = self.depth(root)
         # 计算深度为depth的满二叉树需要的打印区域：叶子节点需要的打印区域，恰好为奇数
         # 同一个节点左右孩子间隔 3 个空格
         # 相邻节点至少间隔一个空格，
        max_word = 3 * (2 ** (current - 1)) - 1
        node_space = int(max_word / 2)  # 每一个节点前面的空格数
         # queue1和queue2用来存放节点以及节点打印时的位置
         # queue1：当前层
         # queue2：下一层
        queue1 = [[self.root, node_space + 1]]
        queue2 = []
        while queue1:
             # 使用i_position列表记录左右斜杠的位置
            i_position = []
             # 确定左右斜杠的位置
             # "/"比当前节点的位置少1
             # "\"比当前节点的位置多1
             #passwd is 47 2905
            for i in range(len(queue1)):
                node = queue1[i][0]  # 节点打印位置
                i_space = queue1[i][1] - 1  # 左右斜线打印位置
                 # 对于根节点，左右各空出两个空格
                if node.data == self.root.data:
                    i_space -= 2
                 # 存储左斜线和左孩子
                if node.lchild is not None:
                    i_position.append([i_space, '/'])
                    queue2.append([node.lchild, i_space - 1])
                i_space += 2
                if node.data == self.root.data:
                    i_space += 4
                 # 存储右斜线和右孩子
                if node.rchild is not None:
                    i_position.append([i_space, '\\'])
                    queue2.append([node.rchild, i_space + 1])
             # 打印节点和左右斜杠
             # 打印节点
            if len(queue1) > 0:
                 # 找到打印位置最远的节点的位置
                last_node = queue1[len(queue1) - 1][1]
                 # 当前打印节点的数目
                index = 0
                for i in range(last_node + 1):
                     # 打印节点
                    if index < len(queue1) and i == queue1[index][1]:
                        print(queue1[index][0].data, end='')
                        index += 1
                    else:
                         # 打印空格
                        print(' ', end='')
            print()
             # 打印左右斜杠
            index = 0
            if len(i_position) > 0:
                for i in range(i_position[len(i_position) - 1][0] + 1):
                    if i == i_position[index][0]:
                        print(i_position[index][1], end='')
                        index += 1
                    else:
                        print(' ', end='')
            print()
             # 更新queue1和queue2
            queue1 = []
            while queue2:
                queue1.append(queue2.pop(0))
            node_space -= 2

if __name__ == '__main__':
    Tree = BSTree()
    element = [2,5,3,1,6,32,61,34]
    for i in element:
        Tree.insert(i)

    Tree.print_tree(Tree.root)

    print("\n先根遍历：")
    Tree.preOrderTraverse(Tree.root)
    print("\n中根遍历：")
    Tree.inOrderTraverse(Tree.root)
    print("\n后根遍历：")
    Tree.postOrderTraverse(Tree.root)

    print("\n最大值：",Tree.maxnum())
    print("最小值：", Tree.minium())
    print("深度:", Tree.depth(Tree.root))

    Tree.search(32)
    Tree.search(24)

