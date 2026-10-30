---
schema: qual/card@1
id: P-UCLAB02F-06
kind: problem
title: A regular level set contains a nonconstant local curve
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Suppose $F:\RR^3\to\RR^2$ is continuously differentiable.
Suppose that for some $v_0\in\RR^3$ and $x_0\in\RR^2$,
$$
F(v_0)=x_0
$$
and the derivative
$$
F'(v_0):\RR^3\to\RR^2
$$
is onto.
Show that there are $\varepsilon>0$ and a continuously differentiable function
$$
\gamma:(-\varepsilon,\varepsilon)\to\RR^3
$$
such that
$$
\gamma'(0)\ne0
$$
and
$$
F(\gamma(t))=x_0
\qquad\text{for every }t\in(-\varepsilon,\varepsilon).
$$
:::

::: {.solution}

Write
$$
v_0=(a_0,b_0,c_0).
$$

::: pf

::: {.pf-step #s1-1}

After relabeling the coordinates of $\RR^3$ if necessary, the $2\times2$ matrix
$$
\frac{\partial(F_1,F_2)}{\partial(a,b)}(v_0)
$$
is invertible.


::: pf-proof

The derivative
$$
F'(v_0):\RR^3\to\RR^2
$$
is onto, so its $2\times3$ matrix has rank $2$. Therefore at least one of its $2\times2$ minors is nonzero. Permuting the three domain coordinates if necessary, take that minor to be the one corresponding to the first two coordinates $(a,b)$.

:::

:::

::: {.pf-step #s1-2}

There exist an interval $I$ containing $c_0$ and a continuously differentiable map
$$
\phi:I\to\RR^2,
\qquad
\phi(c_0)=(a_0,b_0),
$$
such that
$$
F(\phi(c),c)=x_0
$$
for every $c\in I$.


::: pf-proof

Define
$$
G(a,b,c)=F(a,b,c)-x_0.
$$
Then
$$
G(a_0,b_0,c_0)=0.
$$
By step [](#s1-1){.pf-ref}, the derivative of $G$ with respect to the variables $(a,b)$ is invertible at $(a_0,b_0,c_0)$. The implicit function theorem therefore gives a neighborhood $I$ of $c_0$ and a continuously differentiable function
$$
\phi(c)=(\phi_1(c),\phi_2(c))
$$
with
$$
G(\phi(c),c)=0.
$$
Equivalently,
$$
F(\phi(c),c)=x_0.
$$

:::

:::

::: {.pf-step #s1-3}

There exists $\varepsilon>0$ such that
$$
(c_0-\varepsilon,c_0+\varepsilon)\subseteq I.
$$


::: pf-proof

The set $I$ is an open neighborhood of $c_0$, so it contains some open interval centered at $c_0$.

:::

:::

::: {.pf-step #s1-4}

Define
$$
\gamma:(-\varepsilon,\varepsilon)\to\RR^3
$$
by
$$
\gamma(t)=\bigl(\phi_1(c_0+t),\phi_2(c_0+t),c_0+t\bigr).
$$
Then $\gamma$ is continuously differentiable and
$$
F(\gamma(t))=x_0
$$
for every $t\in(-\varepsilon,\varepsilon)$.


::: pf-proof

The map $\phi$ is continuously differentiable by step [](#s1-2){.pf-ref}, so $\gamma$ is continuously differentiable. By step [](#s1-3){.pf-ref}, $c_0+t\in I$ for every $\abs{t}<\varepsilon$. Step [](#s1-2){.pf-ref} therefore gives
$$
F(\gamma(t))
=
F(\phi(c_0+t),c_0+t)
=
x_0.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\gamma'(0)\ne0.
$$


::: pf-proof

Differentiating the formula in step [](#s1-4){.pf-ref} gives
$$
\gamma'(0)
=
\bigl(\phi_1'(c_0),\phi_2'(c_0),1\bigr).
$$
Its third coordinate is $1$, so the vector is nonzero.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} constructs the required continuously differentiable curve in the level set $F^{-1}(x_0)$, and step [](#s1-5){.pf-ref} proves that it is nonconstant to first order at $0$.

:::

:::

:::
