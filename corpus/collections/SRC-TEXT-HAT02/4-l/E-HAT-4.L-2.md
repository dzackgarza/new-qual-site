---
schema: qual/card@1
id: E-HAT-4.L-2
kind: problem
title: Cohomology operations distinguish quotients
classification:
  areas:
  - topology
  topics:
  - Steenrod Squares
  - Cohomology Operations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.L, Exercise 2 and the current corrections; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.L, printed p. 517, with the Künneth theorem over a
    field (Corollary 3B.7, p. 276) and the Cartan formula and instability (Theorem 4L.12, p. 504).
    Correct. For $X$, $\widetilde H^*(X;\ZZ_2)=\Lambda(a)\otimes\ZZ_2[x]$ with $|a|=1$, $|x|=2$, so
    the unique nonzero class in degree three is $u=a\times x$; the Cartan formula gives
    $Sq^2(u)=Sq^2a\times x+Sq^1a\times Sq^1x+a\times Sq^2x=a\times x^2\ne0$, since $Sq^1a=a^2=0$
    and $Sq^2a=0$ by instability while $Sq^2x=x^2$. For $Y=S^3\times\CP^\infty$ the unique nonzero
    degree-three class is $v=\operatorname{pr}_1^*\iota_3$ and naturality gives
    $Sq^2(v)=\operatorname{pr}_1^*(Sq^2\iota_3)=0$ because $H^5(S^3;\ZZ_2)=0$. A homotopy
    equivalence would carry $u$ to $v$ and commute with $Sq^2$, so the two computations separate
    the spaces. Nothing changed. Not claimed: a published solution, and no certificate.
---

::: {.problem}
Use cohomology operations to show that the spaces $(S^1 \times \CP^\infty) / (S^1 \times \{x_0\})$ and $S^3 \times \CP^\infty$ are not homotopy equivalent.
:::

::: {.solution}
Put
$$
X=(S^1\times\CP^\infty)/(S^1\times\{x_0\}),
\qquad
Y=S^3\times\CP^\infty.
$$
With $\ZZ_2$-coefficients, the Künneth theorem over a field (Corollary 3B.7, p. 276) applied to the pair $(S^1\times\CP^\infty, S^1\times\{x_0\})$ gives
$$
\widetilde H^*(X;\ZZ_2)
\cong
H^*(S^1;\ZZ_2)\otimes
\widetilde H^*(\CP^\infty;\ZZ_2).
$$
Let
$$
a\in H^1(S^1;\ZZ_2),
\qquad
x\in H^2(\CP^\infty;\ZZ_2)
$$
be the standard generators. Then the unique nonzero class in $H^3(X;\ZZ_2)$ is
$$
u=a\times x.
$$
Using the Cartan formula (Theorem 4L.12, p. 504),
$$
Sq^2(u)
=Sq^2(a\times x)
=a\times Sq^2x,
$$
since $Sq^1a=a^2=0$ and $Sq^2a=0$ by instability. For the degree-two generator of $\CP^\infty$ the unstable property of Theorem 4L.12 (p. 504) gives
$$
Sq^2x=x^2,
$$
and $Sq^1a=Sq^2a=0$, $a^2=0$ similarly.
Hence
$$
Sq^2(u)=a\times x^2\ne0
\in H^5(X;\ZZ_2).
\tag{1}
$$

On the other hand, the unique nonzero class in $H^3(Y;\ZZ_2)$ is the pullback
$$
v=\operatorname{pr}_1^*(\iota_3)
$$
of the fundamental class of $S^3$. Naturality gives
$$
Sq^2(v)=\operatorname{pr}_1^*(Sq^2\iota_3)=0,
\tag{2}
$$
because $H^5(S^3;\ZZ_2)=0$.

Any homotopy equivalence $X\simeq Y$ would induce an isomorphism on mod-2 cohomology carrying the unique nonzero degree-three class to the unique nonzero degree-three class and commuting with $Sq^2$. Equations (1) and (2) contradict this. Therefore
$$
\boxed{X\not\simeq S^3\times\CP^\infty.}
$$
:::
