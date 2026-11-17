r"""
Exact certificate of the six five-square tuple assignments in the r = 2 specialisation
of Gruson--Peskine, *Genre des courbes de l'espace projectif II*, Ann. Sci. Ec. Norm.
Sup. (4) 15 (1982) 401--418, as the corpus card P-AGH549MINGENUS states them
(Hartshorne, *Algebraic Geometry*, Exercise V.4.9).

The source was read in the text version
`tmp/sources/gruson-peskine-1982-genre-courbes-espace-projectif-ii.md`: the definitions
d(L) = -(L, w_S) and r(L) = d(L) - max{(L, E) : (E, E) = (E, w_S) = -1}, the genus
formula g = 1 + [(r - 1)d - 3r^2/4 - sum_{i=2}^{6} (r/2 - m_i)^2]/2, the definition
F_d(r) = 1 + [(r - 1)d - 3r^2/4]/2, Proposition 2.1 on printed p. 407 and Theorem 2.5 on
printed p. 409.  At r = 2, F_d(2) = (d - 1)/2, and the two theorems say that for a smooth
cubic surface S and an integer g with g <= F_d(2), the pair (d, g) is realised by a
smooth connected curve of degree d on S -- with the three printed exceptions -- exactly
when 8(F_d(2) - g) is a sum of squares of five integers of one parity and of absolute
value at most 2.

WHAT THIS FILE CERTIFIES, AND WHAT IT DOES NOT
----------------------------------------------
Certified here, exactly and symbolically over QQ[m] with d = 2m (even degrees) and
d = 2m + 1 (odd degrees), so the identities hold for every degree of each family and no
degree is sampled:

  (C1) F_d(r) at r = 2 is the polynomial (d - 1)/2 in QQ[m], in both families;
  (C2) for each of the six displayed tuples, the exact integer sum of squares, its five
       entries all of one parity (even) with absolute value at most r = 2, and the
       polynomial identity sum(x_i^2) = 8(F_d(2) - g) with the genus g the card states;
  (C3) the three genera of each family are exactly those reachable at r = 2 -- the
       squared sums are 4j with j in {0,...,5}, g = (d - 1 - j)/2 is an integer only for
       odd j when d = 2m and only for even j when d = 2m + 1, and the six tuples are the
       three realised values in each family;
  (C4) the odd-parity branch of the criterion at r = 2 forces the sum 5, which is not a
       multiple of 4 while 8(F_d(2) - g) always is, so the even branch alone occurs;
  (C5) the rejected and the corrected odd minimum tuple are distinguished: (2,2,0,0,0)
       has squared sum 8 and satisfies the identity only for g = (d - 3)/2, while the
       printed minimum (d - 5)/2 requires 8(F_d(2) - g) = 16 and is attained by the
       corrected tuple (2,2,2,2,0).

NOT certified here, and not touched by any computation in this file: the geometric
content of Proposition 2.1 and of Theorem 2.5 -- that a smooth connected curve of the
stated degree and genus exists on a smooth cubic surface, its smoothness, connectedness or
irreducibility, the attribution r(O_S(C)) = 2, the three printed exceptional triples, the
minimum-genus bound of Exercise V.4.9 and the closedness of its range.  Those are the two
articles' theorems, cited and argued on the card; this file is arithmetic only, and the
row it carries in `proofs/README.md` says so.

Run: the recorded run, its command, interpreter, source revision, wall time and verbatim
output are in `proofs/cards/V49FiveSquaresTuples.out`, which pins this script's sha256.
Entry point is the shared research image's own, through its launcher:

    proot -R $HOME/sage-image/rootfs -b /proc -b /dev -b $REPO:/work -w / \
          /sage/.venv/bin/sage /work/proofs/cards/V49FiveSquaresTuples.sage
"""
from sage.all import QQ, PolynomialRing, ZZ

R = PolynomialRing(QQ, "m")
m = R.gen()

R_ODD = 2  # the value of r specialised throughout

