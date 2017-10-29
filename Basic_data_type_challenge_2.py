if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())#map(aFunction.aSequence)
    t=tuple(integer_list)
    #create a hash for the tuple
    print hash(t)
