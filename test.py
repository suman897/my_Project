#program to print Zig Zag lines pattern

def zigZag(length, height):
    for i in range(length):
        for j in range(height):
            yield('*')


def triangle(height):
    for i in range(height+1):
        print("*"*i)
    for i in range(height+1):
        print("*"*(height-i-1))

print(triangle(5))

