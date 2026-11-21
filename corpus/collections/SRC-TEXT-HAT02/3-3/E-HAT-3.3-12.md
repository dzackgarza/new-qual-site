---
schema: qual/card@1
id: E-HAT-3.3-12
kind: problem
title: Commutator length in free groups
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The card wrote `\nu_i` for the first element of each commutator; the book prints
    `[v_i, w_i]` of elements `v_i, w_i` in F, and the neighbouring letter is `w`, so the
    Greek letter is a transcription slip. Compare the statement with Hatcher §3.3
    exercise 12.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 12; it matches the printed text. The printed bracketed hint recalling the attaching word of $M_k$ and asking to construct a degree 1 map $M_j\to M_k$ was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: a relation of $r_k$ as $j$ commutators turns the attaching words into a
    map $M_j\to M_k$ carrying the $2$-cell once over the $2$-cell, hence of degree $\pm1$, which
    Exercise 11 forbids when $j<k$.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The stored solution claimed degree 1 while this card's own earlier review note said $\pm1$; the
    solution now agrees: the composite with the collapse $M_k\to M_k/M_k^1=S^2$ carries the open
    2-cell homeomorphically onto $S^2$ minus the basepoint, so the degree is $\pm1$ and the
    hypothesis the argument needs is only nonvanishing, which is what the previous exercise's
    converse supplies. No other change; the attaching-word construction is unchanged.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 12 of §3.3, printed p. 258 with
    its bracketed hint (the exercises of §3.3 are 1--6 on p. 257, 7--14 on p. 258, 15--26 on p. 259
    and 27--35 on p. 260, checked at PDF pages 266--269 of the held book), and the printed page is
    added, the card having had none. Checked: the standard one-vertex cell structure of $M_g$ with
    attaching word the commutator product; the map on $1$-skeleta sending $a_i,b_i$ to loops for
    $v_i,w_i$, whose effect on the attaching loop is exactly $r_k$, the attaching word of $M_k$'s
    $2$-cell, so it extends over the $2$-cell by that cell's characteristic map; and the degree,
    computed after the collapse $M_k\to M_k/M_k^1=S^2$, where the open $2$-cell maps homeomorphically
    onto $S^2$ minus a point and the boundary to the basepoint, giving $\pm1$. The contradiction then
    uses the converse of Exercise 11 (card `E-HAT-3.3-11`, step `#s1`), whose own proof of
    injectivity of $f^*$ the card records. No defect. Not claimed: a published solution of this
    exercise, none having been located; the printed hint's construction is followed.
---

::: {.problem}
As an algebraic application of the preceding problem, show that in a free group $F$ with basis $x_1, \ldots, x_{2k}$, the product of commutators $[x_1, x_2] \cdots [x_{2k-1}, x_{2k}]$ is not equal to a product of fewer than $k$ commutators $[v_i, w_i]$ of elements $v_i, w_i \in F$.
[Recall that the $2$-cell of $M_k$ is attached by the product $[x_1, x_2]\cdots[x_{2k-1}, x_{2k}]$. From a relation $[x_1, x_2]\cdots[x_{2k-1}, x_{2k}] = [v_1, w_1]\cdots[v_j, w_j]$ in $F$, construct a degree 1 map $M_j \to M_k$.]
:::

::: {.solution}
The exercise is §3.3 Exercise 12.


The argument is the card's own, built on the converse of the preceding exercise: a relation of $r_{k}$ as $j$ commutators produces a map $M_{j}\to M_{k}$ of nonzero degree, which is impossible for $j<k$.

Let $F$ be free on $x_{1},\ldots,x_{2k}$, and $r_{k}=[x_{1},x_{2}]\cdots[x_{2k-1},x_{2k}]\in F$.

::: pf

