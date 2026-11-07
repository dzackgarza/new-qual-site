---
schema: qual/card@1
id: E-HAT-3.2-17
kind: problem
title: Exercise 3.2.17 now reads as Proposition 3.22
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Read from the printed page 230 with pdftotext. Exercise 17 of Section 3.2 is
    the single bracketed sentence "[This has now been incorporated into
    Proposition 3.22.]" and carries no assertion of its own; the statement it
    refers to is Proposition 3.22 on p.224. This card was missing from the
    collection, which had 17 cards for the 18 exercises printed on pp.228-230.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Proposition 3.22 stated from p.224 and proved along the book's argument on
    pp.224-225, with the two alternating-sum identities for odd n computed
    rather than quoted.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Rechecked the proof step by step against pp.224-225: the CW structure with
    one cell per multiple of n; the alternative argument through the surjective
    cellular map q, which needs no assumption on n; the division of the cup
    product by q^* into the elementary symmetric sums; the even case x_1^m =
    m! x_m from (alpha_1+...+alpha_m)^m = m! alpha_1...alpha_m; and the odd case,
    where x_1^2 = 0 and the two formulas x_1 x_2^m = x_(2m+1) and
    x_2 x_1^(2m-2) = m x_(2m) follow from the alternating sums, whose values
    +1 and m are computed here. Not covered: nothing is said about J(S^n) for
    non-simply-connected coefficients, and the identification of the cup
    product ring with the divided polynomial algebra is reported as the book's
    consequence, not re-proved.
---

::: {.problem}
[This has now been incorporated into Proposition 3.22.]
:::

::: {.solution}
The printed exercise has no assertion of its own in this printing: it records that its content is Proposition 3.22 of p.224, which is therefore what is proved here.

**Proposition 3.22** (p.224). For $n>0$, $H^*(J(S^n);\ZZ)$ consists of a $\ZZ$ in each dimension a multiple of $n$. If $n$ is even, the $i$th power of a generator of $H^n(J(S^n);\ZZ)$ is $i!$ times a generator of $H^{in}(J(S^n);\ZZ)$, for each $i\ge1$. When $n$ is odd, $H^*(J(S^n);\ZZ)$ is isomorphic as a graded ring to $H^*(S^n;\ZZ)\otimes H^*(J(S^{2n});\ZZ)$.

::: pf

::: pf-step
$J(S^n)$ has a CW structure with exactly one cell in each dimension a multiple of $n$.

::: pf-proof
Hatcher p.224: $J_m(S^n)$ is a quotient of $(S^n)^m$ obtained by gluing the $m$ subcomplexes in which one coordinate is the basepoint, the gluings being cellular homeomorphisms, so $J_m(S^n)$ inherits a CW structure from $(S^n)^m$ and $J(S^n)$ is the union of the subcomplexes $J_m(S^n)\subset J_{m+1}(S^n)$. The cells of $(S^n)^m$ are products of $m$ cells each of dimension $0$ or $n$, and the gluing identifies those with a basepoint coordinate, so $J_m(S^n)$ has one cell of each dimension $kn$ with $0\le k\le m$.
:::


:::
::: pf-step
For $n>1$, the conclusion about the additive structure follows from cellular cohomology alone.

::: pf-proof
With one cell in each dimension a multiple of $n$, the cellular cochain complex has $C^{kn}=\ZZ$ and $C^j=0$ for $j$ not a multiple of $n$. For $n>1$ the two neighbours of the degree $kn$ are $kn\pm1$, neither a multiple of $n$, so both differentials into and out of $C^{kn}$ are zero and Theorem 3.5 (p.203) gives $H^{kn}=\ZZ$ and $H^j=0$ otherwise. For $n=1$ the neighbours are nonzero and this argument says nothing, which is why the next step is needed.
:::


:::
::: pf-step
For every $n\ge1$ the cellular boundary maps of $J_m(S^n)$, and hence of $J(S^n)$, are zero, so $H^*(J(S^n);\ZZ)$ is free on the cells.

::: pf-proof
The quotient map $q:(S^n)^m\to J_m(S^n)$ carries each cell homeomorphically onto a cell and takes $k$-skeleta to $k$-skeleta, so it is cellular and induces a chain map of cellular chain complexes, surjective on chains because every cell of $J_m(S^n)$ is the homeomorphic image of a cell of $(S^n)^m$. The boundary maps of $(S^n)^m$ are zero: its cohomology is $\bigotimes_{i=1}^m(\ZZ\oplus\ZZ)$ in degrees $0$ and $n$ by Theorem 3.15 (p.216), so in each degree the rank of the cohomology equals the number of cells of that degree, and a free complex whose cohomology has the rank of its chain groups in every degree has zero differentials. Now let $e$ be a cell of $J_m(S^n)$ and $c$ a cell of $(S^n)^m$ with $q_\#(c)=e$. Since $q$ is a chain map and $\partial c=0$, $\partial e=\partial q_\#(c)=q_\#(\partial c)=0$. So the cellular boundaries of $J_m(S^n)$ vanish, and the inclusion $J_m(S^n)\subset J(S^n)$ induces isomorphisms on $H^i$ for $i\le mn$ because the two have the same cells up to dimension $m$.
:::


