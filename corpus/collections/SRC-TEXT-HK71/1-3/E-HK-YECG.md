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
---

::: {.exercise}
Consider the system of equations AX = 0 where

$$
A = \left[ \begin{array}{c c} a & b \\ c & d \end{array} \right]
$$

is a $2 \times 2$ matrix over the field $F$ . Prove the following.

(a) If every entry of $A$ is 0, then every pair $(x_1, x_2)$ is a solution of $AX = 0$ .

(b) If $ad - bc \neq 0$, the system $AX = 0$ has only the trivial solution $x_{1} = x_{2} = 0$ .

(c) If $ad - bc = 0$ and some entry of $A$ is different from 0, then there is a solution $(x_1^0, x_2^0)$ such that $(x_1, x_2)$ is a solution if and only if there is a scalar $y$ such that $x_1 = yx_1^0, x_2 = yx_2^0$ .
:::

::: {.solution}
**Part (a).**

<1>1. If $A = 0$, then $AX = 0$ for every $X = (x_1, x_2)$.
::: {.proof}
the zero matrix sends every vector to $0$.
:::

**Part (b).**

<1>1. If $ad - bc \neq 0$, then $A$ is invertible.
::: {.proof}
$\det A = ad - bc \neq 0$.
:::

<1>2. Hence $AX = 0$ implies $X = A^{-1} \cdot 0 = 0$.
::: {.proof}
multiply both sides by $A^{-1}$.
:::

<1>3. Therefore the only solution is the trivial one.
::: {.proof}
<1>2.
:::

**Part (c).**

<1>1. If $ad - bc = 0$ and $A \neq 0$, then $\operatorname{rank}(A) = 1$.
::: {.proof}
$A$ is nonzero but singular, so its rank is $1$ (a nonzero $2 \times 2$ matrix of determinant $0$ has rank $1$).
:::

<1>2. Hence the solution space $\{X : AX = 0\}$ is $1$-dimensional.
::: {.proof}
by rank–nullity, $\dim \ker A = 2 - \operatorname{rank}(A) = 1$.
:::

<1>3. Let $(x_1^0, x_2^0)$ be any nonzero solution.
::: {.proof}
such a solution exists since $\ker A \neq 0$.
:::

<1>4. Then $(x_1, x_2)$ is a solution iff $(x_1, x_2) = y(x_1^0, x_2^0)$ for some scalar $y$.
::: {.proof}
the solution space is $1$-dimensional and spanned by $(x_1^0, x_2^0)$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1 (a), <1>3 (b), and <1>4 (c).
:::
:::
