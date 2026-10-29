---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W2
kind: problem
title: Pointwise and uniform equicontinuity on a compact set
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Compactness
  - Uniform Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
A family of functions $\mathcal F\subset C(K,\RR^m)$ mapping a set $K\subset\RR^n$ into $\RR^m$ is pointwise equicontinuous on $K$ provided for every $x\in K$ and $\varepsilon>0$ there exists some $\delta>0$ (which may depend on $x$) such that $\norm{f(x)-f(y)}<\varepsilon$ for all $f\in\mathcal F$ and $y\in K$ with $\norm{x-y}<\delta$.
The family $\mathcal F$ is uniformly equicontinuous if for every $\varepsilon>0$ there exists some $\delta>0$ such that $\norm{f(x)-f(y)}<\varepsilon$ for all $f\in\mathcal F$ and $x,y\in K$ with $\norm{x-y}<\delta$.
Prove that these definitions are equivalent when $K$ is compact.
:::

::: {.solution}

::: pf

::: pf-step

Uniform equicontinuity implies pointwise equicontinuity.

::: pf-proof

Fix $x\in K$ and $\varepsilon>0$. A radius $\delta>0$ satisfying the uniform condition works in particular for every $y\in K$ within $\delta$ of this fixed $x$, uniformly over $f\in\mathcal F$.

:::

:::

::: pf-step

If $K$ is compact, pointwise equicontinuity implies uniform equicontinuity.

::: pf-proof

If $K$ is empty, uniform equicontinuity is vacuous, so assume $K\ne\varnothing$ and fix $\varepsilon>0$.

::: {.pf-step #s2-1}

For each $z\in K$, there exists $r_z>0$ such that
$$
\norm{f(z)-f(w)}<\varepsilon/2
\quad\text{for all }f\in\mathcal F\text{ and }w\in K\text{ with }\norm{z-w}<r_z.
$$

::: pf-proof

This is pointwise equicontinuity at $z$ with tolerance $\varepsilon/2$.

:::

:::

::: {.pf-step #s2-2}

There exist $z_1,\ldots,z_N\in K$ such that
$$
K\subseteq\bigcup_{i=1}^N B(z_i,r_{z_i}/2).
$$

::: pf-proof

The balls $B(z,r_z/2)$ for $z\in K$ form an open cover of $K$. Compactness supplies a finite subcover.

:::

:::

::: pf-step

The number $\delta\coloneqq\min_{1\le i\le N}r_{z_i}/2>0$ satisfies the uniform equicontinuity condition for tolerance $\varepsilon$.

::: pf-proof

Fix $x,y\in K$ with $\norm{x-y}<\delta$. By step [](#s2-2){.pf-ref}, there is $i$ with $\norm{x-z_i}<r_{z_i}/2$. Then
$$
\norm{y-z_i}\leq\norm{y-x}+\norm{x-z_i}
<\delta+r_{z_i}/2\leq r_{z_i}.
$$
Step [](#s2-1){.pf-ref} applied at $z_i$ gives $\norm{f(x)-f(z_i)}<\varepsilon/2$ and $\norm{f(y)-f(z_i)}<\varepsilon/2$ for every $f\in\mathcal F$. The triangle inequality gives $\norm{f(x)-f(y)}<\varepsilon$. The radius $\delta$ depends only on $\varepsilon$, not on $x,y$ or $f$.

:::

:::

:::

:::

:::

:::
