if __name__ == '__main__':
    #to get first input
    N = int(raw_input())
    #initialize the lists(declaration)
    l=[]

    for i in range(N):
        #to get second set of inputs
        op_list=raw_input().strip().split(" ")

        if op_list[0] == 'insert':
            l.insert(int(op_list[1]),int(op_list[2]))
        elif op_list[0] == 'remove':
            l.remove(int(op_list[1]))
        elif op_list[0] == 'append':
            l.append(int(op_list[1]))
        elif op_list[0] == 'sort':
            l.sort()
        elif op_list[0] == 'pop':
            l.pop()
        elif op_list[0] == 'reverse':
            l.reverse()
        else :
            print l
