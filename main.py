def convert_f(f):

    c = (float(f) - 32) * (5/9)
    print("Celsius: " + str(c))

up = True

while up:
    print("================================================")
    f = input("Fahrenheit: ")
    convert_f(f)

