# Moduły

# Użyj pętli for w celu wyświetlenia 10 losowych liczb całkowitych
# z przedziału 0, 20.
import random

# Z wykorzystaniem pętli while
counter = 0
while counter < 10:
    print(random.randint(0, 20))

    counter += 1


# Z wykorzystaniem pętli for
for idx in range(10):
    print(random.randint(0, 20))
