---
schema: qual/card@1
id: E-SS5.EX-16
kind: problem
title: Prescribed principal parts at discrete poles
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 5, §3, exercise 16, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise; nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved by the standard polynomial-correction construction: subtract from $Q_n(1/(z-a_n))$ a
    Taylor polynomial at the origin chosen so that the $n$-th summand is at most $2^{-n}$ on
    $|z|\le R_n$, with $R_n=\min(n,|a_n|/2)\to\infty$ and $R_n<|a_n|$ so that the Taylor series
    converges there. The one hypothesis the printed statement leaves implicit is that the points
    $a_n$ be distinct: if $a_n=a_m$ with $Q_n\ne Q_m$ then $f-Q_n$ and $f-Q_m$ cannot both be
    holomorphic near that point, so no such $f$ exists. A remark records this. Nothing is left in
    outline.
---

::: {.exercise}
For $n=1,2,\ldots$, let
$$
Q_n(z)=\sum_{k=1}^{N_n}c_k^{n}z^k
$$
be polynomials. Let $\{a_n\}$ be a sequence of complex numbers with no finite limit points. Prove that there exists a meromorphic function $f$ whose only poles are at the $a_n$ and for which
$$
f(z)-Q_n\left(\frac{1}{z-a_n}\right)
$$
is holomorphic near $a_n$ for each $n$. Thus $f$ has prescribed poles and principal parts at those poles. This result is due to Mittag-Leffler.
:::

::: {.solution}

Write $Q_n(w)=\sum_{k=1}^{N_n}c_k^{(n)}w^k$, so $Q_n(1/(z-a_n))$ is holomorphic on $\CC\setminus\{a_n\}$ and tends to $0$ at infinity. Assume the points $a_n$ are distinct, which is necessary (see the remark); then $\abs{a_n}\to\infty$ because the sequence has no finite limit point.

::: pf

::: {.pf-step #s1}

For each $n$ there is a polynomial $P_n$ such that
$$
g_n(z):=Q_n\Bigl(\frac{1}{z-a_n}\Bigr)-P_n(z)
$$
is holomorphic on $\abs{z}<R_n$ and satisfies $\sup_{\abs{z}\le R_n}\abs{g_n(z)}\le2^{-n}$, where $R_n=\min\bigl(n,\abs{a_n}/2\bigr)$.

::: pf-proof

Since $R_n<\abs{a_n}$, the function $z\mapsto Q_n(1/(z-a_n))$ is holomorphic on the disc $\abs{z}<R_n$, so its Taylor series at the origin converges to it uniformly on $\abs{z}\le R_n$. Let $P_n$ be a Taylor polynomial of that series of high enough degree; the remainder $g_n$ is the corresponding tail, and a Taylor series converges uniformly on compact subsets of its disc of convergence, so $\sup_{\abs{z}\le R_n}\abs{g_n(z)}\le2^{-n}$ for the degree large enough.

Note that $R_n\to\infty$: $R_n\ge n$ fails only when $\abs{a_n}/2<n$, and in that case $R_n=\abs{a_n}/2\to\infty$ as well, so $R_n\to\infty$ either way.

:::

:::

::: {.pf-step #s2}

The series $f=\sum_{n}g_n$ converges uniformly on every compact set away from the points $a_n$, and defines a meromorphic function on $\CC$ whose only possible poles are the $a_n$.

::: pf-proof

Let $R>0$. For every $n$ with $R_n\ge R$ the function $g_n$ is holomorphic on $\abs{z}\le R$ (because $R\le R_n<\abs{a_n}$) and satisfies $\sup_{\abs{z}\le R}\abs{g_n}\le2^{-n}$; as $R_n\to\infty$ all but finitely many $n$ have this property. Hence the corresponding tail of the series converges uniformly on $\abs{z}\le R$ to a holomorphic function there, and adding the finitely many remaining terms, each meromorphic on $\abs{z}\le R$ with its single pole at the corresponding $a_n$, produces a function meromorphic on $\abs{z}<R$ — but this is only legitimate if no $a_n$ lies on $\abs{z}=R$; choosing $R$ outside the countable set of moduli $\abs{a_n}$ and then letting $R\to\infty$ covers every compact set. So $f$ is meromorphic on $\CC$ and its poles are among the $a_n$.

:::

:::

::: {.pf-step #s3}

Near $a_n$, the function $f-Q_n(1/(z-a_n))$ is holomorphic; hence $f$ has the prescribed principal part $Q_n(1/(z-a_n))$ at $a_n$.

::: pf-proof

Fix $n$ and a small disc $D$ centred at $a_n$ containing no other $a_m$. Then
$$
f(z)-Q_n\Bigl(\frac{1}{z-a_n}\Bigr)=-P_n(z)+\sum_{m\ne n}g_m(z)
$$
on $D$. The first term is a polynomial. In the sum, each $g_m$ with $m\ne n$ is holomorphic on $D$ (its only pole is at $a_m\notin D$), and the sum converges uniformly on $D$: for $R$ with $D\subseteq\abs{z}\le R$, the tail over $\{m:R_m\ge R\}$ is uniformly bounded by $\sum2^{-m}$ there by step [](#s1){.pf-ref}, and the remaining terms are finitely many holomorphic functions on $D$. Hence the sum defines a holomorphic function on $D$, and so does $f-Q_n(1/(z-a_n))$.

Since $Q_n(1/(z-a_n))$ has a pole of finite order at $a_n$ (unless $Q_n=0$, in which case $a_n$ is a removable point of $f$) and differs from $f$ by a function holomorphic near $a_n$, the principal part of $f$ at $a_n$ is exactly $Q_n(1/(z-a_n))$.

:::

:::

:::

:::

::: {.remark}
The printed statement says only that $\{a_n\}$ has no finite limit point. Distinctness is needed: if $a_n=a_m$ for $n\ne m$, then $f-Q_n(1/(z-a_n))$ and $f-Q_m(1/(z-a_n))$ holomorphic near that point would force $Q_n-Q_m$, a nonzero rational function with a pole there, to be holomorphic, which is impossible. When $a_n=a_m$ the two principal parts must therefore be merged into a single pole, which is the usual form of the Mittag-Leffler theorem.
:::
