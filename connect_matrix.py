class ConnectMatrix():
    def __init__(self,root):
        self.ABST = root
        self.matrix = []
        self.index = 0

    def build(self):
        self.RecursiveBuildMatrix(self.index, self.ABST, parent_index=-1)
        return self.matrix

    def RecursiveBuildMatrix(self, index, cur, parent_index):
        if cur.left:
            self.index += 1
            left_index = self.index
            self.RecursiveBuildMatrix(left_index, cur.left, index)
        else:
            left_index = -1
        if cur.right:
            self.index += 1
            right_index = self.index
            self.RecursiveBuildMatrix(right_index, cur.right, index)
        else:
            right_index = -1
        
        self.matrix.append([index, cur.diameter, cur.length, left_index, right_index, parent_index])