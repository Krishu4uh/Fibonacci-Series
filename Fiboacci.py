size =int(input("Enter the size : "))
length = 0
count = 0
term1 = 0
term2 = 1  
while length < size :
    count = count + 1
    nextTerm = term1 + term2
    term1 = term2
    term2 = nextTerm
    length = len(str(term2))
if size == length :
    print("The first fibonacci number of given length is : ",term2)
    print("Index of this number is : ",count)
