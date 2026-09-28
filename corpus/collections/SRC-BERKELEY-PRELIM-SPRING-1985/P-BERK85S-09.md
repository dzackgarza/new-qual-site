---
schema: qual/card@1
id: P-BERK85S-09
kind: problem
title: Smoothness of the real zeta series on $(1,\infty)$
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
    Proved local uniform convergence of every termwise derivative series on
    compact subintervals of (1,infinity), using logarithmic growth dominated
    by an arbitrarily small positive power and the Weierstrass M-test.
---

::: {.problem}
Define
\[
\zeta(x)=\sum_{n=1}^\infty\frac1{n^x}.
\]
Prove that $\zeta(x)$ is defined and has continuous derivatives of all orders for
\[
1<x<\infty.
\]
:::

::: {.solution}
<1>1. For every $x>1$, the series
$$
\zeta(x)=\sum_{n=1}^\infty n^{-x}
$$
converges.

::: {.proof}
For fixed $x>1$, this is the convergent $p$-series with exponent $p=x$.
Thus $\zeta$ is defined on $(1,\infty)$.
:::

<1>2. Let $I=[\alpha,\beta]\subset(1,\infty)$ be compact. For every
integer $k\geq0$, the series
$$
\sum_{n=1}^\infty
(-\log n)^k n^{-x}
$$
converges uniformly for $x\in I$.
Here the factor $(-\log n)^0$ is understood as $1$; for $k\geq1$, the
$n=1$ term is $0$.

::: {.proof}
For $x\in I$,
$$
\abs{(-\log n)^k n^{-x}}
\leq
(\log n)^k n^{-\alpha}.
$$
Set
$$
\varepsilon\coloneqq\frac{\alpha-1}{2}>0.
$$
Since
$$
(\log n)^k=o(n^\varepsilon),
$$
there is $N$ such that, for $n\geq N$,
$$
(\log n)^k\leq n^\varepsilon.
$$
Therefore
$$
(\log n)^k n^{-\alpha}
\leq
n^{-(\alpha-\varepsilon)}
=
n^{-(\alpha+1)/2}.
$$
Because $(\alpha+1)/2>1$, the last series converges. The Weierstrass
M-test proves uniform convergence on $I$.
:::

<1>3. For every integer $k\geq0$ and every $x>1$,
$$
\zeta^{(k)}(x)
=
\sum_{n=1}^\infty
(-\log n)^k n^{-x}.
$$

::: {.proof}
For
$$
f_n(x)\coloneqq n^{-x}=e^{-x\log n},
$$
one has
$$
f_n^{(k)}(x)=(-\log n)^k n^{-x}.
$$
Step <1>2 shows that, on the arbitrary compact interval $I$, the series of
$k$th derivatives converges uniformly for every $k\geq0$. Starting with
the uniformly convergent series from the case $k=0$, apply the standard
termwise-differentiation theorem successively: uniform convergence of
$\sum f_n^{(k+1)}$ permits differentiating the sum
$\sum f_n^{(k)}$. Induction on $k$ gives the displayed formula throughout
$I$.
:::

<1>4. Every derivative $\zeta^{(k)}$ is continuous on $(1,\infty)$.

::: {.proof}
Fix $x_0>1$ and choose a compact interval
$$
I=[\alpha,\beta]\subset(1,\infty)
$$
with $x_0$ in its interior. By step <1>3, $\zeta^{(k)}$ on $I$ is the
uniform limit of the continuous functions
$$
\sum_{n=1}^N(-\log n)^k n^{-x}.
$$
Hence $\zeta^{(k)}$ is continuous at $x_0$. Since $x_0$ and $k$ were
arbitrary, every derivative is continuous on $(1,\infty)$.
:::

<1>5. Therefore
$$
\boxed{\zeta\in C^\infty((1,\infty))}.
$$

::: {.proof}
Step <1>1 proves that $\zeta$ is defined on $(1,\infty)$, while steps
<1>3 and <1>4 prove existence and continuity of derivatives of every
order there.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
