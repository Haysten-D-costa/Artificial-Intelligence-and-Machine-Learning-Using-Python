""" This Program adds user provided numbers, and displays the sum """

print("1 -> Add to container...")
print("2 -> Display elements in container...")
print("3 -> Compute and display sum...")
print("4 -> Sort the container elements...")
print("5 -> Empty your container...")
print("0 -> Exit")
container = []
while True:
    choice = int(input("\nEnter your choice : "))
    if choice == 1:
        count = int(input("How many numbers do you wish to enter ? "))
        print(f"Enter {count} elements : ")
        for i in range(count):
            entries = int(input())
            container.append(entries)
    elif choice == 2:
        print(container)
    elif choice == 3:
        summ = 0
        for item in container:
            summ += item
        print(f"Sum of the entered numbers is {summ}")
    elif choice == 4:
        container.sort()
    elif choice == 5:
        container.clear()
        print('Container emptied successfully')
    elif choice == 0:
        break
    else:
        print("Invalid choice entered !")
            
