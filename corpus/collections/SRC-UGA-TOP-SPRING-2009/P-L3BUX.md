---
schema: qual/card@1
id: P-L3BUX
kind: problem
title: Isometries of compact metric spaces are bijective
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem I of the official UGA Spring 2009 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Injectivity follows immediately from preservation of distance. For
    surjectivity, if x_0 is outside the compact image f(X), its positive
    distance from f(X) makes the forward orbit x_0,f(x_0),f^2(x_0),... a
    uniformly separated sequence, contradicting sequential compactness.
---

::: {.problem}
Let $(X, d)$ be a compact metric space, and let $f : X \to X$ be an isometry:
\[
\forall~ x, y \in X, \qquad d(f (x), f (y)) = d(x, y).
\]
Prove that $f$ is a bijection.
:::

::: {.solution}
<1>1. The map $f$ is injective.
::: {.proof}
Suppose
\[
f(x)=f(y).
\]
Since $f$ preserves distances,
\[
d(x,y)=d(f(x),f(y))=0.
\]
Because $d$ is a metric, $x=y$.
Thus $f$ is injective.
:::

<1>2. Assume for contradiction that $f$ is not surjective, and choose
\[
x_0\in X\setminus f(X).
\]
Then there is a number $\delta>0$ such that
\[
d(x_0,y)\ge\delta
\]
for every $y\in f(X)$.
::: {.proof}
An isometry is continuous, so $f(X)$ is compact as the continuous image of the compact space $X$.

The function
\[
y\longmapsto d(x_0,y)
\]
is continuous on the compact set $f(X)$, hence attains its minimum there.
Since $x_0\notin f(X)$, this minimum cannot be $0$.
Therefore
\[
\delta:=\min_{y\in f(X)}d(x_0,y)>0.
\]
:::

<1>3. Define
\[
x_n=f^n(x_0)
\qquad(n\ge0).
\]
Then for every pair $n>m\ge0$,
\[
d(x_n,x_m)\ge\delta.
\]
::: {.proof}
Because $f$ is an isometry, every iterate $f^m$ is an isometry.
Hence, for $n>m$,
\[
d(x_n,x_m)
=
d(f^n(x_0),f^m(x_0))
=
d(f^{n-m}(x_0),x_0).
\]
Since $n-m\ge1$,
\[
f^{n-m}(x_0)=f(f^{n-m-1}(x_0))\in f(X).
\]
By the definition of $\delta$ in <1>2,
\[
d(f^{n-m}(x_0),x_0)\ge\delta.
\]
Thus $d(x_n,x_m)\ge\delta$.
:::

<1>4. The conclusion of <1>3 contradicts compactness of $X$.
::: {.proof}
Every sequence in a compact metric space has a convergent subsequence.
Thus the sequence $(x_n)_{n\ge0}$ has a convergent subsequence
\[
x_{n_k}\longrightarrow x\in X.
\]
Every convergent sequence is Cauchy, so for sufficiently large $k<\ell$ one must have
\[
d(x_{n_k},x_{n_\ell})<\delta.
\]
This contradicts <1>3, which gives
\[
d(x_{n_k},x_{n_\ell})\ge\delta.
\]
Therefore $f$ must be surjective.
:::

Combining <1>1 and <1>4,
\[
\boxed{f\text{ is bijective}.}
\]
:::
