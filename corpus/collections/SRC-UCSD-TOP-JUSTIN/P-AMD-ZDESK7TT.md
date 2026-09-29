---
schema: qual/card@1
id: P-AMD-ZDESK7TT
kind: problem
title: Word for the genus-$g$ orientable surface
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Classification
relations: []
review: draft
---

::: {.problem}
Orientable surface of genus $g$

1. $g=2$ is given by $a+b-a-b+c+d-c-d$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A closed orientable surface of genus $g$ is obtained from a $4g$-gon by the boundary word
$$
\boxed{a_1b_1a_1^{-1}b_1^{-1}\cdots a_gb_ga_g^{-1}b_g^{-1}}.
$$

::: pf-proof

For each handle, take the standard square model of a torus with boundary word $aba^{-1}b^{-1}$. Taking the connected sum of $g$ such handles gives a polygon whose boundary word is the product of these $g$ commutators.

:::

:::

::: {.pf-step #s2}

In the additive arrow notation of the question, the word is
$$
a_1+b_1-a_1-b_1+\cdots+a_g+b_g-a_g-b_g.
$$

::: pf-proof

Writing a reversed edge as the negative of its oriented label translates the multiplicative word in step [](#s1){.pf-ref} into the displayed notation.

:::

:::

::: pf-step

For $g=2$ this specializes to
$$
a+b-a-b+c+d-c-d,
$$
as stated.

::: pf-proof

Take $(a_1,b_1,a_2,b_2)=(a,b,c,d)$ in step [](#s2){.pf-ref}.

:::

:::

:::

:::
