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

::: {.problem}
Let $U \subset \mathbb{C}$ be an open set and $f$ a continuous function on $U$.
Assume $f^2$ is analytic on $U$.
Prove $f$ is analytic on $U$.
:::

::: {.solution}

::: pf

::: pf-step

Let $Z = \{z \in U : f(z) = 0\}$ be the zero set of $f$.

::: pf-proof

definition.

:::

:::

::: {.pf-step #s2}

On $U \setminus Z$, $f$ is nonzero, and $f = f^2/f$ is the quotient of two analytic functions, hence analytic.

::: pf-proof

$f^2$ is analytic and $f$ is nonzero (so $1/f = f/f^2$ is analytic where $f \neq 0$).

:::

:::

::: {.pf-step #s3}

At a point $z_0 \in Z$, if $f$ is identically zero in a neighborhood of $z_0$, then $f$ is analytic there (it is the zero function).

::: pf-proof

the zero function is analytic.

:::

:::

::: pf-step

Otherwise, $z_0$ is an isolated zero of $f$ (since $f^2$ is analytic and not identically zero, its zeros are isolated, and $f$ and $f^2$ have the same zeros).

::: pf-proof

the zeros of the analytic function $f^2$ are isolated (unless $f^2 \equiv 0$).

:::

:::

::: {.pf-step #s5}

Near an isolated zero $z_0$, $f$ is continuous and $f^2$ is analytic with a zero of some order $2m$; then $f$ has a removable singularity at $z_0$ (it is bounded near $z_0$ since $f$ is continuous), and $f$ extends analytically.

::: pf-proof

$f$ is continuous, hence bounded near $z_0$, so any singularity is removable; and $f = \pm \sqrt{f^2}$ locally (choosing a consistent branch), which is analytic.

:::

:::

::: {.pf-step #s6}

Hence $f$ is analytic on all of $U$.

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
