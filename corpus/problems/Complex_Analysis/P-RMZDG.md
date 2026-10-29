---
schema: qual/card@1
id: P-RMZDG
kind: problem
title: Entire functions of polynomial growth, sector vanishing on the disc, products
  of distances on $S^1$, and constancy when the real part is bounded
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Maximum Modulus Principle
  - Entire Functions
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Use the Cauchy inequalities or the maximum modulus principle to solve the following problems:

(a) Prove that if $f$ is an entire function that satisfies
$$
\sup _{|z|=R}|f(z)| \leq A R^{k}+B
$$
for all $R>0$, some integer $k\geq 0$, and some constants $A, B > 0$, then $f$ is a polynomial of degree $\leq k$.

(b) Show that if $f$ is holomorphic in the unit disc, is bounded, and converges uniformly to zero in the sector $\theta < \arg(z) < \phi$ as $\abs{z} \to 1$, then $f \equiv 0$.

(c) Let $w_1, \ldots, w_n$ be points on $S^1 \subset \CC$.
Prove that there exists a point $z\in S^1$ such that the product of the distances from $z$ to the points $w_j$ is at least 1.
Conclude that there exists a point $w\in S^1$ such that the product of the above distances is *exactly* 1.

(d) Show that if the real part of an entire function is bounded, then $f$ is constant.
:::

::: {.solution title="(a)"}

::: pf

::: {.pf-step #vanish}

$f^{(m)}(0)=0$ for every integer $m>k$.

::: pf-proof

By Cauchy's estimate on $\abs z=R$,
$$
\abs{f^{(m)}(0)}\le\frac{m!}{R^m}\max_{\abs z=R}\abs{f(z)}\le m!\qty(AR^{k-m}+BR^{-m}),
$$
and the right side tends to $0$ as $R\to\infty$.

:::

:::

::: pf-step

$f$ is a polynomial of degree at most $k$.

::: pf-proof

$f$ is entire, so it equals its Taylor series at $0$, and by step [](#vanish){.pf-ref}
$$
f(z)=\sum_{m=0}^k\frac{f^{(m)}(0)}{m!}z^m.
$$

:::

:::

:::

:::

::: {.solution title="(b)"}
Let $S=\theset{z\in\DD : \theta<\arg z<\phi}$ and $M=\sup_{z\in\DD}\abs{f(z)}<\infty$. Choose an integer $N$ with $2\pi/N<\phi-\theta$, so that every ray from $0$ meets one of the rotated sectors $e^{2\pi ij/N}S$, $0\le j<N$. Define
$$
g(z)=\prod_{j=0}^{N-1}f\qty(e^{2\pi ij/N}z).
$$

::: pf

::: {.pf-step #g-zero}

$g\equiv0$ on $\DD$.

::: pf-proof

Fix $\varepsilon>0$. By hypothesis there is $\rho<1$ with $\abs{f(z)}<\varepsilon$ for $z\in S$, $\rho<\abs z<1$. For $r\in(\rho,1)$ and $\abs z=r$, at least one point $e^{2\pi ij/N}z$ lies in $S$, so $\abs{g(z)}\le\varepsilon M^{N-1}$. The maximum modulus principle extends this bound to $\abs z\le r$. Letting $r\to1$ and then $\varepsilon\to0$ gives $g\equiv0$.

:::

:::

::: pf-step

$f\equiv0$.

::: pf-proof

The ring of holomorphic functions on the connected open set $\DD$ is an integral domain, so by step [](#g-zero){.pf-ref} some factor $f(e^{2\pi ij/N}z)$ vanishes identically. Rotation is a bijection of $\DD$, so $f\equiv0$.

:::

:::

:::

:::

::: {.solution title="(c)"}
Let $f(z)\coloneqq\prod_{k=1}^n(w_k-z)$, so that for $z\in S^1$, $\abs{f(z)}$ is the product of the distances from $z$ to the $w_k$. Let $M\coloneqq\max_{\abs z=1}\abs{f(z)}$.

::: pf

::: {.pf-step #big}

$M>1$; in particular some $z\in S^1$ has $\abs{f(z)}\ge1$.

::: pf-proof

$f$ is a nonconstant polynomial and $\abs{f(0)}=\prod\abs{w_k}=1$. By the maximum modulus principle, $\abs{f(0)}<M$.

:::

:::

::: pf-step

Some $w\in S^1$ has $\abs{f(w)}=1$.

::: pf-proof

$\abs f$ is continuous on the connected set $S^1$, takes the value $0$ at $w_1$ and, by step [](#big){.pf-ref}, a value greater than $1$. The intermediate value theorem gives the claim.

:::

:::

:::

:::

::: {.solution title="(d)"}
Suppose $\abs{\Re f(z)}\le M$ on $\CC$ and set $g(z)=e^{f(z)}$.

::: pf

::: {.pf-step #g-const}

$g$ is constant.

::: pf-proof

$g$ is entire and $\abs{g(z)}=e^{\Re f(z)}\le e^M$, so Liouville's theorem applies.

:::

:::

::: pf-step

$f$ is constant.

::: pf-proof

By step [](#g-const){.pf-ref}, $0=g'(z)=f'(z)e^{f(z)}$, and $e^{f(z)}\ne0$, so $f'\equiv0$.

:::

:::

:::

:::
