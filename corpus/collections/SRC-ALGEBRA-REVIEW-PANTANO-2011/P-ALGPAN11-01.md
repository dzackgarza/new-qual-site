---
schema: qual/card@1
id: P-ALGPAN11-01
kind: problem
title: Inverse of a product in a group with torsion relations
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Reversed and inverted the product and reduced exponents modulo the given element orders.
---

::: {.problem}
If $b$ and $c$ are elements in a group $G$, and if $b^5=c^3=e$, where $e$ is the unit element of $G$, then the inverse of $b^2cb^4c^2$ must be

(A) $b^3c^2bc$
(B) $b^4c^2b^2c$
(C) $c^2b^4cb^2$
(D) $cb^2c^2b^4$
(E) $cbc^2b^3$
:::

::: {.solution}
For any product $x_1x_2\cdots x_r$,
$$
(x_1x_2\cdots x_r)^{-1}=x_r^{-1}\cdots x_2^{-1}x_1^{-1}.
$$
Therefore
$$
(b^2cb^4c^2)^{-1}
=c^{-2}b^{-4}c^{-1}b^{-2}.
$$
Using $c^3=e$ and $b^5=e$,
$$
c^{-2}=c,
\qquad
c^{-1}=c^2,
\qquad
b^{-4}=b,
\qquad
b^{-2}=b^3.
$$
Hence
$$
\boxed{(b^2cb^4c^2)^{-1}=cb\,c^2b^3}.
$$
:::
