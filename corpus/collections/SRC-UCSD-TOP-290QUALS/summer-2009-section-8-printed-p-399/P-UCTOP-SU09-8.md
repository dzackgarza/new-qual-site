---
schema: qual/card@1
id: P-UCTOP-SU09-8
kind: problem
title: Euler characteristic parity for even-dimensional manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Let $M^{2n}$ be a closed orientable even-dimensional manifold.
Show that its Euler characteristic is odd if and only if the dimension of $H_n(M; \mathbb{Q})$ is odd, and that consequently a closed manifold of dimension $4n + 2$ with odd Euler characteristic must be non-orientable.

::: {.solution}
**Goal.** For a closed orientable $2n$-manifold $M$, relate the parity of $\chi(M)$ to $\dim H_n(M;\QQ)$, and deduce a non-orientability statement in dimension $4n+2$.

<1>1. $\chi(M) = \sum_{i=0}^{2n} (-1)^i b_i$, where $b_i = \dim H_i(M;\QQ)$.
Proof: the Euler characteristic equals the alternating sum of Betti numbers.

<1>2. By Poincaré duality, $b_i = b_{2n-i}$.
Proof: $H_i(M;\QQ) \cong H^{2n-i}(M;\QQ) \cong H_{2n-i}(M;\QQ)$ (orientable closed manifold).

<1>3. Hence $\chi(M) \equiv b_n \pmod 2$.
<2>1. The terms $(-1)^i b_i$ and $(-1)^{2n-i} b_{2n-i}$ are equal (since $b_i = b_{2n-i}$ and $(-1)^i = (-1)^{2n-i}$).
Proof: $2n - i$ and $i$ have the same parity.
<2>2. So all terms cancel in pairs except the middle term $(-1)^n b_n$.
Proof: the sum $\sum_{i=0}^{2n} (-1)^i b_i$ pairs $i$ with $2n-i$; the only unpaired index is $i = n$.
<2>3. Hence $\chi(M) = (-1)^n b_n + 2(\text{integer})$, so $\chi(M) \equiv b_n \pmod 2$.
Proof: the paired terms sum to an even integer.

<1>4. Therefore $\chi(M)$ is odd iff $b_n = \dim H_n(M;\QQ)$ is odd.
Proof: <1>3.3.

<1>5. A closed $4n+2$-manifold with odd $\chi$ is non-orientable.
<2>1. Suppose $M$ is orientable of dimension $4n+2 = 2(2n+1)$.
Proof: assume for contradiction.
<2>2. Then $b_{2n+1}$ is even.
Proof: the intersection form on $H_{2n+1}(M;\QQ)$ is alternating (skew-symmetric) since $2n+1$ is odd, and a nondegenerate alternating form on a vector space forces the dimension to be even.
<2>3. Hence $\chi(M)$ is even.
Proof: by <1>4, $\chi(M) \equiv b_{2n+1} \equiv 0 \pmod 2$.
<2>4. Contradiction with $\chi(M)$ odd.
Proof: <1>5.3 contradicts the hypothesis.

<1>6. Q.E.D.
Proof: <1>4 is the first claim; <1>5 is the consequence.
:::
