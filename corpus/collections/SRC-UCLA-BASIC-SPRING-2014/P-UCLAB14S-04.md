---
schema: qual/card@1
id: P-UCLAB14S-04
kind: problem
title: Characteristic polynomials of $AB$ and $BA$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 4. Suppose that $A,B\in M_{n,n}(\mathbb C)$.
Show that the characteristic polynomials of $AB$ and $BA$ are equal.

Hint: One approach is to first show that it holds when $B$ is invertible.
:::

::: {.solution}
<1>1. If $B$ is invertible, then $AB$ and $BA$ are similar:
\[
BA=B(AB)B^{-1}.
\]

::: {.proof}
Associativity gives $B(AB)B^{-1}=(BA)(BB^{-1})=BA$.
:::

<1>2. Hence, for invertible $B$,
\[
\det(tI-AB)=\det(tI-BA).
\]

::: {.proof}
Indeed,
\[
tI-BA=B(tI-AB)B^{-1},
\]
and determinants are invariant under similarity.
:::

<1>3. For fixed $A$ and $t$, the functions
\[
F_t(B)=\det(tI-AB),
\qquad
G_t(B)=\det(tI-BA)
\]
are polynomial, hence continuous, functions of the entries of $B$.

::: {.proof}
Matrix multiplication and determinant are polynomial operations in matrix entries.
:::

<1>4. Invertible matrices are dense in $M_n(\mathbb C)$.

::: {.proof}
For arbitrary $B$, the matrix $B+sI$ is singular only when $-s$ is an eigenvalue of $B$. There are finitely many such $s$, so there are arbitrarily small $s$ for which $B+sI$ is invertible, and $B+sI\to B$ as $s\to0$.
:::

<1>5. Therefore
\[
F_t(B)=G_t(B)
\]
for every $B$ and every $t$.

::: {.proof}
Choose invertible $B_j\to B$ using step <1>4. Step <1>2 gives $F_t(B_j)=G_t(B_j)$, and continuity from step <1>3 gives
\[
F_t(B)=\lim_jF_t(B_j)=\lim_jG_t(B_j)=G_t(B).
\]
:::

<1>6. Consequently
\[
\boxed{\chi_{AB}(t)=\chi_{BA}(t).}
\]

::: {.proof}
Step <1>5 states that $\det(tI-AB)=\det(tI-BA)$ for every $t$, which is equality of the two characteristic polynomials.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
