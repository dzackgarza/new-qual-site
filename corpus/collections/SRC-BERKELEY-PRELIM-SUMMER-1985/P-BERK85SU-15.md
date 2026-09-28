---
schema: qual/card@1
id: P-BERK85SU-15
kind: problem
title: Boundary-growth spaces of analytic functions are shifted by differentiation
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    If f is in X_k, Cauchy's derivative estimate on the circle of radius
    (1-|z|)/2 gives |f'(z)|=O((1-|z|)^{-k-1}). Conversely, if f' is in
    X_{k+1}, radial integration from 0 gives
    |f(z)-f(0)|<=C/k((1-|z|)^{-k}-1), hence f is in X_k.
---

::: {.problem}
For each $k>0$, let $X_k$ be the set of analytic functions $f$ on the open unit disk $\mathbb D$ such that
\[
\sup_{z\in\mathbb D}(1-|z|)^k|f(z)|<\infty.
\]
Prove that
\[
f\in X_k\quad\Longleftrightarrow\quad f'\in X_{k+1}.
\]
:::

::: {.solution}
<1>1. If $f\in X_k$, then there is a constant $C>0$ such that
$$
\abs{f(w)}
\le
\frac{C}{(1-\abs{w})^k}
$$
for every $w\in\DD$.

::: {.proof}
This is exactly the defining boundedness condition for $X_k$.
:::

<1>2. If $f\in X_k$, then
$$
f'\in X_{k+1}.
$$

::: {.proof}
Fix $z\in\DD$, and set
$$
d=1-\abs{z},
\qquad
r=\frac d2.
$$
If $\abs{w-z}=r$, then
$$
1-\abs{w}
\ge
1-\abs{z}-\abs{w-z}
=
\frac d2.
$$
By step <1>1,
$$
\abs{f(w)}
\le
\frac{2^kC}{d^k}
$$
on that circle. Cauchy's derivative estimate therefore gives
$$
\abs{f'(z)}
\le
\frac1r
\frac{2^kC}{d^k}
=
\frac{2^{k+1}C}{d^{k+1}}.
$$
Thus
$$
(1-\abs{z})^{k+1}\abs{f'(z)}
\le
2^{k+1}C
$$
for every $z\in\DD$, which is precisely $f'\in X_{k+1}$.
:::

<1>3. Conversely, suppose $f'\in X_{k+1}$. Then there is a constant
$C>0$ such that
$$
\abs{f'(w)}
\le
\frac{C}{(1-\abs{w})^{k+1}}
$$
for every $w\in\DD$.

::: {.proof}
This is the defining boundedness condition for $X_{k+1}$ applied to
$f'$.
:::

<1>4. For every $z\in\DD$,
$$
\abs{f(z)-f(0)}
\le
\frac{C}{k}
\left(
\frac1{(1-\abs{z})^k}-1
\right).
$$

::: {.proof}
Let $r=\abs{z}$. Integrating along the radial segment from $0$ to
$z$ and using step <1>3 gives
$$
\begin{aligned}
\abs{f(z)-f(0)}
&\le
\int_0^1
\abs{z}\,\abs{f'(tz)}\,dt\\
&\le
Cr
\int_0^1
\frac{dt}{(1-tr)^{k+1}}\\
&=
C
\int_0^r
\frac{ds}{(1-s)^{k+1}}\\
&=
\frac{C}{k}
\left(
\frac1{(1-r)^k}-1
\right).
\end{aligned}
$$
This is the claimed inequality.
:::

<1>5. If $f'\in X_{k+1}$, then
$$
f\in X_k.
$$

::: {.proof}
By step <1>4,
$$
\begin{aligned}
(1-\abs{z})^k\abs{f(z)}
&\le
(1-\abs{z})^k\abs{f(0)}
+\frac{C}{k}
\left(1-(1-\abs{z})^k\right)\\
&\le
\abs{f(0)}+\frac{C}{k}.
\end{aligned}
$$
The right-hand side is independent of $z$, so the defining
supremum for $X_k$ is finite.
:::

<1>6. Consequently,
$$
\boxed{
f\in X_k
\quad\Longleftrightarrow\quad
f'\in X_{k+1}
}.
$$

::: {.proof}
Step <1>2 proves the forward implication, and step <1>5 proves the
reverse implication.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required equivalence.
:::
:::
