# coding=utf-8
'''
翻转二叉树
'''
import binary_tree_utils


def invert_binary_tree(root):
    if not root:
        return root
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node:
            node.left, node.right = node.right, node.left
            nodes.extend([node.left, node.right])
    return root


def main():
    r = binary_tree_utils.generate_binary(by_depth=3)
    binary_tree_utils.show_binary_tree(r)
    print '----------------------'
    invert_binary_tree(r)
    binary_tree_utils.show_binary_tree(r)
    print '#####################################'
    input_v = [4, 2, 7, 1, 3, 6, 9]
    input_r = binary_tree_utils.generate_binary(input_v)
    binary_tree_utils.show_binary_tree(input_r)
    print '----------------------'
    invert_binary_tree(input_r)
    binary_tree_utils.show_binary_tree(input_r)

if __name__ == '__main__':
    main()
