---
schema: qual/card@1
id: PR-Y5S7V
kind: proposition
title: The degree of a divisor on a projective curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Degree
  - Curves
relations:
- kind: uses
  target: D-5PQ5W
review: draft
prompts:
- What is the degree of a divisor?
- Why does a principal divisor have degree zero?
---

::: {.definition}
For $D = \sum n_i P_i$ on a curve, $\deg D = \sum n_i [k(P_i) : k]$, which is $\sum n_i$ when $k = \bar{k}$.
:::

::: {.proposition}
On a smooth projective curve, $\deg \div(f) = 0$ for every $f \in K(X)^*$.
Degree therefore descends to a homomorphism $\Pic(X) \to \ZZ$, and $\Pic^0(X)$ is its kernel.
:::

::: {.remark}
The proof is worth knowing in one sentence, because it explains why projectivity is the hypothesis: a nonconstant $f$ is a finite morphism $X \to \PP^1$, and $\div(f) = f^*(0) - f^*(\infty)$, where both fibres have $\deg f$ points counted with multiplicity.
Zeros and poles balance because the map has a well-defined degree, and the map has one because $X$ is projective.

On $\AA^1$ the statement is false — $\div(x) = [0]$ has degree one — and this is the cleanest illustration that divisor theory is a theory about complete curves.
:::
