def func(a, b, c):
    print(a)
    print(b)
    print(c)


# Argumenty pozycyjne (positional arguments)
func(1, 2, 3)

# Argumenty nazwane (keywords arguments)
func(a=1, b=2, c=3)
func(c=3, a=1, b=2)

func(1, c=3, b=2) # zawsze pozycyjne jako pierwsze

# func(c=1, 2, a=3)  # tak nie można


# argumenty domyślne
def func2(a, b, c=10):
    print(a)
    print(b)
    print(c)


func2(3, 4)
