---
schema: qual/card@1
id: P-WESTOP04-05
kind: problem
title: Classify a surface obtained from a labeled hexagon
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: "Direct inspection of page 3 of assets/attachments/topology_2005-2003.pdf confirms that the printed cyclic word is abaca^{-1}c^{-1}. Thus the source itself is inconsistent with its instruction to identify the six edges in pairs: a occurs three times, b once, and c twice."
---

::: {.problem}
1. List the compact connected surfaces up to homeomorphism.

2. Form a surface from a hexagon by identifying its boundary edges in pairs according to the cyclic word recovered as
   \[
   abac a^{-1}c^{-1},
   \]
   and identify the resulting compact connected surface.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The compact connected surfaces are, up to homeomorphism,
$$
\boxed{
S^2,qquad
\#^g(S^1\times S^1)\ (g\ge1),qquad
\#^k\mathbb{RP}^2\ (k\ge1).}
$$


::: pf-proof

This is the classification theorem for compact connected surfaces.
The orientable surfaces are the sphere and the connected sums of
$$
g
$$
tori.
The nonorientable surfaces are the connected sums of
$$
k
$$
real projective planes.

:::

:::

::: {.pf-step #s1-2}

A hexagon whose six boundary edges are to be identified in pairs must have each edge-pair label occur exactly twice in the boundary word.


::: pf-proof

Pairwise edge identification partitions the six boundary edges into three two-element subsets.

If the usual polygon-word notation labels the two members of one pair by the same letter, with an inverse exponent recording reversal of orientation, then every label necessarily appears exactly twice.

:::

:::

::: {.pf-step #s1-3}

In the printed source word
$$
w
=
abaca^{-1}c^{-1},
$$
the multiplicities of the labels are
$$
\boxed{
\#a=3,qquad
\#b=1,qquad
\#c=2.}
$$


::: pf-proof

Reading the six letters in order gives
$$
a, b, a, c, a^{-1}, c^{-1}.
$$
Thus three boundary edges carry the label
$$
a,
$$
one carries
$$
b,
$$
and two carry
$$
c.
$$
The inverse signs affect orientation, not which label occurs.

:::

:::

::: {.pf-step #s1-4}

Therefore the printed data do not specify a pairing of the six boundary edges.


::: pf-proof

By step [](#s1-2){.pf-ref}, every label in a valid pair-identification word must occur exactly twice.
Step [](#s1-3){.pf-ref} violates this condition for both
$$
a
$$
and
$$
b.
$$

In particular, one cannot partition the three
$$
a
$$
-edges into pairs, and the lone
$$
b
$$
-edge has no partner.

:::

:::

::: {.pf-step #s1-5}

Consequently, no quotient surface is determined by the problem as printed.


::: pf-proof

The requested quotient depends on an equivalence relation pairing boundary edges.
Step [](#s1-4){.pf-ref} shows that the printed labeling does not define such an equivalence relation.

Different corrections of the apparent typo can lead to different polygon words and hence to different quotient surfaces.
Therefore a particular compact connected surface cannot be inferred uniquely from the retained source.

:::

:::

::: {.pf-step #s1-6}

Hence the complete answer to the printed problem is:
$$
\boxed{
\text{Part (1) is the standard surface-classification list above, while
part (2) is not well-posed as printed.}}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} answers the classification request.
Steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} prove that the stated boundary word cannot encode the claimed pairwise edge identification, so there is no mathematically determined surface to classify without an external correction to the statement.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the complete mathematically valid disposition of both parts.

:::

:::

:::
