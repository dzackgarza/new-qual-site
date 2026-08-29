---
schema: qual/card@1
id: P-AMD-KFLCBYQU
kind: problem
title: Order-6 homeomorphism of the torus fixing the origin
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $x_0$ be the image of $0$, show that there is an order 6 homeomorphism $f: T \to T$ fixing $x_0$.
Find a representation of $f_*$ as a matrix, and find its determinant.
:::

::: {.solution}
<1>1. Let $T = \mathbb{R}^2/\mathbb{Z}^2$ be the torus, with $x_0$ the image of $0$.
Proof: setup.

<1>2. Define $f : T \to T$ by $f(x, y) = (y, -x - y)$ (mod $\mathbb{Z}^2$), i.e. the linear map with matrix $A = \begin{pmatrix} 0 & 1 \\ -1 & -1 \end{pmatrix}$.
Proof: definition.

<1>3. $A$ has integer entries, so it descends to a well-defined homeomorphism of $T = \mathbb{R}^2/\mathbb{Z}^2$.
Proof: an integer matrix maps $\mathbb{Z}^2$ into itself, so it induces a map on the quotient.

<1>4. $f$ fixes $x_0$ (the image of $0$).
Proof: $A(0,0) = (0,0)$.

<1>5. $A^2 = \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix}$ and $A^3 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I$, so $A^6 = I$.
Proof: direct computation; $A^3 = -I$ implies $A^6 = I$.

<1>6. Hence $f$ has order $6$.
Proof: <1>5 ($A^6 = I$ and no smaller positive power is $I$, since $A^3 = -I \neq I$ and $A, A^2 \neq I$).

<1>7. $f_* : H_1(T) \cong \ZZ^2 \to H_1(T) \cong \ZZ^2$ is represented by the matrix $A = \begin{pmatrix} 0 & 1 \\ -1 & -1 \end{pmatrix}$.
Proof: the induced map on $H_1(T) = \pi_1(T) = \ZZ^2$ is exactly the linear map $A$.

<1>8. $\det A = 0 \cdot (-1) - 1 \cdot (-1) = 1$.
Proof: compute the determinant.

<1>9. Q.E.D.
Proof: <1>6, <1>7, <1>8.
:::
