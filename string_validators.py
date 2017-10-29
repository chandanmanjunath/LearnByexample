#if __name__ == '__main__':
num=False
alp=False
dig=False
low=False
upp=False
s=raw_input()
list_val=list(s)
for i in range(0,len(list_val)):
        #print list_val[i]
    if list_val[i].isalnum():
            num=True
            if list_val[i].isalpha():
                alp=True
                if list_val[i].islower():
                     low=True
                #break;
                elif list_val[i].isupper():
                    upp=True
                else :
                    pass
    elif list_val[i].isdigit():
                dig=True
    else :
                pass
print num
print alp
print dig
print low
print upp
