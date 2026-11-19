---
schema: qual/card@1
id: P-AGH5411WEYLGROUPS
kind: problem
title: Weyl groups and the automorphisms of the configuration of 27 lines
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Picard Group
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.11, the retained Egbert note (which explicitly leaves
    the group theory undone), the cubic-surface Picard description, the 27
    line classes and incidence relations, and the quadratic transformation
    formulas. The proof below is therefore original rather than an integrated
    source solution. Part (a) bounds the A_n presentation by n! via n cosets
    of the preceding parabolic subgroup. For (b), the generators are the
    reflections in e_i-e_{i+1} and h-e_1-e_2-e_3; the 27-line incidence graph
    has exactly 72 unordered sixes of pairwise skew lines, and these
    reflections act transitively on them while the stabilizer of the standard
    six is S_6. Part (c) uses the standard faithful geometric representation
    of a Coxeter group, enumerates the 72 E_6 roots in K^perp, and identifies
    the stabilizer of 2h-sum e_i with the A_5 root subsystem of order 6!.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete three-part proof. Checked the A_n coset reduction,
    every 27-line incidence formula, the classification/count of all 72
    sixes and the four Cremona moves connecting their five S_6-orbits, and
    the 72-root enumeration in K^perp. Made the small intersecting-edge
    arguments and root-sign conjugation explicit. The final order calculation
    uses only the standard faithful geometric representation and root-
    stabilizer theorem for finite Coxeter/Weyl groups.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution pass for issue #121. Read the printed exercise in
    Hartshorne, Algebraic Geometry (1977), V.4.11, printed p. 408 (text
    version tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed
    p. N is PDF p. N+15), with Proposition 4.10 and Remark 4.10.1, printed
    pp. 403-405, and Theorem 4.9, printed pp. 402-403. Read at the cited
    places: Math StackExchange 200840, answer 247553 by user26857, text
    version tmp/sources/mse-200840-symmetric-group-presentation.md;
    National Taiwan University Algebraic Geometry II (2020 Spring),
    Chapter V §4 Exercise 11 by Pei-Hsuan Chang, printed pp. 17-18, text
    version tmp/sources/ntu-ag2-chapter5.md, and the same pages of the PDF
    for the images of the 27 lines; Dolgachev, Topics in Classical
    Algebraic Geometry (September 27, 2010), Proposition 8.2.15 and
    Corollary 8.2.16, printed pp. 261-262, Theorem 9.1.2 and Proposition
    9.1.3, printed pp. 320-321, text version
    tmp/sources/dolgachev-topics-classical-ag.md, with the printed folios
    read in the PDF, where printed p. N is PDF p. N+10; Math StackExchange
    4583421, answers 4736813 and 4736825, text version
    tmp/sources/mse-4583421-coxeter-e6-word-processing.md. Checked: the
    arithmetic of the two order computations (27*16*120 = 27*16*10*6*2 =
    72*720 = 51840); that 36 double-sixers give 72 sixers and one root per
    sixer; that Dolgachev's Corollary 8.2.16 prints 5! for W(E_4) through
    its expression for W(E_5). Not checked: no source outside these was
    read for this card, and the faithfulness of the geometric
    representation is cited (Humphreys, §5.4) rather than verified.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the published arguments transcribed, each step
    naming its source with its answer id or printed page; the card's
    earlier three-part proof, which was not a transcription, is replaced.
    Part (a) is answer 247553's coset bound (steps an-homomorphism,
    an-cosets, an-isomorphism); part (b) is NTU Exercise 11(b) (step
    e6-homomorphism) with the generation of G cited to the book's (4.10)
    and Remark 4.10.1 (step e6-surjective); part (c) is Dolgachev's
    Corollary 8.2.16 and Proposition 9.1.3 for the order of the Weyl group
    (steps weyl-order and sixers) and the book's Remark 4.10.1 for the
    order of G (step group-order-g), then equal orders (step
    e6-isomorphic-g). The remark names the two partial treatments of (c) on
    Math StackExchange 4583421 and what each leaves out.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the card beside each source. Checked the two coset computations
    of step an-cosets case by case, including the braid relation in the
    case j < i-1 and the use of tau_{j+1} in H; checked that step
    an-isomorphism's induction matches the source's (H a quotient of the
    group on tau_2,...,tau_{n-1}); checked the five Coxeter relations of
    the E_6 diagram against the listed images of y, and that the list fixes
    21 of the 27 images with y^2 = 1 supplying the other six; checked that
    G's order 27*16*10*6*2 from Remark 4.10.1 equals 72*6! and
    27*16*120. Left open and recorded on the card: the source's generation
    of G is the book's (4.10) rather than NTU's, and the two published
    coset arguments for the order of the abstract group (answer 4736813,
    answer 4736825) are partial, the first skipping its verification; the
    2026-11-16 COMPLAINTS record names that.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass, on the reader's findings for this card. The first pass
    presented part (c) as proved, resting on the identification of the
    presented group with the reflection group of the E_6 lattice, which it
    attributed to Humphreys, Reflection Groups and Coxeter Groups, §5.4, a
    book that is not among this batch's sources and that was not read. The
    card now keeps what the sources give: Dolgachev's Corollary 8.2.16,
    printed p. 262, and Proposition 9.1.3, printed p. 321, compute the order
    of that reflection group, 27*16*120 = 72*6! = 51840; the reflections in
    a root basis satisfy the diagram relations, so the presentation maps onto
    the reflection group and |E_6| >= 51840; the book's Remark 4.10.1, printed
    pp. 404--405, gives |G| = 51840. The opposite inequality
    |E_6| <= 51840, equivalently the equality of the presented group with the
    reflection group, is not supplied by any source read, so part (c)'s
    isomorphism is stated as following from that inequality and the audit and
    the COMPLAINTS record of this date say so. Also corrected: the sentence
    that the quadratic transformations are "exactly" the images of
    x_1,...,x_5,y, the others being conjugates of the image of y and hence
    also images, and the note that the NTU list covers 21 of the 27 images.
    Checked in this pass: the two order computations (27*16*120 = 51840 and
    27*16*10*6*2 = 51840 = 72*720), and that a surjection onto a group of
    order 51840 with the same source gives |E_6| >= 51840. Not checked: the
    faithfulness of the geometric representation, which no source here
    supplies, and no source outside those named was read.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (c) now separates the published order of the reflection group from
    the inequality that identifies it with the presented group, and the
    final step states that the isomorphism follows from
    |E_6| <= 51840; the claim that the quadratic transformations are the
    images is corrected to include conjugates. Provenance and process
    commentary is removed from the rendered card, and the two Math
    StackExchange answers on the order are no longer discussed there.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Re-read beside the sources. Checked part (a)'s two coset computations
    case by case, including the braid relation for j < i-1 and the use of
    tau_{j+1} in H; checked part (b)'s five relations against the listed
    images and that the six omitted images are forced by y^2 = 1; checked
    that G's generation uses the book's (4.10) and Remark 4.10.1 and not an
    NTU assertion; checked both order computations and that the inequality
    obtained is the one the sources give. Not reviewed: no proof of
    |E_6| <= 51840 was found or added; the COMPLAINTS record of this date
    names it.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass, on the second reader's findings for this card. Read again:
    Chapter V §4 Exercise 11 of tmp/sources/ntu-ag2-chapter5.md, and printed
    pp. 17--18 of tmp/sources/ntu-ag2-chapter5.pdf, whose folios are the PDF
    pages; part (a) is printed on p. 17, its last line the coset partition and
    |A_n| = n!, and part (b) on p. 18. Two corrections. The remark's pointer to
    part (a) said "the same page's part (a)" where part (b) is the page's
    subject, and it now names part (a) with its own page. The remark's closing
    sentence, that the faithfulness of the geometric representation is what
    "the sources cited here do not provide", was a statement about the sources
    rather than about the mathematics, and is replaced by the mathematical
    statement that the equality of the two orders is the injectivity of the
    geometric representation of a Coxeter group. Not checked in this pass: the
    Dolgachev proposition and corollary pages were not re-read, the two order
    computations not reopened beyond their arithmetic in the step, and no
    source outside those named on the card was read.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The two remark corrections above: part (a) of the NTU exercise carries its
    own page, printed p. 17, and the closing sentence states the injectivity of
    the geometric representation instead of reporting what the sources do not
    provide. The mathematics of the card is unchanged, and no part of it was
    moved from "open" to "proved" or the reverse.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Part (c)'s missing inequality is now published and read, which is what
    issue #158 asks for. Source: J. E. Humphreys, *Reflection Groups and
    Coxeter Groups*, Cambridge Studies in Advanced Mathematics 29 (1990),
    read on the copy at
    tmp/sources/humphreys-reflection-groups-coxeter-groups.pdf, a scan of 186
    pages without a text layer whose printed p. N is PDF p. N+17 (the folios
    read: PDF p. 104 is printed p. 87, PDF p. 125 is p. 108, PDF p. 128 is
    p. 111 and PDF p. 130 is p. 113). The geometric representation is
    constructed in §5.3, printed pp. 108--110. Theorem 5.4, printed p. 111
    and proved on pp. 111--113, is the criterion relating the sign of
    w(alpha_s) to the length of ws, and the Corollary on printed p. 113 reads
    "The representation sigma: W -> GL(V) is faithful." Step weyl-faithful now
    cites that Corollary for the bound |E_6| <= 51840, and step
    e6-isomorphic-g concludes part (c) from |E_6| = |G| = 51840 and the
    surjection of part (b), instead of stating the isomorphism as conditional
    on the inequality. The order 51840 itself is Dolgachev's Corollary 8.2.16,
    printed p. 262, already on the card and not re-read in this pass. Checked
    against the card: the six generators of the presentation act by the six
    reflections in a root basis of the E_6 lattice, which is the image whose
    order weyl-order computes. Not checked: the rest of Humphreys beyond
    §5.3--§5.4, and no other source was read for this card.
