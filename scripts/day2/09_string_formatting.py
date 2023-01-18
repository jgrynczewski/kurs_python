# Formatowanie napisów
result = 50

# Konkatenacja napisów
print("Otrzymałeś " + str(50) + " punktów")

# f-string (wprowadzony w Python3.6)
print(f"Otrzymałeś {result} punktów")

# Starsze metody
# metoda format
print("Otrzymałeś {} punktów".format(result))

# C-like
print("Otrzymałeś %s punktów" % result)

# Specjalne właściwości funkcji print
print("Otrzymałeś", result, "punktów")

