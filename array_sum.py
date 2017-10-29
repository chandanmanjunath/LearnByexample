n=int(input("Enter the no. of elements\n"))
print("Enter the elements")
list_var=[]
for i in range(0,n):
    list_var.append(int(input()))


tar_sum=int(input("Enter the target sum"))
sum_var=0

for i in range(0,n):
    print ("for i"+str(i))
    for j in range(0,n):
        if i != j :
            #if sum_var < tar_sum:
                #if sum_var == 0 :
                    sum_var=sum_var+list_var[i]+list_var[j]
                    if sum_var == tar_sum :
                        #print ("The numbers are")
                        print ("Sum found,The numbers are %d and %d " % (list_var[i],list_var[j]))
                        #sum_var=0
                    print ("i"+str(i))
                    print ("j"+str(j))
                    print ("sum_var"+str(sum_var))
                    if sum_var > tar_sum :
                        sum_var=0
