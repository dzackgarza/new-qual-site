---
schema: qual/card@1
id: P-APA23A
kind: problem
title: Schur decomposition; Hermitian vs transpose quadratic forms determine a matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex entries, and $x^H$ denotes the Hermitian transpose of $x$.

(a) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M_n$.

(b) Prove that for $A, B \in M_n$, if $x^H A x = x^H B x$ for all $x \in \mathbb{C}^n$, then $A = B$.
Give an example for which $x^T A x = x^T B x$ for all $x \in \mathbb{C}^n$ but $A \neq B$.
:::

::: {.solution}

**Part (a).**

::: pf

::: pf-step
Schur decomposition: every $A \in M_n$ is unitarily similar to an upper triangular matrix, i.e. there is a unitary $U$ and an upper triangular $T$ with $A = U T U^H$.

::: pf-proof
statement of the theorem.
:::

:::

:::

**Part (b).**

::: pf

::: pf-step
If $x^H A x = x^H B x$ for all $x$, then $x^H (A - B) x = 0$ for all $x$.

::: pf-proof
subtract.
:::

:::

::: {.pf-step #c-vanishing-form-implies-a-equals-b}
Let $C = A - B$; then $x^H C x = 0$ for all $x$ implies $C = 0$.

::: pf-proof

::: {.pf-step #hermitian-form-implies-c-zero}
$C$ is Hermitian (or, more generally, the condition $x^H C x = 0$ for all $x$ forces $C = 0$).

::: pf-proof
if $x^H C x = 0$ for all $x$, then by polarization, $x^H C y = 0$ for all $x, y$ (using $x^H C x = 0$ for all $x$ and the polarization identity), so $C = 0$.
:::

:::

::: pf-step
Hence $A = B$.

::: pf-proof
Step [](#hermitian-form-implies-c-zero){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #transpose-counterexample}
Counterexample for the transpose: $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $B = 0$.

::: pf-proof

::: pf-step
$x^T A x = 0$ for all $x \in \CC^2$.

::: pf-proof
for $x = (x_1, x_2)$, $x^T A x = (x_1, x_2)\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = x_1 x_2 - x_2 x_1 = 0$.
:::

:::

::: pf-step
$x^T B x = 0$ for all $x$.

::: pf-proof
$B = 0$.
:::

:::

::: pf-step
But $A \neq B$.

::: pf-proof
$A \neq 0$.
:::

:::

:::

:::

::: pf-qed
Step [](#c-vanishing-form-implies-a-equals-b){.pf-ref} (b) and step [](#transpose-counterexample){.pf-ref} (counterexample).
:::

:::

:::
