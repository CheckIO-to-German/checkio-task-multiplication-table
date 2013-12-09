"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
TESTS = {
    "Basics": [
        {
            'input': [4, 6],
            'answer': 38,
            'explanation': [[['1', '1', '0'],
                             ['1', '1', '1', '0', 6],
                             ['0', '0', '0', '0', 0],
                             ['0', '0', '0', '0', 0],
                             6],
                            [['1', '1', '0'],
                             ['1', '1', '1', '1', 7],
                             ['0', '1', '1', '0', 6],
                             ['0', '1', '1', '0', 6],
                             19],
                            [['1', '1', '0'],
                             ['1', '0', '0', '1', 1],
                             ['0', '1', '1', '0', 6],
                             ['0', '1', '1', '0', 6],
                             13]],
        },
        {
            'input': [2, 7],
            'answer': 28,
            'explanation': [[['1', '1', '1'],
                             ['1', '1', '1', '1', 7],
                             ['0', '0', '0', '0', 0],
                             7],
                            [['1', '1', '1'],
                             ['1', '1', '1', '1', 7],
                             ['0', '1', '1', '1', 7],
                             14],
                            [['1', '1', '1'],
                             ['1', '0', '0', '0', 0],
                             ['0', '1', '1', '1', 7],
                             7]],
        },
        {
            'input': [7, 2],
            'answer': 18,
            'explanation': [[['1', '0'],
                             ['1', '1', '0', 2],
                             ['1', '1', '0', 2],
                             ['1', '1', '0', 2],
                             6],
                            [['1', '0'],
                             ['1', '1', '1', 3],
                             ['1', '1', '1', 3],
                             ['1', '1', '1', 3],
                             9],
                            [['1', '0'],
                             ['1', '0', '1', 1],
                             ['1', '0', '1', 1],
                             ['1', '0', '1', 1],
                             3]],
        }
    ],
    "Extra": [
        {
            'input': [4, 6],
            'answer': 38,
            'explanation': [[['1', '1', '0'],
                             ['1', '1', '1', '0', 6],
                             ['0', '0', '0', '0', 0],
                             ['0', '0', '0', '0', 0],
                             6],
                            [['1', '1', '0'],
                             ['1', '1', '1', '1', 7],
                             ['0', '1', '1', '0', 6],
                             ['0', '1', '1', '0', 6],
                             19],
                            [['1', '1', '0'],
                             ['1', '0', '0', '1', 1],
                             ['0', '1', '1', '0', 6],
                             ['0', '1', '1', '0', 6],
                             13]],
        },
        {
            'input': [2, 7],
            'answer': 28,
            'explanation': [[['1', '1', '1'],
                             ['1', '1', '1', '1', 7],
                             ['0', '0', '0', '0', 0],
                             7],
                            [['1', '1', '1'],
                             ['1', '1', '1', '1', 7],
                             ['0', '1', '1', '1', 7],
                             14],
                            [['1', '1', '1'],
                             ['1', '0', '0', '0', 0],
                             ['0', '1', '1', '1', 7],
                             7]],
        },
        {
            'input': [7, 2],
            'answer': 18,
            'explanation': [[['1', '0'],
                             ['1', '1', '0', 2],
                             ['1', '1', '0', 2],
                             ['1', '1', '0', 2],
                             6],
                            [['1', '0'],
                             ['1', '1', '1', 3],
                             ['1', '1', '1', 3],
                             ['1', '1', '1', 3],
                             9],
                            [['1', '0'],
                             ['1', '0', '1', 1],
                             ['1', '0', '1', 1],
                             ['1', '0', '1', 1],
                             3]],
        }
    ]
}

