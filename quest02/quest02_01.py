x0 = 0
y0 = 0
xa = 157
ya = 61

for i in range(3):
    x = (x0 * x0) - (y0 * y0)
    y = (x0 * y0) + (y0 * x0)
    x = x // 10
    y = y // 10
    x = x + xa
    y = y + ya
    x0 = x
    y0 = y

print(x, y)
