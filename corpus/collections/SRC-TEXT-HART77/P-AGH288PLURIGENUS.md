---
schema: qual/card@1
id: P-AGH288PLURIGENUS
kind: problem
title: Plurigenera and Hodge numbers are birational invariants
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plurigenera
  - Hodge Numbers
  - Birational Invariance
relations: []
review: draft
---

::: {.problem}
Let $X$ be a projective nonsingular variety over $k$.
For any $n > 0$ define the **$n$th plurigenus of $X$** to be
\[
P_n = \dim_k \Gamma(X, \omega_X^{\tensor n})
.\]
Thus in particular $P_1 = p_g$.
Also, for any $q$ with $0 \leq q \leq \dim X$, define an integer
\[
h^{q, 0} = \dim_k \Gamma(X, \Omega^q_{X/k})
\quad\text{where}\quad
\Omega^q_{X/k} = \bigwedge\nolimits^q \Omega_{X/k}
\]
is the sheaf of regular $q\dash$forms on $X$.
In particular, for $q = \dim X$ we recover the geometric genus.
The integers $h^{q,0}$ are called **Hodge numbers**.

Using the method of (8.19), show that $P_n$ and $h^{q,0}$ are birational invariants of $X$: if $X$ and $X'$ are birationally equivalent nonsingular projective varieties, then $P_n(X) = P_n(X')$ and $h^{q,0}(X) = h^{q,0}(X')$.
:::
