---
schema: qual/card@1
id: P-HCAO26
kind: problem
title: Invariants encoded by the Hilbert polynomial
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
What invariants are encoded by the Hilbert polynomial?
:::

::: {.solution}
<1>1. Definition of the Hilbert polynomial:
<2>1. Let $S = k[x_0, \ldots, x_n]$ be the standard graded polynomial ring over a field $k$, and let $M = \bigoplus_{d \ge 0} M_d$ be a finitely generated graded $S$-module.
The Hilbert function $h_M(d) = \dim_k(M_d)$ coincides for all sufficiently large $d \gg 0$ with a unique polynomial $P_M(d) \in \mathbb{Q}[d]$, called the **Hilbert polynomial** of $M$.
For a projective subscheme $X \subseteq \mathbb{P}^n$, $P_X(d)$ denotes the Hilbert polynomial of its homogeneous coordinate ring $S(X) = S/I(X)$.
Proof: Hilbert–Serre Theorem on graded modules over polynomial rings.

<1>2. Fundamental geometric and algebraic invariants encoded by $P_X(d)$:
<2>1. **Dimension:**
The degree of the Hilbert polynomial equals the dimension of the projective scheme $X$:
\[
\dim(X) = \deg(P_X(d)) = r.
\]
(Equivalently, the Krull dimension of the coordinate ring $S(X)$ is $\dim(S(X)) = r + 1$).
Proof: Hilbert–Serre theorem relating degree of Hilbert polynomial to dimension.
<2>2. **Degree:**
Writing the Hilbert polynomial in the binomial basis:
\[
P_X(d) = \sum_{i=0}^r a_i \binom{d}{i} = \frac{\deg(X)}{r!} d^r + O(d^{r-1}),
\]
the normalized leading coefficient is the **degree** of the projective variety:
\[
\deg(X) = r! \cdot (\text{leading coefficient of } P_X(d)) = a_r.
\]
Geometrically, $\deg(X)$ is the number of points of intersection of $X$ with a generic linear subspace of complementary dimension $n - r$.
Proof: definition of degree via intersection theory and Hilbert polynomials.
<2>3. **Euler Characteristic and Cohomology:**
For the associated coherent sheaf $\mathcal{F} = \widetilde{M}$ on $\mathbb{P}^n$, the Hilbert polynomial computes the Euler characteristic of Serre twists:
\[
P_M(d) = \chi\left(\mathbb{P}^n, \mathcal{F}(d)\right) = \sum_{i=0}^n (-1)^i \dim_k H^i\left(\mathbb{P}^n, \mathcal{F}(d)\right).
\]
In particular, evaluating at $d = 0$ gives the holomorphic Euler characteristic of the structure sheaf:
\[
P_X(0) = \chi\left(X, \mathcal{O}_X\right) = \sum_{i=0}^r (-1)^i \dim_k H^i(X, \mathcal{O}_X).
\]
Proof: Serre's Theorem on cohomology of coherent sheaves on projective space.
<2>4. **Arithmetic Genus:**
The constant term $P_X(0)$ determines the **arithmetic genus** $p_a(X)$ of the variety:
\[
p_a(X) = (-1)^r \left(P_X(0) - 1\right) = (-1)^r \left(\chi(X, \mathcal{O}_X) - 1\right).
\]
For a smooth projective curve ($r = 1$), $P_X(d) = (\deg X) d + (1 - g)$, so the geometric genus is $g = 1 - P_X(0)$.
Proof: definition of arithmetic genus.
<2>5. **Moduli / Hilbert Scheme Invariant:**
By Grothendieck's theorem, the Hilbert polynomial is invariant in flat families of projective schemes, and closed subschemes of $\mathbb{P}^n$ with a fixed Hilbert polynomial $P(d)$ are parameterized by the projective **Hilbert scheme** $\operatorname{Hilb}^{P(d)}(\mathbb{P}^n)$.
Proof: Grothendieck's construction of Hilbert schemes.

<1>3. Conclusion:
The Hilbert polynomial encodes the dimension, degree, arithmetic genus, Euler characteristic of twists $\chi(\mathcal{O}_X(d))$, and the Hilbert scheme parameterization. Q.E.D.
Proof: <1>1 and <1>2.
:::
