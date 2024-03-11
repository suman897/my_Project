#program to print Zig Zag lines pattern

def zigZag(length, height):
    for i in range(length):
        for j in range(height):
            yield('*')


def triangle(height):
    for i in range(height+1):
        print("*"*i)

print(triangle(10))

