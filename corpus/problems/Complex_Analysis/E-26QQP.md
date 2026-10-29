---
schema: qual/card@1
id: E-26QQP
kind: problem
title: $\sum_{k\in\ZZ}\frac{(-1)^k}{(k+a)^2}=\pi^2\cos(\pi a)\csc^2(\pi a)$
  for $a\in\RR\setminus\ZZ$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Meromorphic Functions
  - Series of Numbers
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that
$$
\sum_{k\in \ZZ} { (-1)^k \over (k+a)^2} = \pi^2 \cos(\pi a)\csc^2(\pi a) \quad \text{for } a\in \RR\setminus\ZZ.
$$
:::

::: {.solution}
Fix $a\in\RR\setminus\ZZ$, let
$$
F(z)=\frac{\pi\csc(\pi z)}{(z+a)^2},
$$
and let $\Gamma_N$ be the positively oriented square with vertices $(N+\tfrac12)(\pm1\pm i)$, for integers $N>\abs{a}$.

::: pf

::: {.pf-step #vanish}

$\int_{\Gamma_N}F(z)\,dz\to0$ as $N\to\infty$.

::: pf-proof

$\abs{\csc(\pi z)}$ is bounded on $\Gamma_N$ uniformly in $N$: writing $z=x+iy$, $\abs{\sin(\pi z)}^2=\sin^2(\pi x)+\sinh^2(\pi y)$, so on the vertical sides, where $\sin^2(\pi x)=1$, $\abs{\sin(\pi z)}\ge1$, and on the horizontal sides $\abs{\sin(\pi z)}\ge\sinh(\pi/2)$. On $\Gamma_N$, $\abs{z+a}\ge N+\tfrac12-\abs{a}$, and the length of $\Gamma_N$ is $8(N+\tfrac12)$, so the integral is $O(1/N)$.

:::

:::

::: {.pf-step #residues}

$\operatorname{Res}(F,k)=\dfrac{(-1)^k}{(k+a)^2}$ for $k\in\ZZ$, and $\operatorname{Res}(F,-a)=-\pi^2\cos(\pi a)\csc^2(\pi a)$; these are all the poles of $F$.

::: pf-proof

The poles of $F$ are the zeros $k\in\ZZ$ of $\sin(\pi z)$ and the point $-a\notin\ZZ$. Near $k$, $\sin(\pi z)=(-1)^k\pi(z-k)+O((z-k)^3)$, so $\pi\csc(\pi z)$ has a simple pole with residue $(-1)^k$. At the double pole $-a$,
$$
\operatorname{Res}(F,-a)=\left.\frac{d}{dz}\pi\csc(\pi z)\right|_{z=-a}
=-\pi^2\csc(-\pi a)\cot(-\pi a)
=-\pi^2\cos(\pi a)\csc^2(\pi a).
$$

:::

:::

::: pf-step

$\displaystyle\sum_{k\in\ZZ}\frac{(-1)^k}{(k+a)^2}=\pi^2\cos(\pi a)\csc^2(\pi a)$.

::: pf-proof

For $N>\abs{a}$, the poles inside $\Gamma_N$ are $-N,\ldots,N$ and $-a$, so by the residue theorem and step [](#residues){.pf-ref},
$$
\frac1{2\pi i}\int_{\Gamma_N}F(z)\,dz
=\sum_{k=-N}^N\frac{(-1)^k}{(k+a)^2}-\pi^2\cos(\pi a)\csc^2(\pi a).
$$
The series converges absolutely, and letting $N\to\infty$ with step [](#vanish){.pf-ref} gives the identity.

:::

:::

:::

:::
