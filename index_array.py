n=int(input("Enter the no. of elements\n"))
print("Enter the elements")
list_var=[]
for i in range(0,n):
    list_var.append(int(input()))

tar_sum=int(input("Enter the target sum"))
flag='N'
sum_var=0

for i in range(0,n):
    sum_var=list_var[i]
    for j in range(i+1,n):
              sum_var=sum_var+list_var[j]
              if sum_var == tar_sum:
                    print ("The sum can be obtained between indexes %d and %d" % (i,j))
                    flag='Y'
              if sum_var > tar_sum:
                  sum_var=0
                  break
if flag == 'N':
    print ("Subarray not found  ")
