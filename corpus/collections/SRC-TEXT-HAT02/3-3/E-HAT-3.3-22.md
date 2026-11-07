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
    The fixed-cover assertion is nevertheless still not available verbatim for arbitrary N: for X
    a singleton and N=2, C=(-1,-2) union (2,infinity) has two interval components and H_1(A,C) is Z,
    not zero. The endpoint-parameterized cover is what makes the vanishing and naturality claims
    simultaneously correct.

---

::: {.problem}
Show that $H_c^n(X \times \RR; G) \approx H_c^{n-1}(X; G)$ for all $n$.
:::

::: {.solution}
For $K\subset X$ compact and an integer $N\ge1$, put
$$
I_N=[-N,N],\qquad A=X\times(-N,\infty),\qquad B=X\times(-\infty,N),
$$
and
$$
C=A\cap((X\times\RR)-(K\times I_N)),\qquad
D=B\cap((X\times\RR)-(K\times I_N)).
$$
Then $A\cup B=X\times\RR$, $C\cup D=(X\times\RR)-(K\times I_N)$, and
$$
A\cap B=X\times(-N,N),\qquad C\cap D=(X-K)\times(-N,N).
$$
Taking $N=1$ gives Stanford's fixed overlap $(-1,1)$, so the intersection is the intended copy of $(X,X-K)$.

The pair $(A,C)$ has zero cohomology because it is homotopy equivalent to $(X,X)$. Projection $A\to X$ and inclusion $g:X\to A$ as the slice $\{N+1\}$ give maps of pairs $(A,C)\to(X,X)$ and $(X,X)\to(A,C)$: $g(X)\subset C$ because it lies outside $I_N$. The composite in one direction is the identity on $X$, and in the other is homotopic to the identity through straight-line homotopies in the $t$-coordinate. Along such a homotopy, points with $x\notin K$ remain in $C$; points with $x\in K$ and $(x,t)\in C$ have $t>N$ and remain outside $I_N$ as they move to $N+1$. Thus it is a homotopy of pairs. The same argument for $(B,D)$, using the slice $\{-N-1\}$, shows it too is homotopy equivalent to $(X,X)$.

Since $C\cap D=(X-K)\times(-N,N)$, projection identifies the pair $(A\cap B,C\cap D)$ with $(X,X-K)$ up to homotopy. Applying relative Mayer--Vietoris with coefficients $G$ therefore gives
$$
\begin{aligned}
\cdots&\to H^n(X\times\RR,(X\times\RR)-(K\times I_N);G)\\
&\to H^n(A,C;G)\oplus H^n(B,D;G)=0\\
&\to H^n(A\cap B,C\cap D;G)\cong H^n((X-K)\times(-N,N);G)\\
&\to H^{n+1}(X\times\RR,(X\times\RR)-(K\times I_N);G)\to\cdots .
\end{aligned}
$$
Consequently, shifting degree only at this step,
$$
H^n(X\times\RR,(X\times\RR)-(K\times I_N);G)
\cong H^n(A\cap B,C\cap D;G)
\cong H^{n-1}(X,X-K;G).
$$

For $N\le M$ and $K\subset L$, the inclusions define maps of triples from the object indexed by $(L,M)$ to the one indexed by $(K,N)$:
$$
(A_M,C_M)\to(A_N,C_N),\qquad (B_M,D_M)\to(B_N,D_N),\qquad (A_M\cap B_M,C_M\cap D_M)\to(A_N\cap B_N,C_N\cap D_N).
$$
Here use $C_J$ and $D_J$ for the compact set $L$ and interval $I_M$ on the left, and $K$ and $I_N$ on the right. These are maps of pairs: $A_M\subset A_N$ and $B_M\subset B_N$, while points of $C_M$ or $D_M$ lie outside $L\times I_M$ and hence outside $K\times I_N$. Similarly, on the intersection $(-M,M)\subset(-N,N)$, every point of $C_M\cap D_M$ lies in $(X-L)\times(-M,M)$ and therefore in $(X-K)\times(-N,N)$. The same inclusion convention applies to the total pair $(X\times\RR,(X\times\RR)-L\times I_M)\to(X\times\RR,(X\times\RR)-K\times I_N)$. Relative Mayer--Vietoris is natural with respect to all these inclusions, so the entire diagrams, not merely the groups, are compatible with the filtered system.

The compact sets $K\times I_N$ with $K$ compact and $N\ge1$ are cofinal among compact subsets of $X\times\RR$: any compact $L$ has compact projections $K\subset X$ and $J\subset\RR$, and $J$ is contained in some $I_N$. Taking the filtered direct limit therefore yields
$$
H_c^n(X\times\RR;G)\cong H_c^{n-1}(X;G).
$$

This is the argument in **Stanford Math 215C, Solution Set 4**, Hatcher 3.3.22, printed pp. 1--2, [`solution4.pdf`](https://math.stanford.edu/~ralph/math215c/solution4.pdf) on [Ralph Cohen's Math 215C page](https://math.stanford.edu/~ralph/math215c/), held at `tmp/sources/stanford-math215c-spring2009-solution4.pdf`: relative Mayer--Vietoris, vanishing cohomology of the two side pairs, and cofinal compact products. The explicit slice-and-homotopy checks above supply the exact pairs for that argument; the slices used to define them are listed here rather than assumed.
:::
