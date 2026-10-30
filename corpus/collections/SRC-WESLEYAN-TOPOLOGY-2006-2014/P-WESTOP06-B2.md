---
schema: qual/card@1
id: P-WESTOP06-B2
kind: problem
title: Homotopy equivalences among three rank-two graphs
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $g:X\to Y$ and $h:Y\to X$.

1. Define what it means for $g$ and $h$ to be homotopy equivalences.
2. Show that a map homotopic to a homotopy equivalence is itself a homotopy equivalence.
3. Prove that the three spaces pictured in the source are homotopy equivalent: a figure-eight, two circles joined by an interval, and a circle together with a diameter.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The maps $g:X\to Y$ and $h:Y\to X$ are homotopy equivalences, inverse to one another up to homotopy, if
$$
h\circ g\simeq\operatorname{id}_X
\qquad\text{and}\qquad
g\circ h\simeq\operatorname{id}_Y.
$$


::: pf-proof

This is the definition of a homotopy equivalence and a homotopy inverse.

:::

:::

::: {.pf-step #s1-2}

If $g':X\to Y$ is homotopic to a homotopy equivalence $g:X\to Y$, then $g'$ is also a homotopy equivalence.


::: pf-proof

Let $h:Y\to X$ be a homotopy inverse for $g$. Thus
$$
h\circ g\simeq\operatorname{id}_X,
\qquad
g\circ h\simeq\operatorname{id}_Y.
$$
Since $g'\simeq g$, composition with a fixed continuous map preserves homotopy, so
$$
h\circ g'\simeq h\circ g\simeq\operatorname{id}_X
$$
and
$$
g'\circ h\simeq g\circ h\simeq\operatorname{id}_Y.
$$
Therefore $h$ is also a homotopy inverse for $g'$, and $g'$ is a homotopy equivalence.

:::

:::

::: {.pf-step #s1-3}

Collapsing a contractible tree subcomplex of a graph to a point is a homotopy equivalence.


::: pf-proof

Let $G$ be a graph regarded as a CW complex and let $T\subseteq G$ be a contractible tree subcomplex. Choose a contraction
$$
C:T\times I\to T
$$
from $\operatorname{id}_T$ to a constant map with value $t_0\in T$. Since $T\hookrightarrow G$ is the inclusion of a CW subcomplex, it has the homotopy extension property. Therefore $C$, together with $\operatorname{id}_G$ at time $0$, extends to a homotopy
$$
H:G\times I\to G
$$
with $H_0=\operatorname{id}_G$ and $H\restrict_{T\times I}=C$.

At time $1$, the map $H_1$ is constant on $T$, so it factors uniquely through the quotient:
$$
H_1=s\circ q
$$
for some $s:G/T\to G$, where
$$
q:G\to G/T
$$
is the quotient map. Thus
$$
s\circ q=H_1\simeq\operatorname{id}_G.
$$

For every $u\in I$, the composite $q\circ H_u$ is constant on $T$, because $H_u(T)=C_u(T)\subseteq T$. Hence $q\circ H_u$ factors through a map
$$
K_u:G/T\to G/T.
$$
These maps form a homotopy with
$$
K_0=\operatorname{id}_{G/T},
\qquad
K_1=q\circ s.
$$
Therefore $q\circ s\simeq\operatorname{id}_{G/T}$. Hence $q$ and $s$ are homotopy inverses, so collapsing $T$ is a homotopy equivalence.

:::

:::

::: {.pf-step #s1-4}

The space consisting of two circles joined by an interval is homotopy equivalent to the figure-eight $S^1\vee S^1$.


::: pf-proof

Regard the joining interval as a tree subcomplex $T$. Collapsing $T$ identifies its two endpoints and leaves the two circles otherwise unchanged. The quotient is therefore exactly a figure-eight:
$$
G/T\cong S^1\vee S^1.
$$
By step [](#s1-3){.pf-ref}, the quotient map is a homotopy equivalence.

:::

:::

::: {.pf-step #s1-5}

The space consisting of a circle together with a diameter is homotopy equivalent to the figure-eight $S^1\vee S^1$.


::: pf-proof

The two endpoints of the diameter divide the circle into two semicircular edges. Thus the pictured space is a theta graph with two vertices and three edges: the two semicircles and the diameter.

Take the diameter as the tree subcomplex $T$. Collapsing $T$ identifies its endpoints. Each semicircle then becomes a loop based at the collapsed point, so
$$
G/T\cong S^1\vee S^1.
$$
Step [](#s1-3){.pf-ref} again shows that this quotient map is a homotopy equivalence.

:::

:::

::: {.pf-step #s1-6}

The three pictured spaces are homotopy equivalent.


::: pf-proof

The first pictured space is already the figure-eight $S^1\vee S^1$. Step [](#s1-4){.pf-ref} shows that the second is homotopy equivalent to it, and step [](#s1-5){.pf-ref} shows the same for the third. Hence all three spaces have the same homotopy type:
$$
\boxed{S^1\vee S^1.}
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part $1$, step [](#s1-2){.pf-ref} answers part $2$, and step [](#s1-6){.pf-ref} answers part $3$.

:::

:::

:::
