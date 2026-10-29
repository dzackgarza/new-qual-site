---
schema: qual/card@1
id: P-HQWC5
kind: problem
title: Finite Blaschke products of degree $n$ take every value $n$ times in the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Argument Principle
  - Zeros
  - Rouché
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source asked to show that f(z) = b has n solutions in |z| < 1 without restricting b; this fails for |b| >= 1, since |f| < 1 on the disk. The statement now assumes |b| < 1 and counts solutions with multiplicity.
---

::: {.problem}
For $k=1,2,\ldots, n$, suppose $\abs{a_k} < 1$ and
$$
f(z) \definedas \qty{z - a_1 \over 1 - \bar a_1 z} \qty{z-a_2 \over 1 - \bar a_2 z} \cdots \qty{z - a_n \over 1 - \bar a_n z}
.$$
Show that for every $b$ with $\abs b<1$, $f(z) = b$ has $n$ solutions in $\abs{z} < 1$, counted with multiplicity.
:::

::: {.solution}
::: pf

::: {.pf-step #holo}
$f$ is holomorphic on a neighborhood of $\abs z\le 1$, and $\abs{f(z)}=1$ for $\abs z=1$.

::: pf-proof
The poles of $f$ are at $1/\bar a_k$ (none when $a_k=0$), all of modulus greater than $1$. For $\abs z=1$ and $\abs a<1$, $\abs{1-\bar a z} = \abs{\bar z - \bar a} = \abs{z-a}$, so each factor has modulus $1$.
:::

:::

::: {.pf-step #zeros}
$f$ has exactly $n$ zeros in $\DD$, counted with multiplicity.

::: pf-proof
The zeros of $f$ are the points $a_1,\ldots,a_n$, all in $\DD$, since each factor vanishes only at its $a_k$.
:::

:::

::: pf-step
For $\abs b<1$, $f(z)=b$ has exactly $n$ solutions in $\DD$, counted with multiplicity.

::: pf-proof
On $\abs z=1$, step [](#holo){.pf-ref} gives $\abs{(f(z)-b)-f(z)} = \abs b<1=\abs{f(z)}$. By Rouché's theorem $f-b$ and $f$ have the same number of zeros in $\DD$, which is $n$ by step [](#zeros){.pf-ref}.
:::

:::

:::

:::
