---
schema: qual/card@1
id: P-APAS18A
kind: problem
title: Similarity of $8\times 8$ matrices with prescribed ranks of powers
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $A,B\in\mathbb{C}^{8\times 8}$ be two matrices such that
\[
\operatorname{rank} A=\operatorname{rank} B=6,\quad
\operatorname{rank} A^2=\operatorname{rank} B^2=4,\quad
\operatorname{rank} A^3=\operatorname{rank} B^3=2,\quad
\operatorname{rank} A^4=\operatorname{rank} B^4=0.
\]
Determine whether $A$ and $B$ are similar to each other or not.
If yes, explain why; if no, give a counterexample.
:::

::: {.solution}
<1>1. $A^4 = 0$ and $B^4 = 0$, so both $A$ and $B$ are nilpotent.
Proof: $\operatorname{rank} A^4 = 0$ means $A^4 = 0$.

<1>2. The ranks of the powers of a nilpotent matrix determine its Jordan form.
<2>1. For a nilpotent matrix $N$, the number of Jordan blocks of size $\ge k$ is $\operatorname{rank} N^{k-1} - \operatorname{rank} N^k$.
Proof: standard fact about nilpotent Jordan forms.
<2>2. For $A$: number of blocks of size $\ge 1$ is $8 - 6 = 2$; size $\ge 2$ is $6 - 4 = 2$; size $\ge 3$ is $4 - 2 = 2$; size $\ge 4$ is $2 - 0 = 2$.
Proof: <2>1 applied to the given ranks.
<2>3. Hence $A$ has $2$ Jordan blocks, each of size $4$.
Proof: <2>2 (two blocks of size $\ge 4$, and total size $8$, so two blocks of size exactly $4$).

<1>3. The same computation applies to $B$, so $B$ also has $2$ Jordan blocks of size $4$.
Proof: $B$ has the same ranks of powers.

<1>4. Hence $A$ and $B$ have the same Jordan form (two nilpotent blocks of size $4$), so they are similar.
Proof: <1>2 and <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
