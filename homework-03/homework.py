A = 3
B = 8
C = 4
print("№1 | №2 | №3 |")
print("-" *14)

exercise1 = (not(A & B)) | (not(A | C))
exercise2 = (A & B) | ((not(B)) & C)
exercise3 = (A & B) | (not(C))

print(f"{bin(exercise1)}|{bin(exercise2)} |{bin(exercise3)} |")