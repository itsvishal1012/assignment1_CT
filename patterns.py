def lower_triangular(n):
    print("Lower Triangular Pattern is:")
    for i in range(1, n + 1):
        print("* " * i)
    print()  

def upper_triangular(n):
    print("Upper Triangular Pattern is:")
    for i in range(n, 0, -1):
        print("* " * i)
    print()  

def pyramid(n):
    print("Pyramid Pattern is:")
    for i in range(1, n + 1):
       
        print("  " * (n - i), end="")
        
        print("* " * (2 * i - 1))
    print()  

def main():
    n = 5
    lower_triangular(n)
    upper_triangular(n)
    pyramid(n)

if __name__ == "__main__":
    main()
