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
The degree of $\omega_C$ is $2g(C)-2$ [@Har77, Example IV.1.3.3], and for every divisor $D$ on $X$ the degree of $\OO_X(D)\restrict_C$ is the intersection number $C\cdot D$: the identification is Lemma V.1.3 for $D$ meeting $C$ transversally, and the general case follows by linearity from the very ample case, which is how the pairing is defined in the proof of [@Har77, Proposition V.1.1]. Taking $D=C+K_X$ gives
$$
2g(C)-2=\deg_C\bigl((\omega_X\otimes\OO_X(C))\restrict_C\bigr)=C\cdot(C+K_X).
$$
For a general effective divisor $C$ the display is not a definition but the content of [@Har77, Exercise V.1.3(a)]: the arithmetic genus is defined as $p_a(C)=1-\chi(\OO_C)$, and the identity $2p_a(C)-2=C\cdot(C+K_X)$ is proved there from Riemann--Roch and the sequence just used. In full: from $0\to\OO_X(-C)\to\OO_X\to\OO_C\to0$ additivity of the Euler characteristic gives $\chi(\OO_C)=\chi(\OO_X)-\chi(\OO_X(-C))$, and Riemann--Roch [@Har77, Theorem V.1.6] applied to $-C$ gives
$$
\chi(\OO_X(-C))=\tfrac12(-C)\cdot(-C-K_X)+1+p_a=\tfrac12\,C\cdot(C+K_X)+1+p_a ,
$$
while $\chi(\OO_X)=1+p_a$; hence $\chi(\OO_C)=-\tfrac12\,C\cdot(C+K_X)$ and $2p_a(C)-2=C\cdot(C+K_X)$, which is [@Har77, Exercise V.1.3(a)]; part (c) of that exercise extends the formula to an arbitrary divisor as the definition of the virtual arithmetic genus.
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
