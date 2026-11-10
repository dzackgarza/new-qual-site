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
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter II, section 1,
    exercise 1.2, printed page 66 (PDF page 81 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise has the three parts (a) (ker phi)_P =
    ker(phi_P) and (im phi)_P = im(phi_P), (b) injectivity and surjectivity are
    stalkwise, (c) exactness of a sequence of sheaves is stalkwise exactness.
    The card states exactly these three parts. The proof was read and checked,
    including the two inclusions of part (a) and the sheaf axiom invoked in
    (b): a section of ker phi whose germ vanishes everywhere is zero. What the
    proof takes as known is that a filtered colimit commutes with finite limits
    in sheaves of abelian groups, which is the text's AB5 environment; it does
    not reprove it.
---


::: {.problem}
(a) For any morphism of sheaves $\varphi: \mcf \to \mcg$, show that for each point $P$ one has $(\ker \varphi)_P = \ker(\varphi_P)$ and $(\im \varphi)_P = \im(\varphi_P)$.

(b) Show that $\varphi$ is injective (respectively surjective) if and only if the induced map on stalks $\varphi_P$ is injective (respectively surjective) for all $P$.

(c) Show that a sequence
$$
\cdots \to \mcf^{i-1} \mapsvia{\phi^{i-1}} \mcf^{i} \mapsvia{\phi^{i}} \mcf^{i+1} \to \cdots
$$
of sheaves and morphisms is exact if and only if for each $P \in X$ the corresponding sequence of stalks is exact as a sequence of abelian groups.
:::

::: {.solution}
**Part (a).** The clean argument is formal: taking the stalk at $P$ is a filtered colimit over the neighbourhoods of $P$, a kernel is a finite limit, and filtered colimits commute with finite limits.
This gives $(\ker \phi)_P = \ker(\phi_P)$ at once.
For the image, write $\im \phi \coloneqq \ker(\mcg \to \coker \phi)$, so the image is again a kernel, and the same commutation applies.

A direct diagram chase gives the same conclusion.

$(\ker \phi)_P \subseteq \ker(\phi_P)$: let $s \in (\ker \phi)_P$ and represent it by a pair $(U, \tilde s)$ with $\tilde s \in (\ker \phi)(U)$, so that $\restrictionof{\tilde s}{P} = s$ and $\phi(U)(\tilde s) = 0$ in $\mcg(U)$.
Passing to germs at $P$ and using that the square relating sections over $U$ to stalks at $P$ commutes, we get $\phi_P(s) = \restrictionof{0}{P} = 0$.

$\ker(\phi_P) \subseteq (\ker \phi)_P$: let $s_P \in \ker(\phi_P)$ and lift it to a pair $(U, s)$ with $s \in \mcf(U)$ and $\restrictionof{s}{P} = s_P$.
Put $t \coloneqq \phi(U)(s) \in \mcg(U)$.
Commutativity gives $\restrictionof{t}{P} = \phi_P(s_P) = 0$ in $\mcg_P$.
Since the germ of $t$ at $P$ vanishes, there is an open $V$ with $P \in V \subseteq U$ and $\restrictionof{t}{V} = 0$ in $\mcg(V)$.
Because $\phi$ is a morphism of sheaves the restriction squares commute, so $\phi(V)(\restrictionof{s}{V}) = \restrictionof{t}{V} = 0$, which says $\restrictionof{s}{V} \in (\ker \phi)(V)$.
Taking germs at $P$ exhibits $s_P = \qty{\restrictionof{s}{V}}_P$ as an element of $(\ker \phi)_P$.

The two inclusions for the image are the same computation performed on the image presheaf, whose stalk at $P$ is $(\im \phi)_P$ because sheafification does not change stalks.
$(\im \phi)_P \subseteq \im(\phi_P)$: an element of $(\im \phi)_P$ is the germ at $P$ of a section of the presheaf image over some neighbourhood $U$ of $P$, that is, of $\phi(U)(s)$ for some $s \in \mcf(U)$; it is therefore $\phi_P(s_P)$.
$\im(\phi_P) \subseteq (\im \phi)_P$: for $s_P \in \mcf_P$ represented by $s \in \mcf(U)$, the section $\phi(U)(s)$ lies in the presheaf image over $U$, so its germ $\phi_P(s_P)$ lies in $(\im \phi)_P$.

**Part (b).** *Injectivity.* ($\Rightarrow$) If $\phi$ is injective then $\ker \phi = 0$ as a sheaf, so by part (a) we get $\ker(\phi_P) = (\ker \phi)_P = 0$ for every $P$, and $\phi_P$ is injective.

($\Leftarrow$) Suppose $\ker(\phi_P) = 0$ for all $P$, and set $K \coloneqq \ker \phi$, a sheaf.
By part (a), $K_P = 0$ for all $P$.
Given a section $s \in K(U)$, each $P \in U$ has a neighbourhood $U_P \subseteq U$ with $\restrictionof{s}{U_P} = 0$, since the germ $s_P$ vanishes.
The sets $\theset{U_P \st P \in U}$ cover $U$, and $K$ is a sheaf, so the identity axiom forces $s = 0$.
Hence $K = 0$ and $\phi$ is injective.

*Surjectivity.* The same argument applied to $\coker \phi$, whose stalk at $P$ is $\mcg_P/(\im \phi)_P = \coker(\phi_P)$ by part (a), shows $\coker \phi = 0$ if and only if every $\phi_P$ is surjective.

**Part (c).** Exactness of the sequence of sheaves means $\ker \phi^i = \im \phi^{i-1}$ as subsheaves of $\mcf^i$.

($\Rightarrow$) If $\ker \phi^i = \im \phi^{i-1}$ then these sheaves have the same stalks, so by part (a)
$$
\ker(\phi^i_P) = (\ker \phi^i)_P = (\im \phi^{i-1})_P = \im(\phi^{i-1}_P),
$$
which is exactness at $P$.

($\Leftarrow$) Conversely, if the stalk sequences are exact then the same chain of identities read in the other order gives $(\ker \phi^i)_P = (\im \phi^{i-1})_P$ for every $P$.
Two subsheaves of $\mcf^i$ with the same stalks coincide, so $\ker \phi^i = \im \phi^{i-1}$.

Compactly, using part (a) throughout,
$$
\ker \phi^i = \im \phi^{i-1}
\iff (\ker \phi^i)_P = (\im \phi^{i-1})_P \ \forall P
\iff \ker(\phi^i_P) = \im(\phi^{i-1}_P) \ \forall P.
$$
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §1, Exercise 1.2, PDF pp. 2--3, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he reduces both identities of (a) to two facts, that sheafification does not change stalks and that kernels and images of abelian-group maps commute with the directed colimits which compute stalks, then reads (b) off as $\ker\phi=0$ and $\coker\phi=0$ and (c) off as $\ker\phi^{i}=\im\phi^{i-1}$ checked on stalks.
The proof above uses the same commutation for the kernels, but carries (a) out as an explicit chase on representatives, and the paragraph above carries the image out the same way; (b) and (c) are the same.
Agree.
:::
