---
schema: qual/card@1
id: E-HK-YECG
kind: problem
title: Solutions of $AX = 0$ for $2 \times 2$ matrices
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Exercise 1.3.8 of Hoffman and Kunze, Linear Algebra, in the
    retained PDF assets/attachments/Hoffman-Kunze-Linear-Algebra.pdf, PDF
    p. 19 (the Section 1.3 exercises, item 8): the three parts agree, including
    the field F as base and the "if and only if there is a scalar y" of (c).
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The three arguments are correct, and no hypothesis is missing. (a) is
    immediate. (b) is det A = ad - bc not zero, so A is invertible and the only
    solution is A^{-1} times 0. (c) is the observation that a nonzero singular
    2 x 2 matrix has rank 1, rank-nullity then gives a one-dimensional kernel,
    a nonzero solution exists, and every solution is a scalar multiple of it;
    the "if and only if" is the two inclusions of a one-dimensional subspace.
    Nothing uses any property of F beyond being a field. The card proves the
    steps in one line each, which is terse but correct; no change was made.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read as a second reader against the retained text; the statement matches Hoffman and Kunze
    Exercise 1.3.8, printed p. 11, all three parts. The mathematics is correct: the zero matrix
    sends every vector to 0; det A = ad-bc nonzero makes A invertible, so AX = 0 gives X = 0;
    and a nonzero singular 2x2 matrix has rank 1, so the kernel is 1-dimensional and its
    solutions are the scalar multiples of any nonzero one. Three defects repaired, none
    mathematical: the step 'Therefore the only solution is the trivial one' had a proof that was
    only a reference back to the preceding step and duplicated it, so it is removed and the
    preceding step now states the conclusion; a trailing pf-qed that listed three back-
    references and nothing else is removed, as STYLE-08 asks; and five proofs that began in
    lower case now begin as sentences. No claim changed.
---

::: {.exercise}
Consider the system of equations $AX = 0$ where

$$
A = \left[ \begin{array}{c c} a & b \\ c & d \end{array} \right]
$$

is a $2 \times 2$ matrix over the field $F$ . Prove the following.

(a) If every entry of $A$ is 0, then every pair $(x_1, x_2)$ is a solution of $AX = 0$ .

(b) If $ad - bc \neq 0$, the system $AX = 0$ has only the trivial solution $x_{1} = x_{2} = 0$ .

(c) If $ad - bc = 0$ and some entry of $A$ is different from 0, then there is a solution $(x_1^0, x_2^0)$ such that $(x_1, x_2)$ is a solution if and only if there is a scalar $y$ such that $x_1 = yx_1^0, x_2 = yx_2^0$ .
:::

::: {.solution}
No retained solution set covers this exercise; the book's text is retained as `assets/attachments/Hoffman-Kunze-Linear-Algebra.pdf` (Hoffman and Kunze, *Linear Algebra*, 2nd ed., 1971), where it is §1.3 Exercise 8 on printed p. 11. The argument is the card's own.

**Part (a).**

::: pf

::: {.pf-step #zero-matrix-all-solutions}
If $A = 0$, then $AX = 0$ for every $X = (x_1, x_2)$.

::: pf-proof
The zero matrix sends every vector to $0$.
:::

:::

:::

**Part (b).**

::: pf

::: pf-step
If $ad - bc \neq 0$, then $A$ is invertible.

::: pf-proof
$\det A = ad - bc \neq 0$.
:::

:::

::: {.pf-step #ax0-implies-x-zero}
Hence the only solution of $AX = 0$ is the trivial one, $X = 0$.

::: pf-proof
Multiplying both sides on the left by $A^{-1}$ gives $X=A^{-1}0=0$.
:::

:::

:::

**Part (c).**

::: pf

::: pf-step
If $ad - bc = 0$ and $A \neq 0$, then $\operatorname{rank}(A) = 1$.

::: pf-proof
$A$ is nonzero but singular, so its rank is $1$ (a nonzero $2 \times 2$ matrix of determinant $0$ has rank $1$).
:::

:::

::: pf-step
Hence the solution space $\{X : AX = 0\}$ is $1$-dimensional.

::: pf-proof
By rank–nullity, $\dim\ker A=2-\operatorname{rank}(A)=1$.
:::

:::

::: pf-step
Let $(x_1^0, x_2^0)$ be any nonzero solution.

::: pf-proof
Such a solution exists because $\ker A\ne0$.
:::

:::

::: {.pf-step #solution-iff-scalar-multiple}
Then $(x_1, x_2)$ is a solution iff $(x_1, x_2) = y(x_1^0, x_2^0)$ for some scalar $y$.

::: pf-proof
The solution space is $1$-dimensional and spanned by $(x_1^0,x_2^0)$, so its elements are exactly the scalar multiples of that vector.
:::

:::

:::

:::
