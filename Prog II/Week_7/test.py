def test(s):
    l = [0,0]
    if s[0] == 'N':
        l = [0,1]
    elif s[0] == 'E':
        l = [1, 0]
    elif s[0] == 'W':
        l = [-1,0]
    elif s[0] == 'S':
        l = [0, -1]
    d = test(s[1:])
    return [l[0] + d[0],l[1] + d[1]]