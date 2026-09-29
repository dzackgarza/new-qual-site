---
schema: qual/card@1
id: E-HAT-1.2-13
kind: problem
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

::: {.problem}
The space $Y$ in the preceding exercise can be obtained from a disk with two holes by identifying its three boundary circles.
There are only two essentially different ways of identifying the three boundary circles.
Show that the other way yields a space $Z$ with $\pi_1(Z)$ not isomorphic to $\pi_1(Y)$.
[Abelianize the fundamental groups to show they are not isomorphic.]
:::

::: {.solution}
::: pf

::: pf-step
$Y$ has $\pi_1(Y) = \langle a, b, c \mid aba^{-1}b^{-1}cb^\varepsilon c^{-1}\rangle$ (from the preceding exercise).

::: pf-proof
given.
:::

:::

::: {.pf-step #s2}
$H_1(Y) = \ZZ^2$.

::: pf-proof

::: {.pf-step #s2-1}
Abelianizing the relation $aba^{-1}b^{-1}cb^\varepsilon c^{-1} = 1$ gives $b^\varepsilon = 1$.

::: pf-proof
in the abelianization, $aba^{-1}b^{-1} = 1$ and $cb^\varepsilon c^{-1} = b^\varepsilon$, so the relation becomes $b^\varepsilon = 1$.
:::

:::

::: {.pf-step #s2-2}
Hence $b = 1$ in $H_1(Y)$ (since $\varepsilon = \pm 1$).

::: pf-proof
step [](#s2-1){.pf-ref}.
:::

:::

::: pf-step
Therefore $H_1(Y) = \langle a, b, c \mid b = 1\rangle = \ZZ^2$ (free abelian on $a$ and $c$).

::: pf-proof
step [](#s2-2){.pf-ref}.
:::

:::

:::

:::

::: pf-step
The other identification yields $Z$, the nonorientable surface of genus $3$ (the connected sum of three projective planes), with $\pi_1(Z) = \langle a, b, c \mid a^2 b^2 c^2\rangle$.

::: pf-proof
identifying the three boundary circles of a disk with two holes in the other (nonorientable, boundary-closing) way produces the closed nonorientable surface $N_3$, whose fundamental group has the standard presentation $\langle a,b,c \mid a^2b^2c^2 = 1\rangle$.
:::

:::

::: {.pf-step #s4}
$H_1(Z) = \ZZ^2 \oplus \ZZ/2$.

::: pf-proof

::: pf-step
Abelianizing $a^2 b^2 c^2 = 1$ gives $2a + 2b + 2c = 0$, i.e. $2(a+b+c) = 0$.

::: pf-proof
additive notation in the abelianization.
:::

:::

::: pf-step
Hence $H_1(Z) = \langle a, b, c \mid 2(a+b+c) = 0\rangle \cong \ZZ^2 \oplus \ZZ/2$.

::: pf-proof
the single relation $2(a+b+c) = 0$ introduces one $\ZZ/2$ torsion summand, leaving free rank $2$.
:::

:::

:::

:::

::: {.pf-step #s5}
$H_1(Y) = \ZZ^2 \not\cong \ZZ^2 \oplus \ZZ/2 = H_1(Z)$.

::: pf-proof
steps [](#s2){.pf-ref} and [](#s4){.pf-ref}; one is torsion-free, the other has a $\ZZ/2$ summand.
:::

:::

::: {.pf-step #s6}
Hence $\pi_1(Y) \not\cong \pi_1(Z)$.

::: pf-proof
isomorphic groups have isomorphic abelianizations, but step [](#s5){.pf-ref} shows the abelianizations differ.
:::

:::

::: pf-qed
step [](#s6){.pf-ref}.
:::

:::
:::
