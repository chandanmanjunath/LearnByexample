if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    flag='n'
    if n>=2 and n<=10:
        for i in arr:
            if i>=-100 and i<=100:
                    flag='y'
            else:
                    flag='n'

    if flag =='y':
        var_temp=set(arr)
        var_temp =sorted(var_temp)
        print var_temp[len(var_temp)-2]
