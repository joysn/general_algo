# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference


def sym2(s1, s2):

    d1 = dict()
    for e in s1:
        d1[e] = 1
    d2 = dict()
    for e in s2:
        d2[e] = 1

    op = set()
    for k in d1.keys():
        if k not in d2.keys():
            op.add(k)
    for k in d2.keys():
        if k not in d1.keys():
            op.add(k)

    return op

def sym(ip):
    if len(ip) < 2:
        return ip[1]
    ans = sym2(ip[0],ip[1])
    for idx in range(2,len(ip)):
        ans = sym2(ans,ip[idx])

    return ans

if __name__ == "__main__":

    inputs = [
        [[1, 2, 3], [5, 2, 1, 4]]
        ,[[1, 2, 3, 3], [5, 2, 1, 4]]
        ,[[1, 2, 3], [5, 2, 1, 4, 5]]
        ,[[1, 2, 5], [2, 3, 5], [3, 4, 5]]
        ,[[1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]]
        ,[[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]]
        ,[[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]]
    ]
    for ipargs in inputs:
        print(sym(ipargs))

# {3, 4, 5}
# {3, 4, 5}
# {3, 4, 5}
# {1, 4, 5}
# {1, 4, 5}
# {2, 3, 4, 6, 7}
# {1, 2, 4, 5, 6, 7, 8, 9}