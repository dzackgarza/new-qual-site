---
schema: qual/card@1
id: P-S06CA
kind: problem
title: Every convergent sequence is Cauchy
classification:
  areas:
  - prelim
  topics:
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
i) State what it means for a sequence $\{a_n\}$ of real numbers to be Cauchy.

ii) Prove that every convergent sequence is Cauchy.
:::


::: solution
<1>1. A sequence $(a_n)$ is Cauchy if for every $\varepsilon>0$ there exists $N\in\mathbb N$ such that
\[
m,n\ge N\implies |a_m-a_n|<\varepsilon.
\]
:::

<1>2. Suppose $a_n\to L$ for some $L\in\mathbb R$, and let $\varepsilon>0$.
:::

<1>3. There exists $N\in\mathbb N$ such that
\[
n\ge N\implies |a_n-L|<\frac\varepsilon2.
\]
::: {.proof}
This is the definition of convergence of $a_n$ to $L$, applied with $\varepsilon/2$.
:::

<1>4. If $m,n\ge N$, then $|a_m-a_n|<\varepsilon$.
::: {.proof}
By the triangle inequality and <1>3,
\[
|a_m-a_n|
\le |a_m-L|+|a_n-L|
<\frac\varepsilon2+\frac\varepsilon2
=\varepsilon.
\]
:::

<1>5. Therefore every convergent real sequence is Cauchy.
::: {.proof}
The condition in <1>4 is exactly the Cauchy condition stated in <1>1.
:::
:::
