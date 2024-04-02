def solve_puzzles(puzzles):

    rst = []

    for m in puzzles: 
        if isinstance(m, int) or isinstance(m,float):
            if m!=0:
                rst.append(True)
            else:
                rst.append(False)
        elif isinstance(m,str) or isinstance(m,list) or isinstance(m,set) or isinstance(m,dict):
            if len(m)!=0:
                rst.append(True)
            else:
                rst.append(False)
        elif m==None:
            rst.append(False)
        else:
            if m==True:
                rst.append(True)
            else:
                rst.append(False)                              
            
    return rst

puzzles = [ 'ali', 1233, 0, "", [], {}, 'False', '0', 'None', None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]','[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}','{"a": 1}','True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1,0.1, -0.1]

print(solve_puzzles(puzzles))