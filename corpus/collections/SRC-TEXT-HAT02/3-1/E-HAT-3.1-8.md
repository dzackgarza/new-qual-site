---
schema: qual/card@1
id: E-HAT-3.1-8
kind: problem
title: Cohomology of spheres, good pairs, and retracts
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the cochain, exact-sequence, and universal-coefficient calculations directly.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 8; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the three parts: $H^i(S^n;G)$ comes from the pair $(D^{n+1},S^n)$ and from reducing
    Mayer-Vietoris to $\tilde H^{i-1}(S^{n-1})$; the good-pair isomorphism is carried to cohomology
    by naturality of the universal coefficient sequence together with the short five lemma; and for
    a retract $i^*r^*$ is the identity, so $i^*$ is split surjective and the connecting map
    vanishes.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 8 (p.205) with all three parts as printed, the closedness and deformation-retract hypotheses of (b) included. (a) rewritten to give the two induction steps with their citations: Theorem 2.16 p.117 for the reduced sequence of the pair and Theorem 2.20 p.119 for the excision identifying H^{i+1}(D^{n+1},S^n) with H^{i+1}(S^{n+1},D^{n+1}_+), plus the Mayer-Vietoris sequence of p.149; the base case S^0 and the passage from reduced to unreduced are now explicit. (b) cites Proposition 2.22 p.124 and Theorem 3.2 p.195 with the naturality of p.196, and notes the case A empty, which Proposition 2.22 excludes. (c) now records why the connecting map vanishes: delta = delta i^* r^* = 0. Not covered: no treatment of the axioms beyond the three cases asked.
---

::: {.problem}
Many basic homology arguments work just as well for cohomology even though maps go in the opposite direction.
Verify this in the following cases:

(a) Compute $H^i(S^n; G)$ by induction on $n$ in two ways: using the long exact sequence of a pair, and using the Mayer–Vietoris sequence.

(b) Show that if $A$ is a closed subspace of $X$ that is a deformation retract of some neighborhood, then the quotient map $X \to X/A$ induces isomorphisms $H^n(X, A; G) \approx \widetilde{H}^n(X/A; G)$ for all $n$.

(c) Show that if $A$ is a retract of $X$ then $H^n(X; G) \approx H^n(A; G) \oplus H^n(X, A; G)$.
:::

::: {.solution}
All coefficient groups below are an arbitrary fixed abelian group $G$.

::: pf

::: {.pf-step #s1}

The long exact sequence of the pair $(D^{n+1},S^n)$ gives suspension-style isomorphisms
$$
\widetilde H^i(S^n;G)\cong H^{i+1}(D^{n+1},S^n;G).
$$
Inductively this yields
$$
H^i(S^n;G)\cong
\begin{cases}
G,&i=0,n,\ n>0,\\
0,&\text{otherwise},
\end{cases}
$$
with the usual interpretation for $S^0$.

::: pf-proof

The reduced long exact sequence of the pair (Theorem 2.16, p.117) runs $\widetilde H^i(D^{n+1})\to\widetilde H^i(S^n)\to H^{i+1}(D^{n+1},S^n)\to\widetilde H^{i+1}(D^{n+1})$, and both outer groups vanish because $D^{n+1}$ is contractible, so $\widetilde H^i(S^n)\cong H^{i+1}(D^{n+1},S^n)$. Write $S^{n+1}$ as the union of its closed hemispheres $D^{n+1}_+\cup D^{n+1}_-$ with intersection $S^n$; the same sequence for the pair $(S^{n+1},D^{n+1}_+)$, whose first term vanishes, identifies $\widetilde H^{n+1}(S^{n+1})$ with $H^{i+1}(S^{n+1},D^{n+1}_+)$, and excision (Theorem 2.20, p.119) identifies the latter with $H^{i+1}(D^{n+1}_-,S^n)$, where $D^{n+1}_-$ is a disk and so contractible. Hence $\widetilde H^i(S^n)\cong\widetilde H^{i+1}(S^{n+1})$. Starting from $\widetilde H^0(S^0;G)=G$ and $\widetilde H^i(S^0;G)=0$ for $i>0$, induction gives $\widetilde H^i(S^n;G)=G$ for $i=n$ and $0$ otherwise, and since $S^n$ is path-connected for $n>0$ this is the displayed unreduced answer.

:::

:::

::: pf-step

The same computation follows from Mayer--Vietoris by writing
$$
S^n=U\cup V
$$
as two slightly enlarged hemispheres with $U,V$ contractible and $U\cap V\simeq S^{n-1}$.

::: pf-proof

The reduced Mayer--Vietoris sequence of §2.2 (p.149) applied to $S^n=U\cup V$ gives
$$
\widetilde H^i(S^n;G)\cong\widetilde H^{i-1}(S^{n-1};G),
$$
because the reduced cohomology of $U$ and $V$ vanishes (they are contractible) and $U\cap V\simeq S^{n-1}$. Induction from $S^0$ gives the same answer as step [](#s1){.pf-ref}.

:::

:::

::: pf-step

If $A\subset X$ is closed and is a deformation retract of a neighborhood, then the quotient map induces isomorphisms
$$
\boxed{H^n(X,A;G)\cong\widetilde H^n(X/A;G)}
$$
for all $n$.

::: pf-proof

Proposition 2.22 (p.124) applies to a nonempty closed subspace $A$ that is a deformation retract of a neighborhood: the quotient map induces
$$
H_j(X,A;\ZZ)\xrightarrow{\cong}\widetilde H_j(X/A;\ZZ)
$$
for every $j$. For a complex of free abelian groups the universal coefficient sequence of Theorem 3.2 (p.195) is $0\to\operatorname{Ext}(H_{j-1},G)\to H^j(-;G)\to\operatorname{Hom}(H_j,G)\to0$, and it is natural in the chain complex (p.196). Applying it to the singular chains of $(X,A)$ and of $(X/A,\mathrm{pt})$ and using the homology isomorphism on $H_n$ and $H_{n-1}$ gives isomorphisms of both outer terms in the induced ladder; the five lemma gives the isomorphism in the middle. For $A=\emptyset$ the statement is immediate, since then $X/A=X\sqcup\mathrm{pt}$ and $H^n(X,\emptyset;G)=\widetilde H^n(X;G)=\widetilde H^n(X\sqcup\mathrm{pt};G)$.

:::

:::

::: pf-step

If $A$ is a retract of $X$, then
$$
\boxed{H^n(X;G)\cong H^n(A;G)\oplus H^n(X,A;G).}
$$

::: pf-proof

Let $i:A\hookrightarrow X$ and $r:X\to A$ satisfy $ri=\operatorname{id}_A$. Contravariance gives
$$
i^*r^*=(ri)^*=\operatorname{id}_{H^n(A)},
$$
so $i^*:H^n(X)\to H^n(A)$ is split surjective and $r^*$ is a section of it. In the long exact sequence of the pair (Theorem 2.16, p.117) each connecting map $\delta$ satisfies $\delta i^*=0$, so $\delta=\delta i^*r^*=0$; hence the map $H^n(X,A)\to H^n(X)$ is injective and one gets a short exact sequence
$$
0\to H^n(X,A)\to H^n(X)\xrightarrow{i^*}H^n(A)\to0.
$$
The map $r^*$ splits it, giving the direct sum.

:::

:::

:::

:::
