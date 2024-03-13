#program to print Zig Zag lines pattern

def zigZagPattern(length = 5, height = 4):
    length -= 1
    for j in range(height):
        for i in range(length):
            print("  "*(i), end="*")
            print()
        for i in range(length):
            print("  "*(length-i), end="*")
            print()
    print("*")

if __name__ == '__main__':
    print(zigZagPattern(5,4))

