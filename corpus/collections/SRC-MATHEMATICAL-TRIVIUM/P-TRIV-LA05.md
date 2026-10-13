---
schema: qual/card@1
id: P-TRIV-LA05
kind: problem
title: Determinants of $A^T$, $A^{-1}$ and $cA$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray extraction digit and separated parts (a)-(c) against Linear Algebra Problem 5 on page 1 of the source PDF.
---

::: {.problem}
Let $A$ and $B$ be non-degenerate $n \times n$ matrices, $c \in \mathbb{C}$.
Write the relations between their determinants, if

(a) $B = A^T$,

(b) $B = A^{-1}$,

(c) $B = c \cdot A$.
:::

::: {.solution}
<1>1. If
$$
B=A^T,
$$
then
$$
\boxed{\det B=\det A}.
$$

::: {.proof}
The determinant is invariant under transposition:
$$
\det(A^T)=\det A.
$$
:::

<1>2. If
$$
B=A^{-1},
$$
then
$$
\boxed{\det B=\frac1{\det A}}.
$$

::: {.proof}
Since
$$
AA^{-1}=I,
$$
multiplicativity of the determinant gives
$$
(\det A)(\det A^{-1})
=
\det I
=1.
$$
Because $A$ is nondegenerate, $\det A\neq0$, so
$$
\det A^{-1}
=
\frac1{\det A}.
$$
:::

<1>3. If
$$
B=cA,
$$
then
$$
\boxed{\det B=c^n\det A}.
$$

::: {.proof}
Multiplying the whole matrix by $c$ multiplies each of its $n$ rows by $c$.
The determinant is linear in each row, so each row contributes one factor of
$c$. Therefore
$$
\det(cA)=c^n\det A.
$$
:::

<1>4. If $B=cA$ is also nondegenerate, then necessarily $c\neq0$.

::: {.proof}
By step <1>3,
$$
\det B
=
c^n\det A.
$$
Since both determinants are nonzero, $c^n\neq0$, hence $c\neq0$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 give the requested determinant relations.
:::
:::
