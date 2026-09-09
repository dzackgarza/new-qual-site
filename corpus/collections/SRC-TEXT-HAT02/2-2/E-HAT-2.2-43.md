---
schema: qual/card@1
id: E-HAT-2.2-43
kind: problem
title: Splitting of chain complexes and universal coefficient formula for $H_n(X; G)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Universal Coefficients
  - Chain Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 43; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/algebraic proof checked.
---

(a) Show that a chain complex of free abelian groups $C_n$ splits as a direct sum of subcomplexes $0 \to L_{n+1} \to K_n \to 0$ with at most two nonzero terms.
[Show the short exact sequence $0 \to \ker\partial \to C_n \to \operatorname{Im}\partial \to 0$ splits and take $K_n = \ker\partial$.]

(b) In case the groups $C_n$ are finitely generated, show there is a further splitting into summands $0 \to \mathbb{Z} \to 0$ and $0 \to \mathbb{Z} \xrightarrow{m} \mathbb{Z} \to 0$.
[Reduce the matrix of the boundary map $L_{n+1} \to K_n$ to echelon form by elementary row and column operations.]

(c) Deduce that if $X$ is a CW complex with finitely many cells in each dimension, then $H_n(X; G)$ is the direct sum of the following groups:

- a copy of $G$ for each $\mathbb{Z}$ summand of $H_n(X)$

- a copy of $G/mG$ for each $\mathbb{Z}_m$ summand of $H_n(X)$

- a copy of the kernel of $G \xrightarrow{m} G$ for each $\mathbb{Z}_m$ summand of $H_{n-1}(X)$

::: {.solution}
Let
\[
\cdots\xrightarrow{\partial_{n+1}}C_n\xrightarrow{\partial_n}C_{n-1}\xrightarrow{}\cdots
\]
be a chain complex of free abelian groups.

<1>1. Put
\[
K_n=\ker\partial_n.
\]
Then the short exact sequence
\[
0\to K_n\to C_n\xrightarrow{\partial_n}\operatorname{im}\partial_n\to0
\]
splits.
::: {.proof}
The subgroup $\operatorname{im}\partial_n$ of the free abelian group $C_{n-1}$ is free abelian. A short exact sequence with free quotient splits, so choose a complement $L_n\subset C_n$ such that
\[
C_n=K_n\oplus L_n.
\]
The restriction
\[
\partial_n|_{L_n}:L_n\xrightarrow{\cong}\operatorname{im}\partial_n
\]
is an isomorphism.
:::

<1>2. The original chain complex is the direct sum, over $n$, of two-term subcomplexes
\[
0\to L_{n+1}\xrightarrow{\partial_{n+1}}K_n\to0.
\]
::: {.proof}
At degree $n$ the decomposition is
\[
C_n=K_n\oplus L_n.
\]
The differential vanishes on $K_n$ and maps $L_n$ into $K_{n-1}$. Thus each $L_{n+1}$ interacts only with $K_n$, and the direct sum of these two-term pieces recovers every chain group and every differential.
:::

Assume now that all $C_n$ are finitely generated.

<1>3. Each map
\[
L_{n+1}\to K_n
\]
can be diagonalized by Smith normal form, so the chain complex further decomposes into summands
\[
0\to\mathbb Z\to0
\]
and
\[
0\to\mathbb Z\xrightarrow{m}\mathbb Z\to0
\qquad(m>0).
\]
::: {.proof}
The groups $L_{n+1}$ and $K_n$ are finitely generated free abelian. Smith normal form gives bases in which the injective map $L_{n+1}\to K_n$ is diagonal with nonzero diagonal entries $m_1,\dots,m_r$. Each diagonal entry yields a two-term summand
\[
\mathbb Z\xrightarrow{m_j}\mathbb Z,
\]
while any unused basis vectors of $K_n$ yield one-term summands $\mathbb Z$.
:::

Now let $X$ be a CW complex with finitely many cells in each dimension and tensor its cellular chain complex with an abelian group $G$.

<1>4. A one-term summand $\mathbb Z$ in degree $n$ contributes one copy of $G$ to $H_n(X;G)$.
::: {.proof}
After tensoring with $G$, the summand becomes a one-term complex with $G$ in degree $n$ and zero differential. Such summands correspond exactly to free $\mathbb Z$ summands of $H_n(X)$.
:::

<1>5. A two-term summand
\[
0\to\mathbb Z\xrightarrow{m}\mathbb Z\to0
\]
in degrees $n+1,n$ contributes
\[
G/mG
\]
to $H_n(X;G)$ and
\[
\ker(m:G\to G)
\]
to $H_{n+1}(X;G)$.
::: {.proof}
Tensoring gives
\[
0\to G\xrightarrow{m}G\to0.
\]
Its homology in the lower degree is the cokernel $G/mG$, while its homology in the upper degree is the kernel of multiplication by $m$.
:::

<1>6. Therefore
\[
H_n(X;G)
\]
is the direct sum of:

- one copy of $G$ for each $\mathbb Z$ summand of $H_n(X)$;
- one copy of $G/mG$ for each $\mathbb Z_m$ summand of $H_n(X)$;
- one copy of $\ker(m:G\to G)$ for each $\mathbb Z_m$ summand of $H_{n-1}(X)$.
::: {.proof}
A torsion summand $\mathbb Z_m$ in integral homology arises as the cokernel of one of the multiplication-by-$m$ two-term pieces. Apply <1>4--<1>5 and collect all direct summands contributing in degree $n$.
:::
:::
