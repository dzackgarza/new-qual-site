---
schema: qual/card@1
id: E-HAT-3.A-3
kind: problem
title: "Rational and mod-$p$ cohomology determine integral homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.A Exercise 3, printed p. 267; the statement
    matches the print, reduced groups and all. The exercise is Hatcher's Corollary 3A.7(a) and the
    book prints its proof on pp. 266-267; the card now cites that proof, follows it, and derives the
    two steps that were assertions: $A_n[p]=0$ comes from the universal coefficient sequence in
    degree $n+1$ with Proposition 3A.5(5), where the card had read both $A_n/pA_n=0$ and $A_n[p]=0$
    off the single degree-$n$ sequence, and $\widetilde H_n(X;\QQ)\cong A_n\otimes\QQ$ is Corollary
    3A.6(a) with the Tor term killed by Proposition 3A.5(3). One false step of my own was caught in
    the same pass and is not on the card: $\operatorname{Ext}_\ZZ(H,F)$ does not vanish for a field
    $F$ — $\operatorname{Ext}(\ZZ_p,\FF_p)\cong\FF_p$ — so the first step uses the $F$-dual of the
    complex $C_*(X;F)$ of vector spaces instead, which is where the vanishing of the $\operatorname{Ext}$
    term on p. 197 really applies.
---

::: {.problem}
Show that if $\tilde{H}^n(X; \QQ)$ and $\tilde{H}^n(X; \ZZ_p)$ are zero for all $n$ and all primes $p$, then $\tilde{H}_n(X; \ZZ) = 0$ for all $n$, and hence $\tilde{H}^n(X; G) = 0$ for all $G$ and $n$.
:::

::: {.solution}
The exercise is Hatcher's Corollary 3A.7(a); the argument below carries out the proof printed with it on pp. 266--267.

*Step 1: field coefficients simplify.* For a field $F$,
$$
C^n(X;F)=\operatorname{Hom}_\ZZ(C_n(X),F)\cong\operatorname{Hom}_F(C_n(X)\otimes_\ZZ F,F)=\operatorname{Hom}_F(C_n(X;F),F),
$$
so the cochain complex of $X$ over $F$ is the $F$-dual of the chain complex $C_*(X;F)$ of $F$-vector spaces. Dualizing vector spaces is exact, so taking homology commutes with the duality and
$$
H^n(X;F)\cong\operatorname{Hom}_F(H_n(X;F),F).
$$
A vector space with trivial dual is trivial, so the hypothesis of the exercise implies
$$
\widetilde H_n(X;\QQ)=0,
\qquad
\widetilde H_n(X;\ZZ_p)=0
$$
for every $n$ and every prime $p$. (This is the $R=F$ case of the module-coefficient form of the universal coefficient theorem, Hatcher p. 197: over a field the $\operatorname{Ext}$ term vanishes.)

*Step 2: the integral groups carry a $\QQ$-vector-space structure.* Put $A_n=\widetilde H_n(X;\ZZ)$. The universal coefficient theorem, Theorem 3A.3 (p. 264), applied to the augmented singular chain complex, which is again a complex of free abelian groups, gives for each prime $p$ the exact sequence
$$
0\to A_n\otimes\ZZ_p\to \widetilde H_n(X;\ZZ_p)\to \operatorname{Tor}(A_{n-1},\ZZ_p)\to0 .
$$
Since $A_n\otimes\ZZ_p=A_n/pA_n$, the sequence in degree $n$ has middle term $\widetilde H_n(X;\ZZ_p)=0$ and hence shows $A_n/pA_n=0$; the sequence in degree $n+1$ shows $\operatorname{Tor}(A_n,\ZZ_p)=A_n[p]=0$, using Proposition 3A.5(5) (p. 265). Thus multiplication by $p$ is surjective and injective on $A_n$, hence bijective; as this holds for every prime, multiplication by every nonzero integer is bijective. A torsionfree divisible abelian group is a vector space over $\QQ$, so each $A_n$ is one.

*Step 3: $A_n$ vanishes.* By the universal coefficient theorem with $\QQ$ coefficients, whose Tor term vanishes by Proposition 3A.5(3), $\widetilde H_n(X;\QQ)\cong A_n\otimes\QQ$; this is Corollary 3A.6(a) (p. 266) in the unreduced form. For a $\QQ$-vector space $A_n$ the map $A_n\to A_n\otimes\QQ$ is an isomorphism, and Step 1 gives $\widetilde H_n(X;\QQ)=0$, so $A_n=0$ for every $n$.

*Step 4: every coefficient group.* The cohomology universal coefficient theorem with arbitrary coefficients $G$,
$$
0\to\operatorname{Ext}(A_{n-1},G)
\to \widetilde H^n(X;G)
\to \operatorname{Hom}(A_n,G)\to0,
$$
then has both outer groups zero, so $\widetilde H^n(X;G)=0$ for all $G$ and $n$.
:::
