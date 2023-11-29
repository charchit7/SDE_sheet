# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right


class Preorder:
    def __init__(self, root : Optional[TreeNode]):

        res = []
        self.dfs(root, res)

        return res
    

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)


# merge sort algo
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Merge Sort:", arr)
