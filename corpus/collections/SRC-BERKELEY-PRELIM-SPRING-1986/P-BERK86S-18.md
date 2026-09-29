---
schema: qual/card@1
id: P-BERK86S-18
kind: problem
title: Coefficientwise convergence under an entire majorant gives compact-uniform convergence
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Passed to Taylor coefficients at 0. The coefficients of f give a
    summable majorant on every closed disk; coefficientwise limits define an
    entire candidate, and a finite-head/tail estimate gives uniform
    convergence on each disk.
---

::: {.problem}
Let $f,g_1,g_2,\dots$ be entire. Suppose
\[
|g_n^{(k)}(0)|\le|f^{(k)}(0)|
\]
for all $n,k$, and suppose
\[
\lim_{n\to\infty}g_n^{(k)}(0)
\]
exists for every $k$. Prove that $(g_n)$ converges uniformly on compact subsets of $\mathbb C$, and that its limit is entire.
:::

::: {.solution}
For $k\geq0$, define
$$
a_k\coloneqq\frac{f^{(k)}(0)}{k!},
\qquad
c_{n,k}\coloneqq\frac{g_n^{(k)}(0)}{k!}.
$$

::: pf

::: {.pf-step #ck-limit-exists}
For every $k\geq0$, the limit
$$
c_k\coloneqq\lim_{n\to\infty}c_{n,k}
$$
exists and satisfies
$$
\abs{c_k}\leq\abs{a_k}.
$$

::: pf-proof
Existence follows from the second hypothesis after division by $k!$.
The first hypothesis gives
$$
\abs{c_{n,k}}\leq\abs{a_k}
$$
for every $n$. Passing to the limit in $n$ yields the stated bound.
:::

:::

::: {.pf-step #majorant-series-converges}
For every $R>0$,
$$
\sum_{k=0}^{\infty}\abs{a_k}R^k<\infty.
$$

::: pf-proof
Since $f$ is entire, its Taylor series at $0$ has infinite radius of
convergence:
$$
f(z)=\sum_{k=0}^{\infty}a_kz^k.
$$
A power series converges absolutely at every point strictly inside its
radius of convergence. Since the radius here is infinite, the displayed
majorant series converges for every finite $R$.
:::

:::

::: {.pf-step #g-is-entire}
The series
$$
g(z)\coloneqq\sum_{k=0}^{\infty}c_kz^k
$$
defines an entire function.

::: pf-proof
Fix $R>0$. For $\abs{z}\leq R$, step [](#ck-limit-exists){.pf-ref} gives
$$
\abs{c_kz^k}
\leq
\abs{a_k}R^k.
$$
The right-hand series is summable by step [](#majorant-series-converges){.pf-ref}. Hence the Weierstrass
M-test gives uniform convergence of the series defining $g$ on
$\abs{z}\leq R$. Since each partial sum is a polynomial, the standard
Weierstrass theorem implies that $g$ is holomorphic on $\abs{z}<R$.
As $R$ is arbitrary, $g$ is entire.
:::

:::

::: {.pf-step #uniform-on-disk}
For every $R>0$,
$$
g_n\longrightarrow g
$$
uniformly on the closed disk $\abs{z}\leq R$.

::: pf-proof
Because each $g_n$ is entire,
$$
g_n(z)=\sum_{k=0}^{\infty}c_{n,k}z^k.
$$
For $\abs{z}\leq R$,
$$
\abs{g_n(z)-g(z)}
\leq
\sum_{k=0}^{\infty}
\abs{c_{n,k}-c_k}R^k.
$$
By step [](#ck-limit-exists){.pf-ref} and the corresponding bound on $c_{n,k}$,
$$
\abs{c_{n,k}-c_k}
\leq
2\abs{a_k}.
$$

Let $\varepsilon>0$. By step [](#majorant-series-converges){.pf-ref}, choose $N$ such that
$$
2\sum_{k>N}\abs{a_k}R^k<\frac{\varepsilon}{2}.
$$
For the finitely many indices $0\leq k\leq N$, coefficientwise
convergence gives $n_0$ such that for $n\geq n_0$,
$$
\sum_{k=0}^{N}
\abs{c_{n,k}-c_k}R^k
<
\frac{\varepsilon}{2}.
$$
Therefore, for $n\geq n_0$ and $\abs{z}\leq R$,
$$
\abs{g_n(z)-g(z)}
<
\varepsilon.
$$
This is uniform convergence on the closed disk.
:::

:::

::: {.pf-step #uniform-on-compact}
The sequence $(g_n)$ converges uniformly on every compact subset of
$\CC$, and its limit is the entire function $g$ from step [](#g-is-entire){.pf-ref}.

::: pf-proof
Let $K\subset\CC$ be compact. Then $K$ is bounded, so
$$
K\subset\{z:\abs{z}\leq R\}
$$
for some $R>0$. Step [](#uniform-on-disk){.pf-ref} gives uniform convergence on that disk and hence
on $K$. Step [](#g-is-entire){.pf-ref} proves that the limit $g$ is entire.
:::

:::

::: pf-qed
Step [](#uniform-on-compact){.pf-ref} is exactly the required conclusion.
:::

:::
:::
