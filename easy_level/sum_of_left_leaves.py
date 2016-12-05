# coding=utf-8
'''
左节点的和
判断最后一个节点是左节点

'''
import binary_tree_utils


def sum_left(root):
    '''
    输入是root对象
    '''
    if not root:
        return 0
    sums = []
    is_left = True
    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        if not node.left and not node.right:
            # 当前是最后一个节点
            if is_left:
                # 当前node是左节点，并则append(node.value)
                sums.append(node.value)
                is_left = False
            continue
        if node.right:
            # 下一个节点是右节点
            is_left = False
            nodes.insert(0, node.right)
        if node.left:
            # 下一个节点是左节点
            is_left = True
            nodes.insert(0, node.left)
    return sum(sums)


def main():
    i = [3, 9, 20, None, None, 15, 7]
    root = binary_tree_utils.generate_binary(i)
    binary_tree_utils.show_binary_tree(root)
    s = sum_left(root)
    print s
    print '-----------------------------'
    root = binary_tree_utils.generate_binary(by_depth=3)
    binary_tree_utils.show_binary_tree(root)
    s = sum_left(root)
    print s
    print '########### test ##############'
    for i in [[1, 2, 3, None, None, None, None], [1, 2, None, None, None, None, None], [1, None, 3, None, None, None, None],

              [1, 2, None, None, None, None, None], [1, 2, None, 4, None, None, None], [1, 2, None, 4, 5, None, None],

              [1, None, 3, None, None, None, None], [1, None, 3, None, None, None, 7], [1, None, 3, None, None, 6, None], [1, None, 3, None, None, 6, 7],

              [1, 2, 3, None, None, None, None], [1, 2, 3, None, None, None, 7], [1, 2, 3, None, None, 6, None], [1, 2, 3, None, None, 6, 7],

              [1, 2, 3, None, 5, None, None], [1, 2, 3, None, 5, None, 7], [1, 2, 3, None, 5, 6, None], [1, 2, 3, None, 5, 6, 7],

              [1, 2, 3, 4, None, None, None], [1, 2, 3, 4, None, None, 7], [1, 2, 3, 4, None, 6, None], [1, 2, 3, 4, None, 6, 7],

              [1, 2, 3, 4, 5, None, None], [1, 2, 3, 4, 5, None, 7], [1, 2, 3, 4, 5, 6, None], [1, 2, 3, 4, 5, 6, 7],
              ]:
        sums = 0
        if 2 in i and 4 not in i:
            sums = 2
            if 6 in i:
                sum += 2
        if 4 in i:
            sums = 4
            if 6 in i:
                sum += 2
        if 6 in i:
            sums = 6
        root = binary_tree_utils.generate_binary(i)
        s = sum_left(root)
        if s != sums:
            binary_tree_utils.show_binary_tree(root)
            print 'wrong: %s %s %s' % (i, s, sums)
            print '#############################'


if __name__ == '__main__':
    main()
