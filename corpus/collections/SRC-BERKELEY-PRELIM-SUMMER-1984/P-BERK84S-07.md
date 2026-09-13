---
schema: qual/card@1
id: P-BERK84S-07
kind: problem
title: Local inverse of a triangular nonlinear map
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 7 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the Jacobian determinant and the explicit local inverse obtained from the one-variable inverse function theorem.
---

::: {.problem}
Let $f : \mathbb { R } \to \mathbb { R }$ be $C ^ { 1 }$ and let

$$
\begin{array} { l } { u = f ( x ) } \\ { v = - y + x f ( x ) . } \end{array}
$$

If $f ^ { \prime } ( x _ { 0 } ) \neq 0$ , show that this transformation is locally invertible near $( x _ { 0 } , y _ { 0 } )$ and the inverse has the form

$$
\begin{array} { l } { { x = g ( u ) } } \\ { { y = - v + u g ( u ) . } } \end{array}
$$
:::


::: {.solution}
Define
\[
F(x,y)=\bigl(f(x),-y+xf(x)\bigr).
\]
Let
\[
(u_0,v_0)=F(x_0,y_0).
\]

<1>1. The map $F$ is locally invertible at $(x_0,y_0)$.
::: {.proof}
Its derivative is
\[
DF(x,y)=
\begin{pmatrix}
f'(x)&0\\
f(x)+xf'(x)&-1
\end{pmatrix}.
\]
Hence
\[
\det DF(x_0,y_0)=-f'(x_0)\ne0.
\]
By the inverse function theorem, $F$ is a $C^1$ diffeomorphism between neighborhoods of $(x_0,y_0)$ and $(u_0,v_0)$.
:::

<1>2. The local inverse has the required form.
::: {.proof}
Since $f'(x_0)\ne0$, the one-variable inverse function theorem gives neighborhoods of $x_0$ and $u_0=f(x_0)$ on which $f$ has a $C^1$ inverse $g$. Thus from
\[
u=f(x)
\]
we obtain
\[
x=g(u).
\]
The second coordinate equation is
\[
v=-y+xf(x)=-y+xu.
\]
Therefore
\[
y=-v+xu=-v+u\,g(u).
\]
Hence the local inverse is
\[
\boxed{
F^{-1}(u,v)=\bigl(g(u),-v+u\,g(u)\bigr).
}
\]
:::
:::
