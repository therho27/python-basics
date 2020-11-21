
def iterate_and_add (lst):
    total= 0
    for ele in lst:
        total=total+ele
    return total



lst=[]
#n is integer and length of list taken as input
n = int(input ("Enter length of list :"))
#print = display 
print("Enter List elements")
for ele in range (n):
    num=int(input())
    lst.append (num)
print("sum",lst,"is",iterate_and_add(lst))
3