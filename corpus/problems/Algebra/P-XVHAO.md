---
schema: qual/card@1
id: P-XVHAO
kind: problem
title: $[A_4,A_4]\cong C_2\times C_2$
classification:
  areas:
  - algebra
  topics:
  - Commutators
  - Permutations
relations: []
review: draft
---

::: {.problem}
Show that
$$
[A_4,A_4]\cong C_2\times C_2.
$$
:::

::: {.solution}
Let $V_4=\{1,(12)(34),(13)(24),(14)(23)\}$, a normal subgroup of $A_4$ isomorphic to $C_2\times C_2$.

::: pf

::: {.pf-step #upper}
$[A_4,A_4]\le V_4$.

::: pf-proof
$A_4/V_4$ has order $3$, so it is cyclic and abelian, and the commutator subgroup lies in every normal subgroup with abelian quotient.
:::

:::

::: {.pf-step #one}
$(12)(34)\in[A_4,A_4]$.

::: pf-proof
With $a=(123)$ and $b=(124)$, a direct computation gives $aba^{-1}b^{-1}=(12)(34)$.
:::

:::

::: pf-step
$[A_4,A_4]=V_4\cong C_2\times C_2$.

::: pf-proof
The three double transpositions are conjugate in $A_4$: conjugating $(12)(34)$ by $(123)$ and by $(132)$ gives the other two.
Since $[A_4,A_4]$ is normal, step [](#one){.pf-ref} puts all of $V_4$ in it, and step [](#upper){.pf-ref} gives equality.
:::

:::

:::

:::
