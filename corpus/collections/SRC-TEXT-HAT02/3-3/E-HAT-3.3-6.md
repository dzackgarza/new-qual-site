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
Put $N_i=M_i\setminus\operatorname{int}B_i$, so that $M=M_1\sharp M_2=N_1\cup_{S^{n-1}}N_2$ with $N_1\cap N_2=S^{n-1}$, and collapsing the glued sphere gives $M/S^{n-1}=M_1\vee M_2$. Since $\partial N_i=S^{n-1}$ has a collar in $M$, $(M,S^{n-1})$ is a good pair, so $H_i(M,S^{n-1})\cong\widetilde H_i(M_1\vee M_2)=\widetilde H_i(M_1)\oplus\widetilde H_i(M_2)$ for $i\ge1$. The pair sequence of $(M,S^{n-1})$ therefore reads
$$
\cdots\to\widetilde H_i(S^{n-1})\to H_i(M)\to H_i(M_1)\oplus H_i(M_2)\to\widetilde H_{i-1}(S^{n-1})\to\cdots
$$
with $\widetilde H_i(S^{n-1})=0$ for $i\ne n-1$ and $\widetilde H_{n-1}(S^{n-1})=\ZZ$.

For $1\le i\le n-2$ both neighbouring terms vanish, so $H_i(M)\cong H_i(M_1)\oplus H_i(M_2)$: this is the claimed formula in those degrees.

In degree $n-1$, take $n\ge3$ first, so that $H_{n-2}(S^{n-1})=0$ and the sequence ends
$$
0\to H_n(M)\to H_n(M_1)\oplus H_n(M_2)\xrightarrow{\ \psi\ }\ZZ\to H_{n-1}(M)\to H_{n-1}(M_1)\oplus H_{n-1}(M_2)\to0 .
$$
Here $H_n(M_i)$ is $\ZZ$ or $0$ according as $M_i$ is orientable (Theorem 3.26, p. 236), and $\psi$ is the sum of the two boundary maps $\ZZ\to\ZZ$, each of which is an isomorphism for an orientable summand and zero for a nonorientable one. Three cases follow.

If both $M_i$ are orientable, $\psi:\ZZ\oplus\ZZ\to\ZZ$ is onto, so $H_n(M)\cong\ker\psi\cong\ZZ$ — which makes $M$ orientable — and $H_{n-1}(M)\cong H_{n-1}(M_1)\oplus H_{n-1}(M_2)$.

If exactly one is orientable, $\psi:\ZZ\to\ZZ$ is an isomorphism, so $H_n(M)=0$, $M$ is nonorientable, and again $H_{n-1}(M)\cong H_{n-1}(M_1)\oplus H_{n-1}(M_2)$.

If neither is orientable, $\psi=0$ and $0\to\ZZ\to H_{n-1}(M)\to H_{n-1}(M_1)\oplus H_{n-1}(M_2)\to0$ is exact. In this case $M$, $M_1$ and $M_2$ are all nonorientable, so Corollary 3.28 (p. 238) gives torsion $\ZZ_2$ to $H_{n-1}$ of each of them; hence $H_{n-1}(M)=\ZZ\oplus F\oplus\ZZ_2$ while $H_{n-1}(M_1)\oplus H_{n-1}(M_2)=F\oplus\ZZ_2\oplus\ZZ_2$ with $F$ free. One of the two $\ZZ_2$ summands is replaced by a $\ZZ$ summand, as claimed.

For $n=1$ a closed connected $1$-manifold is a circle, so $M_1\sharp M_2=S^1$: part (a) has no degrees to prove, its range $0<i<1$ being empty, and part (b) reads $0=0+0-0$, both sides being $\chi(S^1)$.

The three cases also settle orientability, since $H_n(M)=\ker\psi$. The map $\psi$ is the sum of the two boundary maps $H_n(M_i)\to H_{n-1}(S^{n-1})$, and each of those is an isomorphism when $M_i$ is orientable (so $H_n(M_i)=\ZZ$) and zero when it is not (so $H_n(M_i)=0$); hence $\ker\psi\cong\ZZ$ exactly when both $M_i$ are orientable and $\ker\psi=0$ otherwise. So $M_1\sharp M_2$ is orientable exactly when both summands are, which is what the torsion step in the third case uses.

For $n=2$ the same three cases apply with the sequence read in reduced homology, where $\widetilde H_0(S^1)=0$ replaces the copy of $\ZZ$ that appears at $i=0$ in the unreduced sequence; the conclusions, and the torsion statement of Corollary 3.28, are unchanged.

For (b), compute the Euler characteristic degree by degree, as the handout does. Since $H_i(M)\cong H_i(M_1)\oplus H_i(M_2)$ for $1\le i\le n-2$, and $H_n(M)$ is $\ZZ$ or $0$ according to the three cases, while $\rk H_{n-1}(M)=\rk H_{n-1}(M_1)+\rk H_{n-1}(M_2)$ in the first two cases and that rank plus one in the third,
$$
\chi(M)=\chi(M_1)+\chi(M_2)+(-1)+(-1)^{n+1}=\chi(M_1)+\chi(M_2)-\bigl(1+(-1)^n\bigr)=\chi(M_1)+\chi(M_2)-\chi(S^n),
$$
because $(-1)+(-1)^{n+1}=-(1+(-1)^n)$ and $\chi(S^n)=1+(-1)^n$ (Corollary 2.14, p. 114).

This is the solution printed in the Math 538 homework solutions, HMW 3, handwritten pages 2--4 (PDF pages 14, 15 and 16 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #6: the same identification $M_1\sharp M_2/S^{n-1}=M_1\vee M_2$, the same pair sequence, the same three cases with Corollary 3.28 for the torsion, and part (b) by the degree-by-degree count of ranks ending in the identity $(-1)+(-1)^{n+1}=-\chi(S^n)$. Two things that sheet leaves implicit are supplied here: the case $n=2$, where $H_{n-2}(S^{n-1})\ne0$ and the sequence must be read in reduced homology, and the good-pair justification of $H_i(M,S^{n-1})\cong H_i(M_1\vee M_2)$.
:::
