---
schema: qual/card@1
id: P-BKF96-4
kind: problem
title: Can a holomorphic function on $\mathbb C^*$ be bounded below by $|z|^{-1/2}$?
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Passed to g=1/f, which extends holomorphically across zero and obeys
    |g(z)|<=|z|^(1/2). Cauchy estimates at arbitrarily large radii force all
    Taylor coefficients of g to vanish.
---

::: {.problem}
Does there exist a function $f$, holomorphic on $\mathbb C\setminus\{0\}$, such that
\[
|f(z)|\ge\frac1{\sqrt{|z|}}
\]
for every $z\ne0$?
:::

::: {.solution}
No such function exists.

<1>1. If such an $f$ existed, then $f$ would have no zeros on
$$
\CC\setminus\{0\},
$$
and
$$
g(z)\coloneqq\frac1{f(z)}
$$
would be holomorphic there with
$$
\abs{g(z)}\leq\sqrt{\abs z}.
$$

::: {.proof}
The assumed lower bound is strictly positive for every $z\neq0$, so
$f(z)\neq0$. Taking reciprocals of
$$
\abs{f(z)}
\geq
\frac1{\sqrt{\abs z}}
$$
gives
$$
\abs{g(z)}
\leq
\sqrt{\abs z}.
$$
:::

<1>2. The singularity of $g$ at $0$ is removable, and the holomorphic
extension satisfies
$$
g(0)=0.
$$

::: {.proof}
Step <1>1 gives
$$
\abs{g(z)}
\leq
\sqrt{\abs z}
\longrightarrow0
$$
as $z\to0$. Thus $g$ is bounded near $0$, so the removable singularity
theorem extends it holomorphically across $0$. The displayed limit forces
the extension to have value $0$ there.
:::

<1>3. Write the resulting entire function as
$$
g(z)=\sum_{n=0}^{\infty}a_nz^n.
$$
Then
$$
a_n=0
$$
for every $n\geq1$.

::: {.proof}
For every $R>0$, step <1>1 gives on the circle $\abs z=R$
$$
\max_{\abs z=R}\abs{g(z)}
\leq
\sqrt R.
$$
Cauchy's coefficient estimate therefore gives
$$
\abs{a_n}
\leq
\frac{\sqrt R}{R^n}
=
R^{1/2-n}.
$$
If $n\geq1$, the right side tends to $0$ as $R\to\infty$. Hence
$a_n=0$.
:::

<1>4. One has
$$
g\equiv0.
$$

::: {.proof}
Step <1>3 shows that $g$ is constant, while step <1>2 gives
$$
g(0)=0.
$$
Therefore the constant is zero.
:::

<1>5. The assumption that such an $f$ exists is impossible.

::: {.proof}
On $\CC\setminus\{0\}$, the definition of $g$ gives
$$
g(z)=\frac1{f(z)}\neq0.
$$
This contradicts step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves that no holomorphic function with the stated lower bound
exists.
:::
:::
