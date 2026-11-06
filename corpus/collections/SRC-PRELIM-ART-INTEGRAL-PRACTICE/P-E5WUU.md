---
schema: qual/card@1
id: P-E5WUU
kind: problem
title: $\int_0^1\int_y^1\sin(x^2)\,dx\,dy$ by reversing the order of integration
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Multivariable Calculus
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-ART-INTEGRAL-PRACTICE has an empty provenance list, its own
    remark records that the drill sheet's original paper was not found, and
    searching assets/attachments/ and the migration records finds no copy of the
    sheet, so there is no page to read and the printed statement could not be
    compared with a source document. What was checked here is the statement and
    its answer: the description of the region, the exchange of order and the evaluation, all of which were re-derived and agree with the printed region 0 <= y <= x <= 1
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The region, the reversed order of integration by Fubini, and the elementary evaluation.
---

::: {.problem}
Evaluate
$$
\int_0^1\int_y^1\sin(x^2)\,dx\,dy.
$$
:::

::: {.solution}

Write $D=\{(x,y):0\le y\le x\le1\}$ for the region of integration.

::: pf

::: {.pf-step #region}

The iterated integral $\int_0^1\int_y^1\sin(x^2)\,dx\,dy$ is the integral of
$\sin(x^2)$ over $D$.

::: pf-proof

For fixed $y\in[0,1]$ the inner integral runs over $x\in[y,1]$, so the
iterated integral is over the set of pairs $(x,y)$ with $0\le y\le1$ and $y\le
x\le1$, which is $D$; $D$ is a compact triangle, the integrand is continuous,
so the integral exists.

:::

:::

::: {.pf-step #swap}

$\displaystyle\int_0^1\int_y^1\sin(x^2)\,dx\,dy=\int_0^1x\sin(x^2)\,dx$.

::: pf-proof

$D$ is also described by $0\le x\le1$, $0\le y\le x$: the conditions $0\le
y\le x\le1$ are symmetric in their statement. The integrand is continuous on
the compact $D$, so Fubini's theorem lets the order be exchanged, and the
inner integral in $y$ is $\int_0^x\sin(x^2)\,dy=x\sin(x^2)$, since $\sin(x^2)$
does not depend on $y$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int_0^1\int_y^1\sin(x^2)\,dx\,dy=\frac{1-\cos1}{2}=\sin^2\!\left(\frac12\right)}$.

::: pf-proof

With $u=x^2$, $du=2x\,dx$, so $\int_0^1x\sin(x^2)\,dx=\frac12\int_0^1\sin
u\,du=\frac12[-\cos u]_0^1=\frac{1-\cos1}{2}$, using step [](#swap){.pf-ref}.
The half-angle identity $1-\cos1=2\sin^2\frac12$ rewrites this as
$\sin^2\frac12$.

:::

:::

:::


:::
