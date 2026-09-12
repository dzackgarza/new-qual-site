---
schema: qual/card@1
id: E-SS8.EX-10
kind: problem
title: "SS 8.10: A Schwarz-type bound on the upper half-plane"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
10. Let $F : \mathbb { H }  \mathbb { C }$ be a holomorphic function that satisfies

$$
| F (z) | \leq 1 \quad \text { and } \quad F (i) = 0.
$$

Figure 11. Successive conformal maps in Exercise 8

Prove that

$$
| F (z) | \leq \left| \frac {z - i}{z + i} \right| \quad \text {   for   all   } z \in \mathbb {H}.
$$
:::

::: solution
Let
\[
\phi(z)=\frac{z-i}{z+i}.
\]
This maps the upper half-plane biholomorphically onto the unit disc and satisfies $\phi(i)=0$. Define
\[
g(w)=F(\phi^{-1}(w)),\qquad w\in\mathbb D.
\]
Then $g$ is holomorphic on $\mathbb D$, $|g(w)|\le1$, and $g(0)=F(i)=0$. By Schwarz's lemma,
\[
|g(w)|\le|w|.
\]
Taking $w=\phi(z)$ gives
\[
|F(z)|\le\left|\frac{z-i}{z+i}\right|,
\qquad z\in\mathbb H.
\]
:::
