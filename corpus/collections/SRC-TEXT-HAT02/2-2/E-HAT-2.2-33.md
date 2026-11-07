---
schema: qual/card@1
id: E-HAT-2.2-33
kind: problem
title: 'Nerve-type vanishing: $\tilde{H}_i(X) = 0$ for $i \geq n-1$ when intersections are acyclic'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 33.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the induction: $Y=A_1\cup\cdots\cup A_{n-1}$ and $Z=Y\cap A_n$ have vanishing reduced
    homology above $n-2$, by the inductive hypothesis applied to their own covers, and the
    Mayer-Vietoris segment then forces $\tilde H_i(X)=0$ for $i\ge n-1$. Read the sharpness
    example: the $n$ open sets $\lambda_j>0$ on $\partial\Delta^{n-1}$ cover it, their total
    intersection is empty on the boundary, each proper intersection retracts to a barycenter inside
    the boundary, and $\tilde H_{n-2}(S^{n-2})=\ZZ$.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 33 as printed on p. 158. The induction is correct: the cover of
    Y has n-1 sets and that of Z = Y cap A_n has n-1 sets, so both vanish in degrees at least
    n-2, and the Mayer-Vietoris segment kills H~_i(X) for i at least n-1. The case Z empty, in
    which the reduced sequence does not apply, is now separated and handled by Proposition 2.6
    p. 109; the sequence is cited to pp. 149-150 and H~_{n-2}(S^{n-2})=Z to Corollary 2.14
    p. 114. The sharpness example was checked: the n sets {lambda_j > 0} are open in the
    boundary, their union is X, the total intersection is empty, and for a proper index set I
    the intersection is contracted to the barycentre of the face I by a straight-line homotopy
    that stays in the boundary because some coordinate outside I is zero at every point of it.
    What is not covered: no certificate.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    The induction and sharpness argument compare correctly with DeMason, M382C Full Credit HW
    Problems (2021), Hatcher 2.2.33, printed pp.79-80. The cover Y∩A_n itself has n-1 open sets, so
    induction at n-1 gives vanishing for Y and every Ai∩An for i>=n-2; reduced MV then gives
    H~_i(X)=0 for i>=n-1. The source's face-neighborhood example on S^{n-2} is reproduced by the
    explicit barycentric open sets in the card, whose proper intersections have trivial reduced
    homology and whose full intersection is empty.

---

::: {.problem}
Suppose the space $X$ is the union of open sets $A_1, \cdots, A_n$ such that each intersection $A_{i_1} \cap \cdots \cap A_{i_k}$ is either empty or has trivial reduced homology groups.
Show that $\tilde{H}_i(X) = 0$ for $i \geq n-1$, and give an example showing this inequality is best possible, for each $n$.
:::

::: {.solution}
We induct on the number of sets. For one set the assertion is the hypothesis. Suppose it holds for covers by fewer than $n$ sets, and put
$$
Y=A_1\cup\cdots\cup A_{n-1},
\qquad
Z=Y\cap A_n=\bigcup_{j=1}^{n-1}(A_j\cap A_n).
$$
Both are open in $X$. Every nonempty finite intersection in the cover of $Z$ is one of the intersections in the hypothesis. Hence induction gives
$$
\widetilde H_i(Y)=\widetilde H_i(Z)=0
\qquad (i\ge n-2).
$$
The same hypothesis gives $\widetilde H_i(A_n)=0$ for every $i$. If $Z=\varnothing$ then $X$ is the disjoint union of the open sets $Y$ and $A_n$, so $\widetilde H_i(X)=\widetilde H_i(Y)\oplus\widetilde H_i(A_n)=0$ for $i\ge n-2$ by Proposition 2.6 (p. 109). Otherwise the reduced Mayer--Vietoris sequence of pp. 149--150 for $X=Y\cup A_n$ applies, and for $i\ge n-1$ it has the segment
$$
0=\widetilde H_i(Y)\oplus\widetilde H_i(A_n)
\longrightarrow \widetilde H_i(X)
\longrightarrow \widetilde H_{i-1}(Z)=0.
$$
Thus $\widetilde H_i(X)=0$ in the claimed range.

For sharpness when $n\ge2$, let $X=\partial\Delta^{n-1}\cong S^{n-2}$ and use barycentric coordinates $\lambda_1,\ldots,\lambda_n$. Set
$$
A_j=\{x\in X:\lambda_j(x)>0\}.
$$
These $n$ open sets cover $X$. Their total intersection is empty. For every proper nonempty set of indices $I$, the intersection $\bigcap_{j\in I}A_j$ contracts to the barycenter of the face spanned by $I$: the straight-line homotopy stays in $X$, since each point and that barycenter share a zero coordinate outside $I$, and all coordinates indexed by $I$ remain positive. Yet
$$
\widetilde H_{n-2}(X)\cong\ZZ,
$$
by Corollary 2.14 (p. 114), the boundary $\partial\Delta^{n-1}$ being homeomorphic to $S^{n-2}$. Thus the vanishing range cannot start at $n-2$. For $n=1$, the hypothesis itself says that the sole nonempty set is acyclic, and the conclusion $\widetilde H_i(X)=0$ for $i\ge0$ is then immediate.
The induction and the acyclic open cover of $\partial\Delta^{n-1}$ appear in **Kenneth DeMason, *M382C Full Credit HW Problems* (4 April 2021)**, Hatcher 2.2.33, printed pp. 79--80, [`DeMason, Kenneth M382C HW Full Credit 20210404.pdf`](https://math.mcmaster.ca/~demasonk/files/exercises/DeMason%2C%20Kenneth%20M382C%20HW%20Full%20Credit%2020210404.pdf), held locally as `tmp/sources/demason-m382c-hatcher-20210404.pdf`. The card refines his small open face-neighborhoods into the explicit barycentric sets $\{\lambda_j>0\}$, whose intersections have exactly the contractible form needed for the induction.

:::
