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

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    DeMason's induction with the card's barycentric cover. Added: the induction hypothesis
    verified separately for $Y$ and for $Z$ (the second was asserted), the disjoint case
    handled before Mayer–Vietoris, the explicit verification that $\lambda_j>0$ survives the
    straight-line homotopy to the barycentre, and the emptiness of the total intersection.
    Page corrected: the exercise is on printed p. 158, not p. 156. Cited: Proposition 2.6
    printed p. 109, the reduced Mayer–Vietoris sequence printed pp. 149–150, Corollary 2.14
    printed p. 114, and DeMason's set at printed pp. 79–80 of his PDF. The card's own
    contribution relative to DeMason remains the barycentric cover.
---

::: {.problem}
Suppose the space $X$ is the union of open sets $A_1, \cdots, A_n$ such that each intersection $A_{i_1} \cap \cdots \cap A_{i_k}$ is either empty or has trivial reduced homology groups.
Show that $\tilde{H}_i(X) = 0$ for $i \geq n-1$, and give an example showing this inequality is best possible, for each $n$.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §2.2 Exercise 33. The induction on the number of sets and the acyclic open cover of $\partial\Delta^{n-1}$ are **Kenneth DeMason, *M382C Full Credit HW Problems* (4 April 2021), Hatcher 2.2.33** (`tmp/sources/demason-m382c-hatcher-20210404.pdf`); the card replaces his small open face-neighbourhoods by the explicit barycentric sets $\theset{\lambda_j>0}$ and verifies that their intersections have exactly the contractible form the induction needs.

Throughout, "acyclic" means having trivial reduced homology in every degree, and a cover is a finite family of open subsets of $X$ whose union is $X$. The claim to be proved, for $n\ge1$, is: if $X=A_1\cup\cdots\cup A_n$ with each nonempty intersection $A_{i_1}\cap\cdots\cap A_{i_k}$ acyclic, then $\widetilde H_i(X)=0$ for $i\ge n-1$.

::: pf

