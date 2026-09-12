---
schema: qual/card@1
id: P-AMD-SLP2J4M6
kind: problem
title: $K$ is not a topological group
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Fundamental Group
  - Groups
relations: []
review: draft
---

::: {.problem}
Show that $K$ can not be a topological group.
:::

::: {.solution}
<1>1. The fundamental group of the Klein bottle $K$ is nonabelian:
$$
\pi_1(K)\cong\langle a,b\mid aba^{-1}=b^{-1}\rangle.
$$
::: {.proof}
This is the standard presentation obtained from the square model of the Klein bottle. It is nonabelian, since the relation gives $aba^{-1}=b^{-1}$ rather than $b$; for example the group maps onto the nonabelian infinite dihedral group after imposing $b^2=1$ and retaining the conjugation relation.
:::

<1>2. The fundamental group of every path-connected topological group is abelian.
::: {.proof}
Let $G$ be a topological group with identity $e$. On based loops at $e$ there are two products: concatenation $*$ and pointwise multiplication
$$
(\alpha\cdot\beta)(t)=\alpha(t)\beta(t).
$$
They have the same unit and satisfy the interchange law
$$
(\alpha*\beta)\cdot(\gamma*\delta)
=(\alpha\cdot\gamma)*(\beta\cdot\delta).
$$
The Eckmann--Hilton argument therefore shows that the induced product on $\pi_1(G,e)$ is commutative.
:::

<1>3. Hence the Klein bottle cannot admit a topological-group structure.
::: {.proof}
If $K$ were a topological group, <1>2 would force $\pi_1(K)$ to be abelian, contradicting <1>1.
:::
:::
