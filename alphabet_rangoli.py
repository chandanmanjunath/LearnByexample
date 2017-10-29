import string

def print_rangoli(size):
    # your code goes here
    str_var=string.ascii_lowercase
    list_var=[]
    for i in xrange(size):
        temp_var='-'.join(str_var[i:size])
        list_var.append((temp_var[::-1]+temp_var[1:]).center(4*size-3,"-"))
    print ("\n".join(list_var[:0:-1]+list_var))    
