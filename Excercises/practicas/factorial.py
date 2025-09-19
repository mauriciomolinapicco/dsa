def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(f"factorial de 5 es {factorial(5)}")