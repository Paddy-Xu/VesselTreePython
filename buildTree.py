import numpy as np
import matplotlib.pyplot as plt
import sys
from connect_matrix import ConnectMatrix
from utils import *
print(sys.getrecursionlimit())


def RecursivelyBuildVessel(D_c, D_stop, G_vlvd, G_ddp):
    # G_vlvd = gauess_distribute(u = D_c,sig = 2)
    # G_ddp = gauess_distribute(u = D_c,sig = 2)

    # D_dv1 = D_c - G_ddp(D_c)
    D_dv1 = np.random.normal(loc=D_c, scale=2, size=1).item()
    while D_dv1 > D_c:
        D_dv1 = np.random.normal(loc=D_c, scale=2, size=1).item()

    D_dv2 = murray_law(D_c, D_dv1)
    L = G_vlvd(D_c)
    kwargs = {'D_stop': D_stop, 'G_vlvd': G_vlvd, 'G_ddp': G_ddp}
    if D_dv1 < D_stop and D_dv2 < D_stop:
        terminal_node = TreeNode(diameter=D_c, length=L)
        return terminal_node
    else:
        if D_dv1 > D_stop:
            left_branch = RecursivelyBuildVessel(D_dv1, **kwargs)
        else:
            left_branch = None
        if D_dv2 > D_stop:
            right_branch = RecursivelyBuildVessel(D_dv2, **kwargs)
        else:
            right_branch = None

    non_terminal = TreeNode(D_c, L, left_branch, right_branch)

    return non_terminal


class TreeNode:
    def __init__(self, diameter, length, left_branch=None, right_branch=None, **kwargs):
        self.left = left_branch
        self.right = right_branch
        self.diameter = diameter
        self.length = length
        # self.diameter_init = diameter_init
        # self.diameter_stop = diameter_stop
        # self.parent = parent
        self.order = 0
    def __str__(self):
        return "Node[Data = %s]" % (self.length,)

    def build(self):
        if self.diameter < self.diameter_threshold:
            return
        else:
            # TODO
            self.left = TreeNode(1)
            self.left.build()

            self.right = TreeNode(1)
            self.right.build()
        pass

    def set_order(self, order):
        self.order =  order

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        depth = 1 + max(left_depth, right_depth)
        self.set_order(depth) # this is only to increase efficiency when call depth on subtrees
        return depth

    def strahler_order(self):
        pass

    def parent(self):
        return self.parent


class DFS:
    def __init__(self):
        self.stack = []

    def dfs(self, treeNode):
        if treeNode is None:
            return
        self.dfs(treeNode.left)
        self.stack.append(treeNode)
        self.dfs(treeNode.right)


if __name__ == '__main__':
    print(murray_law(3, 2))
    gauess_23 = gauess_distribute(2, 3)
    exponential_2 = exponential_distribute(2)
    x = np.linspace(0, 10, 1000)
    fig, axes = plt.subplots(2)
    axes[0].plot(x, gauess_23(x))
    axes[1].plot(x, exponential_2(x))
    fig.show()

    root = RecursivelyBuildVessel(20, 2, gauess_23, gauess_23)
    print(root.diameter)
    print(root.depth())
    dfs_obj = DFS()
    dfs_obj.dfs(root)
    dfs_stack = dfs_obj.stack
    print([i.diameter for i in dfs_stack])
    cM_obj = ConnectMatrix(root)
    cM_obj.build()
    cM = np.array(cM_obj.matrix)
    print(cM)

    print(root.order)
    print(root.left.order)