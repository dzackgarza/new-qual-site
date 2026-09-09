---
schema: qual/card@1
id: P-HL46I
kind: problem
title: Ring of integers and integrality over $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Number Theory
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is a ring of integers?
What does “integral over $\ZZ$” mean?
:::


::: {.solution}
Let $K$ be a number field, i.e. a finite extension of $\QQ$.

An element $\alpha\in K$ is **integral over $\ZZ$** if it satisfies a monic polynomial
\[
\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_0=0
\]
with coefficients $a_i\in\ZZ$.

The **ring of integers** of $K$ is
\[
\mathcal O_K
=
\{\alpha\in K:\alpha\text{ is integral over }\ZZ\}.
\]

<1>1. The set $\mathcal O_K$ is a subring of $K$ containing $\ZZ$.
::: {.proof}
The elements integral over a ring form a subring of any overring: sums, differences, and products of integral elements are integral. Every integer $m$ is integral because it is a root of the monic polynomial $x-m$.
:::

<1>2. For $K=\QQ$, one has
\[
\mathcal O_{\QQ}=\ZZ.
\]
::: {.proof}
Let $a/b\in\QQ$ be in lowest terms and integral over $\ZZ$. If it satisfies a monic polynomial with integer coefficients, multiplying by $b^n$ shows that $b\mid a^n$. Coprimality forces $b=1$, so the rational number is an integer.
:::

Thus $\mathcal O_K$ is the integral closure of $\ZZ$ in the number field $K$.
:::
