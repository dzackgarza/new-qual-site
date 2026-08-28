---
schema: qual/card@1
id: P-TOPF08E
kind: problem
title: "Mod 2 cohomology ring of CP^m x RP^n and homotopy equivalence criterion"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Projective Spaces
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Calculate the mod $2$ cohomology ring of the space $X(m, n) = \mathbb{CP}^m \times \mathbb{RP}^n$ where $m, n$ are positive integers.
Show that $X(m, n)$ is homotopy equivalent to $X(m', n')$ if and only if $(m, n) = (m', n')$.
:::

::: {.solution}
**Goal.** Compute $H^*(X(m,n);\ZZ_2)$ and show it determines $(m,n)$.

<1>1. $H^*(\CP^m;\ZZ_2) = \ZZ_2[\alpha]/(\alpha^{m+1})$ with $|\alpha| = 2$, and $H^*(\RP^n;\ZZ_2) = \ZZ_2[\beta]/(\beta^{n+1})$ with $|\beta| = 1$.
Proof: standard mod-2 cohomology rings of projective spaces.

<1>2. By the Künneth theorem, $H^*(X(m,n);\ZZ_2) = \ZZ_2[\alpha, \beta]/(\alpha^{m+1}, \beta^{n+1})$.
Proof: the cohomology of a product is the tensor product of the cohomology rings (over a field, the Künneth theorem gives a ring isomorphism).

<1>3. The ring $H^*(X(m,n);\ZZ_2)$ determines $(m,n)$.
<2>1. The total dimension is $\dim H^*(X(m,n);\ZZ_2) = (m+1)(n+1)$.
Proof: the monomials $\alpha^i \beta^j$ with $0 \le i \le m$, $0 \le j \le n$ form a basis.
<2>2. The highest degree in which the ring is nonzero is $2m + n$.
Proof: the top class is $\alpha^m \beta^n$ of degree $2m + n$.
<2>3. The number of generators in degree $1$ is $1$ (namely $\beta$), and the number in degree $2$ is $1$ (namely $\alpha$).
Proof: $\beta$ is the only degree-$1$ generator and $\alpha$ the only degree-$2$ generator.
<2>4. $m$ is determined by the relation $\alpha^{m+1} = 0$ (the smallest power of $\alpha$ that vanishes), and $n$ by $\beta^{n+1} = 0$.
Proof: the nilpotence orders of $\alpha$ and $\beta$ are $m+1$ and $n+1$ respectively.
<2>5. Hence the ring determines $(m,n)$.
Proof: <1>3.4.

<1>4. Hence $X(m,n) \simeq X(m',n')$ iff $(m,n) = (m',n')$.
<2>1. If $(m,n) = (m',n')$, then $X(m,n) = X(m',n')$, so they are homotopy equivalent.
Proof: equality.
<2>2. If $X(m,n) \simeq X(m',n')$, then $H^*(X(m,n);\ZZ_2) \cong H^*(X(m',n');\ZZ_2)$.
Proof: homotopy equivalence induces a cohomology ring isomorphism.
<2>3. Hence $(m,n) = (m',n')$.
Proof: by <1>3.5, the ring determines $(m,n)$.

<1>5. Q.E.D.
Proof: <1>4 is the claim.
:::
