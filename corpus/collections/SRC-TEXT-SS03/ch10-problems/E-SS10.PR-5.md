---
schema: qual/card@1
id: E-SS10.PR-5
kind: problem
title: Elliptic discriminant and the Dedekind eta function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Modular Forms
relations: []
review: draft
---

::: {.exercise}
The Weierstrass function satisfies
$$
(\wp')^2=4\wp^3-g_2\wp-g_3,
\qquad g_2=60E_4,\quad g_3=140E_6,
$$
where $E_k$ is the Eisenstein series of order $k$. Define the discriminant of $y^2=4x^3-g_2x-g_3$ by $\Delta=g_2^3-27g_3^2$. Prove that
$$
\Delta(\tau)=(2\pi)^{12}\eta(\tau)^{24}
\qquad(\tau\in\halfplane).
$$
:::

::: {.hint}
$\Delta$ and $\eta^{24}$ satisfy the same transformation laws under $\tau\mapsto\tau+1$ and $\tau\mapsto-1/\tau$. Use the fundamental domain of Chapter 10, Problem 2 and compare behavior at the cusp at infinity.
:::
