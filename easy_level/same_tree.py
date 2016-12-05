# coding=utf-8
'''
判断两个二叉树是否相等

当两个二叉树结构一致并且节点值一样的话，两者相等

我觉得输出两者的list值，比对两者list值是否相等
'''
import binary_tree_utils


def same_tree(root1, root2):
    # root1 == roo2 == None
    if root1 == root2:
        return True
    if root1.value != root2.value:
        return False
    is_same = True
    nodes1 = [root1.left, root1.right]
    nodes2 = [root2.left, root2.right]
    while nodes1:
        node1 = nodes1.pop(0)
        node2 = nodes2.pop(0)
        # node1 == node2 == None
        if node1 == node2:
            continue
        # 两者有一个是None，另外一个不是None，或者两者的value不相等
        if (node1 is None or node2 is None) or node1.value != node2.value:
            is_same = False
            break
        nodes1.extend([node1.left, node1.right])
        nodes2.extend([node2.left, node2.right])
    return is_same


def main():
    r1 = [1, 2, 3, 4, None]
    r2 = [1, 2, 3, 4, None]
    r1 = binary_tree_utils.generate_binary(r1)
    r2 = binary_tree_utils.generate_binary(r2)
    binary_tree_utils.show_binary_tree(r1)
    binary_tree_utils.show_binary_tree(r2)
    print same_tree(r1, r2)
    print '----------------------'
    r1 = [1, 2, 3, 4, 5, 6, None]
    r2 = [1, 2, 3, 4, 5, 6, 7]
    r1 = binary_tree_utils.generate_binary(r1)
    r2 = binary_tree_utils.generate_binary(r2)
    binary_tree_utils.show_binary_tree(r1)
    binary_tree_utils.show_binary_tree(r2)
    print same_tree(r1, r2)

if __name__ == '__main__':
    main()
