---
schema: qual/card@1
id: P-AGXVARPROJCOMPACT
kind: problem
title: Zariski closed subsets of $\PP^n$ are compact in the classical topology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Compactness
  - Classical Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 7.7 in the recorded source. Over k=C it asks that
    every Zariski-closed subset of P^n be compact in the usual Hausdorff
    topology, with the hint to prove compactness of P^n first.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's field C explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Used the quotient map from the unit sphere S^{2n+1} to complex projective
    space. The inverse image of a projective algebraic set is the common zero
    locus on the sphere of its homogeneous equations, hence closed and
    compact; its continuous image is the given projective algebraic set.
---

::: {.problem}
Show that every Zariski-closed subset of
$$
\PP^n_\CC
$$
is compact in the usual Hausdorff topology.
:::

::: {.solution}
Let
$$
S^{2n+1}
=
\left\{
z=(z_0,\ldots,z_n)\in\CC^{n+1}:
\sum_{i=0}^n\abs{z_i}^2=1
\right\}.
$$

::: pf

::: {.pf-step #q-continuous-surjective}
The map
$$
q:S^{2n+1}\longrightarrow\PP^n_\CC,
\qquad
z\longmapsto[z_0:\ldots:z_n]
$$
is continuous and surjective.

::: pf-proof
The usual topology on complex projective space is the quotient topology on
$$
(\CC^{n+1}\sm\{0\})/\CC^\times.
$$
Restricting the quotient map to the unit sphere gives $q$, so $q$ is
continuous.

Every projective point
$$
[z_0:\ldots:z_n]
$$
has a nonzero representative $z\in\CC^{n+1}$. Dividing by its Euclidean norm
produces a representative on $S^{2n+1}$. Hence $q$ is surjective.
:::

:::

::: {.pf-step #pn-compact}
The complex projective space $\PP^n_\CC$ is compact.

::: pf-proof
The sphere $S^{2n+1}$ is compact by the Heine--Borel theorem. By step [](#q-continuous-surjective){.pf-ref},
$$
\PP^n_\CC=q(S^{2n+1}).
$$
A continuous image of a compact space is compact, so $\PP^n_\CC$ is compact.
:::

:::

::: {.pf-step #preimage-closed}
Let
$$
X\subseteq\PP^n_\CC
$$
be Zariski closed. Then
$$
q^{-1}(X)\subseteq S^{2n+1}
$$
is closed.

::: pf-proof
Choose homogeneous polynomials
$$
\{F_\alpha\}_{\alpha\in A}
\subseteq
\CC[x_0,\ldots,x_n]
$$
whose common projective zero locus is $X$:
$$
X=V(F_\alpha:\alpha\in A).
$$
Then
$$
q^{-1}(X)
=
\left\{
z\in S^{2n+1}:
F_\alpha(z)=0
\text{ for every }\alpha
\right\}.
$$
Each restriction
$$
F_\alpha|_{S^{2n+1}}:S^{2n+1}\longrightarrow\CC
$$
is continuous, so
$$
(F_\alpha|_{S^{2n+1}})^{-1}(\{0\})
$$
is closed. Therefore
$$
q^{-1}(X)
=
\bigcap_{\alpha\in A}
(F_\alpha|_{S^{2n+1}})^{-1}(\{0\})
$$
is closed as an arbitrary intersection of closed subsets.
:::

:::

::: {.pf-step #x-compact}
Every Zariski-closed subset
$$
X\subseteq\PP^n_\CC
$$
is compact.

::: pf-proof
By step [](#preimage-closed){.pf-ref}, $q^{-1}(X)$ is closed in the compact sphere $S^{2n+1}$, hence
is compact. By construction,
$$
q(q^{-1}(X))=X.
$$
Since $q$ is continuous, $X$ is a continuous image of a compact space.
Therefore
$$
\boxed{X\text{ is compact}.}
$$
:::

:::

::: pf-qed
Step [](#pn-compact){.pf-ref} proves that $\PP^n_\CC$ is compact, and steps [](#preimage-closed){.pf-ref} and [](#x-compact){.pf-ref} prove
the assertion for every Zariski-closed subset.
:::

:::

:::
