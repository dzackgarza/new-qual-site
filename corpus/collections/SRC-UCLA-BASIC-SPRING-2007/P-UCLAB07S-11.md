---
schema: qual/card@1
id: P-UCLAB07S-11
kind: problem
title: Implicit function theorem at and beyond its hypotheses
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
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
<1>1. Consider
\[
u^3+xv-y=0,\qquad v^3+yu-x=0.
\]
Can these equations be solved uniquely for $u,v$ as functions of $x,y$ near
\[
(x,y,u,v)=(0,1,1,-1)?
\]
Explain your answer.

<1>2. Give an example in which the conclusion of the implicit function theorem is true although its standard nondegeneracy hypothesis fails.
:::

::: {.solution}
For part <1>1, define
\[
F:\mathbb R^4\to\mathbb R^2
\]
by
\[
F(x,y,u,v)
=
\begin{pmatrix}
u^3+xv-y\\
v^3+yu-x
\end{pmatrix}.
\]

<1>1. The point
\[
(x,y,u,v)=(0,1,1,-1)
\]
satisfies
\[
F(0,1,1,-1)=0.
\]

::: {.proof}
The first component is
\[
1^3+0\cdot(-1)-1
=
0.
\]
The second component is
\[
(-1)^3+1\cdot1-0
=
-1+1
=0.
\]
:::

<1>2. The Jacobian matrix of $F$ with respect to the variables $(u,v)$ is
\[
D_{(u,v)}F
=
\begin{pmatrix}
3u^2&x\\
y&3v^2
\end{pmatrix}.
\]

::: {.proof}
Differentiate the first component
\[
u^3+xv-y
\]
with respect to $u$ and $v$ to obtain
\[
3u^2
\quad\text{and}\quad
x.
\]
Differentiate the second component
\[
v^3+yu-x
\]
with respect to $u$ and $v$ to obtain
\[
y
\quad\text{and}\quad
3v^2.
\]
:::

<1>3. At the point $(0,1,1,-1)$,
\[
D_{(u,v)}F(0,1,1,-1)
=
\begin{pmatrix}
3&0\\
1&3
\end{pmatrix}
\]
and
\[
\det D_{(u,v)}F(0,1,1,-1)=9\ne0.
\]

::: {.proof}
Substitute
\[
x=0,\quad y=1,\quad u=1,\quad v=-1
\]
into the matrix from step <1>2.
Its determinant is
\[
3\cdot3-0\cdot1=9.
\]
:::

<1>4. The equations can be solved uniquely for $u,v$ as continuously differentiable functions of $x,y$ near $(0,1)$.

::: {.proof}
The map $F$ is polynomial, hence $C^1$.
By step <1>1,
\[
F(0,1,1,-1)=0,
\]
and by step <1>3 the derivative with respect to the dependent variables $(u,v)$ is invertible.
The implicit function theorem therefore gives neighborhoods
\[
N\subseteq\mathbb R^2
\]
of $(0,1)$ and
\[
M\subseteq\mathbb R^2
\]
of $(1,-1)$, together with a unique $C^1$ map
\[
\phi:N\to M,
\qquad
\phi(x,y)=(u(x,y),v(x,y)),
\]
such that
\[
F(x,y,u(x,y),v(x,y))=0
\]
for all $(x,y)\in N$.
Thus the answer to part <1>1 is yes.
:::

<1>5. For part <1>2, consider the scalar equation
\[
G(x,y)=y^3-x^3=0
\]
near
\[
(x,y)=(0,0).
\]

::: {.proof}
The function
\[
G:\mathbb R^2\to\mathbb R
\]
is smooth and satisfies
\[
G(0,0)=0.
\]
:::

<1>6. Near $(0,0)$, the equation
\[
G(x,y)=0
\]
has the unique solution
\[
\boxed{y=x}.
\]

::: {.proof}
Over the real numbers,
\[
y^3=x^3
\]
if and only if
\[
y=x,
\]
because the function
\[
t\mapsto t^3
\]
is injective on $\mathbb R$.
Thus for every $x$, in particular for every $x$ near $0$, there is exactly one solution
\[
y=x.
\]
The resulting function
\[
y(x)=x
\]
is smooth.
:::

<1>7. The standard nondegeneracy hypothesis of the implicit function theorem fails at $(0,0)$.

::: {.proof}
The derivative with respect to the dependent variable $y$ is
\[
G_y(x,y)=3y^2.
\]
At the base point,
\[
G_y(0,0)=0.
\]
For a scalar implicit equation, the usual hypothesis requires
\[
G_y(0,0)\ne0.
\]
Thus the hypothesis fails even though the conclusion in step <1>6 holds.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 answers part <1>1 affirmatively by the implicit function theorem.
Steps <1>5--<1>7 give the requested example for part <1>2.
:::
:::
