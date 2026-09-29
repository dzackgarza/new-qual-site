---
schema: qual/card@1
id: P-BKF99-5
kind: problem
title: Derivative of the matrix squaring map
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Expanded (X+H)^2 without assuming commutativity and bounded the quadratic
    remainder in the Euclidean matrix norm to verify the Frechet derivative.
---

::: {.problem}
Let $M_n$ be the vector space of real $n\times n$ matrices, identified with $\mathbb R^{n^2}$ with its usual Euclidean norm. Define
\[
f:M_n\to M_n,
\qquad
f(X)=X^2.
\]
Determine the derivative $Df$ of $f$.
:::

::: {.solution}

::: pf

::: {.pf-step #expansion-identity}
For $X,H\in M_n$,
$$
f(X+H)-f(X)=XH+HX+H^2.
$$

::: pf-proof
Matrix multiplication is distributive, so
$$
(X+H)^2=X^2+XH+HX+H^2.
$$
Subtracting $X^2=f(X)$ gives the identity.
:::

:::

::: {.pf-step #L-X-linear}
For fixed $X$, the map
$$
L_X:M_n\longrightarrow M_n,
\qquad
L_X(H)=XH+HX,
$$
is linear.

::: pf-proof
Both left multiplication $H\mapsto XH$ and right multiplication
$H\mapsto HX$ are linear maps on the real vector space $M_n$, so their sum
is linear.
:::

:::

::: {.pf-step #quadratic-remainder-vanishes}
With the Euclidean matrix norm,
$$
\frac{\norm{H^2}}{\norm{H}}\longrightarrow0
\qquad\text{as }H\to0.
$$

::: pf-proof
The Euclidean matrix norm is the Frobenius norm, which satisfies
$$
\norm{AB}\leq\norm{A}\norm{B}.
$$
Hence, for $H\neq0$,
$$
0
\leq
\frac{\norm{H^2}}{\norm{H}}
\leq
\norm{H},
$$
and the right-hand side tends to $0$ as $H\to0$.
:::

:::

::: {.pf-step #derivative-formula}
The derivative of $f$ at $X$ is
$$
\boxed{Df(X)(H)=XH+HX}.
$$

::: pf-proof
By steps [](#expansion-identity){.pf-ref} and [](#L-X-linear){.pf-ref},
$$
f(X+H)-f(X)-L_X(H)=H^2.
$$
Step [](#quadratic-remainder-vanishes){.pf-ref} therefore gives
$$
\frac{\norm{f(X+H)-f(X)-L_X(H)}}{\norm{H}}
\longrightarrow0.
$$
This is the definition of Frechet differentiability at $X$, with derivative
$L_X$.
:::

:::

::: pf-qed
Step [](#derivative-formula){.pf-ref} determines $Df(X)$ for every $X\in M_n$.
:::

:::

:::
