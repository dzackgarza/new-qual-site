---
schema: qual/card@1
id: T-MWDVL
kind: theorem
title: Riemann--Roch and Serre duality on a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Serre Duality
  - Curves
relations:
- kind: uses
  target: PR-Y5S7V
- kind: uses
  target: T-IJW1K
review: draft
prompts:
- State Riemann--Roch.
- State Serre duality for a curve.
- What is the dimension of the space of holomorphic differentials on a curve of genus $g$?
---

::: {.theorem title="Riemann--Roch"}
For $D$ a divisor on a smooth projective curve $X$ of genus $g$ over $k = \bar{k}$,
\[
\ell(D) - \ell(K - D) = \deg D + 1 - g ,
\]
where $\ell(D) = h^0(X, \OO(D))$ and $K$ is a canonical divisor [@Har10a, Theorem IV.1.3].
:::

::: {.theorem title="Serre duality"}
$H^1(X, \OO(D)) \cong H^0(X, \OO(K-D))\dual$, so $\ell(K-D) = h^1(D)$ and Riemann--Roch reads
\[
\chi(\OO(D)) = \deg D + 1 - g .
\]
:::

::: {.remark}
Over a field $k$ that is not algebraically closed, adding a closed point $P$ to $D$ raises $\chi(\OO(D))$ by $\deg P = [\kappa(P) : k]$, and the formula reads $\chi(\OO(D)) = \deg D + \chi(\OO_X)$ with $\deg D = \sum n_P \deg P$ ([[D-CRVDEGREES]]).
:::

::: {.remark}
The second form is the one to state first when asked, because it says what the theorem is: the Euler characteristic is linear in the divisor, and the genus is the constant of integration.
Duality is what converts the unknown $h^1$ into a countable $h^0$.

Two immediate consequences, both asked:

- $D = 0$ gives $\ell(K) = g$: the space of global regular differentials on a curve of genus $g$ has dimension exactly $g$.
  This is the answer to the question about holomorphic differentials on a Riemann surface, and it is also how $g$ can be *defined* so that Riemann--Roch becomes a statement rather than a tautology.

- $D = K$ gives $\deg K = 2g-2$, which is the input to Riemann--Hurwitz and to every genus computation.

For $\deg D > 2g - 2$ the correction term vanishes and $\ell(D) = \deg D + 1 - g$ exactly; this is the range in which everything is computable and where "very ample" questions are settled.
:::
