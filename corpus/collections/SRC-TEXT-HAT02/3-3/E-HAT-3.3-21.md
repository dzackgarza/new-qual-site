---
schema: qual/card@1
id: E-HAT-3.3-21
kind: problem
title: Compactly supported cohomology and one-point compactification
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
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 21; it matches the printed text. The printed bracketed question about $X=\ZZ\times\RR$ was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: excision identifies $H^n(X^+,U_K;G)$ with $H^n(X,X-K;G)$, cone-shaped
    neighbourhoods are cofinal, and on each of them the point $\infty$ is a homotopy equivalence,
    so the limit is $H^n(X^+,\infty;G)$.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The print says "let $X^+$ be the one-point compactification" without hypotheses; that object is
    a compact Hausdorff compactification only when $X$ is locally compact Hausdorff, which the
    solution now states instead of using silently. The sets $U_K$ were also said to "range over all"
    neighbourhoods of $\infty$, which is false — they are cofinal, and the cofinality is now proved.
    DEFERRED, recorded not dropped: the printed bracketed question for $X=\ZZ\times\RR$ is not
    answered. Its hypothesis fails there, since the complement of a compact set meets infinitely many
    lines in unbounded intervals, and the card says only that; whether the isomorphism still holds is
    open on this card.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The bracketed question is now answered from Stanford Math 215C Solution Set 4, Hatcher 3.3.21,
    printed p.1. H_c^1(Z x R) is countable because cofinal rectangles K_N have finite relative
    cohomology Z^{2N+1}: each of the 2N+1 lines in K_N contributes one H^1(R,R-J_m)=Z summand. In
    contrast the circle retractions give H^1((Z x R)^+) containing Hom of the product of Z over N,
    hence uncountable. So no such isomorphism exists; the earlier lim^1 remark was unnecessary and
    has been removed.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdraws the incorrect counterexample and its audit claim. A surjection H_1(X+) to the product
    of Z gives an injection on the corresponding Hom groups, not uncountability; and the Hom group
    of the product is itself countable by Specker's theorem. Frankland, Cohomology of the Hawaiian
    Earring (2017), Theorems 1.2 and 1.3 (p.2) gives H^1(E;Z) equal to the countable direct sum,
    and Theorem 1.4 (p.3) the induced dual iso. Stanford Solution Set 4's false counterexample is
    removed. The definite answer to Hatcher's bracketed question is not established from this
    source and remains deferred.

---

::: {.problem}
For a space $X$, let $X^+$ be the one-point compactification.
If the added point, denoted $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the evident map $H_c^n(X; G) \to H^n(X^+, \infty; G)$ is an isomorphism for all $n$.
[Question: Does this result hold when $X = \ZZ \times \RR$?]
:::

::: {.solution}
Two hypotheses are implicit in taking a one-point compactification of a general $X$: that $X$ is locally compact Hausdorff, so that $X^+$ is a compact Hausdorff space with $X$ open in it. Assume that below.

For a compact $K\subset X$, let $U_K=X^+\setminus K$, an open neighborhood of $\infty$. Excision of the point $\infty$, whose closure lies in the interior of $U_K$, gives
$$
H^n(X^+,U_K;G)\cong H^n(X,X\setminus K;G).
$$
As $K$ ranges over compact subsets of $X$, the neighborhoods $U_K$ are cofinal among the neighborhoods of $\infty$: every neighborhood $U$ of $\infty$ has compact complement $X\setminus U$, and $U_{X\setminus U}\subset U$. Hence
$$
H_c^n(X;G)\cong\varinjlim_{\infty\in U}H^n(X^+,U;G),
$$
the limit on the right being over all neighborhoods of $\infty$.

Inside the cone neighborhood from the hypothesis, every neighborhood of the cone point contains a smaller cone-shaped neighborhood that contracts to the cone point by radial scaling. These contractible neighborhoods are cofinal among the neighborhoods of $\infty$. For each such $U$, the inclusion $\{\infty\}\hookrightarrow U$ is a homotopy equivalence. The map of long exact sequences for the pairs $(X^+,U)$ and $(X^+,\{\infty\})$ therefore shows that restriction is an isomorphism
$$
H^n(X^+,U;G)\xrightarrow{\cong}H^n(X^+,\infty;G).
$$
These isomorphisms commute with restriction to smaller cone neighborhoods. Taking the direct limit gives the asserted isomorphism $H_c^n(X;G)\cong H^n(X^+,\infty;G)$.

For the bracketed question $X=\ZZ\times\RR$, the cone argument above is not available: inverse stereographic projection makes $X^+$ a double Hawaiian earring, so $\infty$ has no cone neighborhood that can supply the contractible $U_K$ used there.

The proposed proof that the isomorphism is false has a substantive error and is not accepted here. Its retraction argument would produce a surjection $H_1(X^+;\ZZ)\to\prod_{\NN}\ZZ$, which by dualization gives an **injection**
$$
\operatorname{Hom}_{\ZZ}(\prod_{\NN}\ZZ,\ZZ)\hookrightarrow \operatorname{Hom}_{\ZZ}(H_1(X^+),\ZZ),
$$
not an uncountability proof. Moreover, by Specker's theorem every homomorphism $\prod_{\NN}\ZZ\to\ZZ$ is a finite linear combination of coordinate projections, so
$$
\operatorname{Hom}_{\ZZ}(\prod_{\NN}\ZZ,\ZZ)\cong\bigoplus_{\NN}\ZZ
$$
is countable.

The precise group computations are in **Martin Frankland, *Cohomology of the Hawaiian Earring* (22 February 2017)**, local file `tmp/sources/frankland-hawaiian-earring-2017.pdf` ([course page PDF](https://uregina.ca/~franklam/Frankland_HawaiianEarring_20170222.pdf)): Theorem 1.2, p. 2, is Specker's theorem; Theorem 1.3, p. 2, gives
$$
H^1(E;\ZZ)\cong\bigoplus_{\NN}\ZZ
$$
for the Hawaiian earring $E$; and Theorem 1.4, p. 3, says that the map induced by the retraction is an isomorphism
$$
\operatorname{Hom}_{\ZZ}(\prod_{\NN}\ZZ,\ZZ)\cong\operatorname{Hom}_{\ZZ}(H_1(E),\ZZ).
$$
As the question does not specify $G$, choose the same integer coefficients used by Frankland: and the compactly supported $H_c^1(\ZZ\times\RR;\ZZ)$ is also countable: the source\'s cofinal rectangle calculation gives $H^1(X,X-K_N;\ZZ)=\ZZ^{2N+1}$, one relative interval generator for each of the $2N+1$ included lines. Countability therefore gives no disproof of the bracketed isomorphism. **The bracketed question is deferred rather than answered falsely by Stanford Solution Set 4's countability argument.** Establishing a definite answer requires a different published argument checking the natural map itself.
:::
