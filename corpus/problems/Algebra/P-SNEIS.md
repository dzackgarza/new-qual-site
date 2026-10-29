---
schema: qual/card@1
id: P-SNEIS
kind: problem
title: 'Fundamental theorem of cosets: $xH=yH\iff x^{-1}y\in H\iff y^{-1}x\in H$'
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.problem}
Let $H\le G$. Prove that
$$
xH=yH\iff x^{-1}y\in H\iff y^{-1}x\in H.
$$
:::

::: {.solution}

::: pf

::: pf-step

If $xH=yH$, then $x^{-1}y\in H$.

::: pf-proof

Since $y=ye\in yH=xH$, there is $h\in H$ with $y=xh$, so $x^{-1}y=h\in H$.

:::

:::

::: pf-step

If $x^{-1}y\in H$, then $xH=yH$.

::: pf-proof

Write $x^{-1}y=h\in H$. Then $y=xh$, and $yH=xhH=xH$ because $hH=H$.

:::

:::

::: pf-qed

Since $H$ is closed under inverses, $x^{-1}y\in H$ if and only if $(x^{-1}y)^{-1}=y^{-1}x\in H$. Together with the first two steps, all three conditions are equivalent.

:::

:::

:::
