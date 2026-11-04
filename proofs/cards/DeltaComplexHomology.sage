"""
Exact certificates for the homology computations of Hatcher §2.1 exercises 4, 5,
6, 9 and §2.2 exercises 11, 19, as the corpus cards state them.

The complexes are built with Sage's own `ChainComplex`, whose constructor checks
that consecutive differentials compose to zero, and the homology is Sage's
`ChainComplex.homology`.  Nothing here recomputes homology by hand.

Convention: `degree=-1`, so `data[k]` is the matrix of `d_k : C_k → C_{k-1}`,
with `rows(data[k]) = rank C_{k-1}` and `cols(data[k]) = rank C_k`, and
`C.homology(k)` is `ker d_k / im d_{k+1}`.

Run:  sage proofs/cards/DeltaComplexHomology.sage

Status of the recorded run: PASSED on the supported Sage development image.

  Sage 11.0.beta5, Python 3.14.10, Sage source checkout at git HEAD
  b0cd7d86e21eb450ed90e4c83707920e1d5d429a (rootfs/sage/.git), image rootfs at
  $HOME/sage-image/rootfs, image config sha256
  2d6a4754b6f1518af356dd28ac6ec2e7678c7fe4ab0d70c2e7c9ecbc2c605eca.

  Reproduce with:

    proot -R $HOME/sage-image/rootfs -b /proc -b /dev -b $REPO:/work -w / \
          /sage/.venv/bin/sage /work/proofs/cards/DeltaComplexHomology.sage

  An earlier run used the host interpreter (Sage 10.8, Python 3.12.14) and is not
  the acceptance evidence; the results agree.
"""
from sage.all import ChainComplex, matrix, ZZ

failures = []


def check(name, data, expected):
    """Build the complex, let Sage check d^2 = 0, and compare `homology(k)`."""
    C = ChainComplex(data, degree=-1)
    got = [str(C.homology(k)) for k in range(len(expected))]
    ok = got == expected
    print(f"{name}: {got}  {'OK' if ok else 'MISMATCH, expected ' + str(expected)}")
    if not ok:
        failures.append(name)


# --- Exercise 2.1-4, the triangular parachute: C_2 = Z, C_1 = Z^3, C_0 = Z,
# d_1 = 0 and d_2(sigma) = a - b + c.
check("2.1-4 parachute",
      {1: matrix(ZZ, 1, 3, 0), 2: matrix(ZZ, 3, 1, [1, -1, 1])},
      ["Z", "Z x Z", "0"])

# --- Exercise 2.1-5, the Klein bottle: two triangles U, L with dU = a + b - c and
# dL = a - b - c, so d_2 is the 3 x 2 matrix with those columns.
check("2.1-5 Klein bottle",
      {1: matrix(ZZ, 1, 3, 0), 2: matrix(ZZ, 3, 2, [1, 1, 1, -1, -1, -1])},
      ["Z", "Z x C2", "0"])

# --- Exercise 2.1-6: n + 1 triangles with all vertices identified,
# d(sigma_0) = e_0 and d(sigma_i) = 2 e_i - e_(i-1).  The k-th column of d_2 is
# the image of sigma_k, so the matrix is assembled column by column.
for n in range(1, 7):
    m = n + 1
    d2 = matrix(ZZ, m, m, 0)
    for k in range(m):
        if k == 0:
            d2[0, 0] = 1
        else:
            d2[k, k] = 2
            d2[k - 1, k] = -1
    check(f"2.1-6 collapsed complex, n={n}",
          {1: matrix(ZZ, 1, m, 0), 2: d2},
          ["Z", f"C{2 ** n}", "0"])

# --- Exercise 2.1-9: X = Delta^n with all k-faces identified, so C_k = Z and d_k
# has the single entry sum_{i=0..k} (-1)^i, which is 1 for k even and 0 for k odd.
for n in range(1, 9):
    data = {}
    for k in range(1, n + 1):
        data[k] = matrix(ZZ, 1, 1, [1 if k % 2 == 0 else 0])
    expected = ["Z"]
    for k in range(1, n + 1):
        if k < n:
            expected.append("0")
        else:
            expected.append("Z" if n % 2 == 1 else "0")
    check(f"2.1-9 collapsed simplex, n={n}", data, expected)

