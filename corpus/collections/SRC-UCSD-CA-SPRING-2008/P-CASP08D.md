---
schema: qual/card@1
id: P-CASP08D
kind: problem
title: "Entire functions with polynomial growth and meromorphic functions with prescribed poles and growth"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(a) Let $m$ be a positive integer.
Describe the set of all entire functions $f$ for which there exist positive constants $C_1$ and $C_2$ such that $\abs{f(z)} \le C_1 \abs{z}^m$ for all $\abs{z} \ge C_2$.

(b) Describe the set of all functions $R$, meromorphic in $\CC$, analytic except at $z = \pm 1$, and satisfying all of the following:
(i) $R$ has a simple pole (order 1) at $z = 1$.
(ii) $R$ has a double pole (order 2) at $z = -1$.
(iii) $\abs{R(z)} \le C\abs{z}$ for all $\abs{z} \ge 2$.
:::

::: {.solution}

::: pf

::: pf-step

For part (a), write $f(z)=\sum_{k=0}^\infty a_kz^k$. For every $r\ge C_2$, Cauchy's estimate gives
$$
\abs{a_k}\le \frac{\max_{\abs{z}=r}\abs{f(z)}}{r^k}\le C_1r^{m-k}.
$$
If $k>m$, letting $r\to\infty$ gives $a_k=0$. Hence $f$ is a polynomial of degree at most $m$ (including the zero polynomial). Conversely every polynomial of degree at most $m$ satisfies such a bound outside a sufficiently large disk.

:::

::: pf-step

For part (b), the principal parts must be
$$
\frac{A}{z-1},\qquad \frac{B}{(z+1)^2}+\frac{D}{z+1},
$$
with $A\ne0$ and $B\ne0$. Thus
$$
g(z)=R(z)-\frac{A}{z-1}-\frac{B}{(z+1)^2}-\frac{D}{z+1}
$$
extends to an entire function.

:::

::: pf-step

For $\abs{z}\ge2$, the principal-part terms are bounded, while $\abs{R(z)}\le C\abs{z}$. Hence $\abs{g(z)}\le C'\abs{z}$ for sufficiently large $\abs{z}$. Part (a), with $m=1$, gives $g(z)=\alpha z+\beta$.

:::

:::

Therefore exactly the functions
$$
R(z)=\alpha z+\beta+\frac{A}{z-1}+\frac{D}{z+1}+\frac{B}{(z+1)^2},
$$
where $A,B\ne0$ and $\alpha,\beta,D\in\CC$, satisfy the requirements.
:::
