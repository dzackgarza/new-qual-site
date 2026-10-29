---
schema: qual/card@1
id: E-DXXL4
kind: problem
title: 'Heine--Cantor theorem: a continuous map on a compact metric space is uniformly
  continuous'
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove the Heine–Cantor Theorem: let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces. If $X$ is compact and $f: X \to Y$ is continuous, then $f$ is uniformly continuous.
:::

::: {.solution}

::: pf

::: pf-step
$f$ is uniformly continuous.

::: pf-proof

::: {.pf-step #finite-cover}
Fix $\varepsilon>0$.
There are $p_1,\ldots,p_N\in X$ and $r_1,\ldots,r_N>0$ such that the balls $B(p_j,r_j/2)$ cover $X$ and $d_X(x,p_j)<r_j$ implies $d_Y(f(x),f(p_j))<\frac\varepsilon2$.

::: pf-proof
By continuity, each $p\in X$ has $r_p>0$ with $d_X(x,p)<r_p\implies d_Y(f(x),f(p))<\frac\varepsilon2$.
The balls $B(p,r_p/2)$ cover $X$, and compactness gives a finite subcover.
:::

:::

::: pf-step
With $\delta\coloneqq\frac12\min_jr_j>0$, $d_X(x,y)<\delta$ implies $d_Y(f(x),f(y))<\varepsilon$.

::: pf-proof
Choose $j$ with $x\in B(p_j,r_j/2)$.
Then $d_X(y,p_j)\le d_X(y,x)+d_X(x,p_j)<\delta+\frac{r_j}2\le r_j$, so by step [](#finite-cover){.pf-ref} both $f(x)$ and $f(y)$ lie within $\frac\varepsilon2$ of $f(p_j)$, and the triangle inequality gives $d_Y(f(x),f(y))<\varepsilon$.
:::

:::

:::

:::

:::

:::
