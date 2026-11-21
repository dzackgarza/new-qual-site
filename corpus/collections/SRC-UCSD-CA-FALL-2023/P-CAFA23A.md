---
schema: qual/card@1
id: P-CAFA23A
kind: problem
title: 'Partial sums of the geometric series converge to $(1-z)^{-1}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $G_N(z) = \sum_{n=0}^{N} z^n$ and $G(z) = (1-z)^{-1}$.

(a) Carefully prove that $G_N \to G$ as $N \to \infty$, uniformly on compact subsets of $\DD$.

(b) What is the power series expansion of $G(z)$ at $z = 2023$, and what is its radius of convergence?
:::

::: {.solution}

The argument is the card's own; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $G_{N}(z)=\sum_{n=0}^{N}z^{n}$ and $G(z)=(1-z)^{-1}$ on $\DD=\{z:\abs{z}<1\}$.

::: pf

::: {.pf-step #difference}
For $z\ne1$, $G_{N}(z)-G(z)=-\dfrac{z^{N+1}}{1-z}$.

::: pf-proof
$G_{N}(z)=(1-z^{N+1})/(1-z)$ for $z\ne1$, and $G(z)=1/(1-z)$; subtracting gives $\big(1-z^{N+1}-1\big)/(1-z)=-z^{N+1}/(1-z)$.
:::

:::

::: {.pf-step #uniform}
(a) $G_{N}\to G$ uniformly on every compact $K\Subset\DD$.

::: pf-proof
Let $K\subset\DD$ be compact. Then $\abs{z}\le r$ on $K$ for some $r<1$, since $z\mapsto\abs{z}$ is continuous and attains its maximum on $K$, which lies in $\DD$; and $\delta=\min_{z\in K}\abs{1-z}>0$, since $1-z$ never vanishes on $K$ and $\abs{1-z}$ attains its minimum there. By step [](#difference){.pf-ref},
$$
\sup_{z\in K}\abs{G_{N}(z)-G(z)}\le\frac{r^{N+1}}{\delta}\longrightarrow0
$$
as $N\to\infty$, because $0\le r<1$. So the convergence is uniform on $K$.
:::

:::

::: {.pf-step #series}
(b) $G(z)=\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^{n+1}}{2022^{n+1}}(z-2023)^{n}$ for $\abs{z-2023}<2022$, and the radius of convergence is $2022$.

::: pf-proof
Put $w=z-2023$; then $1-z=1-2023-w=-2022-w=-2022\big(1+w/2022\big)$, so
$$
G(z)=-\frac{1}{2022}\cdot\frac{1}{1+w/2022}=-\frac{1}{2022}\sum_{n=0}^{\infty}\left(-\frac{w}{2022}\right)^{n}
=\sum_{n=0}^{\infty}\frac{(-1)^{n+1}}{2022^{n+1}}w^{n},
$$
the geometric series converging for $\abs{w/2022}<1$, that is $\abs{z-2023}<2022$, and diverging for $\abs{w}>2022$ because its terms then do not tend to $0$. The radius is therefore $2022$, which is the distance from the centre $2023$ to the singularity $z=1$ of $G$.
:::

:::

:::
:::
