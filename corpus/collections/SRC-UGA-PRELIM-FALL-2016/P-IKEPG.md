---
schema: qual/card@1
id: P-IKEPG
kind: problem
title: $\sum_{i=1}^n i^3 = \bigl(\sum_{i=1}^n i\bigr)^2$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and the missing base case supplied. The prose was one chain of equalities under a numbered list item, with no base case at all and no statement of the inductive hypothesis; the card now states P(n), proves P(1), states and uses the triangular-number formula (itself by induction, since the exercise asks for an induction proof and that formula is not free), and separates the algebraic factorization n^2 + 4(n+1) = (n+2)^2 into the step where it is used. Every line of the original computation survives, and the "qed" marker is gone. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Use induction to prove that, for every positive integer $n$,
$$
1^3+2^3+\cdots+n^3=(1+2+\cdots+n)^2.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own. Write $S_n=\sum_{i=1}^n i^3$ and $T_n=\sum_{i=1}^n i$.

The induction is on $n\ge1$, with the statement $P(n)$: $S_n=T_n^2$.

::: pf

::: {.pf-step #base}
$P(1)$ holds.

::: pf-proof
$S_1=1^3=1$ and $T_1=1$, so $S_1=1=T_1^2$.
:::

:::

::: {.pf-step #triangular}
$T_n=\frac12n(n+1)$ for every $n\ge1$.

::: pf-proof
This is the standard closed form for the sum of the first $n$ positive integers, itself proved by induction: $T_1=1=\frac12\cdot1\cdot2$, and $T_{n+1}=T_n+(n+1)=\frac12n(n+1)+(n+1)=\frac12(n+1)(n+2)$.
:::

:::

::: {.pf-step #step}
If $P(n)$ holds for some $n\ge1$, then $P(n+1)$ holds.

::: pf-proof
Assume $S_n=T_n^2$. Then
$$
S_{n+1}=S_n+(n+1)^3=T_n^2+(n+1)^3=\left(\frac12n(n+1)\right)^2+(n+1)^3
$$
by the inductive hypothesis and step [](#triangular){.pf-ref}. Now
$$
\left(\frac12n(n+1)\right)^2+(n+1)^3=\frac14n^2(n+1)^2+(n+1)(n+1)^2=\frac14(n+1)^2\bigl(n^2+4(n+1)\bigr),
$$
factoring out $\frac14(n+1)^2$ and using $1=\frac44$ in the second term. Since $n^2+4n+4=(n+2)^2$,
$$
S_{n+1}=\frac14(n+1)^2(n+2)^2=\left(\frac12(n+1)(n+2)\right)^2=T_{n+1}^2
$$
by step [](#triangular){.pf-ref} with $n+1$ in place of $n$.
:::

:::

::: {.pf-step}
$1^3+2^3+\cdots+n^3=(1+2+\cdots+n)^2$ for every positive integer $n$.

::: pf-proof
$P(1)$ holds by step [](#base){.pf-ref} and $P(n)$ implies $P(n+1)$ for all $n\ge1$ by step [](#step){.pf-ref}; by induction $P(n)$ holds for every $n\ge1$, which is the displayed identity with $S_n$ and $T_n$ expanded.
:::

:::

:::
:::
