---
schema: qual/card@1
id: E-NVCIF
kind: problem
title: An entire function $h$ with $\frac{\pi^2}{\sin^2(\pi z)}=\sum_{k\in\ZZ}\frac{1}{(z-k)^2}+h(z)$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Principal Parts
  - Removable Singularities
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Show that there is an entire function $h$ such that
$$
\frac{\pi^2}{\sin^2(\pi z)} = \sum_{k\in \ZZ} \frac{1}{(z-k)^2} + h(z).
$$
:::

::: {.concept}
The principal part of $f$ at an isolated singularity $z_0$ is $\sum_{k<0} c_k (z-z_0)^k$, where $f(z) = \sum_{k\in \ZZ} c_k (z-z_0)^k$ is the Laurent expansion of $f$ near $z_0$.
Subtracting a function with the same principal part at $z_0$ leaves a removable singularity at $z_0$.
:::

::: {.solution}

Let $f(z) \coloneqq \frac{\pi^2}{\sin^2(\pi z)}$ and $g(z) \coloneqq \sum_{k\in \ZZ} \frac{1}{(z-k)^2}$.

::: pf

::: {.pf-step #g-mero}
The series $g$ converges locally uniformly on $\CC\setminus\ZZ$, $g$ is holomorphic there, and for each $n\in\ZZ$ the function $g(z)-\frac{1}{(z-n)^2}$ is holomorphic near $n$.

::: pf-proof
Fix $R>0$.
For $\abs{z}\leq R$ and $\abs{k}\geq 2R$, $\abs{z-k}\geq \abs{k}/2$, so $\abs{(z-k)^{-2}}\leq 4/k^2$, which is summable.
By the Weierstrass $M$-test, the series with the finitely many terms $\abs{k}<2R$ removed converges uniformly on $\abs{z}\leq R$ to a holomorphic function.
The remaining terms are holomorphic on $\abs{z}\leq R$ away from $\ZZ$, and the only one singular at $n$ is $\frac{1}{(z-n)^2}$.
:::

:::

::: {.pf-step #f-pp}
For each $n\in\ZZ$ the principal part of $f$ at $n$ is $\frac{1}{(z-n)^2}$.

::: pf-proof
Since $\sin^2(\pi(z+1)) = \sin^2(\pi z)$, $f$ has period $1$, so it suffices to take $n=0$.
Near $0$,
$$
\begin{aligned}
f(z) &= \left(\frac{\pi}{\pi z - \frac{1}{6}(\pi z)^3 + O(z^5)}\right)^2 = \frac{1}{z^2}\left(1 - \frac{\pi^2 z^2}{6} + O(z^4)\right)^{-2} \\
&= \frac{1}{z^2}\left(1 + \frac{\pi^2 z^2}{3} + O(z^4)\right) = \frac{1}{z^2} + \frac{\pi^2}{3} + O(z^2).
\end{aligned}
$$
:::

:::

::: pf-step
$h \coloneqq f - g$ extends to an entire function.

::: pf-proof
$f$ is holomorphic on $\CC\setminus\ZZ$, and so is $g$ by step [](#g-mero){.pf-ref}.
Near $n\in\ZZ$, $h = \left(f - \frac{1}{(z-n)^2}\right) - \left(g - \frac{1}{(z-n)^2}\right)$, which is bounded near $n$ by steps [](#g-mero){.pf-ref} and [](#f-pp){.pf-ref}.
By Riemann's removable singularity theorem, $h$ extends holomorphically over each $n\in\ZZ$.
:::

:::

:::

:::
