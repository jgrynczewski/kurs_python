# Operatory porównania
# Zwracają True lub False (typ logiczny)
#
# ==, !=  (działa dla wszystiego)
# >, <, >=, <=  (działa nie dla wszystkiego)

# Wyrażnie skonstruowane za pomocą operatów porównania
# nazywamy wyrażeniami logicznymi

res = 3 > 4
print(type(res))
print(res)

print(3 < 4)

print(3 != 4)
print(5 == 5)
print(5 >= 5)

print("==== string ===")
print("ala" == "ala")
print("ala" == "bartek")

print(3.2 > 3.4)
print(False == True)

print("ala" == 3)
print(None == 34.2)

print("zew" < "zebra")

print(3 < 3.2)  # niejawne rzutowanie (koercja)
# promocja typów (rzutuje niejawnie 3 (int) na 3.0 (float)
# i dopiero porównuje)

print(3 < 4 < 5 < 6)
