def x(a,b):
    '''x(a,b) --> [a,b]'''
    return [a,b]

def add(a,b):
    '''add(a,b) --> a+b'''
    return a+b

def test():
    '''test code for all modules'''
    print("testing x...")
    print(x(1,2))
    print(x('a','b'))
    print(x([1,2,3],[4,5,6]))
    print("testing add...")
    print(add(1,2))
    print(add('a','b'))
    print(add([1,2,3],[4,5,6]))
    return
