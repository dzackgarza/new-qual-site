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

---

::: {.problem}
Show that $H_c^n(X \times \RR; G) \approx H_c^{n-1}(X; G)$ for all $n$.
:::

::: {.solution}
Let $K\subset X$ be compact and $I=[-a,a]\subset\RR$ with $a>0$. The sets $K\times I$ are cofinal among compact subsets of $X\times\RR$: the projections of any compact subset are compact and lie in such a product. **Published solution required; the proof is deferred.** The retained solution sets contain no solution to Hatcher §3.3 Exercise 22: neither Sam's §3.3 selection nor the Math 538 sheets includes it. Consequently this compact-support computation has no accepted source-backed proof in the corpus.

The argument formerly kept here is withdrawn rather than patched by another derivation. It used $I=[-a,a]$, but $\pm a\notin\mathbb R-I$, so $e:(I,\partial I)\to(\mathbb R,\mathbb R-I)$ was not a map of pairs; $e$ was not a relative cycle and $[a]-[-a]$ was not a class in $H_0(\mathbb R-I)$. The previously displayed product map and the claimed $\operatorname{Hom}$ comparison therefore did not deliver the degree shift. Needed source: a published solution set covering §3.3 Exercise 22, with the set and printed page cited.
:::
