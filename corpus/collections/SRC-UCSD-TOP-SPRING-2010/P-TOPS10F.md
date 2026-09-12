---
schema: qual/card@1
id: P-TOPS10F
kind: problem
title: "A space with free fundamental group and no higher homotopy is a bouquet of circles"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Fundamental Group
  - Free Groups
relations: []
review: draft
---

::: problem
Let $X$ be a path-connected space with $\pi_{\geq 2}(X) = 0$ and whose fundamental group is a free group on a set $S$.
Show that there is a homotopy equivalence between a bouquet of circles, indexed by $S$, and $X$.
:::

::: {.solution}
<1>1. Under the standard additional hypothesis that $X$ has the homotopy type of a CW complex, choose for each free generator $s\in S$ a based loop in $X$ representing $s$. These loops define a map
$$
f:\bigvee_{s\in S}S^1\longrightarrow X.
$$
::: {.proof}
The wedge is the CW complex with one circle for each generator. The chosen loops agree at the common basepoint and hence define the map.
:::

<1>2. The map $f_*$ is an isomorphism on $\pi_1$.
::: {.proof}
The fundamental group of the wedge is the free group on the circle classes indexed by $S$, and by construction $f_*$ sends this free basis to the given free basis of $\pi_1(X)$.
:::

<1>3. For every $i\ge2$, both source and target have zero $\pi_i$, so $f_*$ is an isomorphism on all homotopy groups.
::: {.proof}
The universal cover of a graph is a tree, so a bouquet of circles has no higher homotopy groups. The target has none by hypothesis.
:::

<1>4. Hence $f$ is a weak homotopy equivalence, and by Whitehead's theorem it is a homotopy equivalence when $X$ has CW type.
::: {.proof}
Whitehead's theorem applies to maps between CW complexes, and more generally after replacing a CW-type target by a homotopy-equivalent CW complex.
:::

<1>5. Thus, with the necessary CW-type hypothesis,
$$
\boxed{X\simeq\bigvee_{s\in S}S^1.}
$$
::: {.proof}
This is <1>4.
:::

<1>6. As written for an arbitrary path-connected topological space, the statement is not justified: a weak homotopy equivalence need not be a homotopy equivalence without a CW-type (or comparable) hypothesis.
::: {.proof}
The preceding argument proves exactly a weak equivalence before Whitehead's theorem is invoked. Whitehead's conclusion requires the stated homotopical regularity hypothesis.
:::
:::
