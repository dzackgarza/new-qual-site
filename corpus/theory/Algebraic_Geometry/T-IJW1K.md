---
schema: qual/card@1
id: T-IJW1K
kind: theorem
title: The cohomology of $\OO_{\PP^n}(d)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Twisting Sheaves
  - Serre Duality
relations:
- kind: uses
  target: D-CB9XS
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- Compute $H^*(\PP^n, \OO(d))$.
- What is $H^0(\PP^1, \Omega^1)$?
---

::: {.theorem}
Let $A$ be a ring, $S = A[x_0,\ldots,x_n]$ and $\PP^n = \PP^n_A$.
Then

- $H^0(\PP^n, \OO(d)) = S_d$, a free $A$-module of rank $\binom{n+d}{n}$ for $d \geq 0$, and $0$ for $d < 0$;

- $H^n(\PP^n, \OO(d))$ is the free $A$-module on the monomials $x_0^{a_0} \cdots x_n^{a_n}$ with every $a_i \leq -1$ and $\sum_i a_i = d$, of rank $\binom{-d-1}{n}$, nonzero exactly for $d \leq -n-1$, and dual to $S_{-d-n-1}$;

- $H^p(\PP^n, \OO(d)) = 0$ for $0 < p < n$ and for $p > n$, for every $d$.

[@Har10a, Theorem III.5.1]
:::

::: {.remark}
This one computation carries the subject.
The top and bottom are exchanged by Serre duality with dualizing sheaf $\omega = \OO(-n-1)$, which is why the answer is stated as a dual rather than as another binomial.

Three corollaries used constantly:

- $H^1(\PP^n, \OO(d)) = 0$ for $n \geq 2$, so the only interesting $H^1$ on projective space is for curves;

- on $\PP^1$: $h^0(\OO(d)) = d+1$ and $h^1(\OO(d)) = h^0(\OO(-d-2))$, so $h^1(\OO(-2)) = 1$;

- $H^0(\PP^1, \Omega^1) = H^0(\PP^1, \OO(-2)) = 0$: the projective line has no global holomorphic differentials, which is the genus of $\PP^1$ being zero.
:::
