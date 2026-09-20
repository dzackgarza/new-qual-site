---
schema: qual/card@1
id: P-AGXVARNORMALPROJCURVE
kind: problem
title: Normal projective curves are smooth
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normality
  - Curves
  - Smoothness
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 8.1, Definitions 8.2, and the corresponding clause
    of Exercises 8.5 in the recorded source. The source defines projective
    normality and smoothness chartwise and asks, over C, that every normal
    projective curve be smooth.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's standing field C explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Reduced to the standard affine charts from Definition 8.2, checked that
    every nonempty chart is a normal affine curve, and applied the completed
    affine result P-AGXVARNORMALCURVE.
---

::: {.problem}
Show that every normal projective curve over $\CC$ is smooth.
:::

::: {.solution}
Let
$$
X\subseteq\PP^n_\CC
$$
be a normal projective curve, and let
$$
U_i=\{x_i\ne0\}\subseteq\PP^n_\CC,
\qquad
X_i=X\intersect U_i.
$$
The nonempty $X_i$ form an affine open cover of $X$.

<1>1. Every nonempty chart $X_i$ is a normal affine curve over $\CC$.

::: {.proof}
By the projective normality definition in the source, each affine chart
$X_i$ is normal.

Since $X$ is an irreducible projective curve, every nonempty open subset of
$X$ is irreducible and has the same dimension as $X$. Hence every nonempty
$X_i$ has dimension $1$. Thus each $X_i$ is a normal affine curve over
$\CC$.
:::

<1>2. Every nonempty chart $X_i$ is smooth.

::: {.proof}
Step <1>1 shows that $X_i$ is a normal affine curve over $\CC$. Therefore
[[P-AGXVARNORMALCURVE|the affine normal-curve result]] gives that $X_i$ is
smooth.
:::

<1>3. The projective curve $X$ is smooth.

::: {.proof}
The charts $X_i$ cover $X$, and by step <1>2 every nonempty chart is smooth.
Smoothness is local on the source, so every point of $X$ is smooth. Hence
$$
\boxed{X\text{ is smooth}.}
$$
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 reduce projective normality chartwise to the smoothness of
normal affine curves.
:::
:::
