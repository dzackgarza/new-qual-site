---
schema: qual/card@1
id: E-SS2.EX-15
kind: problem
title: A nonvanishing function holomorphic on the disc with $\abs f=1$ on the circle is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the maximum principle applied to $f$ and to $1/f$ (which is legitimate because $f$ never vanishes on $\overline{\DD}$), the resulting equality $\lvert f\rvert=1$ in the disc, and the open mapping theorem contradiction with $f(\DD)\subset\partial\DD$.
---

::: {.exercise}
Suppose $f$ is a non-vanishing continuous function on $\overline{\DD}$ that is holomorphic in $\DD$. Prove that if
$$
\abs{f(z)} = 1 \quad \text{whenever } \abs{z} = 1,
$$
then $f$ is constant.

[Hint: Extend $f$ to all of $\CC$ by $f(z) = 1/\overline{f(1/\overline{z})}$ whenever $\abs{z} > 1$, and argue as in the Schwarz reflection principle.]
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own.

::: pf

::: {.pf-step #upper}
$\abs{f(z)}\le1$ for $z\in\DD$.

::: pf-proof
$f$ is holomorphic on $\DD$ and continuous on $\overline\DD$ with $\abs f=1$ on the boundary circle, so by the maximum-modulus principle $\abs f$ attains its maximum on the boundary and $\abs{f(z)}\le1$ inside.
:::
:::

::: {.pf-step #reciprocal}
$1/f$ is holomorphic on $\DD$ and continuous on $\overline\DD$, with $\abs{1/f}=1$ on the circle.

::: pf-proof
$f$ is non-vanishing on $\overline\DD$, so $1/f$ is defined and continuous there and holomorphic in the disc; on $\abs z=1$ we have $\abs f=1$, hence $\abs{1/f}=1$.
:::
:::

::: {.pf-step #lower}
$\abs{f(z)}\ge1$ for $z\in\DD$.

::: pf-proof
Applying the maximum-modulus principle to $1/f$ gives $1/\abs{f(z)}\le1$ in the disc, which is the assertion.
:::
:::

::: {.pf-step #constant}
$f$ is constant.

::: pf-proof
By the two bounds $\abs{f(z)}=1$ throughout $\DD$, so $f(\DD)$ lies in the unit circle. If $f$ were non-constant, the open mapping theorem would make $f(\DD)$ open in $\CC$, but the circle has empty interior, a contradiction; hence $f$ is constant, and being continuous on $\overline\DD$ it is that constant there too.
:::
:::

:::
:::
