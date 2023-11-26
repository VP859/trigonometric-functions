from Trigonometric_functions import *

file_path = str(input('Enter path to csv file or leave blank for random generation: '))

functions = Trigonometry(file_path)

while True:
    print('1. Sin function\n2. Cos function\n3. Tan function\n4. Arcsin function\n5. Arccos function\n6. Arctan function\n7. All functions\n8. Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        functions.sin()
        print('Sin function saved to figures/sin_function.png')
    elif choice == 2:
        functions.cos()
        print('Cos function saved to figures/cos_function.png')
    elif choice == 3:
        functions.tan()
        print('Tan function saved to figures/tan_function.png')
    elif choice == 4:
        functions.arcsin()
        print('Arcsin function saved to figures/arcsin_function.png')
    elif choice == 5:
        functions.arccos()
        print('Arccos function saved to figures/arccos_function.png')
    elif choice == 6:
        functions.arctan()
        print('Arctan function saved to figures/arctan_function.png')
    elif choice == 7:
        functions.all()
        print('All functions saved to figures/')
    elif choice == 8:
        break