---

::: {.problem}
Given any diagram consisting of points and line segments joining some of them, we define an abstract group, given by generators and relations, as follows:

- Each point represents a generator $x_i$. The relations are
- $x_i^2=1$ for each $i$;
- $\left(x_i x_j\right)^2=1$ if $i$ and $j$ are not joined by a line segment, and
- $\left(x_i x_j\right)^3=1$ if $i$ and $j$ are joined by a line segment.

(a) The Weyl group $\mathbf{A}_n$ is defined using the diagram of $n-1$ points, each joined to the next:

    \begin{tikzcd}
    	\circ & \circ & \cdots & \circ
    	\arrow[dash, from=1-1, to=1-2]
    	\arrow[dash, from=1-2, to=1-3]
    	\arrow[dash, from=1-3, to=1-4]
    \end{tikzcd}

    Show that it is isomorphic to the symmetric group $\Sigma_n$ as follows:
    - Map the generators of $\mathbf{A}_n$ to the elements $(12),(23), \ldots, (n-1,n)$ of $\Sigma_n$, to get a surjective homomorphism $\mathbf{A}_n \rightarrow \Sigma_n$.
    - Then estimate the number of elements of $\mathbf{A}_n$ to show in fact it is an isomorphism.

(b) The Weyl group $\mathbf{E}_6$ is defined using the diagram

    \begin{tikzcd}
    	\circ & \circ & \circ & \circ & \circ \\
    	&& \circ
    	\arrow[dash, from=1-1, to=1-2]
    	\arrow[dash, from=1-2, to=1-3]
    	\arrow[dash, from=1-3, to=1-4]
    	\arrow[dash, from=1-4, to=1-5]
    	\arrow[dash, from=1-3, to=2-3]
    \end{tikzcd}

    Call the generators $x_1, \ldots, x_5$ and $y$. Show that one obtains a surjective homomorphism $\mathbf{E}_6 \rightarrow G$, the group of automorphisms of the configuration of 27 lines $(4.10.1)$, by sending $x_1, \ldots, x_5$ to the permutations $(12),(23), \ldots,(56)$ of the $E_i$, respectively, and $y$ to the element associated with the quadratic transformation based at $P_1, P_2, P_3$.

