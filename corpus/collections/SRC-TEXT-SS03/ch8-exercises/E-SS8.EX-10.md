---
schema: qual/card@1
id: E-SS8.EX-10
kind: problem
title: A Schwarz-type bound on the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
10. Let $F : \halfplane \to \CC$ be a holomorphic function that satisfies

$$
\abs{ F (z) } \leq 1 \quad \text { and } \quad F (i) = 0.
$$

Figure 11. Successive conformal maps in Exercise 8

Prove that

$$
\abs{ F (z) } \leq \abs{ \frac {z - i}{z + i} } \quad \text {   for   all   } z \in \halfplane.
$$
:::

::: {.solution}
Let
$$
\phi(z)=\frac{z-i}{z+i}.
$$
This maps the upper half-plane biholomorphically onto the unit disc and satisfies $\phi(i)=0$. Define
$$
g(w)=F(\phi^{-1}(w)),\qquad w\in\DD.
$$
Then $g$ is holomorphic on $\DD$, $\abs{g(w)}\le1$, and $g(0)=F(i)=0$. By Schwarz's lemma,
$$
\abs{g(w)}\le\abs{w}.
$$
Taking $w=\phi(z)$ gives
$$
\abs{F(z)}\le\abs{\frac{z-i}{z+i}},
\qquad z\in\halfplane.
$$
:::
