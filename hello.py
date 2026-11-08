# Nama : Vedanta, Baruna, Jessica
# Kelas : DDP-C~
print("Hello, World!")

for i in range(5):
    print("Hello, World!", i)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)