failures = []
checks = 0


def check(name, ok, detail=""):
    """Record one exact check.  Nothing here rounds, samples or evaluates."""
    global checks
    checks += 1
    print(f"{'OK  ' if ok else 'FAIL'}  {name}" + (f"   [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)


def F(d, r):
    """F_d(r) = 1 + [(r - 1)d - 3r^2/4]/2, in QQ[m] for d a polynomial in m."""
    return R(1) + ((R(r) - 1) * d - QQ(3 * r * r) / 4) / 2


def sumsq(t):
    """The exact integer sum of squares of a tuple."""
    return sum(ZZ(x) ** 2 for x in t)


def integral(p):
    """Whether a polynomial of QQ[m] lies in ZZ[m]."""
    return p.denominator() == 1


EVEN_D = 2 * m
ODD_D = 2 * m + 1

# The six rows the card displays: (tuple, genus), with d = 2m and d = 2m + 1.
EVEN_ROWS = [
    ((2, 0, 0, 0, 0), (EVEN_D - 2) / 2),
    ((2, 2, 2, 0, 0), (EVEN_D - 4) / 2),
    ((2, 2, 2, 2, 2), (EVEN_D - 6) / 2),
]
ODD_ROWS = [
    ((0, 0, 0, 0, 0), (ODD_D - 1) / 2),
    ((2, 2, 0, 0, 0), (ODD_D - 3) / 2),
    ((2, 2, 2, 2, 0), (ODD_D - 5) / 2),
]

print(f"r = {R_ODD};  d = 2m (even degrees), d = 2m + 1 (odd degrees);  F_d(r) = "
      f"1 + [(r-1)d - 3r^2/4]/2 in QQ[m]")

# (C1) F_d(2) = (d - 1)/2, both families, as polynomial identities.
for name, d in (("even", EVEN_D), ("odd", ODD_D)):
    lhs, rhs = F(d, R_ODD), (d - 1) / 2
    check(f"C1  F_d(2) = (d-1)/2 for {name} d", lhs == rhs,
          f"F_d(2) = {lhs}, (d-1)/2 = {rhs}")

# (C2) and (C3), row by row.
for family, d, rows in (("even", EVEN_D, EVEN_ROWS), ("odd", ODD_D, ODD_ROWS)):
    target = F(d, R_ODD)
    print(f"\n-- {family} degrees, d = {d}, F_d(2) = {target} --")
    for tuple_, g in rows:
        s = sumsq(tuple_)
        parities = sorted({ZZ(x) % 2 for x in tuple_})
        same_parity = len(parities) == 1
        bound = max(abs(ZZ(x)) for x in tuple_)
        rhs8 = 8 * (target - g)
        check(f"C2  {family} {str(tuple_):>14}  sum(x_i^2) = 8(F_d(2)-g)",
              R(s) == rhs8,
              f"sum = {s}, g = {g}, 8(F_d(2)-g) = {rhs8}")
        check(f"C2  {family} {str(tuple_):>14}  one parity, |x_i| <= r = 2",
              same_parity and bound <= R_ODD,
              f"parity {parities}, max |x_i| = {bound}")
        check(f"C2  {family} {str(tuple_):>14}  g integral", integral(g),
              f"g = {g} in ZZ[m] = {integral(g)}")

    # (C3) the j-classification: sum = 4j, g = (d - 1 - j)/2 integral exactly for the
    # j of one parity, and the three rows are those three j.
    realised = sorted(sumsq(t) for t, _ in rows)
    expected_j = [j for j in range(6) if integral((d - 1 - j) / 2)]
    check(f"C3  {family}: g = (d-1-j)/2 integral exactly for j {expected_j}",
          realised == [4 * j for j in expected_j],
          f"realised sums {realised} = 4 * {[s // 4 for s in realised]}")
    for tuple_, g in rows:
        j = sumsq(tuple_) // 4
        check(f"C3  {family} {str(tuple_):>14}  g = (d-1-j)/2 with j = {j}",
              g == (d - 1 - j) / 2, f"g = {g}")

# (C4) the odd-parity branch at r = 2 gives the sum 5, which is not a multiple of 4.
odd_branch_sum = sumsq((1, 1, 1, 1, 1))
check("C4  odd parity at r = 2 forces sum = 5 (five entries +-1)",
      odd_branch_sum == 5 and all(abs(ZZ(x)) <= R_ODD for x in (1, 1, 1, 1, 1)),
      f"sum = {odd_branch_sum}")
for name, d in (("even", EVEN_D), ("odd", ODD_D)):
    eight_F = 8 * F(d, R_ODD)  # = 4(d - 1)
    check(f"C4  8F_d(2) = 4(d-1) and 8F_d(2) - 8g is a multiple of 4 for every g",
          eight_F == 4 * (d - 1) and integral(eight_F / 4),
          f"8F_d(2) = {eight_F}")
check("C4  5 is not a multiple of 4, so the odd branch yields no (d, g)",
      ZZ(5) % 4 != 0, "5 mod 4 = 1")

# (C5) the rejected tuple against the corrected one, both over QQ[m].
print("\n-- the rejected and the corrected odd minimum tuple --")
REJECTED = (2, 2, 0, 0, 0)
CORRECTED = (2, 2, 2, 2, 0)
MINIMUM_GENUS = (ODD_D - 5) / 2
OLD_GENUS = (ODD_D - 3) / 2
check("C5  rejected (2,2,0,0,0): sum = 8", sumsq(REJECTED) == 8, f"sum = {sumsq(REJECTED)}")
check("C5  corrected (2,2,2,2,0): sum = 16", sumsq(CORRECTED) == 16,
      f"sum = {sumsq(CORRECTED)}")
check("C5  the two sums differ: 8 != 16", sumsq(REJECTED) != sumsq(CORRECTED), "")
check("C5  8 = 8(F_d(2) - g) holds for the rejected tuple exactly at g = (d-3)/2",
      R(sumsq(REJECTED)) == 8 * (F(ODD_D, R_ODD) - OLD_GENUS)
      and R(sumsq(REJECTED)) != 8 * (F(ODD_D, R_ODD) - MINIMUM_GENUS),
      f"g = {OLD_GENUS} gives {8 * (F(ODD_D, R_ODD) - OLD_GENUS)}; "
      f"g = {MINIMUM_GENUS} gives {8 * (F(ODD_D, R_ODD) - MINIMUM_GENUS)}")
check("C5  16 = 8(F_d(2) - g) holds for the corrected tuple at the printed minimum "
      "g = (d-5)/2",
      R(sumsq(CORRECTED)) == 8 * (F(ODD_D, R_ODD) - MINIMUM_GENUS),
      f"g = {MINIMUM_GENUS}, 8(F_d(2)-g) = {8 * (F(ODD_D, R_ODD) - MINIMUM_GENUS)}")
check("C5  the card's two odd tuples below the top one are these, of sums 8 and 16",
      sumsq(ODD_ROWS[1][0]) == 8 and sumsq(ODD_ROWS[2][0]) == 16,
      f"{ODD_ROWS[1][0]} -> {sumsq(ODD_ROWS[1][0])}, "
      f"{ODD_ROWS[2][0]} -> {sumsq(ODD_ROWS[2][0])}")

# The six rows are distinct, three per family, and ordered by decreasing genus.
all_tuples = [t for t, _ in EVEN_ROWS] + [t for t, _ in ODD_ROWS]
check("the six tuple assignments are distinct", len(set(all_tuples)) == 6,
      f"{len(set(all_tuples))} distinct")
check("each family has three rows", len(EVEN_ROWS) == 3 and len(ODD_ROWS) == 3, "")

print()
if failures:
    print(f"{checks} checks, {len(failures)} FAILED: {failures}")
    raise SystemExit(1)
print(f"ALL {checks} CHECKS PASSED")
