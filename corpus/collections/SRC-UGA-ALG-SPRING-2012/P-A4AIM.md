---
schema: qual/card@1
id: P-A4AIM
kind: problem
title: Orbits of $\GL(m,k)\times\GL(n,k)$ acting by $(A,B)\cdot X=AXB^{-1}$
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Matrices
  - Canonical Forms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---
::: {.problem}
Let $k$ be a field and let the group $G = \GL(m, k) \cross \GL(n, k)$ acts on the set of $m\times n$ matrices $M_{m, n}(k)$ as follows:
$$
(A, B) \cdot X = AX\inverseof{B}
$$
where $(A, B) \in G$ and $X\in M_{m, n}(k)$.

a. State what it means for a group to act on a set.
Prove that the above definition yields a group action.

b. Exhibit with justification a subset $S$ of $M_{m, n}(k)$ which contains precisely one element of each orbit under this action.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A group action of $G$ on a set $X$ is a map $G\times X\to X$ satisfying $e\cdot x=x$ and $(gh)\cdot x=g\cdot(h\cdot x)$.

::: pf-proof

These are the identity and associativity axioms defining a left group action.

:::

:::

::: {.pf-step #s2}

The formula $(A,B)\cdot X=AXB^{-1}$ defines an action of $\mathrm{GL}(m,k)\times\mathrm{GL}(n,k)$ on $M_{m,n}(k)$.

::: pf-proof

The identity pair acts by $I_mXI_n=X$. For two pairs $(A_1,B_1)$ and $(A_2,B_2)$, the iterated action is
$$
A_1(A_2XB_2^{-1})B_1^{-1}
=(A_1A_2)X(B_1B_2)^{-1},
$$
which equals their product acting on $X$. Thus the axioms in step [](#s1){.pf-ref} hold.

:::

:::

::: {.pf-step #s3}

Two matrices belong to the same orbit if and only if they have equal rank.

::: pf-proof

Multiplication on either side by an invertible matrix preserves rank. Conversely, elementary row and column operations reduce any matrix of rank $r$ to the matrix $D_r$ with an $r\times r$ identity block in its top-left corner and all other entries zero. Such operations are realized by left multiplication by a member of $\mathrm{GL}(m,k)$ and right multiplication by a member of $\mathrm{GL}(n,k)$, hence by the stated action. Therefore all matrices of rank $r$ lie in one orbit.

:::

:::

::: {.pf-step #s4}

A complete set of orbit representatives is
$$
\boxed{S=\{D_r:0\leq r\leq\min(m,n)\}},
$$
where $D_r$ has ones in the first $r$ diagonal positions and zeros elsewhere.

::: pf-proof

Every possible rank $r$ has representative $D_r$ by step [](#s3){.pf-ref}. Distinct values of $r$ give distinct ranks, hence distinct orbits. Thus $S$ contains exactly one representative of each orbit.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} establish part (a), and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} establish part (b).

:::

:::

:::
