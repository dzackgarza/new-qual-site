---
schema: qual/card@1
id: P-JHUFA08ANF
kind: problem
title: "Entire functions of polynomial growth are polynomials"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
6) (10 points) Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Prove that if there exists some real number C and some positive integer k so that

$$
| f ( z ) | \leq C | z | ^ { k }
$$

for all z with $| z | > 1$ , then f is a polynomial in z of degree at most $k .$
:::

::: {.solution}
Write $f(z)=\sum_{n\ge0}a_nz^n$, the Taylor series of $f$ at $0$, which converges on $\CC$.

::: pf

::: {.pf-step #s1}

$\abs{a_n}\le CR^{k-n}$ for every $R>1$.

::: pf-proof

Cauchy's estimate on $\abs w=R$ with the hypothesis $\abs{f(w)}\le CR^k$ there.

:::

:::

::: pf-qed

For $n>k$, letting $R\to\infty$ in step [](#s1){.pf-ref} gives $a_n=0$, so $f(z)=\sum_{n=0}^ka_nz^n$ is a polynomial of degree at most $k$.

:::

:::

:::
