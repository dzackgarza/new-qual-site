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

Parts (a), (b) and (c) are transcribed from published sources, and each step names its source with
its answer id or its printed page. Part (a) is Math StackExchange question 200840, answer 247553
(user26857, 2012-11-29; text version `tmp/sources/mse-200840-symmetric-group-presentation.md`),
which bounds the group by the number of cosets of a parabolic subgroup. Part (b) is the National
Taiwan University *Algebraic Geometry II*, 2020 Spring, Chapter V §4, Exercise 11, by Pei-Hsuan
Chang, printed p. 18 (text version `tmp/sources/ntu-ag2-chapter5.md`), which checks the Coxeter
relations for the two kinds of generator; the generation of $G$ by these elements is (4.10) and
Remark 4.10.1 of the book, printed pp. 403--405. Part (c) uses the order of the Weyl group
$\mathbf E_6$ from I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010),
Corollary 8.2.16, printed p. 262, and Proposition 9.1.3, printed p. 321 (text version
`tmp/sources/dolgachev-topics-classical-ag.md`), together with the order of $G$ from the book's
Remark 4.10.1, printed p. 405.

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
so their product has order $2$; and $((i,i+1)(i+1,i+2))^3=1$. Hence the images satisfy the defining
relations of $\mathbf A_n$, so $\varphi$ is a homomorphism, and the adjacent transpositions generate
$\Sigma_n$, so $\varphi$ is surjective. This is the opening of the first source, which calls the
relations the Moore relations and says of them only that "it's easily seen that these transpositions
satisfy" them, and that "it's well known that $S_n$ is a homomorphic image of $G$".
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
so that $H_1=H$. Two computations. First, $H_{i+1}\tau_i=H_i$ for $1\le i\le n-1$, since
$\sigma_{i+1}\tau_i=\sigma_i$. Second, if $j\ne i-1,i$ then $H_i\tau_j=H_i$: for $j\ge i+1$ the
generator $\tau_j$ commutes with $\sigma_i$, so
$$
H_i\tau_j=H\sigma_i\tau_j=H\tau_j\sigma_i=H\sigma_i=H_i
$$
because $\tau_j\in H$; and for $1\le j<i-1$ one writes
$\sigma_i=\sigma_j\tau_j\tau_{j+1}\sigma$ with $\sigma$ commuting with $\tau_j$ and computes
$$
H_i\tau_j
=H\sigma_j\tau_j\tau_{j+1}\sigma\tau_j
=H\sigma_j(\tau_j\tau_{j+1}\tau_j)\sigma
=H\sigma_j(\tau_{j+1}\tau_j\tau_{j+1})\sigma
=H\tau_{j+1}\sigma_j\tau_j\tau_{j+1}\sigma
=H\sigma_i ,
$$
using the braid relation and $\tau_{j+1}\in H$. Since $G$ is generated by the $\tau_i$, these two
relations show that every right coset of $H$ in $G$ is one of $H_1,\ldots,H_n$, so there are at most
$n$ of them. This is the first source's coset computation; it writes $G=\langle\tau_1,\ldots,\tau_n\rangle$
where the last index is $n-1$.
:::

:::

