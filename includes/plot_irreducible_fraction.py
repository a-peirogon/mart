#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from math import gcd

# ========================================================
# Verifica si un número complejo a+bi en Z[i] es irreducible
# es decir, gcd(a, b) = 1 (primitividad en Z)
# ========================================================
def is_primitive(a, b):
    return gcd(a, b) == 1

# Rango de búsqueda en la cuadrícula de Gaussian integers
N = 60  # tamaño del dominio

xs = []
ys = []

for a in range(-N, N + 1):
    for b in range(-N, N + 1):
        if a == 0 and b == 0:
            continue
        if is_primitive(a, b):
            # Proyectar el número complejo a/(a+bi)
            z = complex(a, 0) / complex(a, b)
            xs.append(z.real)
            ys.append(z.imag)

# Plot
plt.figure(figsize=(6, 6))
plt.scatter(xs, ys, s=1)
plt.title("Irreducible Fractions in the Complex Plane (ℤ[i])")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.axis("equal")
plt.tight_layout()
plt.show()
