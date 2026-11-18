---
schema: qual/card@1
id: E-HAT-3.3-24
kind: problem
title: Homology of closed 3-manifolds
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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 24; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 24; it matches the printed text. The printed bracketed hint about the manifold obtained from $S^2\times I$ by a reflection was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the computation: for orientable $M$, $H_2\cong H^1\cong\operatorname{Hom}(H_1,\ZZ)$
    because $\operatorname{Ext}(H_0,\ZZ)=0$; for nonorientable $M$, Corollary 3.28 gives the
    $\ZZ_2$ torsion and $\chi(M)=0$ with $H_3=0$ gives rank $r-1$. The examples are read too:
    connected sums of $S^1\times S^2$ with lens spaces, and of the twisted $S^2$-bundle over $S^1$
    (whose mapping torus computation gives $H_1=\ZZ$, $H_2=\ZZ_2$) with $S^1\times S^2$'s and lens
    spaces.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Independently checked Stanford Math 215C Solution Set 4, Hatcher 3.3.24, printed p.2. Its rank
    computation and examples agree with this card, including the r-1 copies of S^1 x S^2 in the
    nonorientable example N. Its "dim H^1(M;Z)" means rank, not dimension of the abelian group.
    The reflection computation gives H_1(N)=Z, H_2(N)=Z_2, H_3(N)=0, and there is only one
    nonorientable summand in each example, so Exercise 6 applies directly.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two formulas and the examples, which is what Queue D asks for on this card. The orientable computation, the nonorientable one (with the torsion and the Euler-characteristic rank as substeps) and the two constructions are separate steps; the universal-coefficient and Poincare-duality locators are named, the vanishing of Ext is justified by the freeness of H_0, and the mapping-torus computation for the reflection is written with its coker(-2). A trailing paragraph restating the citation after the proof, and a sentence about Exercise 6 needing no exceptional-case correction, are folded into the lead and the relevant steps. No statement repair: the exercise is Hatcher §3.3 Exercise 24, printed p. 259.
---

::: {.problem}
Let $M$ be a closed connected 3-manifold, and write $H_1(M; \ZZ)$ as $\ZZ^r \oplus F$, the direct sum of a free abelian group of rank $r$ and a finite group $F$.
Show that $H_2(M; \ZZ)$ is $\ZZ^r$ if $M$ is orientable and $\ZZ^{r-1} \oplus \ZZ_2$ if $M$ is nonorientable.
In particular, $r \geq 1$ when $M$ is nonorientable.
Using Exercise 6, construct examples showing there are no other restrictions on the homology groups of closed 3-manifolds.
[In the nonorientable case consider the manifold $N$ obtained from $S^2 \times I$ by identifying $S^2 \times \{0\}$ with $S^2 \times \{1\}$ via a reflection of $S^2$.]
:::

