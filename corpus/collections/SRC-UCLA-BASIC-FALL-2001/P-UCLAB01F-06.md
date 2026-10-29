---
schema: qual/card@1
id: P-UCLAB01F-06
kind: problem
title: Direct local surjectivity from an identity derivative
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Suppose $F:\RR^2\to\RR^2$ is continuously differentiable, satisfies
\[
F(0,0)=(0,0),
\]
and has Jacobian matrix equal to the identity at $(0,0)$.
Outline a direct proof that there exists $\delta>0$ such that whenever
\[
a^2+b^2<\delta,
\]
there is a point $(x,y)\in\RR^2$ with
\[
F(x,y)=(a,b).
\]

Do not merely restate the Inverse Function Theorem: the requested argument is part of its proof.
You may use without proof basic estimates expressing that the change in $F$ is approximated by its differential.
:::

::: {.solution}

Use the Euclidean norm on $\RR^2$ and the induced operator norm on matrices.

::: pf

::: {.pf-step #s1-1}

There exists $r>0$ such that
\[
\|I-DF(x)\|\le \frac12
\]
whenever $\|x\|\le r$.


::: pf-proof

The derivative $DF$ is continuous and
\[
DF(0)=I.
\]
Hence $\|DF(x)-I\|\to0$ as $x\to0$. Choose $r>0$ so that the displayed bound holds on the closed ball
\[
\overline B_r={x\in\RR^2:\|x\|\le r}.
\]

:::

:::

::: {.pf-step #s1-2}

For all $x,z\in\overline B_r$,
\[
\|(x-F(x))-(z-F(z))\|
\le
\frac12\|x-z\|.
\]


::: pf-proof

The line segment joining $z$ to $x$ lies in the convex set $\overline B_r$. Apply the fundamental estimate for differentiable maps to
\[
H(u)=u-F(u),
\]
whose derivative is
\[
DH(u)=I-DF(u).
\]
By step [](#s1-1){.pf-ref},
\[
\|DH(u)\|\le\frac12
\]
along the segment. Therefore
\[
\|H(x)-H(z)\|
\le
\frac12\|x-z\|.
\]

:::

:::

::: {.pf-step #s1-3}

For any $y\in\RR^2$ with
\[
\|y\|<\frac r2,
\]
the map
\[
T_y(x)=x+y-F(x)
\]
sends $\overline B_r$ into itself and satisfies
\[
\|T_y(x)-T_y(z)\|
\le
\frac12\|x-z\|.
\]


::: pf-proof

Since $F(0)=0$, step [](#s1-2){.pf-ref} with $z=0$ gives
\[
\|x-F(x)\|\le\frac12\|x\|
\]
for $x\in\overline B_r$. Thus
\[
\|T_y(x)\|
\le
\|y\|+\|x-F(x)\|
<
\frac r2+\frac r2
=r,
\]
so $T_y(x)\in\overline B_r$.

Also the constant vector $y$ cancels in differences, so step [](#s1-2){.pf-ref} gives
\[
\|T_y(x)-T_y(z)\|
=
\|(x-F(x))-(z-F(z))\|
\le
\frac12\|x-z\|.
\]

:::

:::

::: pf-step

For such $y$, the iteration
\[
x_0=0,
\qquad
x_{n+1}=T_y(x_n)
\]
converges to a point $x\in\overline B_r$.


::: pf-proof

Step [](#s1-3){.pf-ref} shows inductively that every $x_n\in\overline B_r$. It also gives
\[
\|x_{n+1}-x_n\|
\le
\frac12\|x_n-x_{n-1}\|.
\]
Therefore
\[
\|x_{n+1}-x_n\|
\le
2^{-n}\|x_1-x_0\|.
\]
For $m>n$,
\[
\|x_m-x_n\|
\le
\sum_{j=n}^{m-1}\|x_{j+1}-x_j\|
\le
\|x_1-x_0\|\sum_{j=n}^{\infty}2^{-j},
\]
which tends to $0$ as $n\to\infty$. Thus $(x_n)$ is Cauchy. Since $\RR^2$ is complete and $\overline B_r$ is closed, $x_n\to x$ for some $x\in\overline B_r$.

:::

:::

::: {.pf-step #s1-5}

The limit $x$ satisfies
\[
F(x)=y.
\]


::: pf-proof

The map $T_y$ is continuous because $F$ is continuous. Passing to the limit in
\[
x_{n+1}=T_y(x_n)
\]
gives
\[
x=T_y(x)=x+y-F(x).
\]
Hence $F(x)=y$.

:::

:::

::: {.pf-step #s1-6}

With
\[
\boxed{\delta=\frac{r^2}{4}},
\]
every $(a,b)$ satisfying $a^2+b^2<\delta$ lies in the image of $F$.


::: pf-proof

Let
\[
y=(a,b).
\]
The inequality $a^2+b^2<r^2/4$ is exactly
\[
\|y\|<r/2.
\]
Step [](#s1-5){.pf-ref} therefore supplies $x\in\RR^2$ with $F(x)=y=(a,b)$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required local-surjectivity statement.

:::

:::

:::
