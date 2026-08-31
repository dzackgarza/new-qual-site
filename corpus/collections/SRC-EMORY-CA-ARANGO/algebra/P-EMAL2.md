---
schema: qual/card@1
id: P-EMAL2
kind: problem
title: "Conjugacy classes of matrices with prescribed minimal polynomial"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Determine the number of conjugacy classes of $16 \times 16$ matrices with entries in $\mathbf{Q}$ and minimal polynomial $(x^2 + 1)^2(x^3 + 2)^2$.
:::

::: {.solution}
<1>1. $x^2 + 1$ and $x^3 + 2$ are irreducible over $\QQ$.
::: {.proof}
$x^2 + 1$ has no real root; $x^3 + 2$ is Eisenstein at $2$.
:::

<1>2. The characteristic polynomial $\chi$ of such a matrix is divisible by the minimal polynomial and has the same irreducible factors, so $\chi = (x^2+1)^a (x^3+2)^b$ with $a \ge 2$, $b \ge 2$, and $2a + 3b = 16$.
::: {.proof}
the minimal polynomial divides the characteristic polynomial and they share irreducible factors; the degree of $\chi$ is $16$.
:::

<1>3. The solutions to $2a + 3b = 16$ with $a \ge 2$, $b \ge 2$ are $(a, b) = (5, 2)$ and $(a, b) = (2, 4)$.
::: {.proof}
$b = 2$ gives $a = 5$; $b = 4$ gives $a = 2$; $b = 3$ gives $a = 7/2$ (not integral); $b \ge 5$ gives $a < 2$.
:::

<1>4. For a fixed characteristic polynomial, the conjugacy classes are in bijection with the ways of arranging the elementary divisors (primary components) into invariant factors, subject to the largest invariant factor being the minimal polynomial.
::: {.proof}
the rational canonical form (or the theory of elementary divisors and invariant factors).
:::

<1>5. For the factor $(x^2+1)$ with minimal exponent $2$ and characteristic exponent $a$, the elementary divisors are $(x^2+1)^{e_1}, \ldots, (x^2+1)^{e_k}$ with $e_1 \ge \cdots \ge e_k \ge 1$, $\sum e_i = a$, and $e_1 = 2$; the number of such is the number of partitions of $a$ with largest part exactly $2$.
::: {.proof}
the largest elementary divisor exponent equals the minimal polynomial exponent.
:::

<1>6. Similarly, for $(x^3+2)$ with characteristic exponent $b$, the number of choices is the number of partitions of $b$ with largest part exactly $2$.
::: {.proof}
same reasoning.
:::

<1>7. Partitions with largest part exactly $2$:
- of $5$: $2+2+1$ and $2+1+1+1$ (two);
- of $2$: $2$ (one);
- of $4$: $2+2$ and $2+1+1$ (two).
::: {.proof}
enumerate.
:::

<1>8. Total number of conjugacy classes:
$$(\text{partitions of } 5 \text{ with largest part } 2) \cdot (\text{partitions of } 2 \text{ with largest part } 2) + (\text{partitions of } 2) \cdot (\text{partitions of } 4) = 2 \cdot 1 + 1 \cdot 2 = 4.$$
::: {.proof}
<1>3, <1>5, <1>6, and <1>7.
:::

<1>9. Q.E.D.
::: {.proof}
there are $4$ conjugacy classes (<1>8).
:::
:::
