# coding=utf-8


def max_depth(root):
    if not root:
        return 0
    depth = max_depth = 1
    is_right = False
    data = [root.left, root.right]
    while data:
        node = data.pop(0)
        # 试探往下走一步，深度加1
        depth += 1
        if not node:
            # 下一步走不通，深度减1，回退到当前深度，此时最大深度是max_depth和depth(也就是当前深度的最大值)
            depth -= 1
            max_depth = max(depth, max_depth)
            # 这步是右节点的回退，这时应该回退到父节点的深度
            if is_right:
                depth -= 1
            else:
                # 下一个节点是右节点
                is_right = True
            continue
        # 下一步走通了，ok, 因为append左节点和右节点，所以下一个节点是左节点
        is_right = False
        data.extend([node.left, node.right])
    return max_depth


def main():
    pass


if __name__ == '__main__':
    main()
