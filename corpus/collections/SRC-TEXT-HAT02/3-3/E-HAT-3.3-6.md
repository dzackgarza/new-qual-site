---
schema: qual/card@1
id: E-HAT-3.3-6
kind: problem
title: Connected sums of manifolds
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
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Rechecked the statement against Hatcher and repaired the existing solution.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the invalid homological argument with a correct proof.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 6; it matches the printed text. The printed bracketed sentence "[Euler characteristics may help in the exceptional case.]" was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both parts. For (a): excision identifies $H_j(M_i,N_i)$ with $H_j(D^n,S^{n-1})$,
    Mayer-Vietoris gives the direct sum below degree $n-1$, and the rank of $H_{n-1}$ is settled by
    counting how many of the two boundary spheres are rationally essential, which happens exactly
    for the nonorientable summands; Corollary 3.28 then supplies the torsion, so one $\ZZ_2$ is
    replaced by $\ZZ$ precisely when both summands are nonorientable. For (b) the Euler
    characteristic count $\chi(N_i)=\chi(M_i)-(-1)^n$ with additivity over $S^{n-1}$ gives
    $\chi(M_1)+\chi(M_2)-\chi(S^n)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Re-read at the level of the gap: the vanishing $H_n(N_i;\QQ)=0$ that the rational pair sequence
    displays as a leading zero was asserted, not proved, and it is what makes the rank count work;
    it now comes from $M_i\setminus\{p\}\simeq N_i$ being a connected noncompact $n$-manifold and
    Proposition 3.29 p.239. The Mayer-Vietoris step now also says that it is read in reduced
    homology, which is what removes the $H_0(S^{n-1})$ term at $j=1$. The rest is as previously
    checked: the exceptional case is a rank count plus the torsion of Corollary 3.28 p.238. Not
    checked: the additivity of $\chi$ over a CW decomposition is used as in the text, not reproved.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Source-backed rewrite from the Math 538 homework solutions, HMW 3 handwritten pages 2-4 (PDF
    pages 14, 15, 16), Hatcher 3.3 #6, replacing the card's excision-plus-Mayer-Vietoris route with
    the printed pair-sequence of (M, S^{n-1}) and the identification M/S^{n-1} = M_1 v M_2; the three
    cases, the Corollary 3.28 torsion step, and part (b) as the degree-by-degree rank count ending in
    (-1) + (-1)^{n+1} = -chi(S^n) are the sheet's. Verified independently that all three cases give
    chi(M_1) + chi(M_2) - chi(S^n), and supplied the two things the sheet leaves implicit: n = 2
    (where H_{n-2}(S^{n-1}) is nonzero and the sequence must be read in reduced homology) and the
    good-pair justification of H_i(M,S^{n-1}) = H_i(M_1 v M_2). The earlier note below on
    H_n(N_i;Q) belonged to the route this rewrite replaced.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Two proof defects in the previous revision. (1) The orientability converse argued from the
    injection H_n(M) -> H_n(M_1) + H_n(M_2) that both summands must be Z, which is false (Z injects
    into Z + 0); what settles it is the computation of ker psi already made in the three cases —
    psi is an isomorphism on the summand of an orientable factor and zero on a nonorientable one, so
    ker psi = Z exactly when both factors are orientable. The paragraph now says that. (2) The
    rewrite had dropped the case n = 1; it is restored and settled against the printed exercise: a
    closed connected 1-manifold is a circle, so the connected sum is S^1, part (a) is vacuous there
    (0 < i < 1) and part (b) reads 0 = 0 + 0 - 0.

---

::: {.problem}
Given two disjoint connected $n$-manifolds $M_1$ and $M_2$, a connected $n$-manifold $M_1 \sharp M_2$, their connected sum, can be constructed by deleting the interiors of closed $n$-balls $B_1 \subset M_1$ and $B_2 \subset M_2$ and identifying the resulting boundary spheres $\partial B_1$ and $\partial B_2$ via some homeomorphism between them.
(Assume that each $B_i$ embeds nicely in a larger ball in $M_i$.)

(a) Show that if $M_1$ and $M_2$ are closed then there are isomorphisms $H_i(M_1 \sharp M_2; \ZZ) \approx H_i(M_1; \ZZ) \oplus H_i(M_2; \ZZ)$ for $0 < i < n$, with one exception: If both $M_1$ and $M_2$ are nonorientable, then $H_{n-1}(M_1 \sharp M_2; \ZZ)$ is obtained from $H_{n-1}(M_1; \ZZ) \oplus H_{n-1}(M_2; \ZZ)$ by replacing one of the two $\ZZ_2$ summands by a $\ZZ$ summand.
[Euler characteristics may help in the exceptional case.]

