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

::: pf

::: {.pf-step #s1}

The constant $m$ is positive.

::: pf-proof

Since
$$
0\leq\abs{f(0)}<m,
$$
we have $m>0$.

:::

:::

::: {.pf-step #s2}

Suppose, for contradiction, that $f$ has no zero in the open unit disk.
Then $g\coloneqq 1/f$ is analytic on the open unit disk and continuous on
the closed unit disk.

::: pf-proof

Under the contradiction hypothesis, $f$ has no zero for $\abs{z}<1$.
For $\abs{z}=1$, the boundary hypothesis and step [](#s1){.pf-ref} give
$$
\abs{f(z)}>m>0,
$$
so $f$ has no zero on the unit circle either. Therefore $1/f$ is analytic
on the open disk and extends continuously to its boundary.

:::

:::

::: {.pf-step #s3}

The maximum modulus principle gives
$$
\abs{g(0)}<\frac1m.
$$

::: pf-proof

By step [](#s2){.pf-ref},
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

:::

::: pf-step

The assumption in step [](#s2){.pf-ref} is impossible.

::: pf-proof

By step [](#s3){.pf-ref},
$$
\frac1{\abs{f(0)}}
=\abs{g(0)}
<\frac1m,
$$
and step [](#s2){.pf-ref} gives $\abs{f(0)}>0$, while step [](#s1){.pf-ref} gives $m>0$.
Taking reciprocals therefore yields $\abs{f(0)}>m$, contrary to the
hypothesis.

:::

:::

::: {.pf-step #s5}

Hence $f$ has at least one zero in the open unit disk.

::: pf-proof

This is the negation of the contradiction hypothesis in step [](#s2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
