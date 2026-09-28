---
schema: qual/card@1
id: P-MMAQ-CFGXL3QPK7
kind: problem
title: A meromorphic function on $\CC$ with $|f(z)|\to\infty$ as $|z|\to\infty$ is
  rational
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (11) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMCA11, whose solution repeats this principal-part argument."
- event: solution-reviewed
  by: claude-opus-5
  date: 2026-09-16
  note: "The absence of poles near infinity was asserted from the limit alone; it now follows from the isolated zero of 1/f at infinity. The raw TeX block in the statement is ordinary display math."
---

::: {.problem}
Let $f$ be a meromorphic function in the plane such that
\[
\lim_{|z|\to\infty}|f(z)|=\infty.
\]

1. Show that $f$ has only finitely many poles.

2. Show that $f$ is a rational function.
:::

::: {.solution}
<1>1. There is $R>0$ such that $f$ has no poles in $\{|z|>R\}$.
::: {.proof}
Choose $R_0>0$ with $|f(z)|\ge1$ for $|z|>R_0$ away from the poles.
Then $g=1/f$ is holomorphic on $\{|z|>R_0\}$: it is holomorphic away from the poles of $f$, and it has a removable singularity with value $0$ at each pole.
Put $G(w)=g(1/w)$ for $0<|w|<1/R_0$.
Since $g(z)\to0$ as $|z|\to\infty$, $G$ is bounded near $0$, so by Riemann's removable singularity theorem it extends holomorphically to $|w|<1/R_0$ with $G(0)=0$.
$G$ is not identically zero, because $g$ is nonzero away from the poles of $f$.
By the identity theorem the zero of $G$ at $0$ is isolated, so there is $\delta>0$ with $G(w)\neq0$ for $0<|w|<\delta$.
The poles of $f$ in $\{|z|>R_0\}$ are exactly the zeros of $g$ there, so $f$ has no poles in $\{|z|>R\}$ with $R=\max(R_0,1/\delta)$.
:::

<1>2. $f$ has only finitely many poles.
::: {.proof}
By <1>1 every pole lies in the compact disc $\{|z|\le R\}$.
The poles of a meromorphic function have no accumulation point in $\mathbb C$, so a compact set contains only finitely many of them.
:::

<1>3. $f$ is a rational function.
::: {.proof}
Let $p_1,\dots,p_k$ be the poles, with principal parts $P_j(z)=\sum_{m=1}^{d_j}c_{j,m}(z-p_j)^{-m}$.
Then $h=f-\sum_{j}P_j$ has removable singularities at every $p_j$, so it extends to an entire function.
Each $P_j(z)\to0$ as $|z|\to\infty$, hence $|h(z)|\to\infty$.
An entire function with $|h(z)|\to\infty$ has a pole at $\infty$ and is therefore a polynomial.
Thus $f=h+\sum_jP_j$ is a sum of a polynomial and finitely many rational functions, hence rational.
:::
:::
