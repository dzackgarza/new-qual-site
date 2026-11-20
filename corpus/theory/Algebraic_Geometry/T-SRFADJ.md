---
schema: qual/card@1
id: T-SRFADJ
kind: theorem
title: The adjunction formula on a surface
slogan: 'Adjunction turns genus into intersection theory: $2g(C)-2=C\cdot(C+K_X)$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Adjunction
  - Intersection Theory
  - Canonical Divisor
relations:
- kind: uses
  target: D-SRFINT
review: draft
prompts:
- State the adjunction formula.
- Derive the degree-genus formula for plane curves.
- What is the canonical divisor of $\PP^2$, and its self-intersection?
---

::: {.theorem}
Let $C$ be a smooth integral curve on a smooth projective surface $X$.
Then
$$
\omega_C \cong (\omega_X \otimes \OO_X(C))\restrict_C,
\qquad
2g(C)-2=C\cdot(C+K_X).
$$
More generally, for any effective Cartier divisor $C$ on $X$,
$$
2p_a(C)-2=C\cdot(C+K_X).
$$
:::

::: {.proof}
Apply [@Har77, II.8.20] to the Cartier divisor $C$ on $X$: it identifies the canonical sheaf of $C$ with the restriction of the adjunction sheaf,
$$
\omega_C\cong(\omega_X\otimes\OO_X(C))\restrict_C .
$$
The degree of $\omega_C$ is $2g(C)-2$ [@Har77, Example IV.1.3.3], and for a divisor $D$ meeting $C$ transversally the degree of $\OO_X(D)\restrict_C$ is the intersection number $C\cdot D$ [@Har77, Lemma V.1.3]. Taking $D=C+K_X$, which may be moved into transverse position by the definition of the intersection pairing through the very ample case [@Har77, the proof of Proposition V.1.1], gives
$$
2g(C)-2=\deg_C\bigl((\omega_X\otimes\OO_X(C))\restrict_C\bigr)=C\cdot(C+K_X).
$$
For a general effective divisor the same display is taken as the definition of its arithmetic genus $p_a(C)\coloneqq1+\tfrac12\,C\cdot(C+K_X)$; for a nonsingular $C$ it is the computation above, and it agrees with the arithmetic genus of a projective variety defined as $(-1)^r(P(0)-1)$ from the Hilbert polynomial [@Har77, Exercise I.7.2].
:::

::: {.remark}
Adjunction converts genus calculations on surfaces into intersection-number calculations.

On $\PP^2$ it gives the degree-genus formula.
On $\PP^2$ one has $K = -3H$ and $H^2 = 1$, so $K^2 = 9$; for $C$ of degree $d$,
$$
2g-2 = C \cdot (C - 3H) = d^2 - 3d ,
$$
giving $g = \tfrac{1}{2}(d-1)(d-2)$.
On $\PP^1 \times \PP^1$, $K = (-2,-2)$ and the same computation gives $g = (a-1)(b-1)$ for a curve of type $(a,b)$.

In any dimension, for a smooth effective Cartier divisor $D$ on a smooth variety $X$,
$$
\omega_D\cong(\omega_X\otimes\OO_X(D))\restrict_D.
$$
:::
