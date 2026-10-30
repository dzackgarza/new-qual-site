---
schema: qual/card@1
id: P-CASP07C
kind: problem
title: Convergence of the series of derivatives of an analytic function
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The card printed the series sum of f^(n)(z) without the factor 1/n!, which diverges
    for f(z)=1/(3-z); the statement now asks about the series sum of f^(n)(z)/n!.
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The exam (PDF page 2) prints the series sum of f^(n)(z) without 1/n!; that series
    diverges in general, so the card keeps the 1/n! correction.
---

::: {.problem}
Let $f(z)$ be analytic in the disk $B(0, 2)$.
Show that there is a function $g(z)$, analytic in the unit disk $\DD$, such that the series $\sum_{n=1}^{\infty} \frac{f^{(n)}(z)}{n!}$ converges to $g$ in $\mathcal{O}(\DD)$.
:::

::: {.solution}
We show that the series converges in $\mathcal O(\DD)$ to
$$
\boxed{g(z)=f(z+1)-f(z)}.
$$
For $z\in\DD$, the point $z+1$ lies in $B(0,2)$, so $g$ is analytic on $\DD$.

Let $K\Subset\DD$, and choose $r<1$ with $\abs{z}\le r$ on $K$. Fix $\rho$ with
$1<\rho<2-r$. For every $z\in K$, the closed disk of radius $\rho$ centered at
$z$ lies in the compact disk $\overline{B(0,r+\rho)}\subset B(0,2)$. Let
$$
M=\max_{\abs{w}\le r+\rho}\abs{f(w)}.
$$
Cauchy's estimates on the circle $\abs{w-z}=\rho$ give
$$
\abs{{f^{(n)}(z)\over n!}}\le M\rho^{-n}
\qquad(z\in K,\ n\ge0).
$$
Since $\rho>1$, the Weierstrass M-test shows that the series converges
uniformly on $K$. Since $\abs{1}<\rho$, Taylor's theorem at $z$, evaluated at
$z+1$, gives
$$
f(z+1)=\sum_{n=0}^\infty {f^{(n)}(z)\over n!},
$$
so the sum from $n=1$ equals $f(z+1)-f(z)=g(z)$. Uniform convergence on every
compact subset of $\DD$ is convergence in $\mathcal O(\DD)$.
:::
