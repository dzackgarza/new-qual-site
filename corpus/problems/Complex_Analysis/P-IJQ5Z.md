---
schema: qual/card@1
id: P-IJQ5Z
kind: problem
title: A conformal map from $\CC\setminus(-\infty,0]$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Construct an explicit conformal map (biholomorphic equivalence) from the slit plane $\Omega = \CC \setminus (-\infty, 0]$ onto the open unit disk $\DD = \{w \in \CC \mid \abs{w} < 1\}$.
:::

::: {.solution}
Write $H = \{u : \Re u > 0\}$ for the right half-plane, and for $z = re^{i\theta} \in \Omega$ with $-\pi < \theta < \pi$ let $\sqrt z = \sqrt r\, e^{i\theta/2}$ be the principal square root.

::: pf

::: {.pf-step #sqrt}
$z \mapsto \sqrt z$ is a biholomorphism $\Omega \to H$.

::: pf-proof
The principal square root is holomorphic on $\Omega$, and $-\pi/2 < \arg\sqrt z < \pi/2$, so $\sqrt z \in H$.
Its inverse $u \mapsto u^2$ maps $H$ into $\Omega$, because $\abs{\arg u} < \pi/2$ gives $\abs{\arg u^2} < \pi$.
:::

:::

::: {.pf-step #cayley}
The Cayley transform $C(u) = \frac{u-1}{u+1}$ is a biholomorphism $H \to \DD$.

::: pf-proof
For $u = x+iy$ with $x > 0$,
$$
\abs{C(u)}^2 = \frac{(x-1)^2+y^2}{(x+1)^2+y^2} < 1.
$$
Its inverse $w \mapsto \frac{1+w}{1-w}$ maps $\DD$ into $H$, since $\Re\frac{1+w}{1-w} = \frac{1-\abs{w}^2}{\abs{1-w}^2} > 0$ for $\abs{w} < 1$.
:::

:::

::: pf-step
$$
\boxed{F(z)=\frac{\sqrt z-1}{\sqrt z+1}}
$$
is a conformal bijection $\Omega\to\DD$, with inverse $F^{-1}(w)=\left(\frac{1+w}{1-w}\right)^2$.

::: pf-proof
$F = C \circ \sqrt{\cdot}$ is a composition of the biholomorphisms of steps [](#sqrt){.pf-ref} and [](#cayley){.pf-ref}, and its inverse is the composition of their inverses.
:::

:::

:::
:::
