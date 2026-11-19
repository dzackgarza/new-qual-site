---
schema: qual/card@1
id: P-CASP23C
kind: problem
title: "A holomorphic function with |f|>m on the boundary and |f(0)|<m has a zero in D"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Rouché
  - Holomorphic Functions
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The source is a course examination, so there is no retained solution set behind the card and the problem statement is the source. Each step re-read: the boundary hypothesis keeps f nonzero on the circle, so 1/f is holomorphic on a neighbourhood of the closed disc under the supposition that f is zero-free inside; the maximum modulus principle then gives |1/f(0)| <= max on the circle < 1/m, i.e. |f(0)| > m, contradicting the hypothesis. The card records that both inequalities must be strict, with the constant function m as the boundary case. Not claimed: any statement about the number of zeros.
---

::: {.problem}
Let $f(z)$ be analytic on an open set containing $\overline{\DD}$.
Suppose that $\abs{f(z)} > m$ for $\abs{z} = 1$ and $\abs{f(0)} < m$ for a positive number $m$.
Prove that $f(z)$ has a zero in $\DD$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #nonzero}
$f$ has no zero on $\abs{z}=1$.

::: pf-proof
$\abs{f(z)}>m>0$ on the circle, so $f(z)\ne0$ there.
:::

:::

::: {.pf-step #reciprocal}
If $f$ had no zero in $\DD$, then $1/f$ would be holomorphic on a neighbourhood of $\overline\DD$.

::: pf-proof
$f$ is holomorphic on an open set containing $\overline\DD$ and, under the supposition together with step [](#nonzero){.pf-ref}, is nonzero on $\overline\DD$; so $1/f$ is holomorphic on that open set.
:::

:::

::: {.pf-step #boundary}
$\abs{1/f(z)}<1/m$ for $\abs{z}=1$.

::: pf-proof
Take reciprocals in the hypothesis $\abs{f(z)}>m$.
:::

:::

::: {.pf-step #maxmod}
$\abs{1/f(0)}\le\max_{\abs{z}=1}\abs{1/f(z)}<1/m$.

::: pf-proof
The maximum modulus principle applied to the holomorphic function $1/f$ on $\DD$, continuous on $\overline\DD$, gives that $\abs{1/f}$ attains its maximum on the boundary, so its value at the interior point $0$ is at most the boundary maximum; step [](#boundary){.pf-ref} bounds that maximum by $1/m$ strictly.
:::

:::

::: {.pf-step #contradiction}
This contradicts $\abs{f(0)}<m$.

::: pf-proof
$\abs{1/f(0)}<1/m$ is the same statement as $\abs{f(0)}>m$, which is incompatible with $\abs{f(0)}<m$.
:::

:::

::: {.pf-step}
$f$ has a zero in $\DD$.

::: pf-proof
The supposition that $f$ has no zero in $\DD$ leads to the contradiction of step [](#contradiction){.pf-ref}:
$$
\boxed{\abs{f}>m\text{ on }\abs{z}=1\text{ and }\abs{f(0)}<m\implies f\text{ has a zero in }\DD.}
$$
Both inequalities are needed: with $\abs{f}\ge m$ on the circle and $\abs{f(0)}=m$ the conclusion can fail, as $f\equiv m$ shows.
:::

:::

:::
:::
