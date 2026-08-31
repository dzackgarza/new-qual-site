---
schema: qual/card@1
id: P-6QME4
kind: problem
title: Proper nontrivial normal subgroups of $S_4$ are $A_4$ and $\ZZ_2^2$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Show that $S_4$ has two normal subgroups: $A_4, \ZZ_2^2$.
:::

::: {.solution}
<1>1. $A_4$ is a normal subgroup of $S_4$.
::: {.proof}
$A_4$ is the kernel of the sign homomorphism $\operatorname{sgn}: S_4 \to \{\pm 1\}$, and kernels are normal; it has index $2$.
:::

<1>2. $V_4 = \{e, (12)(34), (13)(24), (14)(23)\} \cong \ZZ_2 \times \ZZ_2$ is a normal subgroup of $S_4$.
<2>1. $V_4$ is a subgroup.
::: {.proof}
the product of any two distinct double transpositions is the third, and each has order $2$.
:::
<2>2. $V_4$ is normal in $S_4$.
::: {.proof}
conjugation preserves cycle type, and $V_4$ is the set of all elements of cycle type $2^2$ together with the identity, so it is closed under conjugation.
:::
<2>3. $V_4 \cong \ZZ_2 \times \ZZ_2$.
::: {.proof}
it is a group of order $4$ in which every nonidentity element has order $2$.
:::

<1>3. These are the only proper nontrivial normal subgroups of $S_4$.
::: {.proof}
the normal subgroups of $S_4$ are exactly $\{e\}$, $V_4$, $A_4$, and $S_4$ (standard fact, verified by checking the conjugacy classes of $S_4$ and which unions of them form subgroups).
:::

<1>4. Q.E.D.
::: {.proof}
<1>1, <1>2, and <1>3.
:::
:::
