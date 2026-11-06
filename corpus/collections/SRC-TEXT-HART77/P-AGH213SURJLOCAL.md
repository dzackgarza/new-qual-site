---
schema: qual/card@1
id: P-AGH213SURJLOCAL
kind: problem
title: Surjectivity of a sheaf morphism is a local lifting condition
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Surjectivity
  - Stalks
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter II, section 1,
    exercise 1.3, printed page 66 (PDF page 81 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "(a) Let phi: F -> G be a morphism
    of sheaves on X. Show that phi is surjective if and only if the following
    condition holds: for every open set U of X, and for every s in G(U), there
    is a covering {U_i} of U and there are elements t_i in F(U_i) such that
    phi(t_i) = s|_{U_i} for all i. (b) Give an example of a surjective morphism
    of sheaves phi: F -> G, and an open set U such that phi(U): F(U) -> G(U) is
    not surjective." The card states exactly this. The proof of (a) was checked
    in both directions, and the example of (b), the exponential sequence on
    the punctured plane, was checked to be a morphism that is surjective on
    stalks (a disc is simply connected) but not on sections over the punctured
    plane.
---


::: {.problem}
(a) Let $\varphi: \mcf \to \mcg$ be a morphism of sheaves on $X$.
   Show that $\varphi$ is surjective if and only if the following condition holds: for every open set $U \subseteq X$ and every $s \in \mcg(U)$, there is a covering $\theset{U_i}$ of $U$ and elements $t_i \in \mcf(U_i)$ such that $\varphi(t_i) = \restrictionof{s}{U_i}$ for all $i$.

(b) Give an example of a surjective morphism of sheaves $\varphi: \mcf \to \mcg$ and an open set $U$ such that $\varphi(U): \mcf(U) \to \mcg(U)$ is not surjective.
:::

::: {.solution}
**Part (a).** ($\Rightarrow$) Suppose $\phi$ is surjective, so $\phi_P$ is surjective for every $P$.
Fix an open $U$ and a section $s \in \mcg(U)$.
For each $P \in U$ the germ $s_P \in \mcg_P$ lifts to some $t_P \in \mcf_P$ with $\phi_P(t_P) = s_P$.
As in the stalk arguments of the previous exercise, this identity of germs is already an identity of sections over a small enough neighbourhood: there is an open $U_P \ni P$ with $U_P \subseteq U$ and a section $t \in \mcf(U_P)$ with $\phi(U_P)(t) = \restrictionof{s}{U_P}$.
Doing this for every $P \in U$ produces the required cover $\theset{U_P}$ together with the lifts.

($\Leftarrow$) Conversely, suppose the condition holds and fix $P$ and a germ $s_P \in \mcg_P$, represented by $(U, s)$.
The condition gives a cover $\theset{U_i}$ of $U$ and lifts $t_i \in \mcf(U_i)$ with $\phi(t_i) = \restrictionof{s}{U_i}$.
Choose an index $i$ with $P \in U_i$; then the germ of $t_i$ at $P$ maps to $s_P$.
So $\phi_P$ is surjective for all $P$, and hence $\phi$ is surjective.

**Part (b).** Take the exponential sequence of sheaves on $\CC$:
$$
0 \to \underline{\ZZ} \injects (\OO_\CC, +) \surjectsvia{\exp} (\units{\OO_\CC}, \cdot) \to 0.
$$
Let $U \coloneqq \CCstar$ and let $f(z) = z$, a nowhere-vanishing holomorphic function, so $f \in \units{\OO_\CC}(U)$.
There is no $g \in \OO_\CC(U)$ with $\exp(g) = z$ on all of $U$: such a $g$ would be a single-valued holomorphic branch of $\log z$ on the punctured plane, and $\log$ is multivalued there.
So $\exp(U)$ is not surjective on sections.

Nevertheless $\exp$ is surjective as a morphism of sheaves.
For any $P \in \CC$, a germ of $\units{\OO_\CC}$ at $P$ is represented by a nowhere-vanishing holomorphic function on some open disc $V \ni P$.
A disc is simply connected, so that function has a holomorphic logarithm on $V$, and $\exp$ is surjective on the stalk at $P$.
:::
