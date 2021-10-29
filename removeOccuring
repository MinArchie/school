#WAP to input list and element and delete all occurance of element in list

while True:
    lst = eval(input("Enter a List: "))
    item = int(input("Enter Element to be Removed: "))
    c = lst.count(item)

    if c == 0:
        print (item,"not in the list")
    else:
        while c > 0:
            i = lst.index(item)
            lst.pop(i)
            c = c - 1
        print ("List after removing", item, ":", lst)
