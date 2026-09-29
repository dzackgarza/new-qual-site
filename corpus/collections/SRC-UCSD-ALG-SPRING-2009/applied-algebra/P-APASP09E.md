---
schema: qual/card@1
id: P-APASP09E
kind: problem
title: "Determinant of the Jacobian of elementary symmetric functions"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 2 of Part II of the official UCSD Spring 2009 Applied Algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Verified homogeneity degree and the Vandermonde Jacobian identity, including the sign convention by the n=2 case.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $e_r$ be the $r$-th elementary symmetric function in the variables $x_1, x_2, \ldots, x_n$.

(a) Show that the determinant of $\left(\frac{\partial e_i}{\partial x_j}\right)_{1 \leq i, j \leq n}$ is a homogeneous polynomial and calculate its degree.

(b) Calculate the determinant.
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
$e_i$ is homogeneous of degree $i$.

::: pf-proof
$e_i = \sum_{1 \le j_1 < \cdots < j_i \le n} x_{j_1} \cdots x_{j_i}$, a sum of monomials of degree $i$.
:::

:::

::: pf-step
$\frac{\partial e_i}{\partial x_j}$ is homogeneous of degree $i - 1$.

::: pf-proof
differentiating a homogeneous polynomial of degree $i$ lowers the degree by $1$.
:::

:::

::: {.pf-step #p1-s3}
The determinant $\det\left(\frac{\partial e_i}{\partial x_j}\right)$ is homogeneous of degree $\sum_{i=1}^n (i-1) = \frac{n(n-1)}{2}$.

::: pf-proof
the determinant is a sum of products, each product taking one entry from each row $i$; the entry in row $i$ has degree $i-1$, so each term has total degree $\sum_{i=1}^n (i-1)$.
:::

:::

:::

**Part (b).**

::: pf

::: pf-step
$\frac{\partial e_i}{\partial x_j} = e_{i-1}(x_1, \ldots, \widehat{x_j}, \ldots, x_n)$.

::: pf-proof
the terms of $e_i$ containing $x_j$ are exactly $x_j$ times the elementary symmetric functions of degree $i-1$ in the remaining variables.
:::

:::

::: pf-step
The matrix $\left(\frac{\partial e_i}{\partial x_j}\right)$ is the Jacobian of the map $x \mapsto (e_1, \ldots, e_n)$.

::: pf-proof
definition.
:::

:::

::: {.pf-step #p2-s3}
$\det\left(\frac{\partial e_i}{\partial x_j}\right) = \prod_{1 \le i < j \le n} (x_i - x_j)$ (the Vandermonde determinant).

::: pf-proof
this is the classical identity for the Jacobian of the elementary symmetric functions; it follows by noting the determinant vanishes whenever $x_i = x_j$ (two columns equal), so it is divisible by $\prod_{i<j}(x_i - x_j)$, and both sides have degree $\frac{n(n-1)}{2}$ by part (a), so they agree up to a constant, which is $1$ (checked on the leading term).
:::

:::

::: pf-qed
step [](#p1-s3){.pf-ref} (part (a)) and step [](#p2-s3){.pf-ref} (part (b)).
:::

:::
:::
