---
schema: qual/card@1
id: E-SS8.PR-9
kind: problem
title: Arithmetic-geometric mean and Gauss's elliptic integral
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Integrals
relations: []
review: draft
---

::: {.exercise}
Let $a_0=a\geq b=b_0>0$ and define
$$
a_{n+1}=\frac{a_n+b_n}{2},\qquad b_{n+1}=\sqrt{a_nb_n}.
$$

(a) Prove that $a_n$ and $b_n$ have a common limit $M(a,b)$, called the arithmetic-geometric mean.

(b) Let
$$
I(a,b)=\frac2\pi\int_0^{\pi/2}
\frac{d\theta}{\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}}.
$$
Prove Gauss's identity $I(a,b)=1/M(a,b)$ by showing that
$$
I(a,b)=I\left(\frac{a+b}{2},\sqrt{ab}\right).
$$
Also observe that
$$
I(a,b)=\frac1a K(k)=\frac1a\int_0^1
\frac{dx}{\sqrt{(1-x^2)(1-k^2x^2)}},
\qquad k^2=1-\frac{b^2}{a^2},
$$
and that the invariance follows from Chapter 8, Exercise 24(b).
:::

::: {.hint}
For (a), show $a_0\geq a_1\geq\cdots\geq a_n\geq b_n\geq\cdots\geq b_1\geq b_0$ and $a_n-b_n\leq(a-b)/2^n$.
:::

::: {.remark}
The source omits the factor $2/\pi$ in its displayed formula $I(a,b)=K(k)/a$ if $K(k)$ is the integral it displays. At $a=b=1$, its left side is $1$ and its right side is $\pi/2$.
:::
