---
schema: qual/card@1
id: P-EN5JE
kind: problem
title: $|HK| = |H||K|/|H \cap K|$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Let $H, K \leq G$ a finite group, and without using the normalizers of $H$ or $K$, show that $\abs{HK} = \abs{H} \abs{K}/\abs{H\intersect K}$.
:::

::: {.solution}
<1>1. Consider the map $\phi: H \times K \to HK$ given by $\phi(h, k) = hk$.
::: {.proof}
definition.
:::

<1>2. $\phi$ is surjective.
::: {.proof}
every element of $HK$ is of the form $hk$ with $h \in H$, $k \in K$.
:::

<1>3. The fibers of $\phi$ all have size $|H \cap K|$.
<2>1. $\phi(h_1, k_1) = \phi(h_2, k_2)$ iff $h_1 k_1 = h_2 k_2$ iff $h_2^{-1} h_1 = k_2 k_1^{-1} \in H \cap K$.
::: {.proof}
rearrange the equation.
:::
<2>2. Hence the fiber over $hk$ is $\{(hx, x^{-1}k) : x \in H \cap K\}$, which has $|H \cap K|$ elements.
::: {.proof}
<2>1.
:::

<1>4. Therefore $|H \times K| = |HK| \cdot |H \cap K|$, i.e. $|H||K| = |HK| \cdot |H \cap K|$.
::: {.proof}
<1>2 and <1>3 (counting the domain by fibers).
:::

<1>5. Hence $|HK| = |H||K|/|H \cap K|$.
::: {.proof}
<1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
