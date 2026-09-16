---
schema: qual/card@1
id: P-YBQ3V
kind: problem
title: When compact sets are closed, and $\overline{A\times B}=\overline{A}\times\overline{B}$
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
---

::: {.problem}
- What property on a space guarantees that compact sets are closed

- What property on a space guarantees that closed sets are compact?

- Show that a continuous bijection from a compact space to a Hausdorff space is necessarily a homeomorphism.

- ![](../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520145801.png)
:::

::: {.solution}
<1>1. In a Hausdorff space every compact subset is closed.
::: {.proof}
For a compact $K$ and $x\notin K$, separate $x$ from each point of $K$ and use compactness to obtain one neighborhood of $x$ disjoint from $K$.
:::

<1>2. In a compact space every closed subset is compact.
::: {.proof}
If $F$ is closed and $\mathcal U$ covers $F$, then $\mathcal U\cup\{X\setminus F\}$ covers $X$; a finite subcover restricts to one of $F$.
:::

<1>3. A continuous bijection $f:X\to Y$ from compact $X$ to Hausdorff $Y$ is a homeomorphism.
::: {.proof}
For closed $F\subseteq X$, $F$ is compact, so $f(F)$ is compact and therefore closed in $Y$. Thus $f$ is a closed bijection, hence $f^{-1}$ is continuous.
:::

<1>4. For arbitrary subsets $A\subseteq X$ and $B\subseteq Y$,
$$\boxed{\overline{A\times B}^{\,X\times Y}=\overline A^{\,X}\times\overline B^{\,Y}.}$$
::: {.proof}
If $(x,y)$ is in the left closure, projections show $x\in\overline A$ and $y\in\overline B$. Conversely, if $x\in\overline A$ and $y\in\overline B$, every basic neighborhood $U\times V$ of $(x,y)$ meets $A\times B$ because $U\cap A$ and $V\cap B$ are both nonempty.
:::
:::
