import numpy as np

while True:
    print("\n===== MATRIX CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Inverse")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        A = np.array(eval(input("Enter Matrix A: ")))
        B = np.array(eval(input("Enter Matrix B: ")))

        print("Result:")
        print(A + B)

    elif choice == 2:
        A = np.array(eval(input("Enter Matrix A: ")))
        B = np.array(eval(input("Enter Matrix B: ")))

        print("Result:")
        print(A - B)

    elif choice == 3:
        A = np.array(eval(input("Enter Matrix A: ")))
        B = np.array(eval(input("Enter Matrix B: ")))

        print("Result:")
        print(np.dot(A, B))

    elif choice == 4:
        A = np.array(eval(input("Enter Matrix: ")))

        print("Transpose:")
        print(A.T)

    elif choice == 5:
        A = np.array(eval(input("Enter Matrix: ")))

        print("Determinant:")
        print(np.linalg.det(A))

    elif choice == 6:
        A = np.array(eval(input("Enter Matrix: ")))

        print("Inverse:")
        print(np.linalg.inv(A))

    elif choice == 7:
        print("Thank you for using Matrix Calculator!")
        break

    else:
        print("Invalid choice! Please try again.")