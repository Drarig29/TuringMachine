from turing import Turing

## Somme de deux nombres unaires
#
# 2, 
# ['B', 'B', 1, 1, 1, 1, 1, 'B', 1, 1, 1, 1, 1, 1, 1, 1, 'B', 'B'], 
# {
#     "initial": 0,
#     0: {
#         1: (0, None, 'R'),
#         'B': (1, 1, 'N')
#     },
#     1: {
#         1: (1, None, 'L'),
#         'B': (2, None, 'R'),
#     },
#     2: {
#         1: (3, 'B', 'R')
#     },
#     3: {
#         1: (4, 'B', 'R')
#     },
#     4: None # état final
# }

turing = Turing(
    10,
    list("BBB1011#110BBBB"), # conversion de chaîne à tableau de caractères (nouvelle façon de faire)
    {
        "initial": 0,
        0: {
            '0': (0, '1', 'L'),
            '1': (1, '0', 'L'),
            'B': (0, None, 'L'),
            '#': (4, None, 'R')
        },
        1: {
            '0': (1, None, 'L'),
            '1': (1, None, 'L'),
            '#': (2, None, 'L')
        },
        2: {
            '0': (3, '1', 'N'),
            '1': (2, '0', 'L'),
            'B': (3, '1', 'N')
        },
        3: {
            '0': (3, None, 'R'),
            '1': (3, None, 'R'),
            '#': (3, None, 'R'),
            'B': (0, None, 'L')
        },
        4: {
            '1': (4, 'B', 'R'),
            'B': (4, None, 'L'),
            '#': (5, 'B', 'L')
        },
        5: None
    }
)

while turing.etape():
    print(turing)