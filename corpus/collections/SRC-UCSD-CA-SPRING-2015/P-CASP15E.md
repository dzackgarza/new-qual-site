---
schema: qual/card@1
id: P-CASP15E
kind: problem
title: Partial fraction expansion of $\pi^2\cos(\pi z)/\sin^2(\pi z)$
classification:
  areas:
  - complex-analysis
  topics:
  - Partial Fractions
  - Meromorphic Functions
  - Periodic Functions
relations: []
review: draft
---

::: {.problem}
Show that
$$
\pi^2\frac{\cos \pi z}{\sin^2 \pi z} = \sum_{n \in \ZZ} \frac{(-1)^n}{(z - n)^2}.
$$
(Hint: Compare singular parts and use periodicity.)
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows the hint, with normal convergence, the principal parts, anti-periodicity and the Liouville step separated.

Let $S(z)=\sum_{n\in\ZZ}\frac{(-1)^{n}}{(z-n)^{2}}$ and $P(z)=\pi^{2}\frac{\cos\pi z}{\sin^{2}\pi z}$.

::: pf

::: {.pf-step #normal}
$S$ converges normally on compact subsets of $\CC\setminus\ZZ$.

::: pf-proof
Let $K$ be compact with $\dist(K,\ZZ)\ge\delta>0$ and $K\subseteq[-N,N]$. For $\abs{z}\le N$ and $\abs{n}>2N$ one has $\abs{z-n}\ge\abs{n}-\abs{z}\ge\abs{n}/2$, so $\abs{\frac{(-1)^{n}}{(z-n)^{2}}}\le4/n^{2}$ there, and $\sum4/n^{2}<\infty$; the finitely many remaining indices are bounded below on $K$ by $\delta^{-2}$. So the series converges uniformly on $K$.
:::

:::

::: {.pf-step #principal}
$P(z)-\frac{(-1)^{n}}{(z-n)^{2}}$ is bounded in a neighbourhood of $z=n$.

::: pf-proof
Write $z=n+h$. Then $\sin\pi z=(-1)^{n}\sin\pi h$ and $\cos\pi z=(-1)^{n}\cos\pi h$, so $P(z)=\pi^{2}\frac{(-1)^{n}\cos\pi h}{\sin^{2}\pi h}$. Since $\cos\pi h=1+O(h^{2})$ and $\sin^{2}\pi h=\pi^{2}h^{2}(1+O(h^{2}))$, we get $P(z)=\frac{(-1)^{n}}{h^{2}}\big(1+O(h^{2})\big)=\frac{(-1)^{n}}{h^{2}}+O(1)$.
:::

:::

::: {.pf-step #entire}
$H=P-S$ extends from $\CC\setminus\ZZ$ to an entire function.

::: pf-proof
Both $P$ and $S$ are holomorphic off $\ZZ$; at $z=n$ the principal part of $P$ is $\frac{(-1)^{n}}{(z-n)^{2}}$ by step [](#principal){.pf-ref}, which is exactly the $n$-th term of $S$, and the remaining terms of $S$ are holomorphic near $n$ by step [](#normal){.pf-ref}. So $H$ is bounded near each $n$, and Riemann's removable singularity theorem extends it across $n$.
:::

:::

::: {.pf-step #periodic}
$P$ and $S$ are anti-periodic with period $1$, so $H(z+1)=-H(z)$.

::: pf-proof
$\cos\pi(z+1)=-\cos\pi z$ and $\sin^{2}\pi(z+1)=\sin^{2}\pi z$, so $P(z+1)=-P(z)$; and $S(z+1)=\sum_{n}\frac{(-1)^{n}}{(z+1-n)^{2}}=\sum_{m}\frac{(-1)^{m+1}}{(z-m)^{2}}=-S(z)$, re-indexing with $m=n-1$.
:::

:::

::: {.pf-step #bounded}
$H$ is bounded on the strip $0\le\operatorname{Re}z\le1$.

::: pf-proof
$H$ is entire, hence continuous and bounded on the compact set $\theset{0\le\operatorname{Re}z\le1,\ \abs{\operatorname{Im}z}\le1}$. For $\abs{\operatorname{Im}z}\ge1$ in that strip, $\abs{\sin^{2}\pi z}\ge\sinh^{2}(\pi\abs{\operatorname{Im}z})/2$ grows exponentially while $\abs{\cos\pi z}\le e^{\pi\abs{\operatorname{Im}z}}$, so $P$ is bounded there; and $\abs{S(z)}\le\sum_{n}\frac{1}{(\abs{\operatorname{Im}z})^{2}}$ for the terms with $\abs{n}\le\abs{z}$, with exponentially small remainder, so $S$ is bounded there too.
:::

:::

::: {.pf-qed}
$H$ is entire and anti-periodic, hence bounded on all of $\CC$ by its bound on the strip of step [](#bounded){.pf-ref}; Liouville makes $H$ constant, and $c=H(z+1)=-H(z)=-c$ forces $c=0$. So $P=S$.
:::

:::

:::
