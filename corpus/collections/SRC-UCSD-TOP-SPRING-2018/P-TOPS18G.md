---
schema: qual/card@1
id: P-TOPS18G
kind: problem
title: '$H^1(N)\cong H_1(M)$ for complementary pieces of $S^3$, and the punctured $\RP^3$ does not embed in $S^3$'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Embeddings
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card's statement did not match its printed source. The problem is number
    7 of the retained assets/attachments/290qualF23_extracted.md, and its second
    half reads: "Let X be the compact 3-manifold-with-boundary obtained by
    removing the interior of a small ball from RP^3. Conclude that X cannot be
    embedded in S^3." The card had that conclusion as "RP^2 cannot be embedded
    in S^3", a different true statement, and proved it by a regular neighbourhood
    argument. The statement now reproduces the printed one, the title is
    corrected, and the two steps that proved the RP^2 conclusion are replaced by
    the argument for X: removing a ball from the open 3-cell of RP^3 leaves a
    space retracting onto RP^2, so H_1(X) = Z/2, which cannot be free as the
    first part forces for a piece of a decomposition of S^3. Provenance note: the
    collection lists the Spring 2018 topology qual, whose problems do not include
    this one; the located source is the Fall 2023 290 qual.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Statement re-read in assets/attachments/290qualF23_extracted.md, problem 7,
    with the provenance discrepancy above recorded.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Both parts are now correct. Alexander duality for the compact locally
    contractible subset N of S^3 gives H_1(M) isomorphic to the reduced first
    cohomology of N, since the interior of M is S^3 minus N and retracts onto M
    along a collar; the universal coefficient theorem makes that group free
    because H_1(N) is finitely generated. For the second part, X retracts onto
    RP^2 and so has first homology Z/2, and an embedding of X in S^3 would make
    it one side of a decomposition of S^3, where the first part forces free first
    homology.
---

::: {.problem}
Suppose that $S^3 = M \cup_\Sigma N$ is a decomposition of the $3$-sphere into two compact $3$-manifolds, glued along their common boundary surface $\Sigma$.
Prove that $H^1(N) \cong H_1(M)$.
Let $X$ be the compact $3$-manifold with boundary obtained by removing the interior of a small ball from $\RP^3$.
Conclude that $X$ cannot be embedded in $S^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #h1-iso}
In any decomposition $S^3=M\cup_\Sigma N$ as in the problem,
$$\boxed{H^1(N;\ZZ)\cong H_1(M;\ZZ)},$$
and $H_1(M;\ZZ)$ is free abelian. By symmetry the same holds with $M$ and $N$ exchanged.

::: pf-proof
The interior of $M$ is $S^3\setminus N$ and is homotopy equivalent to $M$ by a collar of $\partial M$, so Alexander duality for the compact, locally contractible subspace $N\subset S^3$ gives $H_1(M)\cong\widetilde H_1(S^3\setminus N)\cong\widetilde H^{1}(N)=H^1(N)$. The universal coefficient theorem gives $H^1(N;\ZZ)\cong\operatorname{Hom}(H_1(N),\ZZ)$, which is free abelian because $H_1(N)$ is finitely generated.
:::

:::

::: {.pf-step #regular-neighborhood-retracts}
$X$ satisfies $H_1(X;\ZZ)\cong\ZZ/2$.

::: pf-proof
$\RP^3$ is the union of its $2$-skeleton $\RP^2$ with a single $3$-cell, and removing the interior of a small ball in that open $3$-cell leaves a space that deformation retracts onto $\RP^2$. Hence $H_1(X)\cong H_1(\RP^2)=\ZZ/2$, while $X$ is a compact $3$-manifold with boundary $\partial X=S^2$.
:::

:::

::: {.pf-step #contradiction-freeness}
If $X$ embedded in $S^3$ with complement $N$, then $S^3=X\cup_{\partial X}N$ would be a decomposition as in the first part, forcing $H_1(X)$ to be free abelian by step [](#h1-iso){.pf-ref}, which contradicts step [](#regular-neighborhood-retracts){.pf-ref}.

::: pf-proof
A closed regular neighbourhood of the embedded $X$ inside $S^3$ is a compact $3$-manifold with the same boundary, and its complement is the required $N$; the identification $H_1(X)\cong H^1(N)$ from step [](#h1-iso){.pf-ref} makes $H_1(X)$ free, while it is $\ZZ/2$.
:::

:::

::: pf-step
Therefore
$$\boxed{X\text{ does not embed in }S^3.}$$

::: pf-proof
This is the contradiction in step [](#contradiction-freeness){.pf-ref}.
:::

:::

:::

:::
