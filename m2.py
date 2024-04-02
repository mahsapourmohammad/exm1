def solve_puzzles(puzzles):

    rst = []

    for m in puzzles:
            
        if isinstance(m, int) or isinstance(m, float):
            if m == 0 :
                rst.append(False)
            else:
                rst.append(True)
        elif m == None:
            rst.append(None)
        elif len(m)==0:
            rst.append(False)
        else:
             rst.append(True)   
    return rst

puzzles = [ 'ali', 1233, 0, "", [], {}, 'False', '0', 'None', None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]','[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}','{"a": 1}','True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1,0.1, -0.1]

print(solve_puzzles(puzzles))