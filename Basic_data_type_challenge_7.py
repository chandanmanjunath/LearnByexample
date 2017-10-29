print "test"
def swap_case(s):
    list_var=list(s)
    for i in range(0,len(list_var)):
        if list_var[i].islower() == True :
            list_var[i]=list_var[i].upper()
        elif list_var[i].isupper() == True :
            list_var[i]=list_var[i].lower()
        else :
            pass
    tar_str=''.join(map(str, list_var))
    return tar_str
#print "test1"
#if __name__ == '__main__':
s = raw_input('>')
result = swap_case(s)
print result
