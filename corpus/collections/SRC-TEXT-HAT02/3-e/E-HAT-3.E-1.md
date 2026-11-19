---
schema: qual/card@1
id: E-HAT-3.E-1
kind: problem
title: "Cohomology of $K(\\ZZ_m, 1)$ with $\\ZZ_k$ coefficients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.E, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read. The two halves are right. With $m=0$ in the coefficient ring the lens-space
    complex has zero differential, so $H^q(X;\ZZ_m)=\ZZ_m$ and, for $k\mid m$, $H^q(X;\ZZ_k)=\ZZ_k$ in
    every degree; the coefficient map gives a ring homomorphism
    $H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k\to H^*(X;\ZZ_k)$ which is degreewise between free rank-one
    $\ZZ_k$-modules and carries the cellular generator to the cellular generator, hence is an
    isomorphism of rings because it is a bijective ring map. The final reduction is also right:
    for $m$ even, $x^2=(m/2)y$, and if $m/k$ is even then $m/2\equiv0$ in $\ZZ_k$, so $x^2=0$ and the
    ring is $\Lambda_{\ZZ_k}[x]\otimes\ZZ_k[y]$. The repair attributes the cellular complex (Hatcher
    Example 2.43) instead of appealing to "the standard model". Recorded, because the card should
    not be read as more than the exercise asks: when $m$ is even and $m/k$ is odd, $m/2\not\equiv0$
    in $\ZZ_k$ and $x^2\ne0$, so the conclusion in that case is not $\Lambda\otimes\ZZ_k[y]$; the
    exercise only claims the even case, and the card only displays the even case.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the infinite lens space is a
    $K(\ZZ_m,1)$ with one cell per dimension and boundary alternating $0$ and multiplication by $m$
    (Example 2.43); with coefficients in $\ZZ_m$ or in $\ZZ_k$ for $k\mid m$ every scalar $m$ is
    zero, so the cochain differentials vanish and the cohomology is the coefficient ring in each
    degree; the coefficient reduction is a degreewise isomorphism of rank-one free modules, hence a
    ring isomorphism; and Hatcher's $\ZZ_m$ ring $\Lambda[x]\otimes\ZZ_m[y]$ with $x^2=\tfrac m2y$
    for even $m$ reduces to $x^2=0$ exactly when $m/k$ is even. Added: the identification of the
    cellular boundary with the degree of the attaching map, and the case $m/k$ odd, where the
    exterior$-$polynomial description fails, which the earlier text left unsaid. No defect found in
    the statement, §3.E Exercise 1. No retained solution set covers it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology, Section 3.E (printed pp. 303-310): the exercise is
    Exercise 1 of that section. The argument was checked against the section itself. Example 3E.1
    states H^n(X;Z_m) = Z_m in every degree for X = K(Z_m,1), which is the card's second step, and
    the cellular boundary being 0 or multiplication by m is Example 2.43; with m = 0 in Z_m and in
    Z_k the cochain differentials vanish, so each coefficient ring appears in every degree, as the
    card says. The special form for m/k even follows because x^2 = (m/2)y reduces to x^2 = 0 in Z_k
    exactly when k divides m/2. The exact page of the exercise block was not pinned: the retained PDF
    has no text layer on the pages carrying it, so the citation is to the section and its printed
    range, not to a single page.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The page left unpinned in the event above is now pinned. Rendering the running heads at 120 dpi:
    PDF page 318 carries 309, page 319 carries 310 with the heading Exercises at its foot, and page
    320 carries 311, where Section 3.F begins. The exercises of Section 3.E are therefore all on
    printed p. 310, and this card's Exercise 1 is printed there.

---

::: {.problem}
Show that $H^*(K(\ZZ_m, 1); \ZZ_k)$ is isomorphic as a ring to $H^*(K(\ZZ_m, 1); \ZZ_m) \otimes \ZZ_k$ if $k$ divides $m$.
In particular, if $m/k$ is even, this is $\Lambda_{\ZZ_k}[x] \otimes \ZZ_k[y]$.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; it reads the cohomology off the infinite lens-space complex with coefficients in which $m$ vanishes. Let $X=K(\ZZ_m,1)$ and let $k\mid m$.

::: pf

::: {.pf-step #complex}
$X$ has a CW structure with one cell in every dimension whose integral cellular boundary alternates between $0$ and multiplication by $m$.

::: pf-proof
The infinite lens space $S^\infty/\ZZ_m$ is a $K(\ZZ_m,1)$, and its standard CW structure has one cell in each dimension. The cellular boundary $C_j\to C_{j-1}$ is multiplication by the degree of the attaching map $S^{j-1}\to S^{j-1}/\ZZ_m$; that degree is $0$ for $j$ odd and $m$ for $j$ even, which is the computation of Example 2.43.
:::

:::

::: {.pf-step #cohomology}
$H^q(X;\ZZ_m)\cong\ZZ_m$ and $H^q(X;\ZZ_k)\cong\ZZ_k$ for every $q\ge0$.

::: pf-proof
With coefficients in a ring $R$ the cellular cochain differential is the transpose of $C_j\otimes R\to C_{j-1}\otimes R$. In $R=\ZZ_m$ the scalar $m$ is $0$, so every differential vanishes, and the cochain complex is $\ZZ_m$ in each degree with zero maps: its cohomology is $\ZZ_m$ in each degree. The same argument with $R=\ZZ_k$, using $k\mid m$ so that $m=0$ in $\ZZ_k$, gives $\ZZ_k$ in each degree.
:::

:::

::: {.pf-step #isomorphism}
The coefficient reduction $\ZZ_m\to\ZZ_k$ induces an isomorphism $H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k\to H^*(X;\ZZ_k)$ of graded rings.

::: pf-proof
Reduction of coefficients is a natural ring map, so it gives a graded ring homomorphism from $H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k$ to $H^*(X;\ZZ_k)$. In each degree both sides are free $\ZZ_k$-modules of rank one by step [](#cohomology){.pf-ref}, and the class of a cellular generator reduces to the cellular generator of the target; a degreewise isomorphism of graded rings is an isomorphism of rings.
:::

:::

::: {.pf-step}
$\boxed{H^*(K(\ZZ_m,1);\ZZ_k)\cong H^*(K(\ZZ_m,1);\ZZ_m)\otimes\ZZ_k}$, and if $m/k$ is even this is $\Lambda_{\ZZ_k}[x]\otimes_{\ZZ_k}\ZZ_k[y]$ with $\abs x=1$, $\abs y=2$.

::: pf-proof
The first display is step [](#isomorphism){.pf-ref}. For the second, Hatcher's computation of the integral lens-space ring gives generators $x\in H^1(X;\ZZ_m)$ and $y=\beta(x)\in H^2(X;\ZZ_m)$ with $H^*(X;\ZZ_m)=\Lambda_{\ZZ_m}[x]\otimes_{\ZZ_m}\ZZ_m[y]$ and, when $m$ is even, $x^2=\tfrac m2y$. If $m/k$ is even, write $m=2rk$ with $k\mid m$; then $\tfrac m2=rk$, which is $0$ in $\ZZ_k$, so after reduction $x^2=0$ and the ring is the exterior algebra on $x$ tensored with the polynomial algebra on $y$ over $\ZZ_k$. When $m/k$ is odd the reduction keeps $x^2=\tfrac m2y\ne0$ in $\ZZ_k$ and the ring is not that exterior–polynomial product.
:::

:::

:::
:::
