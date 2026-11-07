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

For $X=\ZZ\times\RR$ the conclusion is **false**, not merely the cone-neighborhood proof. Under stereographic projection, $X^+$ is a double shrinking wedge of circles, so a neighborhood of $\infty$ cannot be a cone with cone point $\infty$; but the following explicit computation proves more.

For $N\ge1$ choose the cofinal rectangles
$$
K_N=[-N-\tfrac12,N+\tfrac12]\times[-N,N].
$$
If $K$ meets only the lines $\{m\}\times\RR$ with $-N\le m\le N$, then line by line $K\cap(\{m\}\times\RR)$ is a compact interval $J_m$ in the second coordinate. The relative cohomology decomposes as the finite direct sum
$$
H^1(X,X-K_N;\ZZ)=\bigoplus_{m=-N}^{N}
H^1(\RR,\RR-J_m;\ZZ),
$$
and each summand is $\ZZ$ by the pair sequence $H^1(\RR)=0$ and $\widetilde H^0(\RR-J_m)=0$. Hence $H^1(X,X-K_N)=\ZZ^{2N+1}$. The rectangles are cofinal, so $H_c^1(X;\ZZ)$ is the direct limit of these countable groups and is countable.

On the other hand, the based retractions of $X^+$ onto its circles give a surjection $H_1(X^+;\ZZ)\to\prod_{\NN}\ZZ$, so composing with that surjection embeds $\operatorname{Hom}(\prod_{\NN}\ZZ,\ZZ)$ in $H^1(X^+;\ZZ)$. The group of arbitrary integer coordinate functions is uncountable, so $H^1(X^+;\ZZ)\cong H^1(X^+,\infty;\ZZ)$ is uncountable. Therefore
$$
H_c^1(\ZZ\times\RR;\ZZ)\not\cong H^1((\ZZ\times\RR)^+,\infty;\ZZ).
$$
This is the counterexample in **Stanford Math 215C, Solution Set 4**, Hatcher 3.3.21, printed p. 1, [`solution4.pdf`](https://math.stanford.edu/~ralph/math215c/solution4.pdf), held at `tmp/sources/stanford-math215c-spring2009-solution4.pdf`. The line-by-line finite-rank and cofinality statements above check the countability argument instead of just citing the assertion.
:::
