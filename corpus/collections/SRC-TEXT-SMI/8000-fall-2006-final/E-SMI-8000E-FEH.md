---
schema: qual/card@1
id: E-SMI-8000E-FEH
kind: problem
title: Real spectral theorem or the Cayley-Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both proof choices with Smith Math 8000 Fall 2006 final part H."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Chose Cayley--Hamilton over a commutative field and proved it from the adjugate identity by coefficient comparison."
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith 8000e.pdf page 12, final part H(ii), the
    option proved, with the sheet's instruction to say what the hypotheses are: the
    card states F a field, n ≥ 1 and A in M_n(F), and proves chi_A(A) = 0 by comparing
    coefficients in (tI - A)adj(tI - A) = chi_A(t)I and descending the recurrence to
    B_0. Correct. No defect.
---
---

::: {.exercise}
Prove one:

(i) Every real symmetric matrix is orthogonally diagonalizable;

or

(ii) The Cayley-Hamilton theorem.
Say what your hypotheses are.
:::

::: {.solution}
We prove option (ii). Let $F$ be a field, let $n\ge1$, and let
$A\in M_n(F)$. Write
$$
\chi_A(t)=\det(tI-A)=t^n+c_{n-1}t^{n-1}+\cdots+c_0.
$$
The Cayley--Hamilton theorem asserts
$$
\boxed{\chi_A(A)=0.}
$$

::: pf

::: pf-step

Expand the adjugate identity over $F[t]$.

::: pf-proof

Write
$$
\operatorname{adj}(tI-A)=B_{n-1}t^{n-1}+\cdots+B_0.
$$
Then
$$
(tI-A)\operatorname{adj}(tI-A)=\chi_A(t)I.
$$
Comparing coefficients gives
$$
B_{n-1}=I,
$$
$$
B_{k-1}-AB_k=c_kI\qquad(1\le k\le n-1),
$$
and
$$
-AB_0=c_0I.
$$

:::

:::

::: pf-step

Solve the recurrence and conclude.

::: pf-proof

Starting from $B_{n-1}=I$ and descending through the recurrence gives
$$
B_0=A^{n-1}+c_{n-1}A^{n-2}+\cdots+c_1I.
$$
Substituting this into $-AB_0=c_0I$ yields
$$
A^n+c_{n-1}A^{n-1}+\cdots+c_1A+c_0I=0.
$$
This is exactly
$$
\boxed{\chi_A(A)=0.}
$$

:::

:::

:::

:::
