---
schema: qual/card@1
id: P-UCLAB06S-04
kind: problem
title: Implicit function theorem for $x^2y^3+x^3z+2yz^4=4$ at $(1,1,1)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 4 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
The point $P = (1, 1, 1)$ lies on the surface $S$ in $\RR^3$ defined by

$$
x^2 y^3 + x^3 z + 2 y z^4 = 4.
$$

Prove that there exists a differentiable function $f(x, y)$ defined in an open neighborhood $N$ of $(1, 1)$ in $\RR^2$ such that $f(1, 1) = 1$ and $(x, y, f(x, y))$ lies in $S$ for all $(x, y) \in N$.
:::

::: {.solution}

Define
$$
G(x,y,z)
=
x^2y^3+x^3z+2yz^4-4.
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
1^2\cdot1^3+1^3\cdot1+2\cdot1\cdot1^4-4
=
1+1+2-4
=0.
$$

:::

:::

::: {.pf-step #s1-2}

The partial derivative of $G$ with respect to $z$ is
$$
G_z(x,y,z)
=
x^3+8yz^3.
$$


::: pf-proof

Differentiate the polynomial term by term with respect to $z$:
$$
\frac{\partial}{\partial z}(x^2y^3)=0,
$$
$$
\frac{\partial}{\partial z}(x^3z)=x^3,
$$
and
$$
\frac{\partial}{\partial z}(2yz^4)=8yz^3.
$$

:::

:::

::: {.pf-step #s1-3}

At the point $(1,1,1)$,
$$
\boxed{G_z(1,1,1)=9\ne0}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
G_z(1,1,1)
=
1^3+8\cdot1\cdot1^3
=
1+8
=9.
$$

:::

:::

::: {.pf-step #s1-4}

The function $G$ is continuously differentiable near $(1,1,1)$.


::: pf-proof

The function $G$ is a polynomial in $(x,y,z)$.
Hence it is smooth, in particular $C^1$, on all of $\RR^3$.

:::

:::

::: {.pf-step #s1-5}

There exist open neighborhoods
$$
N\subseteq\RR^2
$$
of $(1,1)$ and
$$
J\subseteq\RR
$$
of $1$, together with a continuously differentiable function
$$
f:N\to J
$$
such that
$$
f(1,1)=1
$$
and
$$
G(x,y,f(x,y))=0
$$
for every $(x,y)\in N$.


::: pf-proof

Apply the implicit function theorem to
$$
G:\RR^2\times\RR\to\RR
$$
at the point
$$
((1,1),1).
$$
The hypotheses are satisfied:
$$
G(1,1,1)=0
$$
by step [](#s1-1){.pf-ref},
$$
G
$$
is $C^1$ by step [](#s1-4){.pf-ref}, and the derivative with respect to the dependent variable $z$ is invertible as a linear map
$$
\RR\to\RR
$$
because
$$
G_z(1,1,1)=9\ne0
$$
by step [](#s1-3){.pf-ref}.
Therefore the implicit function theorem gives the stated neighborhoods and function.

:::

:::

::: {.pf-step #s1-6}

For every $(x,y)\in N$,
$$
\boxed{(x,y,f(x,y))\in S}.
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
G(x,y,f(x,y))=0.
$$
Since
$$
S=G^{-1}(0),
$$
this is exactly the condition that
$$
(x,y,f(x,y))\in S.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the differentiable function with
$$
f(1,1)=1,
$$
and step [](#s1-6){.pf-ref} proves that its graph lies on the surface $S$ near $(1,1,1)$.

:::

:::

:::
