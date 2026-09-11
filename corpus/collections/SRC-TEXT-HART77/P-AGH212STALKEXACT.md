---
schema: qual/card@1
id: P-AGH212STALKEXACT
kind: problem
title: Kernels, images, and exactness of sheaves are computed on stalks
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Exact Sequences
relations: []
review: draft
---

::: problem
a. For any morphism of sheaves $\varphi: \mcf \to \mcg$, show that for each point $P$ one has $(\ker \varphi)_P = \ker(\varphi_P)$ and $(\im \varphi)_P = \im(\varphi_P)$.

b. Show that $\varphi$ is injective (respectively surjective) if and only if the induced map on stalks $\varphi_P$ is injective (respectively surjective) for all $P$.

c. Show that a sequence
\[
\cdots \to \mcf^{i-1} \mapsvia{\phi^{i-1}} \mcf^{i} \mapsvia{\phi^{i}} \mcf^{i+1} \to \cdots
\]
of sheaves and morphisms is exact if and only if for each $P \in X$ the corresponding sequence of stalks is exact as a sequence of abelian groups.
:::

::: solution
**Part a.**
The clean argument is formal: taking the stalk at $P$ is a filtered colimit over the neighbourhoods of $P$, a kernel is a finite limit, and filtered colimits commute with finite limits.
This gives $(\ker \phi)_P = \ker(\phi_P)$ at once.
For the image, write $\im \phi \da \ker(\mcg \to \coker \phi)$, so the image is again a kernel, and the same commutation applies.

A direct diagram chase gives the same conclusion.

$(\ker \phi)_P \subseteq \ker(\phi_P)$: let $s \in (\ker \phi)_P$ and represent it by a pair $(U, \tilde s)$ with $\tilde s \in (\ker \phi)(U)$, so that $\ro{\tilde s}{P} = s$ and $\phi(U)(\tilde s) = 0$ in $\mcg(U)$.
Passing to germs at $P$ and using that the square relating sections over $U$ to stalks at $P$ commutes, we get $\phi_P(s) = \ro{0}{P} = 0$.

$\ker(\phi_P) \subseteq (\ker \phi)_P$: let $s_P \in \ker(\phi_P)$ and lift it to a pair $(U, s)$ with $s \in \mcf(U)$ and $\ro{s}{P} = s_P$.
Put $t \da \phi(U)(s) \in \mcg(U)$.
Commutativity gives $\ro{t}{P} = \phi_P(s_P) = 0$ in $\mcg_P$.
Since the germ of $t$ at $P$ vanishes, there is an open $V$ with $P \in V \subseteq U$ and $\ro{t}{V} = 0$ in $\mcg(V)$.
Because $\phi$ is a morphism of sheaves the restriction squares commute, so $\phi(V)(\ro{s}{V}) = \ro{t}{V} = 0$, which says $\ro{s}{V} \in (\ker \phi)(V)$.
Taking germs at $P$ exhibits $s_P = \qty{\ro{s}{V}}_P$ as an element of $(\ker \phi)_P$.

The diagram chase for images is the same argument run in the other direction.

**Part b.**
*Injectivity.*
($\Rightarrow$) If $\phi$ is injective then $\ker \phi = 0$ as a sheaf, so by part (a) we get $\ker(\phi_P) = (\ker \phi)_P = 0$ for every $P$, and $\phi_P$ is injective.

($\Leftarrow$) Suppose $\ker(\phi_P) = 0$ for all $P$, and set $K \da \ker \phi$, a sheaf.
By part (a), $K_P = 0$ for all $P$.
Given a section $s \in K(U)$, each $P \in U$ has a neighbourhood $U_P \subseteq U$ with $\ro{s}{U_P} = 0$, since the germ $s_P$ vanishes.
The sets $\ts{U_P \st P \in U}$ cover $U$, and $K$ is a sheaf, so the identity axiom forces $s = 0$.
Hence $K = 0$ and $\phi$ is injective.

*Surjectivity.* The same argument applied to $\coker \phi$, whose stalks are the cokernels of the $\phi_P$ by part (a), shows $\coker \phi = 0$ if and only if every $\phi_P$ is surjective.

**Part c.**
Exactness of the sequence of sheaves means $\ker \phi^i = \im \phi^{i-1}$ as subsheaves of $\mcf^i$.

($\Rightarrow$) If $\ker \phi^i = \im \phi^{i-1}$ then these sheaves have the same stalks, so by part (a)
\[
\ker(\phi^i_P) = (\ker \phi^i)_P = (\im \phi^{i-1})_P = \im(\phi^{i-1}_P),
\]
which is exactness at $P$.

($\Leftarrow$) Conversely, if the stalk sequences are exact then the same chain of identities read in the other order gives $(\ker \phi^i)_P = (\im \phi^{i-1})_P$ for every $P$.
Two subsheaves of $\mcf^i$ with the same stalks coincide, so $\ker \phi^i = \im \phi^{i-1}$.

Compactly, using part (a) throughout,
\[
\ker \phi^i = \im \phi^{i-1}
\iff (\ker \phi^i)_P = (\im \phi^{i-1})_P \ \forall P
\iff \ker(\phi^i_P) = \im(\phi^{i-1}_P) \ \forall P.
\]
:::
