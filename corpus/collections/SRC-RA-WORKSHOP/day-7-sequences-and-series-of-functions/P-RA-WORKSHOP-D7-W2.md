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
To clarify Remark 6.6: A family of functions $\mathcal F\subset C(K,\mathbb R^m)$ mapping a set $K\subset\mathbb R^n$ into $\mathbb R^m$ is pointwise equicontinuous on $K$ provided for every $x\in K$ and $\epsilon>0$ there exists some $\delta>0$ (which may depend on $x$) such that $\|f(x)-f(y)\|<\epsilon$ for all $f\in\mathcal F$ and $y\in K$ with $\|x-y\|<\delta$.
The family $\mathcal F$ is uniformly equicontinuous if for every $\epsilon>0$ there exists some $\delta>0$ such that $\|f(x)-f(y)\|<\epsilon$ for all $f\in\mathcal F$ and $x,y\in K$ with $\|x-y\|<\delta$.
Prove that these definitions are equivalent when $K$ is compact.
:::

::: {.solution}
<1>1. Uniform equicontinuity implies pointwise equicontinuity.

::: {.proof}
Fix $x\in K$ and $\varepsilon>0$. A radius $\delta>0$ satisfying the uniform condition works in particular for every $y\in K$ within $\delta$ of this fixed $x$, uniformly over $f\in\mathcal F$.
:::

<1>2. If $K$ is compact, pointwise equicontinuity implies uniform equicontinuity.

<2>1. For each $\varepsilon>0$ and each $z\in K$, there exists $r_z>0$ such that
\[
\|f(z)-f(w)\|<\varepsilon/2
\quad\text{for all }f\in\mathcal F\text{ and }w\in K\text{ with }\|z-w\|<r_z.
\]

::: {.proof}
Apply pointwise equicontinuity at $z$ with tolerance $\varepsilon/2$.
:::

<2>2. If $K\ne\varnothing$, there exist $z_1,\ldots,z_N\in K$ such that
\[
K\subseteq\bigcup_{i=1}^N B(z_i,r_{z_i}/2).
\]

::: {.proof}
The balls $B(z,r_z/2)$ for $z\in K$ form an open cover of $K$. Compactness supplies a finite subcover. If $K$ is empty, uniform equicontinuity is vacuous.
:::

<2>3. For $K\ne\varnothing$, the number $\delta:=\min_{1\le i\le N}r_{z_i}/2>0$ satisfies the uniform equicontinuity condition for tolerance $\varepsilon$.

::: {.proof}
Fix $x,y\in K$ with $\|x-y\|<\delta$. By step <2>2, choose $i$ such that $\|x-z_i\|<r_{z_i}/2$. Then
\[
\|y-z_i\|\leq\|y-x\|+\|x-z_i\|
<\delta+r_{z_i}/2\leq r_{z_i}.
\]
Step <2>1 applied at $z_i$ gives $\|f(x)-f(z_i)\|<\varepsilon/2$ and $\|f(y)-f(z_i)\|<\varepsilon/2$ for every $f\in\mathcal F$. The triangle inequality gives $\|f(x)-f(y)\|<\varepsilon$. The radius $\delta$ depends only on $\varepsilon$, not on $x,y$ or $f$.
:::

<2>4. Q.E.D.

::: {.proof}
Steps <2>2 and <2>3 prove uniform equicontinuity for nonempty $K$, and the empty case is immediate.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 establish both implications.
:::
:::
