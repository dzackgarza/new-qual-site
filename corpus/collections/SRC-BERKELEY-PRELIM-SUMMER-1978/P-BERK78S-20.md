---
schema: qual/card@1
id: P-BERK78S-20
kind: problem
title: Derivative of the matrix-squaring map
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Expanded (X+H)^2-X^2 as XH+HX+H^2. The candidate derivative
    H↦XH+HX is linear, while the Frobenius norm satisfies
    ||H^2||_F<=||H||_F^2, so the quadratic remainder is
    o(||H||_F).
---

::: {.problem}
Let $M_{n\times n}(\mathbb R)$ be the vector space of real $n\times n$ matrices, and define
\[
f:M_{n\times n}(\mathbb R)\to M_{n\times n}(\mathbb R),
\qquad f(X)=X^2.
\]
Find the derivative of $f$.
:::

::: {.solution}
Equip
$$
M_{n\times n}(\RR)
$$
with the Frobenius norm
$$
\norm{A}_F
=
\left(
\sum_{i,j=1}^n a_{ij}^2
\right)^{1/2}.
$$

::: pf

::: {.pf-step #s1}

For every pair of real $n\times n$ matrices $A,B$,
$$
\norm{AB}_F
\leq
\norm{A}_F\norm{B}_F.
$$

::: pf-proof

For each $i,j$,
$$
(AB)_{ij}
=
\sum_{k=1}^n a_{ik}b_{kj}.
$$
By Cauchy--Schwarz,
$$
\abs{(AB)_{ij}}^2
\leq
\left(
\sum_{k=1}^n a_{ik}^2
\right)
\left(
\sum_{k=1}^n b_{kj}^2
\right).
$$
Summing over $i,j$ gives
$$
\begin{aligned}
\norm{AB}_F^2
&=
\sum_{i,j}
\abs{(AB)_{ij}}^2\\
&\leq
\sum_{i,j}
\left(
\sum_k a_{ik}^2
\right)
\left(
\sum_k b_{kj}^2
\right)\\
&=
\left(
\sum_{i,k}a_{ik}^2
\right)
\left(
\sum_{k,j}b_{kj}^2
\right)\\
&=
\norm{A}_F^2\norm{B}_F^2.
\end{aligned}
$$
Taking square roots proves the claim.

:::

:::

::: {.pf-step #s2}

Fix
$$
X\in M_{n\times n}(\RR)
$$
and define
$$
L_X(H)=XH+HX.
$$
Then $L_X$ is a linear map
$$
M_{n\times n}(\RR)\longrightarrow M_{n\times n}(\RR).
$$

::: pf-proof

For matrices $H,K$ and scalars $a,b\in\RR$,
$$
\begin{aligned}
L_X(aH+bK)
&=
X(aH+bK)+(aH+bK)X\\
&=
a(XH+HX)+b(XK+KX)\\
&=
aL_X(H)+bL_X(K).
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

For every increment $H$,
$$
f(X+H)-f(X)-L_X(H)=H^2.
$$

::: pf-proof

Expanding without assuming commutativity,
$$
\begin{aligned}
f(X+H)
&=
(X+H)^2\\
&=
X^2+XH+HX+H^2.
\end{aligned}
$$
Since
$$
f(X)=X^2
$$
and
$$
L_X(H)=XH+HX,
$$
the displayed remainder identity follows.

:::

:::

::: {.pf-step #s4}

The remainder in step [](#s3){.pf-ref} satisfies
$$
\frac{
\norm{f(X+H)-f(X)-L_X(H)}_F
}{
\norm{H}_F
}
\longrightarrow
0
$$
as $H\to0$.

::: pf-proof

For $H\neq0$, steps [](#s1){.pf-ref} and [](#s3){.pf-ref} give
$$
\begin{aligned}
\frac{
\norm{f(X+H)-f(X)-L_X(H)}_F
}{
\norm{H}_F
}
&=
\frac{\norm{H^2}_F}{\norm{H}_F}\\
&\leq
\frac{\norm{H}_F^2}{\norm{H}_F}\\
&=
\norm{H}_F.
\end{aligned}
$$
The right-hand side tends to zero with $H$.

:::

:::

::: {.pf-step #s5}

The derivative of $f$ at $X$ is the linear map
$$
\boxed{
Df(X)[H]=XH+HX.
}
$$

::: pf-proof

Step [](#s2){.pf-ref} shows that $L_X$ is linear, and step [](#s4){.pf-ref} is exactly the
Fréchet differentiability condition with derivative $L_X$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the requested derivative.

:::

:::

:::
