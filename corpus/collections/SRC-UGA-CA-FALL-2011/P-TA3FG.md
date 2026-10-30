---
schema: qual/card@1
id: P-TA3FG
kind: problem
title: 'Power series of radius $1$: convergence on the circle versus analyticity at every boundary point'
classification:
  areas:
    - complex-analysis
  topics:
    - Power Series
    - Convergence Tests
    - Singularities
relations: []
review: draft
---

::: {.problem}
Here $\DD$ denotes the open unit disk and $\TT=\partial\DD$ the unit circle. Suppose $\Omega \subset \CC$ is a region containing $\DD$ and $f$ is holomorphic on $\Omega$. Suppose that on $\DD$ we have $f(z)=\sum a_nz^n$ and the series has radius of convergence equal to $1$.

(a) Give an example of such an $f$ so that the series converges at every point of $\TT$.

(b) Give an example of such an $f$ that is analytic at $z_0 \in \TT$ and for which $\sum a_nz_0^n$ diverges.

(c) Prove that $f$ cannot be analytic at every point of $\TT$.
:::

::: {.solution}

::: pf

::: {.pf-step #a}

$f(z)=\sum_{n\ge1}z^n/n^2$ on $\Omega=\DD$ is an example for part (a).

::: pf-proof

The radius of convergence is $\lim_n\bigl((n+1)/n\bigr)^2=1$. For $\abs{z}=1$, $\abs{z^n/n^2}=1/n^2$, and $\sum1/n^2<\infty$, so the series converges absolutely at every point of $\TT$.

:::

:::

::: {.pf-step #b}

$f(z)=\dfrac{1}{1+z}=\sum_{n\ge0}(-1)^nz^n$ on $\Omega=\CC\setminus\{-1\}$, with $z_0=1$, is an example for part (b).

::: pf-proof

The coefficients have modulus $1$, so the radius of convergence is $1$. The function is holomorphic on $\Omega\ni1$. At $z_0=1$ the terms $(-1)^n$ do not tend to $0$, so the series diverges.

:::

:::

::: {.pf-step #cover}

Suppose $f$ is analytic at every point of $\TT$. Then there are finitely many disks $D_j=D(w_j,r_j)$, $w_j\in\TT$, that cover $\TT$, and holomorphic $f_j$ on $D_j$ with $f_j=f$ on $D_j\cap\DD$.

::: pf-proof

Analyticity at $w\in\TT$ gives a disk $D(w,r_w)$ and a holomorphic $f_w$ on it that equals $f$ on $D(w,r_w)\cap\DD$. These disks cover the compact set $\TT$, so finitely many of them cover it.

:::

:::

::: {.pf-step #glue}

$f$ and the $f_j$ define one holomorphic function $F$ on $U=\DD\cup D_1\cup\cdots\cup D_m$.

::: pf-proof

It suffices that $f_j=f_k$ on $D_j\cap D_k$ when this set is nonempty. The intersection of two disks is convex, so it is connected. It meets $\DD$: if $w_j=w_k$ it is a disk centered on $\TT$; otherwise $\abs{w_j-w_k}<r_j+r_k$, so some point of the open segment from $w_j$ to $w_k$ lies in both disks, and that open segment lies in $\DD$ because $\DD$ is strictly convex. On the nonempty open set $D_j\cap D_k\cap\DD$ both functions equal $f$, so by the identity theorem $f_j=f_k$ on $D_j\cap D_k$.

:::

:::

::: {.pf-step #c}

This contradicts the radius of convergence $1$, which proves part (c).

::: pf-proof

The open set $U$ contains the compact set $\overline\DD$, so it contains $D(0,1+\varepsilon)$ for some $\varepsilon>0$. By Step [](#glue){.pf-ref}, $F$ is holomorphic there, so its Taylor series at $0$ converges on $D(0,1+\varepsilon)$. Since $F=f$ on $\DD$, that Taylor series is $\sum a_nz^n$. Its radius of convergence is then at least $1+\varepsilon$.

:::

:::

::: pf-qed

Steps [](#a){.pf-ref}, [](#b){.pf-ref} and [](#c){.pf-ref} answer parts (a), (b) and (c).

:::

:::

:::