::: {.pf-step #an-isomorphism}
$\mathbf A_n\cong\Sigma_n$, proving part (a).

::: pf-proof
Induct on $n$, the case $n=1$ being trivial. The subgroup $H$ of step [](#an-cosets){.pf-ref} is a
homomorphic image of the group with generators $\tau_2,\ldots,\tau_{n-1}$ and the Moore relations
that do not involve $\tau_1$, so $\cardinality{H}\le\cardinality{\Sigma_{n-1}}$ by induction, and step
[](#an-cosets){.pf-ref} gives
$$
\cardinality{G}\le n\cardinality{H}\le n\cdot(n-1)!=n! .
$$
The base of the induction is $n=2$, where $\mathbf A_2=\langle x_1\mid x_1^2\rangle$ has order $2$.
Together with the surjection of step [](#an-homomorphism){.pf-ref} onto the group of order $n!$,
this gives $\cardinality{G}=n!$ and $G\cong\Sigma_n$. This is the first source's induction.
:::

:::

::: {.pf-step #e6-homomorphism}
The assignment of part (b) --- $x_1,\ldots,x_5$ to the permutations $(12),(23),\ldots,(56)$ of the
$E_i$ and $y$ to the quadratic transformation based at $P_1,P_2,P_3$ --- defines a homomorphism
$$
\Phi:\mathbf E_6\longrightarrow G ,
$$
where $G$ is the group of automorphisms of the configuration of 27 lines (4.10.1).

::: pf-proof
The images of $x_1,\ldots,x_5$ satisfy the relations of the diagram $\mathbf A_5$ by step
[](#an-homomorphism){.pf-ref}. For $y$: the quadratic transformation has order $2$, so
$\Phi(y)^2=1$; it does not depend on the order of the points $P_1,P_2,P_3$, so it commutes with the
permutations of $E_1,E_2,E_3$ and hence $\Phi(y)\Phi(x_i)=\Phi(x_i)\Phi(y)$ for $i=1,2,4,5$; and
$(\Phi(x_3)\Phi(y))^3=1$. The last two are the source's computation from its list of the images of
the $27$ lines under $\Phi(y)$:
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
The list gives the images of $21$ of the $27$ lines; the images of $F_{12},F_{13},F_{23}$ and
$G_4,G_5,G_6$ are then $E_3,E_2,E_1$ and $F_{56},F_{46},F_{45}$, as $\Phi(y)^2=1$ requires, since
$y$ is the involution of the configuration that the quadratic transformation induces.
:::

:::

::: {.pf-step #e6-surjective}
$\Phi$ is surjective, which proves part (b).

::: pf-proof
The source's last sentence cites the book: "the proof of proposition V.4.10 in the textbook says
permutation of $\{E_1,\ldots,E_6\}$ and quadratic transformation generate $G$, so $\varphi$ is
surjective". In the book, this is Remark 4.10.1, printed pp. 404--405: naming $E_1,\ldots,E_6$
uniquely determines the names of the remaining $21$ lines, since $F_{ij}$ is the unique line
meeting $E_i,E_j$ and no other $E_k$ and $G_j$ is the unique line meeting all $E_i$ except $E_j$;
by (4.10) every ordered set of six mutually skew lines is the image of $E_1,\ldots,E_6$ under some
composite of relabellings and quadratic transformations, whose proof in the book, printed
pp. 403--405, moves one line at a time into the position of $E_i$; and every automorphism of the
configuration is determined by the images of $E_1,\ldots,E_6$. Hence $G$ is generated by the
permutations $(12),\ldots,(56)$ and the quadratic transformations, which are exactly the images of
$x_1,\ldots,x_5,y$ under $\Phi$.
:::

:::

::: {.pf-step #weyl-order}
The order of the group of the exercise is
$$
\cardinality{\mathbf E_6}=51840 .
$$

::: pf-proof
The abstract group of the exercise is the Weyl group $W(\mathbf E_6)$ of the $\mathbf E_6$ root
lattice, the group generated by the reflections in a root basis of the diagram $E_6$ (Dolgachev,
§8.2, where the Weyl group of a diagram is defined this way); the two are identified by the
faithfulness of the geometric representation of a Coxeter group (Humphreys, *Reflection Groups and
Coxeter Groups*, §5.4). Dolgachev, Corollary 8.2.16, printed p. 262, computes its order from the
stabilizer of an exceptional vector: the orthogonal complement of $e_N$ in $I^{1,N}$ is
$I^{N-1}$, so the stabilizer of $e_N$ in $W(\mathbf E_N)$ is $W(\mathbf E_{N-1})$; the orbit of
$e_N$ is the set of exceptional vectors, of which there are $27$ for $N=6$ by the table of
Proposition 8.2.15, printed p. 261; and $\#W(\mathbf E_4)=5!=120$. Hence
$$
\#W(\mathbf E_6)=27\cdot\#W(\mathbf E_5)=27\cdot16\cdot120=2^3\cdot3^2\cdot6!=51840 .
$$
The printed line names $\#W(\mathbf E_4)=5!$ through its value $\#W(\mathbf E_5)=16\cdot\#W(\mathbf E_4)=2^4\cdot5!$,
and writes $W(\mathbf E_4)\cong S_5$ in a garbled form as "$W(\mathbf E_3)\cong S_5$".
:::

:::

::: {.pf-step #sixers}
The same order follows from the sixers: $W(\mathbf E_6)$ acts transitively on the sixers, the
stabilizer of a sixer is $\Sigma_6$, and there are $72$ sixers, so
$$
\#W(\mathbf E_6)=72\cdot6!=51840 .
$$

::: pf-proof
A sixer is a set of six mutually orthogonal exceptional vectors of the $\mathbf E_6$ lattice
(Dolgachev, §9.1, printed p. 319). Theorem 9.1.2, printed p. 320, lists the $36$ double-sixers,
that is, the pairs of sixers carried to each other by the reflection in the associated root, which
are $1+15+20=36$ in number; hence there are $72$ sixers, one for each root. Proposition 9.1.3,
printed p. 321, states and proves that $W(\mathbf E_6)$ acts transitively on the sixers, that the
stabilizer of the sixer $(\mathbf a_1,\ldots,\mathbf a_6)$ is $\mathfrak S_6$, and therefore, by
orbit--stabilizer,
$$
\#W(\mathbf E_6)=72\cdot720=51840 ,
$$
the count of sixers being the count of roots, as its proof says.
:::

:::

::: {.pf-step #group-order-g}
$$
\cardinality{G}=27\cdot16\cdot10\cdot6\cdot2\cdot1=51840 .
$$

::: pf-proof
This is Remark 4.10.1 of the book, printed pp. 404--405. By (4.10), every ordered set of six
mutually skew lines among the $27$ is the image of $E_1,\ldots,E_6$ under a unique automorphism of
the configuration, and every automorphism sends skew lines to skew lines and so arises this way;
from the incidence relations of the same remark the numbers of choices are $27$ for $E_1$, $16$ for
$E_2$, $10$ for $E_3$, $6$ for $E_4$, $2$ for $E_5$ and $1$ for $E_6$, which the book multiplies out
as $27\cdot16\cdot10\cdot6\cdot2=51{,}840$.
:::

:::

::: {.pf-step #e6-isomorphic-g}
$$
\mathbf E_6\cong G ,
$$
which proves part (c).

::: pf-proof
Step [](#e6-surjective){.pf-ref} gives a surjective homomorphism $\mathbf E_6\to G$. Steps
[](#weyl-order){.pf-ref} and [](#sixers){.pf-ref} give
$\cardinality{\mathbf E_6}=51840$ and step [](#group-order-g){.pf-ref} gives
$\cardinality{G}=51840$. A surjection between finite groups of the same order is an isomorphism.
:::

:::

::: pf-qed
Steps [](#an-homomorphism){.pf-ref}, [](#an-cosets){.pf-ref} and [](#an-isomorphism){.pf-ref} are
part (a); steps [](#e6-homomorphism){.pf-ref} and [](#e6-surjective){.pf-ref} are part (b); steps
[](#weyl-order){.pf-ref}, [](#sixers){.pf-ref}, [](#group-order-g){.pf-ref} and
[](#e6-isomorphic-g){.pf-ref} are part (c).
:::

:::
:::

::: {.remark title="Published solution"}
Part (a) is Math StackExchange 200840, *generators and relations of symmetric group*, answer 247553
by user26857 (2012-11-29, score 12), text version
`tmp/sources/mse-200840-symmetric-group-presentation.md`: it bounds $\cardinality{G}$ by $[G:H]\cdot\cardinality{H}$ with
$H$ the parabolic subgroup omitting $\tau_1$, as in steps [](#an-cosets){.pf-ref} and
[](#an-isomorphism){.pf-ref}. The same page carries a second answer, 200888 by paul garrett, which
routes the statement through the reflection representation and cites a proof of its injectivity
rather than giving one, and is not used here.

Part (b) is the National Taiwan University *Algebraic Geometry II* (2020 Spring, Chin-Lung Wang),
Chapter V §4, Exercise 11, by Pei-Hsuan Chang, printed p. 18, text version
`tmp/sources/ntu-ag2-chapter5.md`: part (a) of the same exercise is on printed p. 17 and gives the
coset partition $\{\mathbf A_{n-1},x_{n-1}\mathbf A_{n-1},\ldots\}$ and $\cardinality{\mathbf A_n}=n!$ directly,
which is the same argument as steps [](#an-homomorphism){.pf-ref}--[](#an-isomorphism){.pf-ref};
part (b) is step [](#e6-homomorphism){.pf-ref}, with the generation of $G$ cited to the book rather
than proved; part (c) is left blank in that source.

Part (c) is I. V. Dolgachev, *Topics in Classical Algebraic Geometry* (September 27, 2010), Corollary 8.2.16,
printed p. 262, and Proposition 9.1.3, printed p. 321, text version
`tmp/sources/dolgachev-topics-classical-ag.md`, for the order of the Weyl group, and the book's
Remark 4.10.1, printed pp. 404--405, for the order of $G$. Two further published treatments of the
order are partial. Math StackExchange 4583421, *Word processing of Coxeter group $E_6$*, answer
4736813 by KReiser (2023-07-15; text version
`tmp/sources/mse-4583421-coxeter-e6-word-processing.md`) bounds the abstract group by the coset
count $120\cdot16\cdot27=51840$, twice over, for $H=\langle x_1,x_2,x_3,y\rangle\subset F$ and
$F\subset\mathbf E_6$: it displays the two coset graphs but says of their verification "This is
actually the meat of the claim: proving this shows that there are at most this many right coset
representatives. I will skip recording this in the post, it is somewhat tedious", so the bound is
asserted there and not proved. Answer 4736825 by Jyrki Lahtonen on the same page is one paragraph:
the root system has $72$ roots forming one orbit, the highest root lies alone in the closure of the
dominant chamber and corresponds to the vertex that sticks out, "Hence the stabilizer of that root
is a Coxeter group of type $A_5$. That is, isomorphic to $S_6$", so the order is $72\cdot720$; the
$72$ roots and the type of the stabilizer are cited there, not computed, and steps
[](#weyl-order){.pf-ref} and [](#sixers){.pf-ref} are the versions of these counts that the card
transcribes from Dolgachev.
:::
