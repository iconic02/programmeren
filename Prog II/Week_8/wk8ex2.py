def count_evens(nums):
    """count_evens berekent het aantal even getallen in een lijst

    Args:
        nums (list): lijst met getallen

    Returns:
        int: aantal even getallen
    """
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count


def big_diff(nums):
    """big_diff geeft het verschil tussen max en min in lijst nums

    Args:
        nums (list): lijst met getallen

    Returns:
        int: het verschil tussen max en min
    """
    result = abs(min(nums) - max(nums))
    return result


def centered_average(nums):
    """centered_average het gemiddelde van een lijst zonder min en max getal

    Args:
        nums (list): lijst met getallen

    Returns:
        int: het gemiddelde
    """
    for i in nums:
        if i == min(nums):
            nums.remove(i)
            break
    for i in nums:
        if i == max(nums):
            nums.remove(i)
            break
    result = sum(nums) // len(nums)
    return result


def double_char(str):
    """double_char geeft een string terug met alle characters dubbel

    Args:
        str (string): string met woorden

    Returns:
        string: string met alle letters dubbel
    """
    result = ''
    for i in str:
        result += i*2
    return result


def count_hi(str):
    """count_hi telt het aantal keer dat 'hi' in een zin voorkomt

    Args:
        str (string): string met woorden

    Returns:
        int: aantal keer hi
    """
    count = 0
    for i in range(len(str)-1):
        if str[i] == 'h' and str[i+1] == 'i':
            count += 1
    return count


def cat_dog(str):
    """cat_dog geeft boolean als aantal keer 'dog' en 'cat' gelijk zijn

    Args:
        str (string): tja, gewoon nog steeds een string met woorden

    Returns:
        boolean: True of False
    """
    dog_count = 0
    cat_count = 0
    if str == '':
        return True
    else:
        for i in range(len(str)):
            if 'cat' in str:
                str = str.replace('cat', '   ', 1)
                cat_count += 1
                print(str)
            if 'dog' in str:
                str = str.replace('dog', '   ', 1)
                dog_count += 1
                print(str)
        if dog_count == cat_count:
            return True
        else:
            return False
