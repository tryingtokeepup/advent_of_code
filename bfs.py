from collections import deque


class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left  # these are just pointers to child left node
        self.right = right  # these are just pointers to child right node


def bfs(tree):
    # use a queue data struct

    # we need to check every val in tree/ iterate through entire tree
    # tree node is just a class
    """

                            1
                    3		4
            2				5

    TreeNode(1, TreeDone(3), TreeNode(4))
    we think in ONE NODE at a time!
            add all of root's children to the queue
            add to end, take from "front"
    what is deque

    """
    queue = deque([tree])  # 1

    while queue:  # while we have stuff in queue
        current_node = queue.popleft()  # we will have 1

        if current_node.left
# from collections import deque


# class Solution:
#     def size(self, tree):
#         if not tree:
#             return 0
#         count = 0
#         queue = deque([tree])

#         while queue:
#             curr = queue.popleft()
#             count += 1

#             if curr.left: queue.append(curr.left)
#             if curr.right: queue.append(curr.right)

#         return count
