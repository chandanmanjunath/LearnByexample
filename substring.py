str_var=input("Enter the string which has substring\n")
sub_var=input("Enter the substring to search\n")
count=0

tar_len=len(sub_var)
for i in range(0,len(str_var)):
    if str_var[i:tar_len] == sub_var:
        print (sub_var+"  substring found")
        count=count+1
    tar_len+=1
if count > 0 :
    print ("The substring count is %r" % count)
else:
    print ("The substring not found")
