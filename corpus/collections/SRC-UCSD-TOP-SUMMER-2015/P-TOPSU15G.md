---
schema: qual/card@1
id: P-TOPSU15G
kind: problem
title: '$\pi_4$ of $\RP^3$ with a $4$-cell attached via the antipodal quotient'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Cell Complexes
  - Projective Spaces
relations: []
review: draft
---

::: problem
Let $q : S^3 \to \mathbb{RP}^3$ be the usual quotient map which identifies antipodal points.
It can be used to attach a $4$-ball to $\mathbb{RP}^3$, forming a space $X = \mathbb{RP}^3 \cup_q B^4$.
Compute $\pi_4(X)$.
:::

::: {.solution}
<1>1. The standard CW construction of $\mathbb{RP}^4$ is obtained from $\mathbb{RP}^3$ by attaching a $4$-cell via the antipodal quotient
$$
q:S^3\to\mathbb{RP}^3.
$$
::: {.proof}
In the usual CW structure on real projective space, the characteristic map of the top cell descends from a hemisphere of $S^4$, and its boundary attaching map is exactly the double covering $S^3\to\mathbb{RP}^3$.
:::

<1>2. Hence the given space is
$$
X\cong\mathbb{RP}^4.
$$
::: {.proof}
It has precisely the standard cell attachment described in <1>1.
:::

<1>3. The universal covering map $S^4\to\mathbb{RP}^4$ induces an isomorphism on $\pi_4$.
::: {.proof}
Covering maps induce isomorphisms on all homotopy groups in degrees at least $2$.
:::

<1>4. Therefore
$$
\boxed{\pi_4(X)\cong\pi_4(S^4)\cong\mathbb Z.}
$$
::: {.proof}
The identity class generates $\pi_4(S^4)\cong\mathbb Z$.
:::
:::
