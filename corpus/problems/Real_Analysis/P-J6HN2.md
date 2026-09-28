---
schema: qual/card@1
id: P-J6HN2
kind: problem
title: Fatou's lemma and summing series in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Convergence of Integrals
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- Prove Fatou's lemma using the Monotone Convergence Theorem.

- Show that if $\theset{f_n}$ is in $L^1$ and $\sum \int \abs{f_n} < \infty$ then $\sum f_n$ converges to an $L^1$ function and $$\int \sum f_n = \sum \int f_n.$$
:::
::: {.solution}
<1>1. For measurable $f_n \ge 0$, $\int \liminf_n f_n \le \liminf_n \int f_n$.

<2>1. $g_k = \inf_{n \ge k} f_n$ is measurable, and $g_k \uparrow \liminf_n f_n$ pointwise.

::: {.proof}
$g_k$ is an infimum of countably many measurable functions, $g_k \le g_{k+1}$, and $\sup_k g_k = \liminf_n f_n$ by definition.
:::

<2>2. $\int g_k \le \inf_{n \ge k}\int f_n$.

::: {.proof}
$g_k \le f_n$ for $n \ge k$, and the integral is monotone.
:::

<2>3. Q.E.D.

::: {.proof}
By the monotone convergence theorem and steps <2>1 and <2>2, $\int \liminf_n f_n = \lim_k \int g_k \le \lim_k \inf_{n \ge k}\int f_n = \liminf_n \int f_n$.
:::

<1>2. If $f_n \in L^1$ and $\sum_n \int |f_n| < \infty$, then $\sum_n f_n$ converges a.e. to an $L^1$ function $F$ and $\int F = \sum_n \int f_n$.

<2>1. $g = \sum_n |f_n|$ satisfies $\int g = \sum_n \int |f_n| < \infty$, so $g < \infty$ a.e.

::: {.proof}
The first equality is the monotone convergence theorem for the partial sums. A nonnegative function with finite integral is finite a.e.
:::

<2>2. Q.E.D.

::: {.proof}
Where $g(x) < \infty$ the series $\sum_n f_n(x)$ converges absolutely; let $F(x)$ be its sum there and $F = 0$ elsewhere. Then $|F| \le g$, so $F \in L^1$. For every $N$,
$$
\left|\int F - \sum_{n=1}^N \int f_n\right| \le \int \Big|\sum_{n>N} f_n\Big| \le \int \sum_{n>N}|f_n| = \sum_{n>N}\int|f_n|,
$$
using the monotone convergence theorem in the last step. The right side tends to $0$.
:::
:::
