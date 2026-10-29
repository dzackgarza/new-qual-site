---
schema: qual/card@1
id: P-SLWIE
kind: problem
title: $\pi^2/\sin^2(\pi z)=\sum_{n\in\mathbb{Z}}(z-n)^{-2}$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
  - Principal Parts
  - Identity Theorem
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Define
$$
\begin{aligned}
f(z) &= {\pi^2 \over \sin^2 \qty{\pi z} } \\
g(z) &= \sum_{n\in \ZZ} {1\over (z-n)^2}
.\end{aligned}
$$

(a) Show that $f$ and $g$ have the same singularities in $\CC$.

(b) Show that $f$ and $g$ have the same singular parts at each of their singularities.

(c) Show that $f, g$ each have period one and approach zero uniformly on $0\leq x \leq 1$ as $\abs{y}\to \infty$.

(d) Conclude that $f = g$.
:::

::: {.hint}
Show that $f-g$ is entire using (a) and (b), and bounded using (c).
:::

::: {.solution title="(a)"}

::: pf

::: pf-step

$f$ is holomorphic on $\CC\setminus\ZZ$ with a pole at each integer.

::: pf-proof

$\sin(\pi z)=0$ exactly when $z\in\ZZ$, and these zeros are simple, so $f$ has a double pole at each integer.

:::

:::

::: pf-step

$g$ is holomorphic on $\CC\setminus\ZZ$ with a pole at each integer.

::: pf-proof

On a compact set $K\subset\CC\setminus\ZZ$ with $\abs z\le A$, we have $\abs{z-n}\ge\abs n-A$, so the terms with $\abs n>2A$ are bounded by $4/n^2$ and the series converges uniformly on $K$. Hence $g$ is holomorphic on $\CC\setminus\ZZ$. Near an integer $m$, $g(z)=(z-m)^{-2}+\sum_{n\ne m}(z-n)^{-2}$, and the second sum is holomorphic near $m$ by the same estimate.

:::

:::

:::

:::

::: {.solution title="(b)"}

::: pf

::: {.pf-step #g-part}

The singular part of $g$ at $m\in\ZZ$ is $(z-m)^{-2}$.

::: pf-proof

This is the decomposition at the end of solution (a).

:::

:::

::: pf-step

The singular part of $f$ at $m\in\ZZ$ is $(z-m)^{-2}$.

::: pf-proof

Since $\sin^2(\pi(z+1))=\sin^2(\pi z)$, it suffices to take $m=0$. From $\sin(\pi z)=\pi z\bigl(1-\frac{\pi^2z^2}6+O(z^4)\bigr)$,
$$
f(z)=\frac{\pi^2}{\pi^2z^2\bigl(1-\frac{\pi^2z^2}3+O(z^4)\bigr)}=\frac1{z^2}+\frac{\pi^2}3+O(z^2).
$$
This agrees with step [](#g-part){.pf-ref}.

:::

:::

:::

:::

::: {.solution title="(c)"}
Write $z=x+iy$ with $0\le x\le1$.

::: pf

::: pf-step

$f$ and $g$ have period one.

::: pf-proof

$\sin(\pi(z+1))=-\sin(\pi z)$, and $g(z+1)=g(z)$ by reindexing the absolutely convergent series.

:::

:::

::: pf-step

$f(z)\to0$ uniformly in $x$ as $\abs y\to\infty$.

::: pf-proof

$\abs{\sin(\pi z)}^2=\sin^2(\pi x)+\sinh^2(\pi y)\ge\sinh^2(\pi y)$, so $\abs{f(z)}\le\pi^2/\sinh^2(\pi y)$.

:::

:::

::: pf-step

$g(z)\to0$ uniformly in $x$ as $\abs y\to\infty$.

::: pf-proof

$\abs{z-n}^2=(x-n)^2+y^2$. For $n\in\{-1,0,1\}$ this is at least $y^2$, and for $\abs n\ge2$ it is at least $(\abs n-1)^2+y^2$. Hence
$$
\abs{g(z)}\le\frac3{y^2}+\sum_{\abs n\ge2}\frac1{(\abs n-1)^2+y^2},
$$
which is independent of $x$ and tends to $0$ by dominated convergence, with dominating sequence $(\abs n-1)^{-2}$.

:::

:::

:::

:::

::: {.solution title="(d)"}
Let $h\coloneqq f-g$.

::: pf

::: {.pf-step #entire}

$h$ extends to an entire function.

::: pf-proof

By parts (a) and (b), $h$ is holomorphic on $\CC\setminus\ZZ$ and its singular part at each integer is $0$, so each integer is a removable singularity.

:::

:::

::: {.pf-step #bounded}

$h$ is bounded on $\CC$ and $h(z)\to0$ as $\abs{\Im z}\to\infty$.

::: pf-proof

By part (c), there is $Y$ with $\abs h\le1$ on $\theset{0\le x\le1,\ \abs y\ge Y}$, and $h$ is bounded on the compact rectangle $\theset{0\le x\le1,\ \abs y\le Y}$ by step [](#entire){.pf-ref}. By periodicity the same bound holds on $\CC$. The limit is part (c).

:::

:::

::: pf-step

$f=g$.

::: pf-proof

By steps [](#entire){.pf-ref} and [](#bounded){.pf-ref} and Liouville's theorem, $h$ is a constant, and the constant is $\lim_{y\to\infty}h(iy)=0$.

:::

:::

:::

:::
