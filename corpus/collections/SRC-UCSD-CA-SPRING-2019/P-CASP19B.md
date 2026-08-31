---
schema: qual/card@1
id: P-CASP19B
kind: problem
title: "Continuous function whose square is analytic is analytic"
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Functions
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $U \subset \mathbb{C}$ be an open set and $f$ a continuous function on $U$.
Assume $f^2$ is analytic on $U$.
Prove $f$ is analytic on $U$.
:::

::: {.solution}
<1>1. Let $Z = \{z \in U : f(z) = 0\}$ be the zero set of $f$.
::: {.proof}
definition.
:::

<1>2. On $U \setminus Z$, $f$ is nonzero, and $f = f^2/f$ is the quotient of two analytic functions, hence analytic.
::: {.proof}
$f^2$ is analytic and $f$ is nonzero (so $1/f = f/f^2$ is analytic where $f \neq 0$).
:::

<1>3. At a point $z_0 \in Z$, if $f$ is identically zero in a neighborhood of $z_0$, then $f$ is analytic there (it is the zero function).
::: {.proof}
the zero function is analytic.
:::

<1>4. Otherwise, $z_0$ is an isolated zero of $f$ (since $f^2$ is analytic and not identically zero, its zeros are isolated, and $f$ and $f^2$ have the same zeros).
::: {.proof}
the zeros of the analytic function $f^2$ are isolated (unless $f^2 \equiv 0$).
:::

<1>5. Near an isolated zero $z_0$, $f$ is continuous and $f^2$ is analytic with a zero of some order $2m$; then $f$ has a removable singularity at $z_0$ (it is bounded near $z_0$ since $f$ is continuous), and $f$ extends analytically.
::: {.proof}
$f$ is continuous, hence bounded near $z_0$, so any singularity is removable; and $f = \pm \sqrt{f^2}$ locally (choosing a consistent branch), which is analytic.
:::

<1>6. Hence $f$ is analytic on all of $U$.
::: {.proof}
<1>2, <1>3, <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