(b) Show that $\chi(M_1 \sharp M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$ if $M_1$ and $M_2$ are closed.
:::

::: {.solution}

The solution is the one printed in the Math 538 homework solutions, HMW 3, handwritten pages 2--4 (PDF pages 14, 15 and 16 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #6: the same identification $M_1\sharp M_2/S^{n-1}=M_1\vee M_2$, the same pair sequence, the same three cases with Corollary 3.28 for the torsion, and part (b) by a degree-by-degree count of ranks. Two things that sheet leaves implicit are supplied here: the case $n=2$, where $H_{n-2}(S^{n-1})\ne0$ and the sequence must be read in reduced homology, and the good-pair justification of $H_i(M,S^{n-1})\cong\widetilde H_i(M_1\vee M_2)$. Coefficients are $\ZZ$ throughout.

Let $M_1,M_2$ be closed connected $n$-manifolds, $B_i\subset M_i$ closed balls embedded nicely, $N_i=M_i\setminus\operatorname{int}B_i$, and $M=M_1\sharp M_2=N_1\cup_{S^{n-1}}N_2$ with $S^{n-1}=N_1\cap N_2$ the identified boundary.

::: pf

::: {.pf-step #good-pair}
$H_i(M,S^{n-1})\cong\widetilde H_i(M_1\vee M_2)=\widetilde H_i(M_1)\oplus\widetilde H_i(M_2)$ for all $i$.

::: pf-proof
The identification of the two boundary spheres makes $M$ the union of $N_1$ and $N_2$ along their common boundary $S^{n-1}$, and collapsing that sphere gives $M/S^{n-1}\cong M_1\vee M_2$: each $N_i$ becomes $M_i$ with the ball collapsed to the wedge point. Since $\partial N_i=S^{n-1}$ has a collar in $M$ — the balls are embedded nicely in larger balls, so the boundary has a product neighbourhood — the pair $(M,S^{n-1})$ is a good pair, and $H_i(M,S^{n-1})\cong\widetilde H_i(M/S^{n-1})$. Reduced homology of a wedge of two spaces is the sum of the reduced homologies.
:::

:::

::: {.pf-step #sequence}
The long exact sequence of the pair reads
$$
\cdots\to\widetilde H_i(S^{n-1})\to\widetilde H_i(M)\to\widetilde H_i(M_1)\oplus\widetilde H_i(M_2)\xrightarrow{\ \partial\ }\widetilde H_{i-1}(S^{n-1})\to\cdots
$$
with $\widetilde H_i(S^{n-1})=0$ for $i\ne n-1$ and $\widetilde H_{n-1}(S^{n-1})\cong\ZZ$.

::: pf-proof
The pair sequence in reduced homology, with the relative terms replaced by step [](#good-pair){.pf-ref}, has the displayed form; the homology of $S^{n-1}$ is $\ZZ$ in degrees $0$ and $n-1$ and zero between, so the reduced homology vanishes except in degree $n-1$, where it is $\ZZ$ generated by the fundamental class.
:::

:::

::: {.pf-step #middle}
For $1\le i\le n-2$, $H_i(M)\cong H_i(M_1)\oplus H_i(M_2)$.

::: pf-proof
For such $i$ both neighbouring terms of step [](#sequence){.pf-ref} vanish: $\widetilde H_i(S^{n-1})=0$ because $i\ne n-1$, and $\widetilde H_{i-1}(S^{n-1})=0$ because $i-1\ne n-1$. So the map $\widetilde H_i(M)\to\widetilde H_i(M_1)\oplus\widetilde H_i(M_2)$ has zero kernel and zero cokernel, hence is an isomorphism; and for $i\ge1$ the reduced and unreduced groups coincide.
:::

:::

::: {.pf-step #top}
For $n\ge3$ the end of the sequence is
$$
0\to H_n(M)\to H_n(M_1)\oplus H_n(M_2)\xrightarrow{\ \psi\ }\ZZ\to H_{n-1}(M)\to H_{n-1}(M_1)\oplus H_{n-1}(M_2)\to0,
$$
where $H_n(M_i)$ is $\ZZ$ if $M_i$ is orientable and $0$ otherwise, and $\psi$ is the sum of the two boundary maps $H_n(M_i)\to H_{n-1}(S^{n-1})$, each an isomorphism for an orientable summand and zero for a nonorientable one.

::: pf-proof
For $n\ge3$ one has $n-2\ne n-1$, so $\widetilde H_{n-2}(S^{n-1})=0$, which turns the two ends of the fragment into the zero groups displayed. A closed connected $n$-manifold has $H_n\cong\ZZ$ when orientable and $H_n=0$ when not (Theorem 3.26), and the boundary map of a collared boundary sphere is an isomorphism onto $H_{n-1}(S^{n-1})$ in the orientable case and zero in the nonorientable one.
:::

:::

::: {.pf-step #cases}
For $n\ge3$ the following hold, and $M$ is orientable exactly when both $M_i$ are: if both are orientable then $H_n(M)\cong\ZZ$ and $H_{n-1}(M)\cong H_{n-1}(M_1)\oplus H_{n-1}(M_2)$; if exactly one is, then $H_n(M)=0$ and the same isomorphism for $H_{n-1}$; if neither is, then $\psi=0$ and $H_{n-1}(M)\cong\ZZ\oplus H_{n-1}(M_1)\oplus H_{n-1}(M_2)$.

::: pf-proof
Both orientable: $\psi:\ZZ\oplus\ZZ\to\ZZ$ is onto, so $H_n(M)=\ker\psi\cong\ZZ$ and $H_{n-1}(M)\cong\operatorname{coker}\psi=0$ in the exact fragment of step [](#top){.pf-ref}, that is $H_{n-1}(M)\cong H_{n-1}(M_1)\oplus H_{n-1}(M_2)$. Exactly one orientable: $\psi:\ZZ\to\ZZ$ is an isomorphism, so $H_n(M)=0$ and again $\operatorname{coker}\psi=0$. Neither: $\psi=0$, so the fragment is $0\to\ZZ\to H_{n-1}(M)\to H_{n-1}(M_1)\oplus H_{n-1}(M_2)\to0$, and the middle group is the direct sum with an extra $\ZZ$. Orientability is read off from $H_n(M)=\ker\psi$.
:::

:::

::: {.pf-step #torsion}
In the case where neither $M_i$ is orientable, $H_{n-1}(M)$ is obtained from $H_{n-1}(M_1)\oplus H_{n-1}(M_2)$ by replacing one $\ZZ_2$ summand by $\ZZ$.

::: pf-proof
By Corollary 3.28 the torsion subgroup of $H_{n-1}$ of a closed connected nonorientable $n$-manifold is $\ZZ_2$, and there is no other torsion; so $H_{n-1}(M_i)\cong F_i\oplus\ZZ_2$ with $F_i$ free. With $F=F_1\oplus F_2$, step [](#cases){.pf-ref} gives $H_{n-1}(M)\cong\ZZ\oplus F\oplus\ZZ_2$ while $H_{n-1}(M_1)\oplus H_{n-1}(M_2)\cong F\oplus\ZZ_2\oplus\ZZ_2$: one of the two $\ZZ_2$ summands has become a $\ZZ$.
:::

:::

::: {.pf-step #low-dimensions}
For $n\le2$ the assertions hold.

::: pf-proof
$n=1$: a closed connected $1$-manifold is $S^1$, so $M_1\sharp M_2\cong S^1$; the range $0<i<n$ is empty and part (b) reads $\chi(S^1)=0=0+0-0$ with $\chi(S^1)=0$. $n=2$: the same three cases apply, with the fragment of step [](#top){.pf-ref} replaced by the sequence in reduced homology, where $\widetilde H_0(S^1)=0$ gives the same vanishing at the lower end, and the torsion statement of Corollary 3.28 is unchanged, so the conclusions and part (b) are the same.
:::

:::

::: {.pf-step #euler}
(b) $\chi(M)=\chi(M_1)+\chi(M_2)-\chi(S^n)$.

::: pf-proof
Rank by rank: at $i=0$ one has $H_0(M)\cong\ZZ$ while $H_0(M_1)\oplus H_0(M_2)\cong\ZZ^{2}$, since $M$ is connected, so this degree contributes $-1$ to the difference. For $1\le i\le n-2$ the ranks agree by step [](#middle){.pf-ref}. At $i=n$ and $i=n-1$ step [](#cases){.pf-ref} gives: in the first two cases the rank of $H_n$ drops by $1$ and that of $H_{n-1}$ is unchanged, contributing $(-1)^{n}\cdot(-1)=(-1)^{n+1}$; in the third case the rank of $H_n$ is unchanged and that of $H_{n-1}$ rises by $1$, contributing $(-1)^{n-1}=(-1)^{n+1}$. Both alternatives give the same number, so
$$
\chi(M)-\chi(M_1)-\chi(M_2)=(-1)+(-1)^{n+1}=-(1+(-1)^{n})=-\chi(S^{n}),
$$
because $(-1)+(-1)^{n+1}=-(1+(-1)^{n})$ and $\chi(S^{n})=1+(-1)^{n}$ (Corollary 2.14). Hence $\chi(M)=\chi(M_1)+\chi(M_2)-\chi(S^n)$.
:::

:::

:::
:::
