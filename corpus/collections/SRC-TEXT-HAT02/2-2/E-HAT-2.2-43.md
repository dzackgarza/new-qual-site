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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the splitting: $C_n=K_n\oplus L_n$ over the free quotient gives the two-term subcomplexes
    $L_{n+1}\to K_n$; Smith normal form splits each into $\ZZ\xrightarrow{m}\ZZ$ and one-term $\ZZ$
    summands; and tensoring with $G$ gives $G/mG$ in the lower degree and $\ker(m:G\to G)$ in the
    upper, which is the stated decomposition of $H_n(X;G)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 43 (a), (b), (c) as printed on p. 159, the three bullets included.
    Checked the splitting: K_n = ker partial_n, C_n = K_n + L_n with L_n mapping isomorphically to
    im partial_n, and the complex is the direct sum of the pieces L_{n+1} -> K_n; the diagonal form
    of the map between finitely generated free groups gives Z -> Z with entry m and one-term Z
    pieces; and after tensoring, a piece in degrees n+1, n gives G/mG in degree n and ker(m) in
    degree n+1. Additions: the splitting is cited to the remark after the Splitting Lemma p.148,
    the diagonal form is tied to the echelon reduction named in the printed hint, and the two
    facts needed for (c) are stated — C_*(X) tensor G computes H_*(X;G) by the coefficient form of
    Theorem 2.35 p.139 as in Example 2.50 p.154, and tensor and homology preserve the direct sum
    decomposition. What is not covered: no certificate.
---

::: {.problem}
(a) Show that a chain complex of free abelian groups $C_n$ splits as a direct sum of subcomplexes $0 \to L_{n+1} \to K_n \to 0$ with at most two nonzero terms.
[Show the short exact sequence $0 \to \ker\partial \to C_n \to \operatorname{Im}\partial \to 0$ splits and take $K_n = \ker\partial$.]

(b) In case the groups $C_n$ are finitely generated, show there is a further splitting into summands $0 \to \ZZ \to 0$ and $0 \to \ZZ \xrightarrow{m} \ZZ \to 0$.
[Reduce the matrix of the boundary map $L_{n+1} \to K_n$ to echelon form by elementary row and column operations.]

(c) Deduce that if $X$ is a CW complex with finitely many cells in each dimension, then $H_n(X; G)$ is the direct sum of the following groups:

- a copy of $G$ for each $\ZZ$ summand of $H_n(X)$

- a copy of $G/mG$ for each $\ZZ_m$ summand of $H_n(X)$

- a copy of the kernel of $G \xrightarrow{m} G$ for each $\ZZ_m$ summand of $H_{n-1}(X)$
:::

::: {.solution}
Let
$$
\cdots\xrightarrow{\partial_{n+1}}C_n\xrightarrow{\partial_n}C_{n-1}\xrightarrow{}\cdots
$$
be a chain complex of free abelian groups.

::: pf

::: pf-step

Put
$$
K_n=\ker\partial_n.
$$
Then the short exact sequence
$$
0\to K_n\to C_n\xrightarrow{\partial_n}\operatorname{im}\partial_n\to0
$$
splits.

::: pf-proof

The subgroup $\operatorname{im}\partial_n$ of the free abelian group $C_{n-1}$ is free abelian, as a subgroup of a free abelian group. A short exact sequence with free quotient splits, by the remark following the Splitting Lemma on p. 148, so choose a complement $L_n\subset C_n$ such that
$$
C_n=K_n\oplus L_n.
$$
The restriction
$$
\partial_n\restrict_{L_n}:L_n\xrightarrow{\cong}\operatorname{im}\partial_n
$$
is an isomorphism.

:::

:::

::: pf-step

The original chain complex is the direct sum, over $n$, of two-term subcomplexes
$$
0\to L_{n+1}\xrightarrow{\partial_{n+1}}K_n\to0.
$$

::: pf-proof

At degree $n$ the decomposition is
$$
C_n=K_n\oplus L_n.
$$
The differential vanishes on $K_n$ and maps $L_n$ into $K_{n-1}$. Thus each $L_{n+1}$ interacts only with $K_n$, and the direct sum of these two-term pieces recovers every chain group and every differential.

Assume now that all $C_n$ are finitely generated.

:::

:::

::: pf-step

Each map
$$
L_{n+1}\to K_n
$$
can be diagonalized by Smith normal form, so the chain complex further decomposes into summands
$$
0\to\ZZ\to0
$$
and
$$
0\to\ZZ\xrightarrow{m}\ZZ\to0
\qquad(m>0).
$$

::: pf-proof

The groups $L_{n+1}$ and $K_n$ are finitely generated free abelian, so the matrix of the injective map $L_{n+1}\to K_n$ with respect to some bases is diagonal with nonzero diagonal entries $m_1,\dots,m_r$; this is the reduction to echelon form by row and column operations named in the printed hint. Each diagonal entry yields a two-term summand
$$
\ZZ\xrightarrow{m_j}\ZZ,
$$
while the basis vectors of $K_n$ not hit by the map yield one-term summands $\ZZ$ in degree $n$.

Now let $X$ be a CW complex with finitely many cells in each dimension, so that each cellular chain group is a finitely generated free abelian group, and tensor its cellular chain complex with an abelian group $G$. The complex $C_*^{CW}(X)\otimes G$ computes $H_*(X;G)$, which is the coefficient form of Theorem 2.35 (p. 139) used in Example 2.50 (p. 154). Since the tensor product distributes over direct sums, this complex is the direct sum of the tensor products of the two-term pieces found above, and the homology of a direct sum of chain complexes is the direct sum of their homologies.

:::

:::

::: {.pf-step #s4}

A one-term summand $\ZZ$ in degree $n$ contributes one copy of $G$ to $H_n(X;G)$.

::: pf-proof

After tensoring with $G$, the summand becomes a one-term complex with $G$ in degree $n$ and zero differential. Such summands correspond exactly to free $\ZZ$ summands of $H_n(X)$.

:::

:::

::: {.pf-step #s5}

A two-term summand
$$
0\to\ZZ\xrightarrow{m}\ZZ\to0
$$
in degrees $n+1,n$ contributes
$$
G/mG
$$
to $H_n(X;G)$ and
$$
\ker(m:G\to G)
$$
to $H_{n+1}(X;G)$.

::: pf-proof

Tensoring gives
$$
0\to G\xrightarrow{m}G\to0.
$$
Its homology in the lower degree is the cokernel $G/mG$, while its homology in the upper degree is the kernel of multiplication by $m$.

:::

:::

::: pf-step

Therefore
$$
H_n(X;G)
$$
is the direct sum of:

- one copy of $G$ for each $\ZZ$ summand of $H_n(X)$;
- one copy of $G/mG$ for each $\ZZ_m$ summand of $H_n(X)$;
- one copy of $\ker(m:G\to G)$ for each $\ZZ_m$ summand of $H_{n-1}(X)$.

::: pf-proof

A torsion summand $\ZZ_m$ in integral homology arises as the cokernel of one of the multiplication-by-$m$ two-term pieces, by part (b); a free summand as a one-term piece. Apply steps [](#s4){.pf-ref} and [](#s5){.pf-ref} and collect all direct summands contributing in degree $n$. A summand $\ZZ_m$ of $H_n(X)$ is the cokernel of a piece with lower degree $n$, contributing $G/mG$ to $H_n(X;G)$; a summand $\ZZ_m$ of $H_{n-1}(X)$ is the cokernel of a piece with lower degree $n-1$, whose upper term lies in degree $n$ and contributes $\ker(m:G\to G)$.

:::

:::

:::

:::
