---
schema: qual/card@1
id: P-UGR7G
kind: problem
title: Evaluate $\int\frac{1}{9+x^2}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int\frac{dx}{9+x^2}.
\]
:::

::: solution
With $u=x/3$, $dx=3\,du$,
\[
\int\frac{dx}{9+x^2}
=\frac13\int\frac{du}{1+u^2}
=\boxed{\frac13\arctan\!\left(\frac x3\right)+C.}
\]
:::
