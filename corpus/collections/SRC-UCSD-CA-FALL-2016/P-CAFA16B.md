---
schema: qual/card@1
id: P-CAFA16B
kind: problem
title: "Convergence of the series Σ f(z^n) for a self-map of the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Assume that $f: \mathbb{D} \to \mathbb{D}$ is an analytic function such that $f(0) = 0$.
Show that $g(z) = \sum_{n=1}^{\infty} f(z^n)$ converges to an analytic function on $\mathbb{D}$.
:::

::: {.remark}
The official Fall 2016 exam starts the sum at $n=0$. Since $z^0=1$ and $f$ is only defined on the open unit disk, that term is undefined. The intended series necessarily starts at $n=1$.
:::

::: solution
By Schwarz's lemma,
\[
|f(w)|\le |w|\qquad (w\in\mathbb D).
\]
Fix $0<r<1$. For $|z|\le r$,
\[
|f(z^n)|\le |z|^n\le r^n.
\]
Since $\sum_{n\ge1}r^n$ converges, the Weierstrass $M$-test shows that
\[
\sum_{n=1}^\infty f(z^n)
\]
converges uniformly on $|z|\le r$.

Each summand is holomorphic on $\mathbb D$, so the locally uniform limit is holomorphic. As $r<1$ was arbitrary, $g$ is analytic on all of $\mathbb D$.
:::