::: {.pf-step #setup}
For each $g\ge1$ the surface $M_{g}$ has a CW structure with $1$-skeleton a wedge of $2g$ circles and a single $2$-cell attached along the commutator product $[a_{1},b_{1}]\cdots[a_{g},b_{g}]$; $M_{k}$ has the same structure with generators $x_{1},\ldots,x_{2k}$ and attaching word $r_{k}$.

::: pf-proof
The standard cell decomposition of a closed orientable surface of genus $g$ is a $2g$-gon with its boundary edges identified in pairs; the quotient of the boundary is a wedge of $2g$ circles generating the fundamental group freely, and the single $2$-cell is attached by the word reading the polygon's boundary, which in the standard identification is the commutator product. In particular $\pi_{1}(M_{k}^{1})=F$ with the $x_{i}$ a free basis.
:::

:::

::: {.pf-step #skeleta}
If $r_{k}=[v_{1},w_{1}]\cdots[v_{j},w_{j}]$ in $F$ with $j\ge1$, there is a map $g:(M_{j})^{1}\to(M_{k})^{1}$ carrying the $i$-th pair of loops to loops representing $v_{i},w_{i}$, and $g$ extends over the $2$-cell to a map $f:M_{j}\to M_{k}$.

::: pf-proof
The $1$-skeleton of $M_{j}$ is a wedge of $2j$ circles with free generators $a_{i},b_{i}$, so assigning loops representing $v_{i}$ and $w_{i}$ in $(M_{k})^{1}$ defines a map of the wedges. The boundary of the $2$-cell of $M_{j}$ is the loop $[a_{1},b_{1}]\cdots[a_{j},b_{j}]$, whose image under $g$ is the loop $[v_{1},w_{1}]\cdots[v_{j},w_{j}]=r_{k}$ — precisely, the attaching loop of the $2$-cell of $M_{k}$. Since $M_{k}$'s $2$-cell is attached along $r_{k}$, that loop is null-homotopic in $M_{k}$, so the composite $\partial D^{2}\to(M_{k})^{1}\subset M_{k}$ extends to a map of the $2$-cell $D^{2}\to M_{k}$, which may be taken to carry the interior of $D^{2}$ homeomorphically onto the interior of the $2$-cell of $M_{k}$. Together with $g$ on the $1$-skeleton this gives $f$.
:::

:::

::: {.pf-step #degree}
$f$ has degree $\pm1$.

::: pf-proof
Both surfaces are closed and orientable, so it suffices to compute the induced map on $H_{2}\cong\ZZ$. Compose $f$ with the collapse $c:M_{k}\to M_{k}/M_{k}^{1}\cong S^{2}$: the open $2$-cell of $M_{j}$ maps homeomorphically onto the open $2$-cell of $M_{k}$, which the collapse carries homeomorphically onto $S^{2}$ minus the basepoint, and the boundary of the $2$-cell of $M_{j}$ maps into the $1$-skeleton, hence to the basepoint. So $c\circ f$ is a map of $S^{2}$ that is a homeomorphism off a point, which has degree $\pm1$; and $c$ is an isomorphism on $H_{2}$, so $f_{*}$ is multiplication by $\pm1$.
:::

:::

::: {.pf-step #contradiction}
No such relation exists with $j<k$, so $r_{k}$ is not a product of fewer than $k$ commutators.

::: pf-proof
The converse of the preceding exercise gives that a map $M_{j}\to M_{k}$ of nonzero degree exists only if $j\ge k$. The reason, recorded here because it is what the argument uses: for a map of nonzero degree between closed oriented $n$-manifolds the induced map $f^{*}$ is injective in every degree, since if $f^{*}\alpha=0$ for $\alpha\in H^{m}(M_{k})$ then for the Poincaré dual class $\beta\in H^{n-m}(M_{k})$ one has $f^{*}(\alpha\smile\beta)=f^{*}\alpha\smile f^{*}\beta=0$, while $\alpha\smile\beta$ is a nonzero multiple of the fundamental class and $f^{*}$ of it is that multiple times $\deg f\cdot[M_{j}]\ne0$. So $f^{*}:H^{1}(M_{k})\to H^{1}(M_{j})$ is injective, whence $2k=\dim H^{1}(M_{k})\le\dim H^{1}(M_{j})=2j$, that is $j\ge k$. By step [](#degree){.pf-ref} the map constructed in step [](#skeleta){.pf-ref} has degree $\pm1\ne0$, so $j\ge k$. Hence an expression of $r_{k}$ as a product of $j$ commutators is possible only for $j\ge k$, which is the assertion.
:::

:::

:::
:::
