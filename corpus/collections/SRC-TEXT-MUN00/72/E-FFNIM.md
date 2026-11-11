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

The inclusion $U\hookrightarrow X$ induces an epimorphism $\pi_1(U,a)\to\pi_1(X,a)$ with kernel the least normal subgroup containing the image of $\pi_1(U\cap V,a)$.

::: pf-proof

$U$ and $V$ are open in $X$ and $X=U\cup V$; $U$ is path connected because $A$ is a deformation retract of it, $V$ is contractible, and $U\cap V$ is path connected, being homeomorphic to $\operatorname{Int}B^n-\mathbf{0}$ for $n\ge2$. Corollary 70.4 (printed p. 432) applies, $V$ being simply connected.

:::

:::

::: pf-step

$\pi_1(A,a)\to\pi_1(X,a)$ is an isomorphism.

::: pf-proof

By step 3 the kernel of $\pi_1(U,a)\to\pi_1(X,a)$ is the least normal subgroup containing the image of the trivial group $\pi_1(U\cap V,a)$, hence is trivial; so $\pi_1(U,a)\to\pi_1(X,a)$ is an isomorphism. By step 1 the inclusion $A\hookrightarrow U$ induces an isomorphism $\pi_1(A,a)\to\pi_1(U,a)$. The composite of the two is induced by inclusion $A\hookrightarrow X$, so it is an isomorphism.

:::

:::

::: pf-qed

For $n>2$ the inclusion induces an isomorphism $\pi_1(A,a)\cong\pi_1(X,a)$; equivalently, the attaching map of the $n$-cell kills no element of $\pi_1(A,a)$, because $\pi_1(S^{n-1})=0$.

:::

:::
:::
