#program to print Zig Zag lines pattern
class Pattern:
    def zigZagPattern(self, length = 5, height = 4):
        length -= 1
        for j in range(height):
            for i in range(length):
                print("  "*(i), end="*")
                print()
            for i in range(length):
                print("  "*(length-i), end="*")
                print()
        print("*")

    def user_Input(args):
        while True:
            try:
                return int(input("Enter an integer: "))  
            except ValueError:
                print("Invalid input. Please enter an integer.")

if __name__ == '__main__':
    p=Pattern()
    length=p.user_Input()
    breath=p.user_Input()
    print(p.zigZagPattern(length,breath))

