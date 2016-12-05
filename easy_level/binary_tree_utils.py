# coding=utf-8


class TreeNode(object):
    def __init__(self, value, left=None, right=None, parent_v=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent_v = parent_v


def generate_binary(vs=None, by_depth=None):
    if by_depth:
        assert isinstance(by_depth, int)
        vvs = range(1, 2**(by_depth + 1))
    else:
        vvs = []
        for i in vs:
            vvs.append(i)
    rv = vvs.pop(0)
    root = TreeNode(rv)
    depth = 1
    nodes = [root]
    while vvs:
        ns = []
        while nodes:
            n = nodes.pop(0)
            if not n:
                continue
            if not vvs:
                break
            l_v = vvs.pop(0)
            r_v = vvs.pop(0)
            left, right = None, None
            if l_v:
                left = TreeNode(l_v, parent_v=n.value)
            if r_v:
                right = TreeNode(r_v, parent_v=n.value)
            n.left = left
            n.right = right
            ns.extend([left, right])
        depth += 1
        nodes = ns
    root.depth = depth
    return root


def show_binary_tree(root):
    d = root.depth
    nodes = [root]
    while d >= 0:
        ns = []
        msg = ''
        for n in nodes:
            if not n:
                continue
            msg += '[{p}, {v}, {l}, {r}]'.format(**{'p': n.parent_v, 'v': n.value, 'l': n.left.value if n.left else None,
                                                    'r': n.right.value if n.right else None})
            ns.extend([n.left, n.right])
        print msg
        nodes = ns
        d -= 1


def list_binary_tree(root):
    pass
