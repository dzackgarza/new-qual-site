---
schema: qual/card@1
id: P-TOPS13H
kind: problem
title: "Mayer-Vietoris exact sequence for the double mapping cylinder"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Exact Sequences
  - Mapping Cylinder
relations: []
review: draft
---

::: problem
Let $X$, $Y$ and $Z$ be spaces, and let $f : X \to Y$, $g : X \to Z$ be continuous maps.
Define the double mapping cylinder $D$ to be the quotient of the disjoint union of $X \times [0, 1]$, $Y$ and $Z$ via the equivalence relation $(x, 0) \sim f(x)$, $(x, 1) \sim g(x)$.
Show there is an exact sequence
$$
\cdots \to H_q(X) \to H_q(Y) \oplus H_q(Z) \to H_q(D) \to H_{q-1}(X) \to \cdots.
$$
:::

::: {.solution}
<1>1. Let
$$
U=Y\cup_f(X\times[0,2/3)),\qquad
V=Z\cup_g(X\times(1/3,1]).
$$
These are open subsets of a slightly thickened model of the double mapping cylinder and cover $D$.
::: {.proof}
Mapping cylinders admit standard open neighborhoods of their endpoint spaces obtained by taking overlapping subintervals of the cylinder coordinate.
:::

<1>2. We have homotopy equivalences
$$
U\simeq Y,\qquad V\simeq Z,\qquad U\cap V\simeq X.
$$
::: {.proof}
Each endpoint mapping cylinder deformation-retracts onto its endpoint space, while the overlap is $X$ times an open interval and hence deformation-retracts onto $X$.
:::

<1>3. The Mayer--Vietoris sequence for $D=U\cup V$ is
$$
\cdots\to H_q(U\cap V)\to H_q(U)\oplus H_q(V)\to H_q(D)
\to H_{q-1}(U\cap V)\to\cdots.
$$
::: {.proof}
This is the standard homological Mayer--Vietoris exact sequence.
:::

<1>4. Using the identifications from <1>2 gives
$$
\boxed{\cdots\to H_q(X)\xrightarrow{(f_*,-g_*)}H_q(Y)\oplus H_q(Z)
\to H_q(D)\to H_{q-1}(X)\to\cdots.}
$$
::: {.proof}
Under the deformation retractions, the two inclusion maps of the overlap into $U$ and $V$ become $f$ and $g$. The Mayer--Vietoris sign convention makes the first map $(f_*,-g_*)$.
:::
:::
