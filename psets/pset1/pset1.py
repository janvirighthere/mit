def evaluate_poly(poly, x):
    r = len(poly) - 1
    f_of_x = 0
    for i in range(r, 1, -1):
        val = poly[i] * (x**i)
        f_of_x += val

    return f_of_x

def compute_deriv(poly):
    l = []

    for i in range(1, len(poly)):
        val = poly[i]*i
        l.append(val)
    
    return tuple(l)
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
print(compute_deriv(poly))
