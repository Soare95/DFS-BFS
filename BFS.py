class Node:..

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.__dict__)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right == None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        current_node = self.root
        while True:
            if current_node == None:
                return None
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif current_node.value == value:
                return current_node

    def remove(self, value):
        if self.root == None:
            return None
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.value:
                # We have a match

                # Option 1: no right child
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        # if parent_node > current_node.value, make current left child a child of parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left

                        # if parent_node < current_node.value, make left child a right child of parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left

                # Option 2: right child which doesn't have a left child
                elif current_node.right.left == None:
                    current_node.right.left = current_node.left
                    if parent_node == None:
                        self.root = current_node.right
                    else:
                        current_node.right.left = current_node.left

                        # if parent_node > current_node, make right child of the left the parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right

                        # if parent_node < current_node, make right child a right child of the parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right

                # Option 3: right child that has a left child
                else:
                    # find the right child's left most child
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left != None:
                        left_most_parent = left_most
                        left_most = left_most.left

                    # parent's left subtree is now left most's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node == None:
                        self.root = left_most
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = left_most
                        elif current_node.value > parent_node.value:
                            parent_node.right = left_most
                return True

    def breadth_first_search(self):
        current_node = self.root
        answer_list = []  # we insert numbers in the order of BFS
        queue_list = []  # keep track of the layer we are at, so we can access the children
        queue_list.append(current_node)

        while len(queue_list) > 0:
            current_node = queue_list[0]
            del queue_list[0]
            answer_list.append(current_node.value)
            if current_node.left:
                queue_list.append(current_node.left)
            if current_node.right:
                queue_list.append(current_node.right)
        return answer_list

    def breadth_first_search_recursive(self, queue_list, answer_list):
        if len(queue_list) == 0:
            return answer_list
        current_node = queue_list[0]
        del queue_list[0]
        answer_list.append(current_node.value)
        if current_node.left:
            queue_list.append(current_node.left)
        if current_node.right:
            queue_list.append(current_node.right)
        return self.breadth_first_search_recursive(queue_list, answer_list)


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(6)
binary_search_tree.insert(20)
binary_search_tree.insert(170)
binary_search_tree.insert(15)
binary_search_tree.insert(1)
# binary_search_tree.remove(9)
print(binary_search_tree.breadth_first_search())
print(binary_search_tree.breadth_first_search_recursive([binary_search_tree.root], []))
# print(binary_search_tree.lookup(170))

print(binary_search_tree)
