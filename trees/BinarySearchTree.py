from collections import deque

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # Add left
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def print_tree(self):
        if self is None:
            return
        print(self.data, end="-->")
        if self.left:
            print("L:", self.left.data, end=", ")
        if self.right:
            print('R:', self.right.data)
        print()

        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, data):
        if data == self.data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()

        if self.right:
            sum += self.right.calculate_sum()

        sum += self.data

        return sum

    def get_min(self):
        if self.left:
            return self.left.get_min()
        else:
            return self.data

    def invert_binary_tree(self):
        if self is None:
            return

        tmp = self.left
        self.left = self.right
        self.right = tmp

        if self.left:
            self.left.invert_binary_tree()
        if self.right:
            self.right.invert_binary_tree()

    def max_depth_recursive(self, node):
        if node is None:
            return 0

        return 1 + max(node.max_depth_recursive(node.left), node.max_depth_recursive(node.right))

    def max_depth_bfs(self, node) -> int:
        if node is None:
            return 0

        level = 0
        queue = deque([node])
        while queue:

            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level


    def lowestCommonAncestor(self, root: 'TreeNode', p: int, q: int) -> 'TreeNode':
        if not root or root.data == p or root.data == q:
            return root

        i = root.lowestCommonAncestor(root.left, p, q)
        j = root.lowestCommonAncestor(root.right, p, q)

        if (i and j) or root.data in [p, q]:
            return root
        else:
            return i or j

        # if not root or root == p or root == q:
        #     return root
        #
        # x = self.lowestCommonAncestor(root.left, p, q)
        # y = self.lowestCommonAncestor(root.right, p, q)
        #
        # if (x and y) or root in [p, q]:
        #     return root
        # else:
        #     return x or y

        """
        Function lowestCommonAncestor(root, p, q)
        """

    def findingMissing(arr, size):
        # Extreme cases
        # if (arr[0] != 1):
        #     return 1
        # if (arr[size - 1] != (size + 1)):
        #     return size + 1

        a = 0
        b = size - 1
        mid = 0
        while b > a + 1:
            mid = (a + b) // 2
            if (arr[a] - a) != (arr[mid] - mid):
                b = mid
            elif (arr[b] - b) != (arr[mid] - mid):
                a = mid
        return arr[a] + 1

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 8]
    n = len(a)

    root = BinarySearchTree(17)
    print("Missing number:", root.findingMissing(a, n))
    # elements = [17, 4, 1, 20, 9, 23, 18, 34]
    # root = build_tree(elements)
    # root.print_tree()
    # print("In Order Traversal: ")
    # print(root.in_order_traversal())
    # print("Pre Order Traversal: ")
    # print(root.pre_order_traversal())
    # print("Post Order Traversal: ")
    # print(root.post_order_traversal())
    # print(root.search(10))
    # print(root.calculate_sum())
    # print(root.get_min())
    # print(root.invert_binary_tree())
    # root.print_tree()
    # print(root.max_depth_recursive(root))
    # print(root.max_depth_bfs(root))
    # print(root.lowestCommonAncestor(root, ))
    # root = BinarySearchTree(17)
    # root.left = BinarySearchTree(4)
    # root.right = BinarySearchTree(20)
    # root.left.left = BinarySearchTree(1)
    # root.left.right = BinarySearchTree(9)
    # root.right.left = BinarySearchTree(18)
    # root.right.right = BinarySearchTree(23)
    # root.right.right.right = BinarySearchTree(34)
    # print(root.lowestCommonAncestor(root, root.right.left.data, root.left.right.data).data)