---
schema: qual/card@1
id: P-PJA4A
kind: problem
title: Unique quadratic subfield of a Galois extension of degree $14$, and two distinct
  degree-$7$ subfields imply a nonabelian Galois group
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Suppose that $F\subset E$ are fields such that $E/F$ is Galois and $\abs{\gal(E/F)} = 14$.

a. Show that there exists a unique intermediate field $K$ with $F\subset K \subset E$ such that $[K: F] = 2$.

b. Assume that there are at least two distinct intermediate subfields $F \subset L_1, L_2 \subset E$ with $[L_i: F]= 7$.
Prove that $\gal(E/F)$ is nonabelian.
:::

::: solution
Let $G=\operatorname{Gal}(E/F)$, so $|G|=14$.

For (a), an intermediate field $K$ with $[K:F]=2$ corresponds under the Galois correspondence to a subgroup $H=\operatorname{Gal}(E/K)$ of order
\[
|H|=[E:K]=\frac{14}{2}=7.
\]
The number $n_7$ of Sylow $7$-subgroups of $G$ satisfies
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid2,
\]
so $n_7=1$. Thus there is a unique subgroup of order $7$, hence a unique such intermediate field $K$.

For (b), an intermediate field $L_i$ with $[L_i:F]=7$ corresponds to a subgroup
\[
H_i=\operatorname{Gal}(E/L_i)
\]
of order $2$. Distinct fields correspond to distinct subgroups, so the hypotheses give two distinct subgroups of order $2$ in $G$. If $G$ were abelian, every Sylow $2$-subgroup would be fixed by conjugation; since Sylow subgroups are all conjugate, there could be only one Sylow $2$-subgroup. This contradicts $H_1\ne H_2$. Therefore $G$ is nonabelian.
:::
