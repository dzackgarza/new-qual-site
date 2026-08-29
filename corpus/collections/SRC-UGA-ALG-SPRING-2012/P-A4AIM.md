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

::: problem
Let $k$ be a field and let the group $G = \GL(m, k) \cross \GL(n, k)$ acts on the set of $m\times n$ matrices $M_{m, n}(k)$ as follows:
\[
(A, B) \cdot X = AXB\inv
\]
where $(A, B) \in G$ and $X\in M_{m, n}(k)$.

a. State what it means for a group to act on a set.
Prove that the above definition yields a group action.

b. Exhibit with justification a subset $S$ of $M_{m, n}(k)$ which contains precisely one element of each orbit under this action.
:::

::: {.solution}
**Part (a).**

<1>1. A group $G$ acts on a set $X$ if there is a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$, such that $e \cdot x = x$ and $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$, $x \in X$.
Proof: definition of a group action.

<1>2. The given formula defines a group action.
<2>1. Identity: $(I_m, I_n) \cdot X = I_m X I_n^{-1} = X$.
Proof: the identity matrices act trivially.
<2>2. Compatibility: $(A_1, B_1) \cdot ((A_2, B_2) \cdot X) = (A_1, B_1) \cdot (A_2 X B_2^{-1}) = A_1 A_2 X B_2^{-1} B_1^{-1} = (A_1 A_2) X (B_1 B_2)^{-1} = (A_1 A_2, B_1 B_2) \cdot X$.
Proof: direct computation, using $(B_1 B_2)^{-1} = B_2^{-1} B_1^{-1}$.

<1>3. Hence this is a group action.
Proof: <1>1 and <1>2.

**Part (b).**

<1>1. Two matrices $X, Y \in M_{m,n}(k)$ are in the same orbit iff they have the same rank.
Proof: $AXB^{-1}$ has the same rank as $X$ (since $A$ and $B^{-1}$ are invertible); conversely, two matrices of the same rank $r$ are related by $X = A Y B^{-1}$ for suitable invertible $A, B$ (row and column operations reduce any rank-$r$ matrix to the same canonical form).

<1>2. Hence a set $S$ containing exactly one element of each orbit is
$$S = \{ D_r : 0 \le r \le \min(m, n) \},$$
where $D_r$ is the $m \times n$ matrix with $1$'s in the first $r$ diagonal positions and $0$'s elsewhere.
Proof: $D_r$ has rank $r$, and by <1>1 the orbits are exactly the rank classes, so the $D_r$ (one per possible rank) form a complete set of orbit representatives.

<1>3. Q.E.D.
Proof: <1>3 (a) and <1>2 (b).
:::
