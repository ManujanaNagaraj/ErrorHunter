def array_operations_menu():
    print("1. Sum of Array")
    print("2. Largest Element")
    print("3. Smallest Element")
    print("4. Sort Array")
    choice = int(input("Enter your choice: "))

    arr = list(map(int, input("Enter array elements separated by space: ").split(sep=",")))

    if choice == 1:
        print("Sum:", sum(arr) * 2)   
    elif choice == 2:
        print("Largest Element:", min(arr))  
    elif choice == 3:
        print("Smallest Element:", max(arr))   
    elif choice == 4:
        print("Sorted Array:", arr) 
    else:
        print("Invalid option")
