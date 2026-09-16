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
---

# E-HAT-3.1-8

Many basic homology arguments work just as well for cohomology even though maps go in the opposite direction.
Verify this in the following cases:

(a) Compute $H^i(S^n; G)$ by induction on $n$ in two ways: using the long exact sequence of a pair, and using the Mayer–Vietoris sequence.

(b) Show that if $A$ is a closed subspace of $X$ that is a deformation retract of some neighborhood, then the quotient map $X \to X/A$ induces isomorphisms $H^n(X, A; G) \approx \widetilde{H}^n(X/A; G)$ for all $n$.

(c) Show that if $A$ is a retract of $X$ then $H^n(X; G) \approx H^n(A; G) \oplus H^n(X, A; G)$.

::: {.solution}
All coefficient groups below are an arbitrary fixed abelian group $G$.

<1>1. The long exact sequence of the pair $(D^{n+1},S^n)$ gives suspension-style isomorphisms
\[
\widetilde H^i(S^n;G)\cong H^{i+1}(D^{n+1},S^n;G).
\]
Inductively this yields
\[
H^i(S^n;G)\cong
\begin{cases}
G,&i=0,n,\ n>0,\\
0,&\text{otherwise},
\end{cases}
\]
with the usual interpretation for $S^0$.
::: {.proof}
Since $D^{n+1}$ is contractible, its reduced cohomology vanishes. The reduced long exact sequence of the pair therefore identifies the relative group with the shifted reduced cohomology of the boundary. Excision identifies the relative group with the reduced cohomology contributed by the top cell, giving the induction.
:::

<1>2. The same computation follows from Mayer--Vietoris by writing
\[
S^n=U\cup V
\]
as two slightly enlarged hemispheres with $U,V$ contractible and $U\cap V\simeq S^{n-1}$.
::: {.proof}
The reduced Mayer--Vietoris sequence gives isomorphisms
\[
\widetilde H^i(S^n;G)\cong\widetilde H^{i-1}(S^{n-1};G),
\]
since the reduced cohomology of $U$ and $V$ vanishes. Induction from $S^0$ gives the same answer as <1>1.
:::

<1>3. If $A\subset X$ is closed and is a deformation retract of a neighborhood, then the quotient map induces isomorphisms
\[
\boxed{H^n(X,A;G)\cong\widetilde H^n(X/A;G)}
\]
for all $n$.
::: {.proof}
Choose a neighborhood $N$ of $A$ that deformation retracts onto $A$. Excision and homotopy invariance identify
\[
H^n(X,A)\cong H^n(X,N).
\]
Collapsing $N$ to a point identifies the latter relative cochain theory with reduced cohomology of $X/N$. Since $N/A$ is contractible, the natural map $X/A\to X/N$ is a homotopy equivalence. Composing these identifications gives the asserted quotient isomorphism.
:::

<1>4. If $A$ is a retract of $X$, then
\[
\boxed{H^n(X;G)\cong H^n(A;G)\oplus H^n(X,A;G).}
\]
::: {.proof}
Let $i:A\hookrightarrow X$ and $r:X\to A$ satisfy $ri=\operatorname{id}_A$. Contravariance gives
\[
i^*r^*=\operatorname{id}_{H^n(A)},
\]
so $i^*:H^n(X)\to H^n(A)$ is split surjective. In the long exact sequence of the pair, the connecting map after $i^*$ is therefore zero, so one gets a short exact sequence
\[
0\to H^n(X,A)\to H^n(X)\xrightarrow{i^*}H^n(A)\to0.
\]
The map $r^*$ splits it, giving the direct sum.
:::
:::
