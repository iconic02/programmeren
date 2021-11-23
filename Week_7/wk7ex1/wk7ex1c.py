#
# wk7ex1c.py
#
# Naam:Timo
#
# Getallen bij a = 21 & c = 17:
NUMBERS = """
99
96
33
10
27
84
81
18
95
12
69
66
3
80
97
54
51
88
65
82
39
36
73
50
67
24
21
58
35
52
9
6
43
20
37
94
91
28
5
22
79
76
13
90
7
64
61
98
75
92
49
46
83
60
77
34
31
68
45
62
19
16
53
30
47
4
1
38
15
32
89
86
23
0
17
74
71
8
85
2
59
56
93
70
87
44
41
78
55
72
29
26
63
40
57
14
11
48
25
42
"""


def unique(L):
    """
    Een test om te kijken of elk cijfer niet nog een keer in de lijst voorkomt
    Als dit het geval is, wordt False gegeven, anders True
    """
    if L == []:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])


def test(s):
    """
    Een functie die van string NUMBERS een int list maakt en deze naar unique stuurt
    """
    s = s.strip()                 
    list_of_strings = s.split()   
    list_of_integers = [int(s) for s in list_of_strings]
    return unique(list_of_integers)


#door het py bestand te runnen, wordt de string NUMBERS automatisch getest
result = test(NUMBERS)
print("\nTest op uniekheid:  Het resultaat is", result)
