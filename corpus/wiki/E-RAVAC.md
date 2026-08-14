---
schema: qual/card@1
id: E-RAVAC
kind: exercise
title: "Let $f$ be entire, and discuss (with proofs and examples) the\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - singularities
  - essential-singularities
  - zeros
relations: []
review: draft
---

::: {.problem title="?"}
Let $f$ be entire, and discuss (with proofs and examples) the types of singularities $f$ might have (removable, pole, or essential) at $z=\infty$ in the following cases:

1. $f$ has at most finitely many zeros in $\CC$.

2. $f$ has infinitely many zeros in $\CC$.
:::

::: {.solution}
Write $f(z) = \sum_{k\geq 0} c_k z^k$ since it is entire.

- If $f$ has finitely many zeros, $f$ is nonconstant and entire, and thus unbounded by Liouville.
  If $f$ is nonconstant, $z=\infty$ can not be removable, since this would force $f$ to be constant.
  So $z=\infty$ can be a pole or an essential singularity.
  Both possibilities can occur: if $f$ is a polynomial, it is entire with finitely many zeros and a pole at $z=\infty$.
  Taking $f(z)= e^z$ has no zeros and an essential singularity at $z=\infty$.

- If $f$ has infinitely many zeros, if $f$ is nonconstant then infinitely many $c_k$ are nonzero -- otherwise $f$ is a polynomial and can only have finitely many zeros.
  Then $g(z) \da f(1/z) = \sum_{k\geq 0}{c_k\over z^k}$ has infinitely many nonzero terms, making $z=0$ an essential singularity for $g$ and $z=\infty$ essential for $f$.
:::
