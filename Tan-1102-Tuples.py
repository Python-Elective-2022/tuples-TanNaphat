'''
define skip_tuples function with t as variable:
    return the slice with every other value of t

define main
    test1 is some tuples
    test2 is also some tuples
    print the skip tuples of test 1
    print the skip tuples of test 2

run main
'''

def skip_tuples(t):
    '''
    t = tuple
    return out every other value of a tuple
    '''
    return t[::2]

def main():
    test1 = ('i', 'am', 'the', 'hulk')
    test2 = ('lala', 'dada', 'gaga', 'sasa', 'tata')
    print(skip_tuples(test1))
    print(skip_tuples(test2))

if __name__ == "__main__":
    main()



