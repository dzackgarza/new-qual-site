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
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Answers the bracketed question negatively in degree two with integer coefficients. The
    cofinal-rectangle calculation gives H_c^2(Z x R; Z) = 0. The compactification is the
    Hawaiian earring E, whose H_1 has a Q direct summand by Eda-Kawamura, Theorem 3.1,
    pp.307-310 (also stated as Frankland Theorem 2.1, p.3). Universal coefficients and
    Wiegold's nonzero Ext(Q,Z), pp.341-342, then give H^2(E; Z) != 0, so the natural map is not
    an isomorphism. Replaces the deferred and H^1-only discussion with this complete published
    argument; the cone-neighborhood proof in the first part is unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read Hatcher pp.243-244 and the complete Eda-Kawamura and Wiegold papers. Checked that
    H^2(E, infinity; Z) agrees with H^2(E; Z) by the pair sequence, that Ext is additive over
    the Q direct summand, and that the cofinal relative intervals make all degree-two compactly
    supported groups vanish. Thus this is a counterexample already for n = 2 and G = Z, not a
    claim that H^1 fails or that no coefficient group could work.
---

::: {.problem}
For a space $X$, let $X^+$ be the one-point compactification.
If the added point, denoted $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the evident map $H_c^n(X; G) \to H^n(X^+, \infty; G)$ is an isomorphism for all $n$.
[Question: Does this result hold when $X = \ZZ \times \RR$?]
:::

::: {.solution}
Assume that $X$ is locally compact Hausdorff, so that $X^+$ is a compact Hausdorff space with $X$ open in it.

::: pf

::: {.pf-step #excision-limit}
Excision identifies $H_c^n(X;G)$ with the direct limit of $H^n(X^+,U;G)$ over all neighborhoods $U$ of $\infty$.

::: pf-proof
For a compact $K\subset X$, let $U_K=X^+\setminus K$, an open neighborhood of $\infty$. Excision of the point $\infty$, whose closure lies in the interior of $U_K$, gives
$$
H^n(X^+,U_K;G)\cong H^n(X,X\setminus K;G).
$$
As $K$ ranges over compact subsets of $X$, the neighborhoods $U_K$ are cofinal among the neighborhoods of $\infty$: every neighborhood $U$ of $\infty$ has compact complement $X\setminus U$, and $U_{X\setminus U}\subset U$. Since the direct limit defining $H_c^n(X;G)$ can be taken over this cofinal family,
$$
H_c^n(X;G)\cong\varinjlim_{\infty\in U}H^n(X^+,U;G).
$$
:::

:::

::: {.pf-step #cone-case}
If $\infty$ has a cone neighborhood in $X^+$, then the evident map $H_c^n(X;G)\to H^n(X^+,\infty;G)$ is an isomorphism for all $n$.

::: pf-proof
Inside the cone neighborhood from the hypothesis, every neighborhood of the cone point contains a smaller cone-shaped neighborhood that contracts to the cone point by radial scaling. These contractible neighborhoods are cofinal among the neighborhoods of $\infty$. For each such $U$, the inclusion $\{\infty\}\hookrightarrow U$ is a homotopy equivalence. The map of long exact sequences for the pairs $(X^+,U)$ and $(X^+,\{\infty\})$ therefore shows that restriction is an isomorphism
$$
H^n(X^+,U;G)\xrightarrow{\cong}H^n(X^+,\infty;G).
$$
These isomorphisms commute with restriction to smaller cone neighborhoods. Taking the direct limit and using step [](#excision-limit){.pf-ref} gives the asserted isomorphism $H_c^n(X;G)\cong H^n(X^+,\infty;G)$.
:::

:::

::: {.pf-step #compact-degree-two}
For $X=\ZZ\times\RR$ and integer coefficients, $H_c^2(X;\ZZ)=0$.

::: pf-proof
Let $J_N=[-N-1/2,N+1/2]$ and $K_N=([-N-1/2,N+1/2]^2)\cap X$ for $N\ge1$. These compact rectangles are cofinal among compact subsets of $X$. On each of the $2N+1$ lines meeting $K_N$, the relative cohomology is $H^q(\RR,\RR-J_N;\ZZ)$, which is $\ZZ$ for $q=1$ and zero otherwise. Hence
$$
H^q(X,X-K_N;\ZZ)\cong
\begin{cases}
\ZZ^{2N+1},&q=1,\\
0,&q\ne1.
\end{cases}
$$
In particular, the direct limit in step [](#excision-limit){.pf-ref} vanishes in degree two.
:::

:::

::: {.pf-step #earring-degree-two}
The compactification $E=(\ZZ\times\RR)^+$ has $H^2(E,\infty;\ZZ)\ne0$.

::: pf-proof
Each line becomes a circle in $E$, with all circles sharing $\infty$, and every neighborhood of $\infty$ contains all but finitely many whole circles. Thus $E$ is the Hawaiian earring. The pair sequence gives $H^2(E,\infty;\ZZ)\cong H^2(E;\ZZ)$, and universal coefficients give an injection
$$
\operatorname{Ext}_{\ZZ}(H_1(E;\ZZ),\ZZ)\hookrightarrow H^2(E;\ZZ).
$$
By **K. Eda and K. Kawamura, *The Singular Homology of the Hawaiian Earring*, Theorem 3.1, pp. 307--310** (`tmp/sources/eda-kawamura-hawaiian-earring-2000.pdf`), $H_1(E;\ZZ)$ has a direct summand isomorphic to $\QQ$; this is also stated as Theorem 2.1 of **Martin Frankland, *Cohomology of the Hawaiian Earring*, p. 3** (`tmp/sources/frankland-hawaiian-earring-2017.pdf`). Consequently $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)$ is a direct summand of the left-hand group above. By **James Wiegold, *Ext(Q,Z) is the additive group of real numbers*, pp. 341--342** (`tmp/sources/wiegold-ext-q-z-1969.pdf`), $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)\cong\RR\ne0$. The target group is therefore nonzero.
:::

:::

::: pf-step
The answer to the bracketed question is no, already for $G=\ZZ$ and $n=2$.

::: pf-proof
Steps [](#compact-degree-two){.pf-ref} and [](#earring-degree-two){.pf-ref} give
$$
\boxed{H_c^2(\ZZ\times\RR;\ZZ)=0,\qquad H^2((\ZZ\times\RR)^+,\infty;\ZZ)\ne0,}
$$
so the evident map cannot be an isomorphism. Inverse stereographic projection already shows that $\infty$ has no cone neighborhood that could supply the contractible $U_K$ in step [](#cone-case){.pf-ref}. This counterexample does not depend on the previously rejected countability argument, and it makes no assertion that the degree-one map fails.
:::

:::

:::
:::
