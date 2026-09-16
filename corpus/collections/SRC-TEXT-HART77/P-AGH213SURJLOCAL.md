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
---

::: {.problem}
a. Let $\varphi: \mcf \to \mcg$ be a morphism of sheaves on $X$.
Show that $\varphi$ is surjective if and only if the following condition holds: for every open set $U \subseteq X$ and every $s \in \mcg(U)$, there is a covering $\ts{U_i}$ of $U$ and elements $t_i \in \mcf(U_i)$ such that $\varphi(t_i) = \ro{s}{U_i}$ for all $i$.

b. Give an example of a surjective morphism of sheaves $\varphi: \mcf \to \mcg$ and an open set $U$ such that $\varphi(U): \mcf(U) \to \mcg(U)$ is not surjective.
:::

::: {.solution}
**Part a.** ($\Rightarrow$) Suppose $\phi$ is surjective, so $\phi_P$ is surjective for every $P$.
Fix an open $U$ and a section $s \in \mcg(U)$.
For each $P \in U$ the germ $s_P \in \mcg_P$ lifts to some $t_P \in \mcf_P$ with $\phi_P(t_P) = s_P$.
As in the stalk arguments of the previous exercise, this identity of germs is already an identity of sections over a small enough neighbourhood: there is an open $U_P \ni P$ with $U_P \subseteq U$ and a section $t \in \mcf(U_P)$ with $\phi(U_P)(t) = \ro{s}{U_P}$.
Doing this for every $P \in U$ produces the required cover $\ts{U_P}$ together with the lifts.

($\Leftarrow$) Conversely, suppose the condition holds and fix $P$ and a germ $s_P \in \mcg_P$, represented by $(U, s)$.
The condition gives a cover $\ts{U_i}$ of $U$ and lifts $t_i \in \mcf(U_i)$ with $\phi(t_i) = \ro{s}{U_i}$.
Choose an index $i$ with $P \in U_i$; then the germ of $t_i$ at $P$ maps to $s_P$.
So $\phi_P$ is surjective for all $P$, and hence $\phi$ is surjective.

**Part b.** Take the exponential sequence of sheaves on $\CC$:
\[
0 \to \ul{\ZZ} \injects (\OO_\CC, +) \surjectsvia{\exp} (\OO_\CC\units, \cdot) \to 0.
\]
Let $U \da \cstar$ and let $f(z) = z$, a nowhere-vanishing holomorphic function, so $f \in \OO_\CC\units(U)$.
There is no $g \in \OO_\CC(U)$ with $\exp(g) = z$ on all of $U$: such a $g$ would be a single-valued holomorphic branch of $\log z$ on the punctured plane, and $\log$ is multivalued there.
So $\exp(U)$ is not surjective on sections.

Nevertheless $\exp$ is surjective as a morphism of sheaves.
For any $P \in \cstar$, choose a disc $V \ni P$ small enough to avoid the origin.
On $V$ a holomorphic branch of $\log$ exists, so $\exp$ is surjective on sections over $V$ and over every smaller open set, hence surjective on the stalk at $P$.
:::