# --- Exercise 2.2-11: the cube with quarter twists.  Card E-HAT-1.2-14 gives
# pi_1 = <i, j, k | i = jk, j = ki, k = ij>, so H_1 is the cokernel of the
# abelianized relation matrix, presented as d_1 : C_1 = Z^3 -> C_0 = Z^3.
rel = matrix(ZZ, 3, 3, [-1, 1, 1,
                         1, -1, 1,
                         1, 1, -1])
check("2.2-11 cube complex abelianization", {1: rel}, ["C2 x C2", "0"])

# --- Exercise 2.2-19: RP^n / RP^m has one cell in each degree m+1, ..., n, with
# d_{m+1} = 0 and d_i = 2 for even i > m+1, 0 for odd i.  The card's case table
# predicts H_n = Z for n odd and 0 for n even (n > m+1); H_i = Z/2 for
# m+1 < i < n with i odd and 0 for i even; H_{m+1} = Z for m+1 even and Z/2 for
# m+1 odd; and H_0 = Z.
for m in range(0, 5):
    for n in range(m + 1, 9):
        # rank of C_k: one 0-cell, no cells in degrees 1..m, one cell in m+1..n
        rank = [0] * (n + 1)
        rank[0] = 1
        for k in range(m + 1, n + 1):
            rank[k] = 1
        data = {1: matrix(ZZ, rank[0], rank[1], [0] * (rank[0] * rank[1]))}
        for k in range(2, n + 1):
            if k <= m:
                data[k] = matrix(ZZ, rank[k - 1], rank[k], [0] * (rank[k - 1] * rank[k]))
            else:
                coeff = 0
                if k > m + 1:
                    coeff = 2 if k % 2 == 0 else 0
                data[k] = matrix(ZZ, rank[k - 1], rank[k], [coeff] if rank[k - 1] * rank[k] == 1 else [])
        expected = []
        for k in range(n + 1):
            if k == 0:
                expected.append("Z")
            elif k <= m:
                expected.append("0")
            elif n == m + 1:
                expected.append("Z" if k == n else "0")
            elif k == n:
                expected.append("Z" if n % 2 == 1 else "0")
            elif k == m + 1:
                expected.append("Z" if (m + 1) % 2 == 0 else "C2")
            else:
                expected.append("C2" if k % 2 == 1 else "0")
        check(f"2.2-19 RP^{n}/RP^{m}", data, expected)

# --- Exercise 2.3-1, the Moore pair (X, A) = (S^1 ∪_m e^2, S^1).  The cellular
# complex of X has one cell in dimensions 0, 1, 2 with d_1 = 0 and d_2 = m, so
# H_0 = Z, H_1 = Z/m and H_2 = 0.  This is the group data on which the exactness
# failures certified in proofs/cards/MooreSpaceExactness.lean turn: T_1(X) = Z/m
# is nontrivial while T_1(A) and T_1(X,A) = coker(Z --m--> Z) restricted to the
# torsion of Z vanish, and MT_1(A) = Z is not hit by multiplication by m.
for m in [2, 3, 4, 5, 6, 12]:
    check(f"2.3-1 Moore space M(Z/{m},1)",
          {1: matrix(ZZ, 1, 1, [0]), 2: matrix(ZZ, 1, 1, [m])},
          ["Z", "C%d" % m, "0"])

# The same map d_2 = m as a linear map Z -> Z: its Smith form is (m), so it is
# injective with cokernel Z/m of order m, which is what makes the mod-torsion
# sequence Z --m--> Z -> 0 fail exactness for m > 1.
for m in [2, 3, 4, 5, 6, 12]:
    D = matrix(ZZ, 1, 1, [m]).smith_form()[0]
    ok = D[0, 0] == m and m > 1
    print(f"2.3-1 Smith form of (x{m}) on Z: diag({D[0, 0]})  {'OK' if ok else 'MISMATCH'}")
    if not ok:
        failures.append(f"2.3-1 smith m={m}")

print()
if failures:
    print("MISMATCHES:", failures)
    raise SystemExit(1)
print("all certificates pass")
