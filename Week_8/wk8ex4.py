#wk8ex4
#conway probleem

def conway(n):
    start = '1'
    placehold = ''
    count = 0
    if start == '' or n < 0:
        return 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        if len(start) > 1:
            if start[0] == start[1]:
                start = start.replace(start[0], '', 1)
            else:
                placehold = convert(start[0], count)
                start = start.replace(start[0], '', 1)
                count = 0
        else:
            placehold = convert(start[0], count)
        n -= 1
    return start
        

def convert(num, count):
    return str(count) + str(num)
        




# split alle opeenvolgende nummers van elkaar:
# 111221 wordt 111, 22, 1
    

