---
schema: qual/card@1
id: P-CAFA23A
kind: problem
title: "Partial sums of geometric series converge to (1-z)^{-1}"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G_N(z) = \sum_{n=0}^{N} z^n$ and $G(z) = (1-z)^{-1}$.

(a) Carefully prove that $G_N \to G$ as $N \to \infty$, uniformly on compact subsets of $\mathbb{D}$.

(b) What is the power series expansion of $G(z)$ at $z = 2023$, and what is its radius of convergence?
:::

::: solution
(a) For $z\ne1$,
\[
G_N(z)=\frac{1-z^{N+1}}{1-z},
\]
so
\[
G_N(z)-G(z)=-\frac{z^{N+1}}{1-z}.
\]
If $K\Subset\mathbb D$, choose $r<1$ with $|z|\le r$ on $K$. Also
$\delta=\min_{z\in K}|1-z|>0$. Hence
\[
\sup_{z\in K}|G_N(z)-G(z)|
\le \frac{r^{N+1}}{\delta}\longrightarrow0.
\]
Thus $G_N\to G$ uniformly on compact subsets of $\mathbb D$.

(b) Put $w=z-2023$. Then
\[
G(z)=\frac1{1-z}
=-\frac1{2022+w}
=-\frac1{2022}\frac1{1+w/2022}.
\]
Therefore
\[
\boxed{
G(z)=\sum_{n=0}^\infty
\frac{(-1)^{n+1}}{2022^{n+1}}(z-2023)^n
}
\]
for $|z-2023|<2022$. The radius is
\[
\boxed{2022},
\]
the distance from the center $2023$ to the unique singularity $z=1$.
:::
