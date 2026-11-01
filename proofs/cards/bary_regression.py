"""Exact chain-level regression for E-HAT-2.1-25.

Compares three things in the singular chain group of the standard simplex, as maps on
vertex-tuples:
  H  : Hatcher's recursive definition  S(l) = b_l(S d l)   (p.121)
  C  : the card's ascending-barycentre formula  sum_pi sgn(pi) (b_{F_0},...,b_{F_n})
  D  : the descending formula  sum_pi sgn(pi) (b_{F_n},...,b_{F_0})
Vertices are integers; a barycentre of a face is the symbol ('b', sorted face).
"""
from itertools import permutations
from fractions import Fraction

def sgn(p):
    p = list(p); s = 1
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]: s = -s
    return s

def add(c, k, v):
    c[tuple(k)] = c.get(tuple(k), 0) + v

def face(simplex, k):
    return simplex[:k] + simplex[k+1:]

def bary(face_vertices):
    return ('b', tuple(sorted(face_vertices)))

def hatcher(simplex):
    n = len(simplex) - 1
    if n == 0:
        return {(bary(simplex),): 1}   # a vertex of the subdivision is b_{0-face}
    out = {}
    b = bary(simplex)
    for k in range(n + 1):
        for sub, coef in hatcher(face(simplex, k)).items():
            add(out, (b,) + sub, (-1) ** k * coef)
    return {k: v for k, v in out.items() if v}

def formula(simplex, descending):
    n = len(simplex) - 1
    out = {}
    for pi in permutations(range(n + 1)):
        chain = [bary([simplex[i] for i in pi[:k+1]]) for k in range(n + 1)]
        if descending: chain = chain[::-1]
        add(out, tuple(chain), sgn(pi))
    return {k: v for k, v in out.items() if v}

def scale(c, s):
    return {k: s*v for k, v in c.items() if s*v}

for n in (1, 2):
    simplex = tuple(range(n + 1))
    H, C, D = hatcher(simplex), formula(simplex, False), formula(simplex, True)
    rev = (-1) ** (n*(n+1)//2)
    print(f"--- n = {n}")
    print("  Hatcher :", H)
    print("  card    :", C)
    print("  desc    :", D)
    print("  card == Hatcher ?      ", C == H)
    print("  desc == Hatcher ?      ", D == H)
    print("  Hatcher == rev * card ?", H == scale(C, rev), f"(rev = {rev})")
    print("  Hatcher == -desc ?     ", H == scale(D, -1))
    print("  Hatcher == desc*sign?  ", H == scale(D, rev))
    print("  equal as SETS (flip convention): ", set(H) == set(C) or set(H) == set(D))
