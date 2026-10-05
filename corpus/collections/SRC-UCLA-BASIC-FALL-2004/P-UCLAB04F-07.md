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
The point $P=(1,1,1)$ belongs to the set $S\subset\mathbb R^3$ defined by
\[
x^4y^2+x^2z+yz^2=3.
\]
Explain carefully how the Implicit Function Theorem implies, in this case, that there exists a differentiable function $f(x,y)$ such that
\[
(x,y,f(x,y))\in S
\]
for every $(x,y)$ in some small open set containing $(1,1)$.
:::

::: {.solution}
Define
\[
G(x,y,z)=x^4y^2+x^2z+yz^2-3.
\]
Then
\[
S=G^{-1}(0).
\]

<1>1. One has
\[
G(1,1,1)=0.
\]

::: {.proof}
Direct substitution gives
\[
G(1,1,1)
=
1^4\cdot1^2+1^2\cdot1+1\cdot1^2-3
=
1+1+1-3
=0.
\]
Thus $(1,1,1)\in S$.
:::

<1>2. The partial derivative of $G$ with respect to $z$ is
\[
\frac{\partial G}{\partial z}(x,y,z)
=
x^2+2yz,
\]
and
\[
\frac{\partial G}{\partial z}(1,1,1)=3\ne0.
\]

::: {.proof}
Differentiate the polynomial $G$ with respect to $z$. Evaluating at $(1,1,1)$ gives
\[
1+2=3.
\]
:::

<1>3. There are open neighborhoods
\[
W\subseteq\mathbb R^2
\quad\text{of }(1,1)
\]
and
\[
J\subseteq\mathbb R
\quad\text{of }1,
\]
and a differentiable function
\[
f:W\to J
\]
such that
\[
f(1,1)=1
\]
and
\[
G(x,y,f(x,y))=0
\]
for every $(x,y)\in W$.

::: {.proof}
The map $G:\mathbb R^3\to\mathbb R$ is continuously differentiable because it is a polynomial. By step <1>1,
\[
G(1,1,1)=0,
\]
and by step <1>2 the derivative with respect to the variable $z$ is nonzero at that point. The Implicit Function Theorem therefore applies with $(x,y)$ as the free variables and $z$ as the dependent variable, giving the stated neighborhoods and function.
:::

<1>4. For every $(x,y)\in W$,
\[
(x,y,f(x,y))\in S.
\]

::: {.proof}
By step <1>3,
\[
G(x,y,f(x,y))=0.
\]
Since $S=G^{-1}(0)$, this is exactly the statement that
\[
(x,y,f(x,y))\in S.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required differentiable local graph of $S$ over an open neighborhood of $(1,1)$.
:::
:::