(c) Estimate the number of elements in $\mathbf{E}_6$, and thus conclude that $\mathbf{E}_6 \cong G$.

Note: See Manin $[3, \S 25,26]$ for more about Weyl groups, root systems, and exceptional curves.
:::

::: {.solution}

Part (a) is proved by bounding the group of the presentation by the number of cosets of the subgroup
generated by all but one of its generators; parts (b) and (c) concern the group $\mathbf E_6$ of the
$E_6$ diagram and the group $G$ of automorphisms of the configuration of 27 lines.

::: pf

::: {.pf-step #an-homomorphism}
For $n\ge2$ the assignment
$$
x_i\longmapsto(i,i+1),
\qquad 1\le i\le n-1,
$$
defines a surjective homomorphism
$$
\varphi:\mathbf A_n\longrightarrow\Sigma_n .
$$

::: pf-proof
The transposition $(i,i+1)$ is an involution; two such transpositions with disjoint supports commute,
so their product has order $2$; and $((i,i+1)(i+1,i+2))^3=1$. So the images satisfy the defining
relations of $\mathbf A_n$, and $\varphi$ is a homomorphism. The adjacent transpositions generate
$\Sigma_n$, so $\varphi$ is surjective. This is the opening of Math StackExchange question 200840,
answer 247553, which calls the relations the Moore relations.
:::

:::

::: {.pf-step #an-cosets}
Let $G$ be the group with generators $\tau_1,\ldots,\tau_{n-1}$ and the Moore relations, and let
$$
H=\langle\tau_2,\ldots,\tau_{n-1}\rangle\le G .
$$
Then
$$
[G:H]\le n .
$$

::: pf-proof
Put
$$
\sigma_i=\tau_1\tau_2\cdots\tau_{i-1},
\qquad
H_i=H\sigma_i,
\qquad 1\le i\le n,
$$
so $H_1=H$. First, $H_{i+1}\tau_i=H_i$ for $1\le i\le n-1$, since $\sigma_{i+1}\tau_i=\sigma_i$.
Second, if $j\ne i-1,i$ then $H_i\tau_j=H_i$: for $j\ge i+1$ the generator $\tau_j$ commutes with
$\sigma_i$, so
$$
H_i\tau_j=H\sigma_i\tau_j=H\tau_j\sigma_i=H\sigma_i=H_i
$$
because $\tau_j\in H$; for $1\le j<i-1$ one writes $\sigma_i=\sigma_j\tau_j\tau_{j+1}\sigma$ with
$\sigma$ commuting with $\tau_j$ and computes
$$
H_i\tau_j
=H\sigma_j\tau_j\tau_{j+1}\sigma\tau_j
=H\sigma_j(\tau_j\tau_{j+1}\tau_j)\sigma
=H\sigma_j(\tau_{j+1}\tau_j\tau_{j+1})\sigma
=H\tau_{j+1}\sigma_j\tau_j\tau_{j+1}\sigma
=H\sigma_i,
$$
using the braid relation and $\tau_{j+1}\in H$. Since $G$ is generated by the $\tau_i$, every right
coset of $H$ is one of $H_1,\ldots,H_n$, so there are at most $n$ of them. This is answer 247553's
coset computation; it writes the generating set as $\tau_1,\ldots,\tau_n$ where the last index
is $n-1$.
:::

:::

::: {.pf-step #an-isomorphism}
$\mathbf A_n\cong\Sigma_n$, which is part (a).

::: pf-proof
Induct on $n$, the case $n=1$ being trivial. The subgroup $H$ of step [](#an-cosets){.pf-ref} is a
homomorphic image of the group with generators $\tau_2,\ldots,\tau_{n-1}$ and the Moore relations not
involving $\tau_1$, so $\cardinality{H}\le\cardinality{\Sigma_{n-1}}$ by induction, and step
[](#an-cosets){.pf-ref} gives
$$
\cardinality{G}\le n\cardinality{H}\le n\cdot(n-1)!=n! .
$$
For $n=2$, $\mathbf A_2=\langle x_1\mid x_1^2\rangle$ has order $2$. With the surjection of step
[](#an-homomorphism){.pf-ref} onto the group of order $n!$ this gives $\cardinality{G}=n!$ and
$G\cong\Sigma_n$. This is answer 247553's induction.
:::

:::

::: {.pf-step #e6-homomorphism}
The assignment of part (b), sending $x_1,\ldots,x_5$ to the permutations $(12),(23),\ldots,(56)$ of
the $E_i$ and $y$ to the quadratic transformation based at $P_1,P_2,P_3$, defines a homomorphism
$$
\Phi:\mathbf E_6\longrightarrow G
$$
to the group of automorphisms of the configuration of 27 lines (4.10.1).

::: pf-proof
The images of $x_1,\ldots,x_5$ satisfy the relations of the diagram $\mathbf A_5$ by step
[](#an-homomorphism){.pf-ref}. For $y$: the quadratic transformation has order $2$, so
$\Phi(y)^2=1$; it does not depend on the order of $P_1,P_2,P_3$, so it commutes with the permutations
of $E_1,E_2,E_3$ and $\Phi(y)\Phi(x_i)=\Phi(x_i)\Phi(y)$ for $i=1,2,4,5$; and
$(\Phi(x_3)\Phi(y))^3=1$. The last two are computed in Chapter V §4 Exercise 11 of the National
Taiwan University *Algebraic Geometry II* homework (2020 Spring), by Pei-Hsuan Chang, printed p. 18,
from the images of the $27$ lines under $\Phi(y)$:
$$
\Phi(y)(E_i)=F_{jk}\ \ (\{i,j,k\}=\{1,2,3\}),\quad
\Phi(y)(E_i)=E_i\ \ (i=4,5,6),
$$
$$
\Phi(y)(F_{ij})=F_{ij}\ \ (i\in\{1,2,3\},\ j\in\{4,5,6\}),\quad
\Phi(y)(F_{ij})=G_k\ \ (\{i,j,k\}=\{4,5,6\}),
$$
$$
\Phi(y)(G_i)=G_i\ \ (i=1,2,3).
$$
These are $21$ of the $27$ images; the remaining six are $E_3,E_2,E_1$ and $F_{56},F_{46},F_{45}$, the
inverse images of $F_{12},F_{13},F_{23}$ and $G_4,G_5,G_6$, since $\Phi(y)^2=1$.
:::

:::

::: {.pf-step #e6-surjective}
$\Phi$ is surjective, which is part (b).

::: pf-proof
By Proposition 4.10 and Remark 4.10.1 of the book, printed pp. 403--405, naming $E_1,\ldots,E_6$
uniquely determines the remaining $21$ lines, since $F_{ij}$ is the unique line meeting $E_i,E_j$ and
no other $E_k$ and $G_j$ is the unique line meeting all $E_i$ except $E_j$; every ordered set of six
mutually skew lines is the image of $E_1,\ldots,E_6$ under a composite of relabellings and quadratic
transformations, the proof moving one line at a time into the position of $E_i$; and every
automorphism of the configuration is determined by the images of $E_1,\ldots,E_6$. Hence $G$ is
generated by the permutations $(12),\ldots,(56)$ and the quadratic transformations. The images under
$\Phi$ are those permutations and the single quadratic transformation at $P_1,P_2,P_3$; a quadratic
transformation at any other triple is the conjugate of that one by a permutation of the indices,
hence also lies in the image, since the permutations do.
:::

:::

::: {.pf-step #weyl-order}
Let $W(\mathbf E_6)$ be the Weyl group of the $\mathbf E_6$ lattice, the group generated by the
reflections in a root basis of the diagram $E_6$. Then
$$
\cardinality{W(\mathbf E_6)}=51840,
\qquad\text{and}\qquad
\cardinality{\mathbf E_6}\ge51840 .
$$

::: pf-proof
The first equality is I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010),
Corollary 8.2.16, printed p. 262, which counts the stabilizer of an exceptional vector: the
orthogonal complement of $e_N$ in $I^{1,N}$ is $I^{N-1}$, so the stabilizer of $e_N$ in
$W(\mathbf E_N)$ is $W(\mathbf E_{N-1})$; the orbit of $e_N$ is the set of exceptional vectors, of
which there are $27$ for $N=6$ by the table of Proposition 8.2.15, printed p. 261; and
$\#W(\mathbf E_4)=5!=120$. Hence
$$
\#W(\mathbf E_6)=27\cdot\#W(\mathbf E_5)=27\cdot16\cdot120=2^3\cdot3^2\cdot6!=51840 .
$$
For the inequality: the generators $x_i$ and $y$ of the presentation act on the $\mathbf E_6$ lattice
by the reflections in the corresponding root basis, whose pairwise products have orders $2$ and $3$
as the diagram prescribes, so the assignment is a homomorphism $\mathbf E_6\to W(\mathbf E_6)$, and
it is surjective because those reflections generate $W(\mathbf E_6)$; hence
$\cardinality{\mathbf E_6}\ge\cardinality{W(\mathbf E_6)}$.
:::

:::

::: {.pf-step #weyl-faithful}
$$
\cardinality{\mathbf E_6}\le 51840 .
$$

::: pf-proof
The geometric representation of the Coxeter group $\mathbf E_6$ is faithful. On the real vector space
$V$ with basis the simple roots $\alpha_s$, the form $B(\alpha_s,\alpha_t)=-\cos(\pi/m_{st})$ and the
reflections $\sigma_s(\lambda)=\lambda-2B(\alpha_s,\lambda)\alpha_s$ define a homomorphism
$\sigma\colon\mathbf E_6\to\operatorname{GL}(V)$, and Humphreys, *Reflection Groups and Coxeter Groups*,
§5.4, Theorem 5.4 with the Corollary that follows it, printed pp. 111--113, proves that $\sigma$ is
injective; the Corollary, on printed p. 113, reads "The representation $\sigma\colon W\to\operatorname{GL}(V)$ is faithful."
Its image is the reflection group $W(\mathbf E_6)$ of the $\mathbf E_6$ lattice, of order $51840$ by step
[](#weyl-order){.pf-ref}. Hence $\cardinality{\mathbf E_6}=51840$, and in particular the inequality displayed.
:::

:::

::: {.pf-step #sixers}
The same order is the orbit--stabilizer count of the sixers:
$$
\cardinality{W(\mathbf E_6)}=72\cdot6!=51840 .
$$

::: pf-proof
A sixer is a set of six mutually orthogonal exceptional vectors of the $\mathbf E_6$ lattice:
Dolgachev, §9.1, printed p. 319. Theorem 9.1.2, printed p. 320, lists the $36$ double-sixers, the
pairs of sixers carried to each other by the reflection in the associated root, and they number
$1+15+20=36$, so there are $72$ sixers, one for each root. Proposition 9.1.3, printed p. 321, states
and proves that $W(\mathbf E_6)$ acts transitively on the sixers and that the stabilizer of the sixer
$(\mathbf a_1,\ldots,\mathbf a_6)$ is $\mathfrak S_6$; orbit--stabilizer then gives the displayed
order.
:::

:::

::: {.pf-step #group-order-g}
$$
\cardinality{G}=27\cdot16\cdot10\cdot6\cdot2\cdot1=51840 .
$$

::: pf-proof
This is Remark 4.10.1 of the book, printed pp. 404--405. By Proposition 4.10 every ordered set of six
mutually skew lines among the $27$ is the image of $E_1,\ldots,E_6$ under a unique automorphism of
the configuration, and every automorphism sends skew lines to skew lines and so arises this way; from
the incidence relations of the same remark the numbers of choices are $27$ for $E_1$, $16$ for $E_2$,
$10$ for $E_3$, $6$ for $E_4$, $2$ for $E_5$ and $1$ for $E_6$, which the book multiplies out as
$51{,}840$.
:::

:::

::: {.pf-step #e6-isomorphic-g}
$\mathbf E_6\cong G$, which is part (c).

::: pf-proof
Steps [](#e6-surjective){.pf-ref} and [](#group-order-g){.pf-ref} give a surjection
$\mathbf E_6\to G$ and $\cardinality{G}=51840$; step [](#weyl-faithful){.pf-ref} gives
$\cardinality{\mathbf E_6}=51840$. A surjection between finite groups of equal order is an
isomorphism.
:::

:::

::: pf-qed
Steps [](#an-homomorphism){.pf-ref}, [](#an-cosets){.pf-ref} and [](#an-isomorphism){.pf-ref} are
part (a); steps [](#e6-homomorphism){.pf-ref} and [](#e6-surjective){.pf-ref} are part (b); steps
[](#weyl-order){.pf-ref}, [](#weyl-faithful){.pf-ref}, [](#sixers){.pf-ref},
[](#group-order-g){.pf-ref} and [](#e6-isomorphic-g){.pf-ref} are part (c).
:::

:::
:::

::: {.remark title="Published solution"}
Part (a): Math StackExchange question 200840, answer 247553 by user26857 (2012-11-29), whose coset
bound is steps [](#an-cosets){.pf-ref} and [](#an-isomorphism){.pf-ref}.

Part (b): National Taiwan University, *Algebraic Geometry II* (2020 Spring, Chin-Lung Wang), Chapter
V §4 Exercise 11, by Pei-Hsuan Chang: part (b), printed p. 18, checks the Coxeter relations for the
two kinds of generator, and part (a), printed p. 17, gives the coset partition of $\mathbf A_n$ and
$\cardinality{\mathbf A_n}=n!$ directly.

Parts (b) and (c): Proposition 4.10 and Remark 4.10.1 of the book, printed pp. 403--405, for the
generation of $G$ and its order $51{,}840$.

Part (c): I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010), Proposition
8.2.15 and Corollary 8.2.16, printed pp. 261--262, for $\#W(\mathbf E_6)=2^3\cdot3^2\cdot6!$ from
the count of exceptional vectors, and Theorem 9.1.2 and Proposition 9.1.3, printed pp. 320--321, for
the same order as $72\cdot6!$ from the sixers. Both are orders of the reflection group of the
$\mathbf E_6$ lattice, which the presentation maps onto, so they give
$\cardinality{\mathbf E_6}\ge51840$; the reverse inequality is the faithfulness of the geometric
representation of the Coxeter group $\mathbf E_6$: Humphreys, *Reflection Groups and Coxeter Groups*,
§5.4, Theorem 5.4 with its Corollary, printed pp. 111--113.
:::
