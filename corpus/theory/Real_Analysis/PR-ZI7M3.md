---
schema: qual/card@1
id: PR-ZI7M3
kind: proposition
title: Parseval's identity
slogan: 'For an orthonormal basis $(e_k)$ of $H$, $\norm{x}^2=\sum_k\abs{\inner{x}{e_k}}^2$ for every $x\in H$.'
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Bases
relations: []
review: draft
---

::: {.proposition}
Let $H$ be a [[D-7QQUO|Hilbert space]] and let $(e_k)_{k\geq 1}$ be an [[D-4IXAO|orthonormal]] sequence in $H$ that is a [[D-AQX7W|basis]] of $H$.
Then for every $x\in H$,
$$
\sum_{k\geq 1} \abs{ \inner{x}{e_k} }^2 = \norm{x}^2.
$$
:::

::: {.remark}
This is the case of equality in Bessel's inequality [[T-4BDE3]].
For an orthonormal sequence, being a basis is equivalent to being [[D-SLYE5|complete]]; see [[T-5AALA]].
:::
