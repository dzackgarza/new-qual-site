---
schema: qual/card@1
id: P-BERK98S-02
kind: problem
title: Boundary modulus and the value at zero force an interior zero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f$ be analytic on an open set containing the closed unit disk. Suppose
\[
|f(z)|>m\quad\text{for }|z|=1,
\qquad
|f(0)|<m.
\]
Prove that $f$ has at least one zero in the open unit disk.
:::

::: {.solution}
<1>1. The constant $m$ is positive.

::: {.proof}
Since
$$
0\leq\abs{f(0)}<m,
$$
we have $m>0$.
:::

<1>2. Suppose, for contradiction, that $f$ has no zero in the open unit disk.
Then $g\coloneqq 1/f$ is analytic on the open unit disk and continuous on
the closed unit disk.

::: {.proof}
Under the contradiction hypothesis, $f$ has no zero for $\abs{z}<1$.
For $\abs{z}=1$, the boundary hypothesis and step <1>1 give
$$
\abs{f(z)}>m>0,
$$
so $f$ has no zero on the unit circle either. Therefore $1/f$ is analytic
on the open disk and extends continuously to its boundary.
:::

<1>3. The maximum modulus principle gives
$$
\abs{g(0)}<\frac1m.
$$

::: {.proof}
By step <1>2,
$$
\abs{g(0)}
\leq
\max_{\abs{z}=1}\abs{g(z)}.
$$
On the unit circle,
$$
\abs{g(z)}
=\frac1{\abs{f(z)}}
<\frac1m.
$$
The continuous function $\abs{g}$ attains its boundary maximum, so that
maximum is also strictly less than $1/m$.
:::

<1>4. The assumption in step <1>2 is impossible.

::: {.proof}
By step <1>3,
$$
\frac1{\abs{f(0)}}
=\abs{g(0)}
<\frac1m,
$$
and step <1>2 gives $\abs{f(0)}>0$, while step <1>1 gives $m>0$.
Taking reciprocals therefore yields $\abs{f(0)}>m$, contrary to the
hypothesis.
:::

<1>5. Hence $f$ has at least one zero in the open unit disk.

::: {.proof}
This is the negation of the contradiction hypothesis in step <1>2.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
