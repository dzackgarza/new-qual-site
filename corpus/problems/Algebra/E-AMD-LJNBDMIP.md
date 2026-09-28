---
schema: qual/card@1
id: E-AMD-LJNBDMIP
kind: problem
title: A permutation is odd iff it has an odd number of even cycles
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that a permutation is odd iff it has an odd number of even cycles.
:::

::: {.solution}
Write $\sigma\in S_n$ as a product $\sigma=c_1c_2\cdots c_r$ of disjoint cycles of lengths $\ell_1,\dots,\ell_r$, and let $E=\{i:\ell_i\text{ is even}\}$.

<1>1. A cycle of length $\ell\ge1$ has sign $(-1)^{\ell-1}$.

::: {.proof}
For $\ell\ge2$,
$$(a_1\ a_2\ \dots\ a_\ell)=(a_1\ a_\ell)(a_1\ a_{\ell-1})\cdots(a_1\ a_2)$$
is a product of $\ell-1$ transpositions, and $\operatorname{sgn}$ is a homomorphism sending each transposition to $-1$.
For $\ell=1$ the cycle is the identity, of sign $1=(-1)^0$.
:::

<1>2. $\operatorname{sgn}(\sigma)=(-1)^{|E|}$.

::: {.proof}
By step <1>1 and multiplicativity of $\operatorname{sgn}$,
$$\operatorname{sgn}(\sigma)=\prod_{i=1}^r(-1)^{\ell_i-1}=(-1)^{\sum_i(\ell_i-1)}.$$
The integer $\ell_i-1$ is odd exactly when $i\in E$, so $\sum_i(\ell_i-1)\equiv|E|\pmod 2$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, $\sigma$ is odd if and only if $(-1)^{|E|}=-1$, that is, if and only if $|E|$ is odd.
:::
:::