::: {.pf-step #base}
The claim holds for $n=1$ and for $n=2$.

::: pf-proof
For $n=1$ the hypothesis says $X=A_1$ is acyclic, which is the conclusion for $i\ge0=n-1$. The case $n=2$ is the induction step below with $n-1=1$ supplying the two acyclicity statements it uses, so nothing separate is needed beyond acyclicity of $A_1$, $A_2$ and $A_1\cap A_2$ (the last if nonempty), all of which are hypotheses.

:::

:::

::: {.pf-step #induction-hypothesis}
Assume $n\ge2$ and the claim for all covers by $n-1$ sets. With $Y=A_1\cup\cdots\cup A_{n-1}$ and $Z=Y\cap A_n=\bigcup_{j<n}(A_j\cap A_n)$, one has $\widetilde H_i(Y)=0$ and $\widetilde H_i(Z)=0$ for $i\ge n-2$, and $\widetilde H_i(A_n)=0$ for all $i$.

::: pf-proof
$Y$ is covered by the $n-1$ open sets $A_1,\dots,A_{n-1}$, and every nonempty finite intersection of these is an intersection in the given cover, hence acyclic; so the induction hypothesis gives $\widetilde H_i(Y)=0$ for $i\ge n-2$. For $Z$, the sets $A_j\cap A_n$ with $j<n$ are open in $Z$ and cover it, and a finite intersection of them is $\bigl(\bigcap_{j\in I}A_j\bigr)\cap A_n$, an intersection of the given cover, hence acyclic when nonempty; so the induction hypothesis applies to $Z$ as well. Finally $A_n$ is a single member of the cover, hence acyclic.

:::

:::

::: {.pf-step #disjoint}
If $Z=\varnothing$, then $\widetilde H_i(X)=0$ for $i\ge n-2$, in particular for $i\ge n-1$.

::: pf-proof
With $Z$ empty, $Y$ and $A_n$ are disjoint open subsets covering $X$, so $X$ is their disjoint union as a space. Then $\widetilde H_i(X)\cong\widetilde H_i(Y)\oplus\widetilde H_i(A_n)$ (Proposition 2.6), and both summands vanish for $i\ge n-2$ by step [](#induction-hypothesis){.pf-ref}.

:::

:::

::: {.pf-step #mayer-vietoris}
If $Z\ne\varnothing$, then $\widetilde H_i(X)=0$ for $i\ge n-1$.

::: pf-proof
$X=Y\cup A_n$ with $Y,A_n$ open and $Y\cap A_n=Z$, so the reduced Mayer–Vietoris sequence of §2.2 applies and contains the segment
$$
\widetilde H_i(Y)\oplus\widetilde H_i(A_n)\longrightarrow\widetilde H_i(X)\longrightarrow\widetilde H_{i-1}(Z)\longrightarrow\widetilde H_{i-1}(Y)\oplus\widetilde H_{i-1}(A_n)
$$
for every $i$. For $i\ge n-1$ we have $i\ge n-2$ and $i-1\ge n-2$, so step [](#induction-hypothesis){.pf-ref} makes both outer groups zero; exactness then forces $\widetilde H_i(X)=0$.

:::

:::

::: {.pf-step #sharp-cover}
For $n\ge2$ let $X=\partial\Delta^{n-1}$ and $A_j=\theset{x\in X\mid\lambda_j(x)>0}$, where $\lambda_1,\dots,\lambda_n$ are the barycentric coordinates. Then $A_1,\dots,A_n$ is a cover of $X$ by $n$ open sets, every nonempty proper subfamily has acyclic intersection, and the total intersection is empty.

::: pf-proof
$X=\theset{\lambda_j\ge0,\ \sum_j\lambda_j=1,\ \lambda_j=0\text{ for some }j}$ with the subspace topology of the simplex, and $A_j=X\cap\theset{\lambda_j>0}$ is open in $X$. Each point of $X$ has some $\lambda_j>0$, so the $A_j$ cover $X$. Since $\sum_j\lambda_j=1$, a point of $X$ has some coordinate zero, so no point lies in every $A_j$: the total intersection is empty. For a nonempty proper $I\subset\theset{1,\dots,n}$ put $F_I=\theset{x\in\Delta^{n-1}\mid\lambda_j=0\text{ for }j\notin I}$ and $c_I=\sum_{j\in I}e_j/\abs{I}$, the barycenter of $F_I$; the map $H(x,t)=(1-t)x+tc_I$ is a homotopy in $\Delta^{n-1}$ from the identity to the constant map at $c_I$, and it stays in $F_I$ because a point of $\bigcap_{j\in I}A_j$ has $\lambda_j=0$ for $j\notin I$, a condition preserved by the straight-line homotopy, and $\lambda_j>0$ for $j\in I$, the barycenter having $\lambda_j=1/\abs{I}>0$ there, so the segment keeps those coordinates positive. Hence $\bigcap_{j\in I}A_j\simeq\theset{c_I}$ is contractible, in particular acyclic.

:::

:::

::: {.pf-step #sharp-homology}
With $X=\partial\Delta^{n-1}$ as in step [](#sharp-cover){.pf-ref}, $\widetilde H_{n-2}(X)\cong\ZZ\ne0$.

::: pf-proof
$\partial\Delta^{n-1}$ is homeomorphic to $S^{n-2}$, so $\widetilde H_{n-2}(X)\cong\widetilde H_{n-2}(S^{n-2})\cong\ZZ$ (Corollary 2.14). The cover of step [](#sharp-cover){.pf-ref} satisfies the hypothesis of the claim, so the claim would force $\widetilde H_i(X)=0$ for $i\ge n-1$; it gives nothing in degree $n-2$, and there the group is nonzero. Hence the vanishing range $i\ge n-1$ cannot be improved to $i\ge n-2$, and the inequality is best possible for each $n\ge2$.

:::

:::

::: {.pf-step #conclusion}
$\widetilde H_i(X)=0$ for $i\ge n-1$, and the bound is sharp for every $n$.

::: pf-proof
Steps [](#base){.pf-ref}, [](#disjoint){.pf-ref} and [](#mayer-vietoris){.pf-ref} prove the vanishing by induction on $n$, and steps [](#sharp-cover){.pf-ref} and [](#sharp-homology){.pf-ref} show, for each $n\ge2$, that the range cannot start lower: on $S^{n-2}$ the cover by $n$ barycentric sets meets the hypothesis and has $\widetilde H_{n-2}\ne0$, so the vanishing cannot hold in degree $n-2$. For $n=1$ the hypothesis itself says that $X$ is acyclic, which is the conclusion, and there is nothing to sharpen.

:::

:::

:::
:::
