---
schema: qual/card@1
id: P-ZJF2W
kind: problem
title: When the Galois group of a polynomial is contained in $A_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
If we think of the Galois group of a polynomial as contained in $S_n$, when is it contained in $A_n$?
:::

::: {.solution}
Let $f\in K[x]$ be separable of degree $n$ with $\operatorname{char}K\ne2$, let $L$ be its splitting field, let $G=\Gal(L/K)$ act on the roots $\alpha_1,\ldots,\alpha_n$ of $f$ in $L$, and let
$$
\delta=\prod_{i<j}(\alpha_i-\alpha_j),\qquad \Delta(f)=\delta^2.
$$

::: pf

::: {.pf-step #sign}

For $\sigma\in G$, $\sigma(\delta)=\operatorname{sgn}(\sigma)\delta$, and $\delta\ne0$.

::: pf-proof

$\sigma$ permutes the factors $\alpha_i-\alpha_j$ up to sign, and the number of sign changes is the number of inversions of $\sigma$, whose parity is $\operatorname{sgn}(\sigma)$. The roots are distinct since $f$ is separable, so $\delta\ne0$.

:::

:::

::: pf-step

$G\subseteq A_n$ if and only if $\delta\in K$.

::: pf-proof

Since $\operatorname{char}K\ne2$ and $\delta\ne0$, $-\delta\ne\delta$, so by step [](#sign){.pf-ref} $\sigma$ fixes $\delta$ exactly when $\sigma$ is even. By the Galois correspondence, $\delta\in L^G=K$ exactly when every $\sigma\in G$ fixes it.

:::

:::

::: pf-step

$G\subseteq A_n$ if and only if $\boxed{\Delta(f)\text{ is a square in }K}$.

::: pf-proof

$\Delta(f)=\delta^2$ is fixed by $G$, so it lies in $K$. If $\Delta(f)=c^2$ with $c\in K$, then $\delta=\pm c\in K$; conversely $\delta\in K$ makes $\Delta(f)$ a square in $K$.

:::

:::

:::

:::
