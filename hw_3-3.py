def a(v1, v2, v3):
    b = sorted([v1, v2, v3]).pop(1) + sorted([v1, v2, v3]).pop(2)
    return b
print(a(100, 200, 4))
