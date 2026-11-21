---
schema: qual/card@1
id: E-MYMF4
kind: problem
title: The first homology of the connected sum of the projective plane and the torus
classification:
  areas:
  - topology
  topics:
  - Homology of Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §75 Exercise 1, printed p. 457. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-358724-E-MYMF4.md, read whole.
    Math StackExchange 358724, "connected sum of torus with projective plane" (asked by harlekin 2013-04-11),
    has two answers, neither a proof of this exercise. 358728 by xyzzyz (2013-04-11) is two sentences: it says
    to calculate the Euler characteristic, that the surface is non-orientable, and that the two together are
    a complete set of invariants; it computes no characteristic, exhibits no cell structure, and names no
    classification theorem. 568338 by Fang Hung-chien (2013-11-15) is a figure of the cut-and-paste, whose
    source is a handout by Emina Alibegovic, and it computes nothing. Neither proves H_1(P^2#T), which is the
    first half of the exercise, and neither proves the second half beyond naming its route. Both are recorded
    as sources searched, and the card keeps its own proof: the one-vertex cell structure of the 6-gon scheme
    aabc b^{-1}c^{-1} giving H_1 = Z^2 + Z/2, then chi = -1 with non-orientability in Theorem 77.5.
    Rejected in the search: mse 100825, a link only.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 75 Exercise 1, printed p. 457. H_1 from the one-vertex cell structure of the 8-gon scheme, giving Z^2 + Z/2, then chi = -1 and non-orientability give 3P^2 by Theorem 77.5. What was corrected: the identification cited "Dyck's Theorem / classification invariants"; the invariants are those of Theorem 77.5 and the card now cites it. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The computation is correct. P^2 # T is the 6-gon with word c c a b a^{-1}
    b^{-1}, that is, one 0-cell, three 1-cells and one 2-cell; abelianizing the
    attaching word gives 2c, so the image of the boundary map is 2Z inside
    Zc + Za + Zb and H_1 is Z/2 + Z^2, with H_0 = Z and H_2 = 0, which also
    matches chi = 1 - 3 + 1 = -1. For the identification, P^2 # T is
    non-orientable since it contains a Moebius band, and the connected sum
    formula gives chi = 1 + 0 - 2 = -1; a closed connected non-orientable
    surface kP^2 has chi = 2 - k, so k = 3, and Theorem 77.5 turns chi and
    orientability into the homeomorphism type. Nothing was changed.
---

::: {.exercise}

Calculate $H_1(P^2 \# T)$.
Assuming that the list of compact surfaces given in Theorem 75.5 is a complete list, to which of these surfaces is $P^2 \# T$ homeomorphic?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Cellular presentation and computation of $H_1(P^2 \# T)$:

::: pf-proof

::: pf-step

The connected sum $X = P^2 \# T$ admits a standard CW decomposition with one 0-cell, three 1-cells $c, a, b$, and one 2-cell attached along the boundary loop $c^2 [a, b] = c^2 a b a^{-1} b^{-1}$.

::: pf-proof

connected sum of polygonal schemas for $P^2$ ($c^2$) and $T$ ($aba^{-1}b^{-1}$).

:::

:::

::: pf-step

The cellular chain complex for $X$ is:
$$
0 \longrightarrow \ZZ \xrightarrow{\partial_2} \ZZ c \oplus \ZZ a \oplus \ZZ b \xrightarrow{\partial_1} \ZZ \longrightarrow 0.
$$

::: pf-proof

cellular homology definition.

:::

:::

::: pf-step

The boundary map $\partial_2: C_2(X) \to C_1(X)$ maps the generator of $C_2(X)$ to:
$$
\partial_2(e^2) = 2c + a + b - a - b = 2c.
$$

::: pf-proof

abelianizing the boundary loop word $c^2 a b a^{-1} b^{-1}$.

:::

:::

::: pf-step

The first homology group is:
$$
H_1(P^2 \# T) = \frac{\ZZ c \oplus \ZZ a \oplus \ZZ b}{\operatorname{im}(\partial_2)} = \frac{\ZZ c}{2\ZZ c} \oplus \ZZ a \oplus \ZZ b \cong \ZZ_2 \oplus \ZZ \oplus \ZZ \cong \ZZ^2 \oplus \ZZ_2.
$$

::: pf-proof

quotient of free abelian groups.

:::

:::

:::

:::

::: {.pf-step #s2}

Identification with standard compact surface:

::: pf-proof

::: pf-step

$P^2 \# T$ is non-orientable because it contains an embedded Möbius band from the $P^2$ summand.

::: pf-proof

non-orientability of $P^2$.

:::

:::

::: pf-step

Compute the Euler characteristic using $\chi(A \# B) = \chi(A) + \chi(B) - 2$:
$$
\chi(P^2 \# T) = \chi(P^2) + \chi(T) - 2 = 1 + 0 - 2 = -1.
$$

::: pf-proof

$\chi(P^2) = 1$ and $\chi(T) = 0$.

:::

:::

::: pf-step

By the Classification Theorem for compact surfaces, every closed connected non-orientable surface is homeomorphic to the connected sum of $k$ projective planes $k P^2 = P^2 \# \cdots \# P^2$, which has Euler characteristic $\chi(k P^2) = 2 - k$.

::: pf-proof

Theorem 75.5.

:::

:::

::: pf-step

Setting $2 - k = -1$ gives $k = 3$.
Thus $P^2 \# T \cong P^2 \# P^2 \# P^2 = 3P^2$, the connected sum of three projective planes.

::: pf-proof

Theorem 77.5 with the invariants $\chi$ and orientability.

:::

:::

:::

:::

::: pf-step

Conclusion:
$H_1(P^2 \# T) \cong \ZZ^2 \oplus \ZZ_2$, and $P^2 \# T$ is homeomorphic to $P^2 \# P^2 \# P^2$ ($3 P^2$). Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
