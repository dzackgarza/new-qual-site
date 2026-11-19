---
schema: qual/card@1
id: P-UCLAB05S-AN4
kind: problem
title: Total variation of a continuously differentiable function
classification:
  areas: [prelim]
  topics:
  - Total Variation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 4 of the official UCLA Basic Exam, May 2005 PDF.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The argument is correct. On each subinterval the mean value theorem gives a
    point with the difference equal to one n-th of the derivative there, so the
    sum of absolute differences is the right Riemann sum of the continuous
    function |f'| over the uniform partition with mesh 1/n, and such sums
    converge to the integral. The statement itself was not re-read against the
    scan in this pass: the retained file assets/attachments/basic-05S.pdf has no
    text layer, and the source check above is the earlier one.
---

::: {.problem}
Suppose $f:\RR\to\RR$ is $C^1$.
Show that
$$
\lim_{n\to\infty}
\sum_{j=1}^n
\abs{f\!\left(\frac{j-1}{n}\right)-f\!\left(\frac jn\right)}
=\int_0^1\abs{f'(t)}\,dt.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For each $n\ge1$ and each $1\le j\le n$, there exists
$$
\xi_{j,n}\in\left(\frac{j-1}{n},\frac jn\right)
$$
such that
$$
\abs{f\!\left(\frac{j-1}{n}\right)-f\!\left(\frac jn\right)}
=\frac1n\abs{f'(\xi_{j,n})}.
$$


::: pf-proof

Apply the mean value theorem to $f$ on
$$
\left[\frac{j-1}{n},\frac jn\right].
$$
There is a point $\xi_{j,n}$ in the interior such that
$$
f\!\left(\frac jn\right)-f\!\left(\frac{j-1}{n}\right)
=f'(\xi_{j,n})\frac1n.
$$
Taking absolute values gives the claim.

:::

:::

::: {.pf-step #s1-2}

For every $n$,
$$
\sum_{j=1}^n
\abs{f\!\left(\frac{j-1}{n}\right)-f\!\left(\frac jn\right)}
=\sum_{j=1}^n\frac1n\abs{f'(\xi_{j,n})}.
$$


::: pf-proof

Sum the identities from step [](#s1-1){.pf-ref} over $j=1,\ldots,n$.

:::

:::

::: {.pf-step #s1-3}

The right-hand side in step [](#s1-2){.pf-ref} converges to
$$
\int_0^1\abs{f'(t)}\,dt.
$$


::: pf-proof

Because $f$ is $C^1$, the function $t\mapsto\abs{f'(t)}$ is continuous on $[0,1]$. The sum in step [](#s1-2){.pf-ref} is a tagged Riemann sum for this function on the uniform partition of $[0,1]$ into subintervals of length $1/n$. Since the mesh is $1/n\to0$, the Riemann sums converge to the integral.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\lim_{n\to\infty}
\sum_{j=1}^n
\abs{f\!\left(\frac{j-1}{n}\right)-f\!\left(\frac jn\right)}
=\int_0^1\abs{f'(t)}\,dt.}
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required limit identity.

:::

:::

:::
