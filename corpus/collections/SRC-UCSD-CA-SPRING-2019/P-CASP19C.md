---
schema: qual/card@1
id: P-CASP19C
kind: problem
title: 'A holomorphic function on $B(0,1+\varepsilon)$ with $\abs f<1$ on $\abs z=1$ has a unique fixed point in $\DD$'
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Rouché
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. The source is a course examination, so there is no retained
    solution set behind the card and the problem statement is the source. Each step re-read: z - f
    is holomorphic on a neighbourhood of the closed disc because epsilon > 0; |g - z| = |f| < 1 =
    |z| on the circle; Rouche then identifies the number of zeros of g inside with that of z; and
    z has a single simple zero. The card records why each hypothesis is needed. Not claimed: any
    statement when |f| = 1 somewhere on the circle, where the fixed point may fail to exist.
---

::: {.problem}
Let $f$ be an analytic function on the open disk $B(0, 1 + \varepsilon)$ for some $\varepsilon > 0$.
Assume that $\abs{f(z)} < 1$ for all $\abs{z} = 1$.
Prove that there exists a **unique fixed point** $z_0 \in \DD$ (i.e. $\abs{z_0} < 1$ and $f(z_0) = z_0$).
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #g}
$g(z)=z-f(z)$ is holomorphic on $B(0,1+\varepsilon)$, hence on a neighbourhood of the closed unit disc.

::: pf-proof
$f$ is holomorphic on $B(0,1+\varepsilon)$ by hypothesis and $z$ is entire, so $g$ is holomorphic there; since $\varepsilon>0$, that disc contains $\overline{\DD}$.
:::

:::

::: {.pf-step #rouche}
$\abs{g(z)-z}< \abs{z}$ for $\abs{z}=1$.

::: pf-proof
$g(z)-z=-f(z)$, so $\abs{g(z)-z}=\abs{f(z)}<1=\abs{z}$ on the unit circle, by the hypothesis.
:::

:::

::: {.pf-step #zeros}
$g$ and $z$ have the same number of zeros in $\DD$, counted with multiplicity.

::: pf-proof
This is Rouché's theorem applied to the functions $z$ and $g$ on the disc $\DD$: both are holomorphic on a neighbourhood of the closed disc by step [](#g){.pf-ref}, and the strict inequality on the boundary is step [](#rouche){.pf-ref}.
:::

:::

::: {.pf-step #fixed}
$g$ has exactly one zero in $\DD$, and it is simple.

::: pf-proof
$z$ has exactly one zero in $\DD$, at $0$, and it is simple; by step [](#zeros){.pf-ref} the same holds for $g$. So there is exactly one $z_{0}\in\DD$ with $z_{0}-f(z_{0})=0$.
:::

:::

::: {.pf-step}
$f$ has a unique fixed point in $\DD$.

::: pf-proof
Step [](#fixed){.pf-ref} gives that $f(z_{0})=z_{0}$ for exactly one $z_{0}$ with $\abs{z_{0}}<1$:
$$
\boxed{\exists!\,z_{0}\in\DD\text{ with }f(z_{0})=z_{0}.}
$$
The hypothesis $\varepsilon>0$ is what makes $g$ holomorphic on the closed disc, and the strict inequality on the circle is what lets Rouché count inside; neither can be dropped.
:::

:::

:::
:::
