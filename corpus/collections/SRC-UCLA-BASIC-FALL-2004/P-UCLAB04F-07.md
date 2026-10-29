---
schema: qual/card@1
id: P-UCLAB04F-07
kind: problem
title: Applying the implicit function theorem to an explicit surface
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the official UCLA Basic Exam Fall 2004 PDF; the scan confirms the defining equation $x^4y^2+x^2z+yz^2=3$.
---

::: {.problem}
The point $P=(1,1,1)$ belongs to the set $S\subset\RR^3$ defined by
$$
x^4y^2+x^2z+yz^2=3.
$$
Explain carefully how the Implicit Function Theorem implies, in this case, that there exists a differentiable function $f(x,y)$ such that
$$
(x,y,f(x,y))\in S
$$
for every $(x,y)$ in some small open set containing $(1,1)$.
:::

::: {.solution}

Define
$$
G(x,y,z)=x^4y^2+x^2z+yz^2-3.
$$
Then
$$
S=G^{-1}(0).
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
G(1,1,1)=0.
$$


::: pf-proof

Direct substitution gives
$$
G(1,1,1)
=
1^4\cdot1^2+1^2\cdot1+1\cdot1^2-3
=
1+1+1-3
=0.
$$
Thus $(1,1,1)\in S$.

:::

:::

::: {.pf-step #s1-2}

The partial derivative of $G$ with respect to $z$ is
$$
\frac{\partial G}{\partial z}(x,y,z)
=
x^2+2yz,
$$
and
$$
\frac{\partial G}{\partial z}(1,1,1)=3\ne0.
$$


::: pf-proof

Differentiate the polynomial $G$ with respect to $z$. Evaluating at $(1,1,1)$ gives
$$
1+2=3.
$$

:::

:::

::: {.pf-step #s1-3}

There are open neighborhoods
$$
W\subseteq\RR^2
\quad\text{of }(1,1)
$$
and
$$
J\subseteq\RR
\quad\text{of }1,
$$
and a differentiable function
$$
f:W\to J
$$
such that
$$
f(1,1)=1
$$
and
$$
G(x,y,f(x,y))=0
$$
for every $(x,y)\in W$.


::: pf-proof

The map $G:\RR^3\to\RR$ is continuously differentiable because it is a polynomial. By step [](#s1-1){.pf-ref},
$$
G(1,1,1)=0,
$$
and by step [](#s1-2){.pf-ref} the derivative with respect to the variable $z$ is nonzero at that point. The Implicit Function Theorem therefore applies with $(x,y)$ as the free variables and $z$ as the dependent variable, giving the stated neighborhoods and function.

:::

:::

::: {.pf-step #s1-4}

For every $(x,y)\in W$,
$$
(x,y,f(x,y))\in S.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
G(x,y,f(x,y))=0.
$$
Since $S=G^{-1}(0)$, this is exactly the statement that
$$
(x,y,f(x,y))\in S.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required differentiable local graph of $S$ over an open neighborhood of $(1,1)$.

:::

:::

:::
