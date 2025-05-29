def sqrt(x, epsilon):
    approx = x / 2
    while abs(x - approx) > epsilon:
        approx = (approx + x /approx)