---
schema: qual/card@1
id: E-HAT-3.3-22
kind: problem
title: Compactly supported cohomology and $\times \RR$
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2, eight of them, transcribing the retained
    solution of Hatcher §3.3 Exercise 22 in Stanford Math 215C's Solution Set 4 and checking it
    against the book. The set cites nothing by number and asserts the side-pair deformations; they
    are now steps, with the homotopy written out and the two cases $x\notin K$ and $x\in K$ of the
    condition that $C$ be preserved separated, and with the vanishing of $H^n(X,X;G)$ named as the
    reason the Mayer--Vietoris middle term disappears. The citation is by exercise number only: the
    URLs and the printed locator are gone from the body, and the retained file is named. Not checked:
    no certificate, and no second source for the relative Mayer--Vietoris sequence beyond Hatcher
    §2.2, where it is stated.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 22; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 22; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: products $K\times I$ are cofinal among compact sets in $X\times\RR$, and the
    relative suspension isomorphism, from the cross product with the generator of $H^1(\RR,\RR-I)$,
    shifts degree by one compatibly with inclusions.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The step was named a "relative suspension isomorphism" without saying which map it is or why it
    is an isomorphism. It is now written as the relative cross product with the generator of
    $H^1(\RR,\RR\setminus I;\ZZ)$, identified as the relative Künneth formula of Theorem 3.18 p.219
    applied to the two pairs — one term in the sum, no Tor term because the real factor's group is
    $\ZZ$ — with coefficients $G$ reached afterwards by the universal coefficient theorem. The
    cofinality of the products $K\times I$ and compatibility with inclusions are unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The previous rewrite cited Theorem 3.18 for (X,X-K), but that theorem explicitly assumes CW
    pairs, while the exercise quantifies over arbitrary spaces X. The replacement uses the algebraic
    Kunneth argument for free relative singular cochain complexes: (R,R-I) has a free model Z in
    degree 1 with zero differential, so its contribution in total degree n is H^{n-1}(X,X-K) tensor
    the generator and its free rank-one cohomology gives no Tor term. Arbitrary G then follows from
    naturality of the universal coefficient sequence of Theorem 3.2. This covers the cofinal compact
    products K x I without introducing a CW hypothesis.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Free singular cochain groups cannot be assumed, and cohomological universal coefficients
    involves homology, so the prior Hom/Ext comparison was not justified. The proof now uses free
    relative singular chain groups, the rank-one free relative-cycle model J for the interval pair,
    and Hom(C tensor J,G) = Hom(C,G) shifted by one after the Eilenberg-Zilber comparison; the
    dependence on G is explicit before taking cohomology. Also (R,R-I) is not called an excision of
    (I,dI): the inclusion is only a relative cycle, whose generator property is proved by the
    reduced pair sequence because R is contractible and R-I has two contractible components.

- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    SOURCE DEFERRED, NOT VERIFIED. In the discarded interval-cycle step, I=[-a,a] is closed and
    its endpoints are not in R-I, so the claimed pair map, relative cycle, and class [a]-[-a] in
    H_0(R-I) were all ill-defined. Those assertions are removed. No published solution of Ex.22 is
    present in either retained solution set; earlier source-corrected events are not a completed
    source-backed proof under the current source requirement. Needed is a published solution set
    with precise page coverage, not another argument derived from Hatcher's statement or theory.

- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Source now supplied and used: Stanford Math 215C Spring 2009, Solution Set 4, Hatcher 3.3.22,
    printed pp.1-2, relative Mayer-Vietoris and cofinal compact products. The side pairs have zero
    cohomology from explicit projection maps and slice homotopies, and the intersection is (X,X-K).
    Taking N=1 gives the source's fixed (-1,1) overlap; writing A and B with N in their endpoints
    shows precisely why its retractions respect C and D for the whole cofinal family, rather than
    leaving the tangent-bottom components implicit. All claims from the earlier invalid interval-
    cycle and free-cochain argument remain withdrawn.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Two corrections to the relative MV presentation. The intersection term in the displayed long
    exact sequence is now H^n(A cap B,C cap D), with the connecting map to H^{n+1} of the union;
    only the subsequent comparison H^n(union) = H^{n-1}(X,X-K) has the degree shift. Also the
    compatibility assertion is supplied explicitly: for N<=M and K contained in L, the maps of
    triples go from the (L,M) object to the (K,N) object, and relative MV is natural under them.
    The earlier special case of H^n(union) = H^{n-1}(X,X-K) has now been corrected explicitly.
    The fixed Stanford cover works for every N>=1: for any x in K, the points of C have t>N, and
    no lower interval (-1,-N) exists, since the interval bounds already force -N<=-1. The alleged
    singleton counterexample involving (-1,-2) was an error on my part: that interval is empty.
    Its assertion that the fixed-cover side pair can be nonzero is withdrawn.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Degree and conditional-structure repairs. In the isolated comparison, the source's relative MV
    sequence gives H^{n-1}(A cap B,C cap D) is isomorphic to H^n of the union, not H^n of the
    intersection. The sequence itself retains H^n of the intersection, with connecting degree n+1.
    The fixed Stanford cover is restored, and the previously alleged counterexample is withdrawn:
    the interval written "(-1,-2)" is empty by the usual convention, and in general points in A
    with t<-N cannot exist when N>=1. For X a point the nonzero-pair assertion was therefore false.
    Under K contained in L and N<=M, the source's fixed side sets include C_{L,M} in C_{K,N}, with
    B symmetric, and the intersection inclusions make the resulting relative MV diagrams commute.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 22 of §3.3, printed p. 258, and
    against the published solution transcribed, Stanford Math 215C Spring 2009, Solution Set 4,
    Hatcher 3.3.22, printed pp. 1--2 of `tmp/sources/stanford-math215c-spring2009-solution4.pdf` —
    the construction, the two deformation retractions and the relative Mayer--Vietoris sequence on
    p. 1, and the cofinality of the products $K\times[-N,N]$ with the direct limit on p. 2, so the
    page range is right. Checked in the card: $A\cup B=X\times\RR$ and $A\cap B=X\times(-1,1)$;
    $C\cup D$ is the complement of $K\times I_N$ and $C\cap D=(X-K)\times(-1,1)$ because $N\geq1$
    puts $(-1,1)$ inside $I_N$; $(A,C)\simeq(X,X)$ through the slice $\{N+1\}$, the straight-line
    homotopy respecting $C$ since a point of $C$ over $K$ has $t>N$, with no lower component because
    $t>-1$ and $N\geq1$; $(B,D)\simeq(X,X)$ through $\{-N-1\}$; $(A\cap B,C\cap D)\simeq(X,X-K)$ by
    projection; and relative Mayer--Vietoris then gives
    $H^n(X\times\RR,(X\times\RR)-(K\times I_N))\cong H^{n-1}(X,X-K)$, with the comparison made in
    degree $n-1$ of the intersection and not in degree $n$. Checked the naturality: for $K\subset L$
    and $N\leq M$ the inclusions run $C_{L,M}\subset C_{K,N}$ and $D_{L,M}\subset D_{K,N}$, with
    $C_{L,M}\cap D_{L,M}=(X-L)\times(-1,1)\subset(X-K)\times(-1,1)$, all induced by the identity,
    so relative Mayer--Vietoris is natural for the filtered limit. The cofinality of the products and
    the direct limit give the isomorphism. No change to the mathematics. The one hypothesis the card
    states and the source does not is $N\geq1$, which is what makes $(-1,1)\subset I_N$; the source
    takes $N\in\RR$.
---

::: {.problem}
Show that $H_c^n(X \times \RR; G) \approx H_c^{n-1}(X; G)$ for all $n$.
:::

::: {.solution}
The argument is that of the retained solution set: **Stanford Math 215C, *Solution Set 4*, the solution of Hatcher §3.3 Exercise 22**, read in `tmp/sources/stanford-math215c-spring2009-solution4.pdf`, and checked against Hatcher's relative Mayer--Vietoris sequence and the definition of compactly supported cohomology in §3.1 and §3.3. Fix a coefficient group $G$ and, for a compact $K\subset X$ and an integer $N\ge1$, put $I_N=[-N,N]$ and
$$A=X\times(-1,\infty),\qquad B=X\times(-\infty,1),$$
$$C=A\cap((X\times\RR)-(K\times I_N)),\qquad D=B\cap((X\times\RR)-(K\times I_N)).$$

::: pf

