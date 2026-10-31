"""
Exact certificates for the simplicial homology computations of Hatcher §2.1
exercises 4, 5 and 6, as the corpus cards state them.

Each certificate builds the integer boundary matrices the card writes down, and
computes the homology of the chain complex of free abelian groups exactly:

    H_k = Z^(dim C_k - rank d_k - rank d_(k+1))  +  torsion of d_(k+1),

the torsion being the elementary divisors > 1 of the next boundary map, which is
what the Smith normal form of that map gives.

Run:  sage proofs/cards/DeltaComplexHomology.sage
"""

def homology(dims, bd):
    """dims[k] = rank of C_k; bd[k] = matrix of d_k : C_k -> C_(k-1)."""
    out = []
    top = len(dims) - 1
    for k in range(top + 1):
        rank_dk = bd[k].rank() if k >= 1 else 0
        if k + 1 <= top:
            d_next = bd[k + 1]
            rank_next = d_next.rank()
            snf = d_next.smith_form()[0]
            torsion = [snf[i][i] for i in range(min(snf.nrows(), snf.ncols()))
                       if snf[i][i] > 1]
        else:
            rank_next, torsion = 0, []
        free = dims[k] - rank_dk - rank_next
        assert free >= 0, (k, free)
        out.append((free, sorted(torsion)))
    return out

def show(name, dims, bd, expect):
    got = homology(dims, bd)
    ok = got == expect
    print(f"{name}: {got}  {'OK' if ok else 'MISMATCH, expected ' + str(expect)}")
    return ok

results = []

# --- Exercise 4: the triangular parachute, C2 = Z<sigma>, C1 = Z<a,b,c>, C0 = Z<v>,
# d1 = 0 and d2(sigma) = a - b + c.
d2 = matrix(ZZ, 3, 1, [1, -1, 1])
results.append(show("2.1-4 parachute", [1, 3, 1],
                    {1: matrix(ZZ, 0, 3, []), 2: d2},
                    [(1, []), (2, []), (0, [])]))

# --- Exercise 5: the Klein bottle as two triangles U, L with dU = a + b - c and
# dL = a - b - c.
d2k = matrix(ZZ, 3, 2, [1, 1, 1, -1, -1, -1])
results.append(show("2.1-5 Klein bottle", [1, 3, 2],
                    {1: matrix(ZZ, 0, 3, []), 2: d2k},
                    [(1, []), (1, [2]), (0, [])]))

# --- Exercise 6: n + 1 triangles with all vertices identified, d(sigma_0) = e_0 and
# d(sigma_i) = 2 e_i - e_(i-1) for i > 0.  Claimed H_1 = Z/2^n.
for n in range(1, 7):
    m = n + 1
    cols = []
    for j in range(m):
        col = [0] * m
        if j == 0:
            col[0] = 1
        else:
            col[j] = 2
            col[j - 1] = -1
        cols.append(col)
    d2n = matrix(ZZ, m, m, [cols[j][i] for j in range(m) for i in range(m)])
    results.append(show(f"2.1-6 collapsed complex, n={n}", [1, m, m],
                        {1: matrix(ZZ, 0, m, []), 2: d2n},
                        [(1, []), (0, [2 ** n]), (0, [])]))

# --- Exercise 9: X = Delta^n with all faces of a given dimension identified, so
# C_k = Z and d_k has the single entry sum_{i=0..k} (-1)^i, which is 1 for k even
# and 0 for k odd.  Claimed: H_0 = Z, H_k = 0 for 0 < k < n, and H_n = Z for n odd,
# 0 for n even.
for n in range(1, 9):
    dims = [1] * (n + 1)
    bd = {}
    for k in range(1, n + 1):
        coeff = 1 if k % 2 == 0 else 0
        bd[k] = matrix(ZZ, 1, 1, [coeff])
    expect = [(1, [])]
    for k in range(1, n + 1):
        if k < n:
            expect.append((0, []))
        else:
            expect.append((1, []) if n % 2 == 1 else (0, []))
    results.append(show(f"2.1-9 collapsed simplex, n={n}", dims, bd, expect))

print()

# --- Exercise 2.2-19: RP^n / RP^m.  One cell in each degree m+1, ..., n, with
# d_{m+1} = 0 and, for i > m+1, d_i = 2 for i even and 0 for i odd.  The card
# predicts: H_n = Z for n odd and 0 for n even (when n > m+1); H_i = Z/2 for
# m+1 < i < n with i odd and 0 for i even; H_{m+1} = Z for m+1 even and Z/2 for
# m+1 odd; and H_0 = Z.
def rp_quotient(m, n):
    dims = [1 if m + 1 <= i <= n else 0 for i in range(n + 1)]
    dims[0] = 1
    bd = {}
    for i in range(1, n + 1):
        k = 0
        if i > m + 1:
            k = 2 if i % 2 == 0 else 0
        rows, cols = dims[i - 1], dims[i]
        bd[i] = matrix(ZZ, rows, cols, [k] if rows * cols == 1 else [])
    return dims, bd

for m in range(0, 5):
    for n in range(m + 1, 9):
        dims, bd = rp_quotient(m, n)
        got = homology(dims, bd)
        expect = []
        for i in range(n + 1):
            if i == 0:
                expect.append((1, []))
            elif i <= m:
                expect.append((0, []))
            elif n == m + 1:
                expect.append((1, []) if i == n else (0, []))
            elif i == n:
                expect.append((1, []) if n % 2 == 1 else (0, []))
            elif i == m + 1:
                expect.append((1, []) if (m + 1) % 2 == 0 else (0, [2]))
            else:
                expect.append((0, [2]) if i % 2 == 1 else (0, []))
        results.append(show(f"2.2-19 RP^{n}/RP^{m}", dims, bd, expect))

print()

# --- Exercise 2.2-11: the cube with quarter twists.  Card 1.2-14 gives
# pi_1 = <i, j, k | i = jk, j = ki, k = ij>, and H_1 of a path-connected space is
# the abelianization of pi_1.  Abelianizing gives the relation matrix below; its
# Smith normal form gives the abelian invariants.
rel = matrix(ZZ, 3, 3, [-1, 1, 1,
                         1, -1, 1,
                         1, 1, -1])
snf = rel.smith_form()[0]
diag = [snf[i][i] for i in range(3)]
invariants = [d for d in diag if d > 1]
free_rank = sum(1 for d in diag if d == 0)
ok = (free_rank, invariants) == (0, [2, 2])
print(f"2.2-11 cube: Smith form {diag} -> Z^{free_rank} + {['Z/%d' % d for d in invariants]}  "
      f"{'OK' if ok else 'MISMATCH, expected Z/2 + Z/2'}")
results.append(ok)

print()

print("all certificates pass" if all(results) else "CERTIFICATE FAILURE")
assert all(results)
