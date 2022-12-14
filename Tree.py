class BinaryTree():
    #-----二叉树节点------
    class _BTNode():
        __slots__ = "data","lchild","rchild"
        def __init__(self,d):
            self.data = d
            self.lchild = None
            self.rchild = None
    #-----end--------------

    def __init__(self):
        self.root = None

    def add(self,e):                 #添加节点
        node = self._BTNode(e)
        #若节点为空
        if self.root == None:
            self.root = node
            print("根节点：",e)
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)        #弹出
            if cur.lchild == None:
                cur.lchild = node
                print("左节点：",c)
                return
            else:
                queue.append(cur.lchild)
            if cur.rchild == None:
                cur.rchild = node
                print("右节点：",c)
                return
            else:
                queue.append(cur.rchild)

    def depth(self,node):
        #二叉树为空树，层数就是0
        if node is None:
            return 0
        #左子树的深度
        dl = self.depth(node.lchild)
        #右子树的深度
        dr = self.depth(node.rchild)
        return max(dl,dr)+1

if __name__ == "__main__":
    bt = BinaryTree()
    name = "Home Password is not here!"
    for c in name:
        bt.add(c)
    print("深度:",bt.depth(bt.root))
