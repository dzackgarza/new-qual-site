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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read again for issue #164. The exercise is printed on p. 66 of Hartshorne,
    Algebraic Geometry (1977), II.1: the folio 66 is printed at the foot of PDF
    p. 81 of tmp/sources/hartshorne-1977-algebraic-geometry.pdf, whose text layer
    was read there, and the extraction
    tmp/sources/hartshorne-1977-algebraic-geometry.md carries the same exercise
    under its marker for PDF p. 81. The statement on the card is the printed one,
    part for part. Caution 1.2.1, printed p. 65 (PDF p. 80), is where the book
    states that a morphism is surjective if and only if it is surjective on
    stalks; that is the criterion the last line of part (a) uses. The proof of
    (a) in the direction (=>) is transcribed from Dongryul Kim, Solutions to
    Hartshorne's Algebraic Geometry, Chapter II §1, Exercise 2.1.3, PDF p. 3 (the
    folio printed on the page): the lift of the germ, its representative on a
    neighbourhood, the shrink on which the two sections agree, and the cover by
    the shrunk neighbourhoods are his. He writes of the direction (<=) only
    "the converse follows by 1.2.b", so the one line proving it is supplied on
    the card. Part (b) is his example -- the exponential map of the sheaf of
    holomorphic functions on C \ {0}, with the section z -- and he asserts
    without proof that z "doesn't have a global inverse"; the loop integral
    $\int_\gamma g'(z)\,dz = g(\gamma(2\pi)) - g(\gamma(0)) = 0$ against
    $\int_\gamma dz/z = 2\pi i$, and the construction of a primitive of $h'/h$
    on a disc that gives a logarithm, are the card's. Egbert, PDF pp. 59-60, and
    Saglam--Chris, PDF p. 1, were read and carry the same exercise with the same
    two omissions. Checked by typesetting the display with the project preamble
    in pdflatex: it renders one arrow with exp above it, not the doubled arrow
    the one-argument \surjectsvia produced. Not checked: the printed book, only
    the text layer of the retained PDF; and no other retained set was searched
    for a proof of the two omitted steps.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The event above says no other retained set was searched for a proof of the
    two steps Kim omits. They were searched in this pass. Steven V. Sam's
    solutions carry II.1.3 at printed p. 2 -- PDF p. 15 of
    tmp/sources/hartshorne-solutions-sam.pdf, whose text layer is mirrored and
    was read after reversing it; the running foot of that page reads
    "1 SHEAVES 2", so printed p. = PDF p. - 13 -- and prove part (a) in both
    directions: the lift of the germ with its representative on a neighbourhood,
    and the converse by an index i with P in U_i. His part (b) takes
    differentiation of analytic functions instead of the exponential: it is
    surjective on stalks because an analytic function has an antiderivative on a
    simply connected neighbourhood, and 1/z on C \ {0} has none, its integral
    over the unit circle being 2 pi i. The remark now says so. Cais, printed
    p. 1, and Cutrone--Marshburn, printed pp. 29--30, also carry the exercise;
    they were located in this pass but not read closely enough to be named on
    the card. Not checked: the printed copies of any of these sets.
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
The germ $t_P$ is represented by a section $t \in \mcf(U_P)$ on an open neighbourhood $U_P \ni P$.
Then $\phi(t)$ and $s$ have the same germ at $P$, so they agree on an open $V_P$ with $P \in V_P \subseteq U_P \cap U$, that is, $\phi(\restrictionof{t}{V_P}) = \restrictionof{s}{V_P}$.
As $P$ ranges over $U$, the $V_P$ cover $U$, and $\restrictionof{t}{V_P}$ is the required lift of $\restrictionof{s}{V_P}$.

($\Leftarrow$) Conversely, suppose the condition holds and fix $P$ and a germ $s_P \in \mcg_P$, represented by $(U, s)$.
The condition gives a cover $\theset{U_i}$ of $U$ and lifts $t_i \in \mcf(U_i)$ with $\phi(t_i) = \restrictionof{s}{U_i}$.
Choose an index $i$ with $P \in U_i$; then the germ of $t_i$ at $P$ maps to $s_P$.
So $\phi_P$ is surjective for all $P$, and hence $\phi$ is surjective.

**Part (b).** Take the exponential sequence of sheaves on $\CC$:
$$
0 \to \underline{\ZZ} \injects (\OO_\CC, +) \xrightarrow{\ \exp\ } (\units{\OO_\CC}, \cdot) \to 0.
$$
Let $U \coloneqq \CCstar$ and let $f(z) = z$, a nowhere-vanishing holomorphic function, so $f \in \units{\OO_\CC}(U)$.
There is no $g \in \OO_\CC(U)$ with $\exp(g) = z$ on all of $U$.
Such a $g$ would satisfy $g'(z)\exp(g(z)) = 1$, hence $g'(z) = 1/z$.
For $\gamma(t) = e^{it}$, $0 \leq t \leq 2\pi$, the chain rule gives
$$
\int_\gamma g'(z)\dz = g(\gamma(2\pi)) - g(\gamma(0)) = 0,
$$
since $g$ is single-valued and $\gamma$ is closed, whereas $\int_\gamma \dz/z = 2\pi i$.
So $\exp(U)$ is not surjective on sections.

Nevertheless $\exp$ is surjective as a morphism of sheaves.
For any $P \in \CC$, a germ of $\units{\OO_\CC}$ at $P$ is represented by a nowhere-vanishing holomorphic function $h$ on some open disc $V \ni P$.
A disc is simply connected, so $h'/h$ has a primitive $G$ on $V$; then $h\exp(-G)$ has zero derivative, hence equals a nonzero constant $e^{a}$, and $h = \exp(G+a)$ on $V$.
So every germ of $\units{\OO_\CC}$ at $P$ is the exponential of a germ of $\OO_\CC$, and $\exp$ is surjective on the stalk at $P$.
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §1, Exercise 1.3 (his Exercise 2.1.3), PDF p. 3, the folio printed on the page, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: for (a) he lifts the germ $s_P$ to an element $t_P$, represents it by a section $t_{U_P}$ on a neighbourhood, shrinks to a $V_P$ on which $\phi(t_{U_P})$ and $s$ agree, and lets those neighbourhoods range over $U$. Of the converse he writes only that it "follows by 1.2.b"; Sam writes that direction out by the one line the card uses, and the book states the criterion it uses as Caution 1.2.1, printed p. 65.
For (b) he uses $U=\CC\sm\{0\}$ and the exponential map of the sheaf of holomorphic functions, with the one assertion that the section $z$ "doesn't have a global inverse". The loop integral that excludes a global logarithm, and the construction of a logarithm on a disc that gives surjectivity on stalks, are the card's, as is writing the two sheaves on $\CC$ and restricting to $U = \CC^\times$.
Steven V. Sam, *Solutions to Hartshorne's Algebraic Geometry*, Chapter II §1, Exercise 1.3, printed p. 2 (PDF p. 15 of `tmp/sources/hartshorne-solutions-sam.pdf`, whose text layer is mirrored), proves (a) in both directions by the same two steps, and takes differentiation $D\colon\mcf\to\mcf$ of analytic functions for the example of (b): $D$ is surjective on stalks because an analytic function has an antiderivative on a simply connected neighbourhood, and $1/z$ on $\CC^\times$ has none, its integral over the unit circle being $2\pi i$.
Egbert, PDF pp. 59--60, and Saglam--Chris, PDF p. 1, carry the same exercise and the same two omissions as Kim: each states that a logarithm exists locally and that the section $z$ has none globally, without proving either.
:::
