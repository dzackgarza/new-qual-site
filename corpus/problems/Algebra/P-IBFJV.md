---
schema: qual/card@1
id: P-IBFJV
kind: problem
title: Nonisomorphic groups with equivalent representation theory
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Are there two nonisomorphic groups with the same representations?
:::

::: {.solution}
Yes, if "the same representations" means the same complex character table or the same complex representation ring. A standard example is the dihedral group $D_8$ of order $8$ and the quaternion group $Q_8$.

::: pf

::: pf-step

The groups $D_8$ and $Q_8$ are not isomorphic.

::: pf-proof

The quaternion group has a unique element of order $2$, namely $-1$. The dihedral group of order $8$ has five elements of order $2$ (the half-turn and four reflections). Thus the groups are not isomorphic.

:::

:::

::: pf-step

Each group has four one-dimensional complex irreducible representations and one two-dimensional irreducible representation.

::: pf-proof

Both abelianizations are isomorphic to $C_2\times C_2$, so both have four one-dimensional characters. Each group has five conjugacy classes, hence five irreducible complex characters. The sum-of-squares formula
$$
\sum_i (\dim V_i)^2=8
$$
forces the remaining irreducible to have dimension $2$.

:::

:::

::: pf-step

After a suitable matching of conjugacy classes, their character tables are identical, so their complex representation rings are isomorphic.

::: pf-proof

In both groups the four linear characters factor through $C_2\times C_2$. The two-dimensional irreducible character has value $2$ at the identity, $-2$ at the unique central nonidentity element in the commutator subgroup, and $0$ on the remaining three noncentral conjugacy classes. Thus the character tables coincide after relabeling the classes.
Characters multiply pointwise, so the matching of classes identifies the two character rings, which are the complex representation rings.

:::

:::

:::

:::

::: {.remark}
The symmetric tensor categories of representations, together with the forgetful fiber functor, do distinguish the two groups: Tannakian reconstruction recovers a group from that richer structure. The example concerns coarser data, such as characters or the representation ring.
:::
