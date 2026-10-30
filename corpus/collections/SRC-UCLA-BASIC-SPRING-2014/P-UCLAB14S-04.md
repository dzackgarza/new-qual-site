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
Suppose that $A,B\in M_{n,n}(\CC)$.
Show that the characteristic polynomials of $AB$ and $BA$ are equal.

Hint: One approach is to first show that it holds when $B$ is invertible.
:::

::: {.solution}

::: pf

::: pf-step

If $B$ is invertible, then $AB$ and $BA$ are similar:
$$
BA=B(AB)B^{-1}.
$$


::: pf-proof

Associativity gives $B(AB)B^{-1}=(BA)(BB^{-1})=BA$.

:::

:::

::: {.pf-step #s1-2}

Hence, for invertible $B$,
$$
\det(tI-AB)=\det(tI-BA).
$$


::: pf-proof

Indeed,
$$
tI-BA=B(tI-AB)B^{-1},
$$
and determinants are invariant under similarity.

:::

:::

::: {.pf-step #s1-3}

For fixed $A$ and $t$, the functions
$$
F_t(B)=\det(tI-AB),
\qquad
G_t(B)=\det(tI-BA)
$$
are polynomial, hence continuous, functions of the entries of $B$.


::: pf-proof

Matrix multiplication and determinant are polynomial operations in matrix entries.

:::

:::

::: {.pf-step #s1-4}

Invertible matrices are dense in $M_n(\CC)$.


::: pf-proof

For arbitrary $B$, the matrix $B+sI$ is singular only when $-s$ is an eigenvalue of $B$. There are finitely many such $s$, so there are arbitrarily small $s$ for which $B+sI$ is invertible, and $B+sI\to B$ as $s\to0$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
F_t(B)=G_t(B)
$$
for every $B$ and every $t$.


::: pf-proof

Choose invertible $B_j\to B$ using step [](#s1-4){.pf-ref}. Step [](#s1-2){.pf-ref} gives $F_t(B_j)=G_t(B_j)$, and continuity from step [](#s1-3){.pf-ref} gives
$$
F_t(B)=\lim_jF_t(B_j)=\lim_jG_t(B_j)=G_t(B).
$$

:::

:::

::: {.pf-step #s1-6}

Consequently
$$
\boxed{\chi_{AB}(t)=\chi_{BA}(t).}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} states that $\det(tI-AB)=\det(tI-BA)$ for every $t$, which is equality of the two characteristic polynomials.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