::: {.solution}
The published solution is **Stanford Math 215C, Spring 2009, Solution Set 4, Hatcher 3.3.24, printed p. 2** ([`solution4.pdf`](https://math.stanford.edu/~ralph/math215c/solution4.pdf)): the rank and torsion computation for both orientability cases and the connected-sum examples are its. The statement is Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 24, printed p. 259. In the set's typography "$\dim H^1(M;\ZZ)$" has to be read as rank, not as a vector-space dimension, since the finite summand $F$ contributes no rank.

Throughout, $M$ is a closed connected $3$-manifold and $H_1(M;\ZZ)\cong\ZZ^r\oplus F$ with $F$ finite.

::: pf

::: {.pf-step #orientable}
If $M$ is orientable then $H_2(M;\ZZ)\cong\ZZ^r$.

::: pf-proof
Poincaré duality for the closed orientable $3$-manifold $M$ gives $H_2(M;\ZZ)\cong H^{3-2}(M;\ZZ)=H^1(M;\ZZ)$ (Theorem 3.30, printed p. 241). The universal coefficient theorem gives $H^1(M;\ZZ)\cong\operatorname{Hom}(H_1(M;\ZZ),\ZZ)\oplus\operatorname{Ext}(H_0(M;\ZZ),\ZZ)$, and $H_0(M;\ZZ)\cong\ZZ$ is free, so the Ext term vanishes (Theorem 3.2, printed p. 195). Finally $\operatorname{Hom}(\ZZ^r\oplus F,\ZZ)\cong\ZZ^r$, because a homomorphism kills the finite group $F$.
:::

:::

::: {.pf-step #nonorientable}
If $M$ is nonorientable then $H_2(M;\ZZ)\cong\ZZ^{r-1}\oplus\ZZ_2$, and in particular $r\ge1$.

::: pf-proof

::: {.pf-step #torsion}
The torsion subgroup of $H_2(M;\ZZ)$ is $\ZZ_2$.

::: pf-proof
Corollary 3.28, printed p. 238, states that for a closed connected $n$-manifold the torsion subgroup of $H_{n-1}(M;\ZZ)$ is trivial if $M$ is orientable and $\ZZ_2$ if not; with $n=3$ this is the claim.
:::

:::

::: {.pf-step #rank}
$\operatorname{rank}H_2(M;\ZZ)=r-1$.

::: pf-proof
A closed odd-dimensional manifold has Euler characteristic zero, and $\chi(M)=\sum_i(-1)^ib_i(M)$ with $b_i$ the ranks. Here $b_0=1$ because $M$ is connected, $b_1=r$, $b_3=0$ because $H_3(M;\ZZ)=0$ for a closed connected nonorientable $3$-manifold, and $b_2=\operatorname{rank}H_2(M;\ZZ)$. So $0=\chi(M)=1-r+\operatorname{rank}H_2(M;\ZZ)$, giving $\operatorname{rank}H_2(M;\ZZ)=r-1$.
:::

:::

The torsion subgroup is $\ZZ_2$ by step [](#torsion){.pf-ref} and the rank is $r-1$ by step [](#rank){.pf-ref}, so $H_2(M;\ZZ)\cong\ZZ^{r-1}\oplus\ZZ_2$ by the classification of finitely generated abelian groups; and $r-1\ge0$ because a rank is nonnegative, which is the assertion $r\ge1$.
:::

:::

::: {.pf-step #no-other-restrictions}
Every pair $(r,F)$ with $r\ge0$ and $F$ finite occurs for an orientable $M$, and every pair with $r\ge1$ occurs for a nonorientable $M$; so the formulas above are the only restrictions.

::: pf-proof

::: {.pf-step #orientable-examples}
For orientable $M$, take the connected sum of $r$ copies of $S^1\times S^2$ with the lens spaces $L(m_j,1)$, where $F\cong\ZZ_{m_1}\oplus\cdots\oplus\ZZ_{m_s}$.

::: pf-proof
Connected sum adds $H_1$ in the range $0<i<n$ by §3.3 Exercise 6, and each summand is a closed connected orientable $3$-manifold, so $H_1\cong\ZZ^r\oplus\ZZ_{m_1}\oplus\cdots\oplus\ZZ_{m_s}=\ZZ^r\oplus F$ and $H_2\cong\ZZ^r$: indeed $H_1(S^1\times S^2)\cong\ZZ$ and $H_2(S^1\times S^2)\cong\ZZ$, while $H_1(L(m,1))\cong\ZZ_m$ and $H_2(L(m,1))=0$, the latter by the homology of a lens space computed from its CW structure. The result is orientable and has the prescribed $H_1$, and its $H_2$ is $\ZZ^r$, as the orientable formula requires.
:::

:::

::: {.pf-step #nonorientable-examples}
For nonorientable $M$, take the connected sum of the twisted $S^2$-bundle $N$ over $S^1$ with $r-1$ copies of $S^1\times S^2$ and the same lens spaces.

::: pf-proof
Realize $N$ as the mapping torus of a reflection of $S^2$, that is $S^2\times I$ with the two ends identified by a reflection. Its Wang sequence, with $r_*=-1$ on $H_2(S^2;\ZZ)$, gives $H_2(N;\ZZ)\cong\operatorname{coker}(-2)=\ZZ_2$ and $H_1(N;\ZZ)\cong\ker(r_*-1\text{ on }H_0)=\ZZ$, while $H_3(N)=0$ because $N$ is a closed nonorientable $3$-manifold. Connected sum adds $H_1$ and $H_2$ in the range $0<i<3$, so the sum has
$$
H_1\cong\ZZ\oplus\ZZ^{r-1}\oplus F=\ZZ^r\oplus F,
\qquad
H_2\cong\ZZ_2\oplus\ZZ^{r-1},
$$
which is $\ZZ^{r-1}\oplus\ZZ_2$; it is nonorientable because exactly one connected-sum factor is, and $r\ge1$ because the factor $N$ contributes the class $\ZZ$. So every allowed pair occurs.
:::

:::

Both halves of the statement are therefore sharp: steps [](#orientable){.pf-ref} and [](#nonorientable){.pf-ref} give the two formulas, and steps [](#orientable-examples){.pf-ref} and [](#nonorientable-examples){.pf-ref} show that nothing further is forced. This is the last part of the exercise.
:::

:::

:::
:::
