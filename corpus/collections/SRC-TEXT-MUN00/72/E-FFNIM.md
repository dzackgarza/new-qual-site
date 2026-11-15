---
schema: qual/card@1
id: E-FFNIM
kind: problem
title: Adjoining cells of dimension above two does not change the fundamental group
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §72 Exercise 1, printed p. 441. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The proof is the proof of Theorem 72.1 (printed
    pp. 439--440) with the disk B^2 replaced by B^n and the circle S^1 by S^{n-1}: steps 1 and 2 below are that
    proof, read on its page, with the two homotopy types it uses (B^2 - 0 onto S^1) replaced by the
    corresponding ones in dimension n. The theorem itself does not apply, since it is stated for a two-cell,
    so the argument is carried over and the place where n > 2 enters is the simple connectivity of S^{n-1},
    Theorem 59.3 (printed p. 369). Corollary 70.4 (printed p. 432) is used as in the book's step 2.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144) for §72 Exercise 1 (printed p. 441); queries and sets are in the
    COMPLAINTS.md entry for §66--§73 of SRC-TEXT-MUN00. Query used: "Munkres exercise if n > 2 homomorphism
    fundamental group B^n Int B^n bijectively onto X - A induced by inclusion trivial". Nothing located: the
    search returned the book's own page and course notes on §58, no treatment of this exercise; dbFin has no
    §72 page, Murayama's selection does not reach §72, the fourteen repositories stop at Chapter 3. Nothing was
    transcribed. The card's own proof was re-read against Corollary 70.4 (printed p. 432), Theorem 59.3 (printed
    p. 369) and step 1 of the proof of Theorem 72.1 (printed pp. 439--440), and answers the exercise: for n > 2
    the inclusion A -> X induces an isomorphism on fundamental groups, and it is n > 2 that makes U cap V and V
    simply connected. Nothing changed.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that step 3 applied Corollary 70.4 (printed p. 432) at the point a, which
    lies in A and hence outside V = X - A, while the corollary is stated for a base point in U cap V. Steps 3
    and 4 are now the book's own Step 3 of the proof of Theorem 72.1 (printed p. 440): the corollary is applied
    at a point b of U cap V, whose existence is recorded; the kernel of pi_1(U,b) -> pi_1(X,b) is the least
    normal subgroup containing the trivial group pi_1(U cap V,b); a path delta in U from b to a, which exists
    because U is path connected and contains A, gives isomorphisms delta-hat at b and at a which commute with
    the maps induced by inclusion, so pi_1(U,a) -> pi_1(X,a) is an isomorphism as the conjugate of one; and
    step 1 identifies pi_1(A,a) with pi_1(U,a). Steps 1 and 2 were re-read and kept.
---

::: {.exercise}

Let $X$ be a Hausdorff space; let $A$ be a closed path-connected subspace.
Suppose that $h: B^n \to X$ is a continuous map that maps $S^{n-1}$ into $A$ and maps $\operatorname{Int} B^n$ bijectively onto $X - A$.
Let $a$ be a point of $h(S^{n-1})$.
If $n > 2$, what can you say about the homomorphism of $\pi_1(A, a)$ into $\pi_1(X, a)$ induced by inclusion?
:::

::: {.solution}

For $n>2$ the homomorphism induced by inclusion is an isomorphism: adjoining a cell of dimension at least three changes no fundamental group.

::: pf

::: pf-step

$A$ is a deformation retract of the open set $U=X-h(\mathbf{0})$.

::: pf-proof

This is step 1 of the proof of Theorem 72.1 (printed pp. 439--440), which uses only that $\pi:B^n\to h(B^n)$, the restriction of $h$ to its image, is a quotient map, that $(B^n-\mathbf{0})\times I$ is saturated and open in $B^n\times I$, and that $B^n-\mathbf{0}$ deformation retracts onto $S^{n-1}$; the last holds for every $n\ge2$. Hence the deformation retraction descends to $h(B^n)-h(\mathbf{0})$, and is extended by the identity on $A$.

:::

:::

::: pf-step

$V=X-A$ is simply connected and $U\cap V$ is simply connected, since $n>2$.

::: pf-proof

By the book's step 2 (printed p. 440), $\pi$ restricts to a homeomorphism of $\operatorname{Int}B^n$ onto $V=X-A$, so $V$ is homeomorphic to an open ball, which is convex and hence contractible. Similarly $U\cap V=V-h(\mathbf{0})$ is homeomorphic to $\operatorname{Int}B^n-\mathbf{0}$, which deformation retracts onto $S^{n-1}$; and $S^{n-1}$ is simply connected for $n-1\ge2$ by Theorem 59.3 (printed p. 369). So $\pi_1(U\cap V)=0$.

:::

:::

::: pf-step

For $b$ a point of $U\cap V$, the inclusion $U\hookrightarrow X$ induces an epimorphism $\pi_1(U,b)\to\pi_1(X,b)$ with kernel the least normal subgroup containing the image of $\pi_1(U\cap V,b)$.

::: pf-proof

$U$ and $V$ are open in $X$ and $X=U\cup V$; $U$ is path connected because $A$ is a deformation retract of it, $V$ is contractible, and $U\cap V$ is path connected, being homeomorphic to $\operatorname{Int}B^n-\mathbf{0}$ for $n\ge2$; in particular $U\cap V$ is not empty, and its points are the base points at which Corollary 70.4 can be applied. Corollary 70.4 (printed p. 432) applies at a point $b\in U\cap V$, $V$ being simply connected.

:::

:::

::: pf-step

$\pi_1(A,a)\to\pi_1(X,a)$ is an isomorphism.

::: pf-proof

By step 2 the group $\pi_1(U\cap V,b)$ is trivial, so by step 3 the kernel of $\pi_1(U,b)\to\pi_1(X,b)$ is trivial and that homomorphism is an isomorphism. Let $\delta$ be a path in $U$ from $b$ to $a$, which exists because $U$ is path connected and contains the point $a$ of $A$. The isomorphisms $\hat\delta:\pi_1(U,b)\to\pi_1(U,a)$ and $\hat\delta:\pi_1(X,b)\to\pi_1(X,a)$ induced by $\delta$ commute with the homomorphisms induced by inclusion, as in the diagram of Step 3 of the proof of Theorem 72.1 (printed p. 440), so $\pi_1(U,a)\to\pi_1(X,a)$ is an isomorphism, being the conjugate of an isomorphism by $\hat\delta$. By step 1 the inclusion $A\hookrightarrow U$ induces an isomorphism $\pi_1(A,a)\to\pi_1(U,a)$. The composite of the two is induced by inclusion $A\hookrightarrow X$, so it is an isomorphism.

:::

:::

::: pf-qed

For $n>2$ the inclusion induces an isomorphism $\pi_1(A,a)\cong\pi_1(X,a)$; equivalently, the attaching map of the $n$-cell kills no element of $\pi_1(A,a)$, because $\pi_1(S^{n-1})=0$.

:::

:::
:::
