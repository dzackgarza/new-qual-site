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

---

::: {.problem}
Let $M$ be a closed connected 3-manifold, and write $H_1(M; \ZZ)$ as $\ZZ^r \oplus F$, the direct sum of a free abelian group of rank $r$ and a finite group $F$.
Show that $H_2(M; \ZZ)$ is $\ZZ^r$ if $M$ is orientable and $\ZZ^{r-1} \oplus \ZZ_2$ if $M$ is nonorientable.
In particular, $r \geq 1$ when $M$ is nonorientable.
Using Exercise 6, construct examples showing there are no other restrictions on the homology groups of closed 3-manifolds.
[In the nonorientable case consider the manifold $N$ obtained from $S^2 \times I$ by identifying $S^2 \times \{0\}$ with $S^2 \times \{1\}$ via a reflection of $S^2$.]
:::

::: {.solution}
Write
$$
H_1(M;\ZZ)\cong\ZZ^r\oplus F
$$
with $F$ finite.

If $M$ is orientable, Poincaré duality and the universal coefficient theorem give
$$
H_2(M;\ZZ)\cong H^1(M;\ZZ)
\cong\operatorname{Hom}(H_1(M),\ZZ)
\cong\ZZ^r.
$$

Suppose $M$ is nonorientable. Corollary 3.28 says that the torsion subgroup of $H_2(M;\ZZ)$ is exactly $\ZZ_2$. Also every closed odd-dimensional manifold has Euler characteristic zero. Since $M$ is connected and nonorientable,
$$
H_0(M)\cong\ZZ,
\qquad H_3(M)=0.
$$
Hence
$$
0=\chi(M)=1-r+\operatorname{rank}H_2(M),
$$
so
$$
\operatorname{rank}H_2(M)=r-1.
$$
Therefore
$$
\boxed{H_2(M;\ZZ)\cong\ZZ^{r-1}\oplus\ZZ_2.}
$$
In particular $r\ge1$.

It remains to see that there are no further restrictions. Write
$$
F\cong\ZZ_{m_1}\oplus\cdots\oplus\ZZ_{m_s}.
$$
For orientable examples, take the connected sum of $r$ copies of $S^1\times S^2$ and lens spaces $L(m_j,1)$. Exercise 6 gives
$$
H_1\cong\ZZ^r\oplus F,
\qquad
H_2\cong\ZZ^r.
$$

The building blocks have homology
$$
H_*(S^1\times S^2)=\ZZ,\ZZ,\ZZ,\ZZ
\quad\text{in degrees }0,1,2,3,
$$
$$
H_*(L(m_j,1))=\ZZ,\ZZ_{m_j},0,\ZZ
\quad\text{in degrees }0,1,2,3.
$$
For nonorientable examples, let $N$ be the twisted $S^2$-bundle over $S^1$, obtained as the mapping torus of a reflection of $S^2$. Its mapping-torus sequence gives
$$
H_0(N)=\ZZ,\quad H_1(N)\cong\ZZ,\quad
H_2(N)\cong\ZZ_2,\quad H_3(N)=0.
$$
Taking the connected sum of $N$, $r-1$ copies of $S^1\times S^2$, and the same lens spaces yields, since connected sum adds $H_1$ and $H_2$ (the range $0<i<3$ of Exercise 6),
$$
H_1\cong\ZZ\oplus\ZZ^{r-1}\oplus F=\ZZ^r\oplus F,
\qquad
H_2\cong\ZZ_2\oplus\ZZ^{r-1}.
$$
The rank and torsion computation and the connected-sum examples appear in **Stanford Math 215C, Solution Set 4**, Hatcher 3.3.24, printed p. 2, [`solution4.pdf`](https://math.stanford.edu/~ralph/math215c/solution4.pdf). It uses odd-dimensional Euler characteristic zero and Corollary 3.28 for the torsion, as above. In its typography "dim $H^1(M;\ZZ)$" must be read as **rank**, not vector-space dimension: the finite summand $F$ contributes no rank. The mapping-torus sequence for the reflection $r$ has $r_*=-1$ on $H_2(S^2)$, so $H_2(N)\cong\operatorname{coker}(-2)=\ZZ_2$, $H_1(N)\cong\ZZ$, and $H_3(N)=0$. Since every example has exactly one nonorientable connected-sum factor, Exercise 6 requires no exceptional-case correction.
Thus every group pattern allowed by the formulas occurs.
:::