::: {.pf-step #cover}
$A\cup B=X\times\RR$, $C\cup D=(X\times\RR)-(K\times I_N)$, $A\cap B=X\times(-1,1)$ and $C\cap D=(X-K)\times(-1,1)$.

::: pf-proof
The first two are immediate from the definitions, since $(X\times\RR)-(K\times I_N)$ meets $A$ and $B$ in $C$ and $D$ and is covered by them. For the third, $t>-1$ and $t<1$ give $A\cap B=X\times(-1,1)$. For the fourth, a point of $C\cap D$ lies in $A\cap B$, so it is $(x,t)$ with $-1<t<1$, and it lies in $(X\times\RR)-(K\times I_N)$; since $N\ge1$ gives $(-1,1)\subset I_N$, the condition $(x,t)\notin K\times I_N$ is exactly $x\notin K$. So $C\cap D=(X-K)\times(-1,1)$.
:::

:::

::: {.pf-step #sides}
$(A,C)$ and $(B,D)$ are homotopy equivalent to $(X,X)$ as pairs.

::: pf-proof
The projection $\pi\colon A\to X$ sends $C$ into $X$ and the inclusion $g\colon X\to A$ onto the slice $\{N+1\}$ lands in $C$, because $N+1\notin I_N$; so both are maps of pairs. Clearly $\pi g=\id_X$. The straight-line homotopy $H((x,t),s)=(x,(1-s)t+s(N+1))$ deforms $g\pi$ to $\id_A$ and keeps $C$ inside $C$: if $x\notin K$ every point of the slice lies in $C$, and if $x\in K$ and $(x,t)\in C$ then $t>N$, so the segment from $t$ to $N+1$ stays outside $I_N$; there is no lower component to arrange because points of $A$ have $t>-1\ge-N$ when $N\ge1$. The same argument with $B$ and the slice $\{-N-1\}$ gives $(B,D)\simeq(X,X)$.
:::

:::

::: {.pf-step #intersection}
$(A\cap B,C\cap D)$ is homotopy equivalent to $(X,X-K)$ as pairs.

::: pf-proof
$A\cap B=X\times(-1,1)$ and $C\cap D=(X-K)\times(-1,1)$ by step [](#cover){.pf-ref}, and the projection to $X$ carries the first pair onto the second by a homotopy equivalence of pairs, the fibre $(-1,1)$ being contractible and the homotopy $(x,t,s)\mapsto(x,(1-s)t)$ preserving membership in $(X-K)\times(-1,1)$.
:::

:::

::: {.pf-step #mv}
The relative Mayer--Vietoris sequence gives an isomorphism $H^n(X\times\RR,(X\times\RR)-(K\times I_N);G)\cong H^{n-1}(A\cap B,C\cap D;G)$.

::: pf-proof
Apply the relative Mayer--Vietoris sequence of the excisive pair $(A,B)$ with the subsets $C\subset A$ and $D\subset B$: it reads
$$\cdots\to H^n(A,C;G)\oplus H^n(B,D;G)\to H^n(A\cap B,C\cap D;G)\to H^{n+1}(X\times\RR,(X\times\RR)-(K\times I_N);G)\to\cdots,$$
using $A\cup B=X\times\RR$ and $C\cup D=(X\times\RR)-(K\times I_N)$ from step [](#cover){.pf-ref}. The first term vanishes in every degree because $(A,C)\simeq(X,X)$ by step [](#sides){.pf-ref} and $H^n(X,X;G)=0$, so exactness makes the map out of $H^n(A\cap B,C\cap D;G)$ an isomorphism, and a map that is an isomorphism of abelian groups is an isomorphism.
:::

:::

::: {.pf-step #reduce}
Hence $H^n(X\times\RR,(X\times\RR)-(K\times I_N);G)\cong H^{n-1}(X,X-K;G)$.

::: pf-proof
Combine step [](#mv){.pf-ref} with step [](#intersection){.pf-ref}, which identifies the group on the right of that isomorphism with $H^{n-1}(X,X-K;G)$.
:::

:::

::: {.pf-step #naturality}
The isomorphisms of step [](#reduce){.pf-ref} are compatible with inclusions of the indexing pairs: for compact $K\subset L$ and $N\le M$ the horizontal maps of the two Mayer--Vietoris diagrams commute.

::: pf-proof
$(L\times I_M)\supset(K\times I_N)$ gives $C_{L,M}\subset C_{K,N}$, $D_{L,M}\subset D_{K,N}$, $(X\times\RR)-(L\times I_M)\subset(X\times\RR)-(K\times I_N)$, and on the intersections $C_{L,M}\cap D_{L,M}=(X-L)\times(-1,1)\subset(X-K)\times(-1,1)$, all by step [](#cover){.pf-ref}. Each inclusion is induced by the identity of the ambient space, and relative Mayer--Vietoris is natural for maps of excisive pairs, so the resulting diagrams commute, not merely their cohomology groups.
:::

:::

::: {.pf-step #cofinal}
The sets $K\times I_N$ with $K\subset X$ compact and $N\ge1$ are cofinal among the compact subsets of $X\times\RR$.

::: pf-proof
A compact $L\subset X\times\RR$ has compact projection $K\subset X$ and bounded second projection, contained in some $[-N,N]$ with $N\ge1$; then $L\subset K\times I_N$. Passing to a larger compact set and a larger interval gives the directed structure that step [](#naturality){.pf-ref} uses.
:::

:::

::: {.pf-step}
$H_c^n(X\times\RR;G)\cong H_c^{n-1}(X;G)$.

::: pf-proof
By definition $H_c^n(X\times\RR;G)$ is the direct limit of $H^n(X\times\RR,(X\times\RR)-L;G)$ over the compact $L\subset X\times\RR$, and step [](#cofinal){.pf-ref} says that the sub-indexing by the sets $K\times I_N$ is cofinal, so the limit may be computed over them. Step [](#reduce){.pf-ref} identifies each term with $H^{n-1}(X,X-K;G)$ and step [](#naturality){.pf-ref} says the identifications are compatible with the maps of the system, so the limit is the direct limit of $H^{n-1}(X,X-K;G)$ over the compact $K\subset X$, which is $H_c^{n-1}(X;G)$.
:::

:::

:::

:::

