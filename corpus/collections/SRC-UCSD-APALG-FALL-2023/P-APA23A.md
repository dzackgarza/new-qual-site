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

::: problem
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex entries, and $x^H$ denotes the Hermitian transpose of $x$.

(a) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M_n$.

(b) Prove that for $A, B \in M_n$, if $x^H A x = x^H B x$ for all $x \in \mathbb{C}^n$, then $A = B$.
Give an example for which $x^T A x = x^T B x$ for all $x \in \mathbb{C}^n$ but $A \neq B$.
:::

::: {.solution}
**Part (a).**

<1>1. Schur decomposition: every $A \in M_n$ is unitarily similar to an upper triangular matrix, i.e. there is a unitary $U$ and an upper triangular $T$ with $A = U T U^H$.
::: {.proof}
statement of the theorem.
:::

**Part (b).**

<1>1. If $x^H A x = x^H B x$ for all $x$, then $x^H (A - B) x = 0$ for all $x$.
::: {.proof}
subtract.
:::

<1>2. Let $C = A - B$; then $x^H C x = 0$ for all $x$ implies $C = 0$.
<2>1. $C$ is Hermitian (or, more generally, the condition $x^H C x = 0$ for all $x$ forces $C = 0$).
::: {.proof}
if $x^H C x = 0$ for all $x$, then by polarization, $x^H C y = 0$ for all $x, y$ (using $x^H C x = 0$ for all $x$ and the polarization identity), so $C = 0$.
:::
<2>2. Hence $A = B$.
::: {.proof}
<2>1.
:::

<1>3. Counterexample for the transpose: $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $B = 0$.
<2>1. $x^T A x = 0$ for all $x \in \CC^2$.
::: {.proof}
for $x = (x_1, x_2)$, $x^T A x = (x_1, x_2)\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = x_1 x_2 - x_2 x_1 = 0$.
:::
<2>2. $x^T B x = 0$ for all $x$.
::: {.proof}
$B = 0$.
:::
<2>3. But $A \neq B$.
::: {.proof}
$A \neq 0$.
:::

<1>4. Q.E.D.
::: {.proof}
<1>2 (b) and <1>3 (counterexample).
:::
:::
