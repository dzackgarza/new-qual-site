---
schema: qual/card@1
id: E-5VQHD
kind: problem
title: Heine–Cantor theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Uniform Continuity
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $f: A\to B$ is a continuous map between metric spaces and $K\subset A$ is compact, then $\restrictionof{f}{K}$ is uniformly continuous.
:::

::: {.solution}
Fix $\varepsilon>0$.

::: pf

::: {.pf-step #radii}

For each $x\in K$ there is $r_x>0$ such that $d_A(z,x)<r_x$ implies $d_B(f(z),f(x))<\varepsilon/2$.

::: pf-proof

This is continuity of $f$ at $x$.

:::

:::

::: {.pf-step #delta}

There are $x_1,\ldots,x_m\in K$ with $K\subseteq\bigcup_{i=1}^m B_A(x_i,r_{x_i}/2)$, and then $\delta=\min_{1\le i\le m}r_{x_i}/2>0$.

::: pf-proof

The balls $B_A(x,r_x/2)$, $x\in K$, cover the compact set $K$, so finitely many of them do. A minimum of finitely many positive numbers is positive.

:::

:::

::: pf-qed

Let $x,y\in K$ with $d_A(x,y)<\delta$. By step [](#delta){.pf-ref}, choose $i$ with $x\in B_A(x_i,r_{x_i}/2)$. Then $d_A(x,x_i)<r_{x_i}/2<r_{x_i}$ and
$$
d_A(y,x_i)\le d_A(y,x)+d_A(x,x_i)<\delta+r_{x_i}/2\le r_{x_i}.
$$
By step [](#radii){.pf-ref}, $d_B(f(x),f(x_i))<\varepsilon/2$ and $d_B(f(y),f(x_i))<\varepsilon/2$, so the triangle inequality gives $d_B(f(x),f(y))<\varepsilon$. Since $\delta$ depends only on $\varepsilon$, $\restrictionof{f}{K}$ is uniformly continuous.

:::

:::

:::
