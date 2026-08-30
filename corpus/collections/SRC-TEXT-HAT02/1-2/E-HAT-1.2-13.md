---
schema: qual/card@1
id: E-HAT-1.2-13
kind: exercise
title: Two ways to identify boundary circles of disk with two holes give non-isomorphic fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

The space $Y$ in the preceding exercise can be obtained from a disk with two holes by identifying its three boundary circles.
There are only two essentially different ways of identifying the three boundary circles.
Show that the other way yields a space $Z$ with $\pi_1(Z)$ not isomorphic to $\pi_1(Y)$.
[Abelianize the fundamental groups to show they are not isomorphic.]

::: {.solution}
<1>1. $Y$ has $\pi_1(Y) = \langle a, b, c \mid aba^{-1}b^{-1}cb^\varepsilon c^{-1}\rangle$ (from the preceding exercise).
Proof: given.

<1>2. $H_1(Y) = \ZZ^2$.
<2>1. Abelianizing the relation $aba^{-1}b^{-1}cb^\varepsilon c^{-1} = 1$ gives $b^\varepsilon = 1$.
Proof: in the abelianization, $aba^{-1}b^{-1} = 1$ and $cb^\varepsilon c^{-1} = b^\varepsilon$, so the relation becomes $b^\varepsilon = 1$.
<2>2. Hence $b = 1$ in $H_1(Y)$ (since $\varepsilon = \pm 1$). Proof: <2>1. <2>3. Therefore $H_1(Y) = \langle a, b, c \mid b = 1\rangle = \ZZ^2$ (free abelian on $a$ and $c$). Proof: <2>2.

<1>3. The other identification yields $Z$, the nonorientable surface of genus $3$ (the connected sum of three projective planes), with $\pi_1(Z) = \langle a, b, c \mid a^2 b^2 c^2\rangle$.
Proof: identifying the three boundary circles of a disk with two holes in the other (nonorientable, boundary-closing) way produces the closed nonorientable surface $N_3$, whose fundamental group has the standard presentation $\langle a,b,c \mid a^2b^2c^2 = 1\rangle$.

<1>4. $H_1(Z) = \ZZ^2 \oplus \ZZ/2$.
<2>1. Abelianizing $a^2 b^2 c^2 = 1$ gives $2a + 2b + 2c = 0$, i.e. $2(a+b+c) = 0$.
Proof: additive notation in the abelianization.
<2>2. Hence $H_1(Z) = \langle a, b, c \mid 2(a+b+c) = 0\rangle \cong \ZZ^2 \oplus \ZZ/2$.
Proof: the single relation $2(a+b+c) = 0$ introduces one $\ZZ/2$ torsion summand, leaving free rank $2$.

<1>5. $H_1(Y) = \ZZ^2 \not\cong \ZZ^2 \oplus \ZZ/2 = H_1(Z)$.
Proof: <1>2 and <1>4; one is torsion-free, the other has a $\ZZ/2$ summand.

<1>6. Hence $\pi_1(Y) \not\cong \pi_1(Z)$.
Proof: isomorphic groups have isomorphic abelianizations, but <1>5 shows the abelianizations differ.

<1>7. Q.E.D. Proof: <1>6.
:::
