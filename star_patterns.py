"""
STAR PATTERNS IN PYTHON
-----------------------
Each function prints a pattern using '*'. 
Keep n small (3–15) when testing to fit on screen.

Run this file directly to see all patterns for a chosen n.
"""

def print_square(n):
    for _ in range(n):
        print('*' * n)

def left_triangle(n):
    for i in range(1, n+1):
        print('*' * i)

def right_triangle(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * i)

def inverted_left_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

def pyramid(n):
    for i in range(1, n+1):
        spaces = n - i
        stars = 2*i - 1
        print(' ' * spaces + '*' * stars)

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        spaces = n - i
        stars = 2*i - 1
        print(' ' * spaces + '*' * stars)

def diamond(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * (2*i - 1))
    for i in range(n-1, 0, -1):
        print(' ' * (n - i) + '*' * (2*i - 1))

def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n-2) + '*')

def hollow_pyramid(n):
    for i in range(1, n+1):
        if i == 1:
            print(' ' * (n-1) + '*')
        elif i == n:
            print('*' * (2*n - 1))
        else:
            gaps = 2*i - 3
            print(' ' * (n - i) + '*' + ' ' * gaps + '*')

def hollow_diamond(n):
    # top
    for i in range(1, n+1):
        if i == 1:
            print(' ' * (n-1) + '*')
        else:
            gaps = 2*i - 3
            print(' ' * (n - i) + '*' + ' ' * gaps + '*')
    # bottom
    for i in range(n-1, 0, -1):
        if i == 1:
            print(' ' * (n-1) + '*')
        else:
            gaps = 2*i - 3
            print(' ' * (n - i) + '*' + ' ' * gaps + '*')

def hourglass(n):
    # top filled pyramid inverted
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2*i - 1))
    # bottom filled pyramid
    for i in range(2, n+1):
        print(' ' * (n - i) + '*' * (2*i - 1))

def sandglass(n):
    # top hollow inverted pyramid
    for i in range(n, 0, -1):
        if i == n:
            print('*' * (2*n - 1))
        elif i == 1:
            print(' ' * (n-1) + '*')
        else:
            gaps = 2*i - 3
            print(' ' * (n - i) + '*' + ' ' * gaps + '*')
    # bottom hollow pyramid
    for i in range(2, n+1):
        if i == n:
            print('*' * (2*n - 1))
        else:
            gaps = 2*i - 3
            print(' ' * (n - i) + '*' + ' ' * gaps + '*')

def butterfly(n):
    # top wings
    for i in range(1, n+1):
        left = '*' * i
        mid = ' ' * (2*(n - i))
        print(left + mid + left)
    # bottom wings
    for i in range(n, 0, -1):
        left = '*' * i
        mid = ' ' * (2*(n - i))
        print(left + mid + left)

def zigzag(n, width=3):
    # simple zigzag pattern of stars over 3 rows
    rows = 3
    for r in range(rows):
        line = []
        for c in range(n):
            if (r + c) % (rows - 1) == 0:
                line.append('*')
            else:
                line.append(' ')
        print(''.join(line))

def main():
    try:
        n = int(input("Enter n (e.g., 5): "))
    except:
        n = 5
    print("\nSQUARE")
    print_square(n)
    print("\nLEFT TRIANGLE")
    left_triangle(n)
    print("\nRIGHT TRIANGLE")
    right_triangle(n)
    print("\nINVERTED LEFT TRIANGLE")
    inverted_left_triangle(n)
    print("\nPYRAMID")
    pyramid(n)
    print("\nINVERTED PYRAMID")
    inverted_pyramid(n)
    print("\nDIAMOND")
    diamond(n)
    print("\nHOLLOW SQUARE")
    hollow_square(n)
    print("\nHOLLOW PYRAMID")
    hollow_pyramid(n)
    print("\nHOLLOW DIAMOND")
    hollow_diamond(n)
    print("\nHOURGLASS")
    hourglass(n)
    print("\nSANDGLASS")
    sandglass(n)
    print("\nBUTTERFLY")
    butterfly(n)
    print("\nZIGZAG")
    zigzag(max(2*n, 10))

if __name__ == "__main__":
    main()
