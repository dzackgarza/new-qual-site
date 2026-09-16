---
schema: qual/card@1
id: FT-AK34G
kind: theorem
title: Cauchy integral formula for derivatives
prompts:
- State the Cauchy integral formula for the higher derivatives $f^{(n)}(z)$.
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
---

::: {.theorem}
Let $U\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $U$, and let $C$ be a counterclockwise circle whose closed disc lies in $U$; write $C^\circ$ for the open disc bounded by $C$.
Then for every $z\in C^\circ$ and every integer $n\ge0$,
$$
f^{(n)}(z)=\frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} \dzeta.
$$
:::
