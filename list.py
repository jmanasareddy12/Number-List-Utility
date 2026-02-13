def create_list():
    n = int(input("Enter number of elements: "))
    lst = []
    for i in range(n):
        lst.append(int(input(f"Enter element {i+1}: ")))
    return lst

def find_max(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

def find_min(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

def find_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

def sort_list(lst, order):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (order == "asc" and lst[i] > lst[j]) or  (order == "desc" and lst[i] < lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def display(lst):
    print("Current List:", lst)


# Main Program
numbers = create_list()

while True:
    print("\n--- Number List Utility Tool ---")
    print("1. Find Maximum")
    print("2. Find Minimum")
    print("3. Find Sum")
    print("4. Sort Ascending")
    print("5. Sort Descending")
    print("6. Display List")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Maximum:", find_max(numbers))
    elif choice == 2:
        print("Minimum:", find_min(numbers))
    elif choice == 3:
        print("Sum:", find_sum(numbers))
    elif choice == 4:
        print("Sorted (Asc):", sort_list(numbers, "asc"))
    elif choice == 5:
        print("Sorted (Desc):", sort_list(numbers, "desc"))
    elif choice == 6:
        display(numbers)
    elif choice == 7:
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")