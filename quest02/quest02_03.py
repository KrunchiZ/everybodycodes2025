xa = -79725
ya = -16616
engrave = 0

yb = ya

for i in range(1001):
    xb = xa
    for j in range(1001):
        x0 = 0
        y0 = 0
        ok = True
        for i in range(100):
            x = (x0 * x0) - (y0 * y0)
            y = (x0 * y0) + (x0 * y0)
            x = int(x / 100000)
            y = int(y / 100000)
            x = x + xb
            y = y + yb
            x0 = x
            y0 = y
            if ((abs(x0) > 1000000) or (abs(y0) > 1000000)):
                ok = False
                break
        if (ok):
            engrave += 1
        xb += 1
    yb += 1
print(engrave)