:::
::: pf-step
Let $x_k\in H^{kn}(J_m(S^n);\ZZ)$ be dual to the $kn$ cell, with $q^*(x_k)=\sum_{i_1<\cdots<i_k}\alpha_{i_1}\cdots\alpha_{i_k}$, where $\alpha_i\in H^n((S^n)^m;\ZZ)$ is dual to the $i$th $n$ cell.

::: pf-proof
Since $q$ identifies the $m$ copies of the $n$ cell to form the $n$ cell of $J_m(S^n)$, cellular cohomology gives $q^*(x_1)=\alpha_1+\cdots+\alpha_m$; applying the same reasoning to the $kn$ cell, which is the image of the cells indexed by $k$-element subsets of the $m$ coordinates, gives the displayed formula. Cellular cohomology is Theorem 3.5 (p.203).
:::


:::
::: pf-step
If $n$ is even then $x_1^m=m!\,x_m$ in $H^{mn}(J(S^n);\ZZ)$.

::: pf-proof
For even $n$ the classes $\alpha_i$ commute with each other, and $H^*((S^n)^m;\ZZ)=\ZZ[\alpha_1,\dots,\alpha_m]/(\alpha_1^2,\dots,\alpha_m^2)$ by Theorem 3.15 (p.216). Then
$$q^*(x_1^m)=(\alpha_1+\cdots+\alpha_m)^m=m!\,\alpha_1\cdots\alpha_m=m!\,q^*(x_m),$$
the middle equality because every other monomial contains a repeated factor. Since $q^*$ is an isomorphism on $H^{mn}$, this gives $x_1^m=m!\,x_m$ in $J_m(S^n)$, and the inclusion of step three carries it to $H^*(J(S^n);\ZZ)$.
:::


:::
::: pf-step
If $n$ is odd then $x_1^2=0$ and, in $H^*(J(S^n);\ZZ)$, $x_1x_2^m=x_{2m+1}$ and $x_2x_1^{2m-2}=m\,x_{2m}$ for $m\ge1$.

::: pf-proof
For odd $n$ the classes $\alpha_i$ anticommute, so $H^*((S^n)^m;\ZZ)=\Lambda_{\ZZ}[\alpha_1,\dots,\alpha_m]$ and $x_1^2=0$ by graded commutativity of the cup product (Theorem 3.11, p.210). For the first formula, in $\Lambda_{\ZZ}[\alpha_1,\dots,\alpha_{2m+1}]$,
$$q^*(x_1x_2^m)=\Big(\sum_i\alpha_i\Big)\Big(\sum_{i_1<\cdots<i_m}\alpha_{i_1}\cdots\alpha_{i_m}\Big)=\sum_i(-1)^{i-1}\alpha_1\cdots\alpha_{2m+1},$$
and the coefficients $+1,-1,+1,\dots,+1$ over an odd number of terms sum to $+1$. For the second, in $\Lambda_{\ZZ}[\alpha_1,\dots,\alpha_{2m}]$,
$$q^*(x_2x_1^{2m-2})=\Big(\sum_{i_1<i_2}\alpha_{i_1}\alpha_{i_2}\Big)\alpha_1\cdots\widehat{\alpha_{i_1}}\cdots\widehat{\alpha_{i_2}}\cdots\alpha_{2m}=\sum_{i_1<i_2}(-1)^{i_1-1}(-1)^{i_2-2}\alpha_1\cdots\alpha_{2m},$$
and the coefficient sum $\sum_{i_1<i_2}(-1)^{i_1+i_2-3}$ equals $m$: splitting the pairs by whether the second index is $2m$ gives $\sum_{i=1}^{2m-1}(-1)^{i-1}$, which alternates from $+1$ over an odd number of terms and so totals $+1$, plus the sum over the pairs inside $\{1,\dots,2m-1\}$, which is $m-1$ by induction from the value $1$ at $m=1$. Since $q^*$ is an isomorphism in degree $mn$, both formulas follow, and the inclusion of step three carries them to $H^*(J(S^n);\ZZ)$.
:::


:::
::: pf-step
Hence for even $n$, $H^*(J(S^n);\ZZ)$ is the subring of $\QQ[x]$ generated additively by the monomials $x^i/i!$, and for odd $n$ it is $H^*(S^n;\ZZ)\otimes H^*(J(S^{2n});\ZZ)$.

::: pf-proof
For even $n$, the classes $x_i$ have $x_ix_j=\binom{i+j}{i}x_{i+j}$, which is exactly the multiplication of the divided powers $x^i/i!$, the identification being over $\QQ$; Hatcher p.224 records this as the description of the divided polynomial algebra $\Gamma_{\ZZ}[x]$. For odd $n$, $x_1^2=0$ says that the odd part is the exterior algebra on $x_1$, and the two formulas of the previous step say that the even part is generated by $x_2$ with $x_2x_1^{2m-2}=m\,x_{2m}$, which is the even case applied to $J(S^{2n})$; so the ring is the tensor product of $H^*(S^n;\ZZ)=\Lambda_{\ZZ}[x_1]$ with $H^*(J(S^{2n});\ZZ)=\Gamma_{\ZZ}[x_2]$.
:::


:::
::: pf-qed
Steps three, six and seven give the three assertions of the proposition.
:::

:::
:::
