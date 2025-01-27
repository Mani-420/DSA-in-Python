def search(root, target):
    if not root:
        return False
    
    if target > root.value:
        return search(root.right, target)
    elif target < root.value:
        return search(root.left, target)
    else:
        return True