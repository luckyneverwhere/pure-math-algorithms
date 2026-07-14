print("Quadratic equation solver: ax² + bx + c = 0")
a = float(input("Enter Leading coefficient a (x² term): "))
b = float(input("Enter Leading coefficient b (x term): "))
c = float(input("Enter Constant term c (constant term): "))

def discriminant(a, b, c):
    return (b * b) - (4 * a * c)

D = discriminant(a, b, c)

def calc(b, a, D):
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        return x
    elif D < 0:
        real = -b / (2 * a)
        imag = (-D) ** 0.5 / (2 * a) 
        x1 = complex(real, imag)
        x2 = complex(real, -imag)
        return x1, x2

result = calc(b, a, D)
print(result)

# 2 -4 -6 - normal
# 1 2 5 - complex
#1 -4 4 - 0 
