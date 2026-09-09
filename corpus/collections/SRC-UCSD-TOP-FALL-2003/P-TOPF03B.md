---
schema: qual/card@1
id: P-TOPF03B
kind: problem
title: "Covers of the figure-eight corresponding to subgroups (abab) and (ab, ba)"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: problem
Let $X = S^1 \vee S^1$ be the figure-of-eight space.
Draw pictures of the covers of $X$ corresponding to the subgroups $\langle abab \rangle$ and $\langle ab, ba \rangle$.
:::

::: {.solution}
<1>1. Let $R=S^1_a\vee S^1_b$ be the rose with oriented edges labelled $a,b$. A connected cover of $R$ is equivalently a connected graph in which every vertex has exactly one incoming and one outgoing edge of each label $a,b$.
::: {.proof}
This is the usual Schreier-graph model for coverings of a bouquet of circles.
:::

<1>2. For $H_1=\langle abab\rangle=\langle(ab)^2\rangle$, the Stallings core is the based $4$-cycle
$$v_0\xrightarrow{a}v_1\xrightarrow{b}v_2\xrightarrow{a}v_3\xrightarrow{b}v_0.$$
::: {.proof}
The unique reduced generator $(ab)^2$ traces exactly this closed labelled path, and there are no folds because no two equally labelled oriented edges leave the same vertex.
:::

<1>3. The covering corresponding to $H_1$ is obtained from this core by attaching infinite labelled trees at every missing $a$- or $b$-half-edge so that the local covering condition holds at every vertex.
::: {.proof}
Completing a finite folded core graph to a full Schreier graph by adding trees does not create new based reduced loops, hence preserves the represented subgroup while producing a genuine covering of $R$.
:::

<1>4. For $H_2=\langle ab,ba\rangle$, the Stallings core has vertices $v_0,v_1,v_2$ and labelled edges
$$v_0\xrightarrow a v_1\xrightarrow b v_0,
\qquad
v_0\xrightarrow b v_2\xrightarrow a v_0.$$
::: {.proof}
The first two-edge loop reads $ab$, the second reads $ba$, and the graph is already folded. Its rank is $4-3+1=2$, agreeing with the rank of the generated subgroup.
:::

<1>5. The covering corresponding to $H_2$ is obtained by attaching infinite labelled trees at every missing half-edge of this three-vertex core.
::: {.proof}
As in <1>3, this completion gives the Schreier graph of the subgroup without changing its core fundamental group.
:::

<1>6. Thus the requested pictures are precisely the two completed Schreier graphs whose finite cores are described in <1>2 and <1>4.
::: {.proof}
Connected covering spaces of the rose correspond bijectively to conjugacy classes of subgroups, and the chosen base vertex fixes the actual subgroup rather than only its conjugacy class.
:::
:::
