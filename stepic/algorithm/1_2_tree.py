# n = input()
# seq = input()

# [0,  1, 2, 3, 4]
# [4, -1, 4, 1, 1] parents

#       1
#      / \
#     3   4
#        / \
#       0   2

# 0 1 2 3 4 5
#   3     0
#   4     2

#  0 1 2 3 4
# -1 0 4 0 3

#  0 1 2 3 4
#  1     4 2
#  3

n = int(5)

seq = '4 -1 4 1 1'
# seq = '-1 0 4 0 3'

parents = list(map(int, seq.split()))

tree = {}
root = 0

for i, p in enumerate(parents):
    if p != -1:
        if not p in tree:
            tree[p] = []
        tree[p].append(i)
    else:
        root = i

def print_tree(root):
    print(root)

    if root in tree:
        for c in tree[root]:
            print_tree(c)


def get_height(root):
    height = 1

    if root in tree:
        for c in tree[root]:
            height = max(height, 1 + get_height(c))

    return height

print(get_height(root))
