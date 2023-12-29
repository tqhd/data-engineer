# define input data int
n = int(input("Sample input : "))

# If n is odd, print Hello
if n%2==1:
    print("Hello")
# If n is even and in the inclusive range of 2 to 5, print World
elif n%2==0 and n in range(2, 6):
    print("World")
# If n is even and in the inclusive range of 6 to 20, print Hell
elif n%2==0 and n in range(6, 21):
    print("Hello")
# If n is even and greater than 20, print World
elif n%2==0 and n>20:
    print("World")

