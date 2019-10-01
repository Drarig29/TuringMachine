from turing import Turing

somme_unaires = Turing(
    2, 
    ['B', 'B', 1, 1, 1, 1, 1, 'B', 1, 1, 1, 1, 1, 1, 1, 1, 'B', 'B'], 
    {
        "initial": 0,
        0: {
            1: (0, None, 'R'),
            'B': (1, 1, 'N')
        },
        1: {
            1: (1, None, 'L'),
            'B': (2, None, 'R'),
        },
        2: {
            1: (3, 'B', 'R')
        },
        3: {
            1: (4, 'B', 'R')
        },
        4: None # état final
    }
)

while somme_unaires.etape():
    print(somme_unaires.bande)