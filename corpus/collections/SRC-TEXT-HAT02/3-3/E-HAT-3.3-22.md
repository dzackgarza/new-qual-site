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

---

::: {.problem}
Show that $H_c^n(X \times \RR; G) \approx H_c^{n-1}(X; G)$ for all $n$.
:::

::: {.solution}
For each compact $K\subset X$ and integer $N\ge1$, set $I_N=[-N,N]$, and use Stanford's fixed cover
$$
A=X\times(-1,\infty),\qquad B=X\times(-\infty,1).
$$
Define
$$
C=A\cap((X\times\RR)-(K\times I_N)),\qquad
D=B\cap((X\times\RR)-(K\times I_N)).
$$
Then $A\cup B=X\times\RR$, $C\cup D=(X\times\RR)-(K\times I_N)$, $A\cap B=X\times(-1,1)$ and, because $N\ge1$ gives $(-1,1)\subset I_N$,
$$
C\cap D=(X-K)\times(-1,1).
$$

I prove that $(A,C)$ has zero cohomology. The projection $\pi:A\to X$ and the inclusion $g:X\to A$ onto the slice $\{N+1\}$ give maps of pairs $(A,C)\to(X,X)$ and $(X,X)\to(A,C)$: $g(X)\subset C$ because $N+1\notin I_N$. Plainly $\pi g=\operatorname{id}_X$, and $g\pi$ is homotopic to $\operatorname{id}_A$ by straight-line homotopy in the second coordinate. This respects $C$: if $x\notin K$, all points on the slice belong to $C$; if $x\in K$ and $(x,t)\in C$, then $t>N$, so the segment from $t$ to $N+1$ remains outside $I_N$. There is no lower component with $t<-N$, because points of $A$ have $t>-1$ and $N\ge1$. Similarly $(B,D)\simeq(X,X)$ using the slice $\{-N-1\}$.

Projection also gives the pair homotopy equivalence
$$
(A\cap B,C\cap D)\simeq(X,X-K).
$$
Relative Mayer--Vietoris therefore reads
$$
\cdots\to H^n(A,C;G)\oplus H^n(B,D;G)=0
\to H^n(A\cap B,C\cap D;G)
\to H^{n+1}(X\times\RR,(X\times\RR)-(K\times I_N);G)\to\cdots .
$$
Consequently,
$$
H^{n-1}(A\cap B,C\cap D;G)
\cong H^n(X\times\RR,(X\times\RR)-(K\times I_N);G).
$$
In particular,
$$
H^n(X\times\RR,(X\times\RR)-(K\times I_N);G)
\cong H^{n-1}(X,X-K;G).
$$
The comparison is **not** with $H^n$ of the intersection.

For naturality, let $K\subset L$ and $N\le M$, and distinguish the objects by writing $C_{K,N}$ and $D_{K,N}$ on the left and $C_{L,M}$ and $D_{L,M}$ next:
$$
C_{L,M}\subset C_{K,N},\qquad D_{L,M}\subset D_{K,N}.
$$
These inclusions are immediate from $(L\times I_M)\supset(K\times I_N)$. The same holds for the total pair:
$$
(X\times\RR)-(L\times I_M)\subset (X\times\RR)-(K\times I_N).
$$
On the intersections, both inclusions and their targets agree:
$$
C_{L,M}\cap D_{L,M}=(X-L)\times(-1,1)
\;\subset\; (X-K)\times(-1,1)=C_{K,N}\cap D_{K,N}.
$$
Each such inclusion is induced by the identity on the ambient space. The resulting restrictions are exactly the maps used to form the filtered compact-support limit, and relative Mayer--Vietoris is functorial in these inclusions. Thus the whole diagrams, not merely their cohomology groups, commute.

The sets $K\times I_N$ with $K$ compact and $N\ge1$ are cofinal among compact subsets of $X\times\RR$: a compact set has compact projection $K$ in $X$ and bounded projection in $\RR$, contained in some $I_N$. Taking the filtered direct limit yields
$$
H_c^n(X\times\RR;G)\cong H_c^{n-1}(X;G).
$$

This is **Stanford Math 215C, Solution Set 4**, Hatcher 3.3.22, printed pp. 1--2, from [Ralph Cohen's Math 215C page](https://math.stanford.edu/~ralph/math215c/), [`solution4.pdf`](https://math.stanford.edu/~ralph/math215c/solution4.pdf), held at `tmp/sources/stanford-math215c-spring2009-solution4.pdf`. The fixed overlap is $(-1,1)$, with the side-pair homotopies and cofinal compact products proved above.
:::
