values = [1, 2, 3, 4, 5, 6]

print(values)
# Unpack
print(*values)


def my_sum(a, b, c):
    return a + b + c


values = [1, 2, 3]
print(my_sum(*values))
v1, v2, v3 = values
print(v1, v2, v3)
v1, *v2, v3 = values
print(v1, v2, v3)
