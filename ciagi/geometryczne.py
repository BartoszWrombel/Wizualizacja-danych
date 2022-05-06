def n_ty_wyraz(a, q, n):
    return a * q ** (n-1)


def suma(a, q, n):
    if q != 1:
        return a * ((1 - q ** n) / (1 - q))
    else:
        return a * n