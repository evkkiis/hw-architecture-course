# Задание №1.
# ¬(A ∧ B) ∨ ¬(A ∨ C)
print ("A B C f")
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            f = not (A and B) or not (A or C)
            print (A, B, C, int(f))

print("-" * 20)

# Задание №2.
# (A ∧ B) ∨ (¬B ∧ C)
print ("A B C f")
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            f = (A and B) or (not B and C)
            print(A, B, C, int(f))

print("-" * 20)

# Задание №3.
# (A ∧ B) ∨ ¬C
print("A B C f")
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            f = (A and B) or not C
            print(A, B, C, int(f))

print("-" * 20)