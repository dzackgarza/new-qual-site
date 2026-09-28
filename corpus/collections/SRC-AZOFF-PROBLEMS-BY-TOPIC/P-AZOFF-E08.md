---
schema: qual/card@1
id: P-AZOFF-E08
kind: problem
title: Entire functions with $f(z)/z^n\to0$ are polynomials of degree less than $n$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash separates the limit arrow and $z\to\infty$ from the displayed quotient; the card recombines those extracted pieces without changing the mathematical statement.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Applied Cauchy's coefficient estimate on circles of radius R. The given
    limit makes the circle maximum M(R)/R^n tend to zero, forcing every
    Taylor coefficient a_m with m>=n to vanish.
---

::: {.problem}
Suppose $f$ is entire and, for some integer $n\ge1$,
\[
\lim_{z\to\infty}\frac{f(z)}{z^n}=0.
\]
Prove that $f$ is a polynomial of degree at most $n-1$.
:::

::: {.solution}
Write
$$
f(z)=\sum_{m=0}^{\infty}a_mz^m
$$
for the Taylor series of $f$ at the origin. For $R>0$, set
$$
M(R)=\max_{\abs{\zeta}=R}\abs{f(\zeta)}.
$$

<1>1. One has
$$
\frac{M(R)}{R^n}\longrightarrow0
$$
as $R\to\infty$.

::: {.proof}
The hypothesis means that for every $\varepsilon>0$ there is $R_0>0$ such
that
$$
\frac{\abs{f(z)}}{\abs{z}^n}<\varepsilon
$$
whenever $\abs{z}\geq R_0$. Hence for every $R\geq R_0$ and every
$\zeta$ with $\abs{\zeta}=R$,
$$
\frac{\abs{f(\zeta)}}{R^n}<\varepsilon.
$$
Taking the maximum over the circle gives
$$
\frac{M(R)}{R^n}\leq\varepsilon.
$$
:::

<1>2. For every integer $m\geq n$ and every $R>0$,
$$
\abs{a_m}
\leq
\frac{M(R)}{R^m}.
$$

::: {.proof}
Cauchy's coefficient formula gives
$$
a_m
=
\frac{1}{2\pi i}
\int_{\abs{\zeta}=R}
\frac{f(\zeta)}{\zeta^{m+1}}
\,d\zeta.
$$
The circle has length $2\pi R$, so
$$
\abs{a_m}
\leq
\frac{1}{2\pi}(2\pi R)
\frac{M(R)}{R^{m+1}}
=
\frac{M(R)}{R^m}.
$$
:::

<1>3. For every integer $m\geq n$,
$$
a_m=0.
$$

::: {.proof}
Fix $m\geq n$. For $R\geq1$, step <1>2 gives
$$
\abs{a_m}
\leq
\frac{M(R)}{R^n}R^{n-m}
\leq
\frac{M(R)}{R^n}.
$$
By step <1>1, the right-hand side tends to zero as $R\to\infty$. Thus
$\abs{a_m}=0$.
:::

<1>4. The function $f$ is a polynomial of degree at most $n-1$.

::: {.proof}
Step <1>3 shows that every Taylor coefficient of degree at least $n$
vanishes. Therefore
$$
f(z)=\sum_{m=0}^{n-1}a_mz^m.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
