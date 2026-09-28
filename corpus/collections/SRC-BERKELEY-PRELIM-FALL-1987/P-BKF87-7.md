---
schema: qual/card@1
id: P-BKF87-7
kind: problem
title: Maximum of the generalized Rayleigh quotient $\langle Ax,x\rangle/\langle Bx,x\rangle$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $A,B$ be real symmetric $n\times n$ matrices, with $B$ positive definite. For $x\ne0$, define
\[
G(x)=\frac{\langle Ax,x\rangle}{\langle Bx,x\rangle}.
\]

1. Show that $G$ attains its maximum value.
2. Show that any maximum point is an eigenvector of a matrix naturally associated to $A$ and $B$, and identify that matrix.
:::

::: {.solution}
<1>1. The function $G$ is continuous on $\RR^n\setminus\{0\}$ and satisfies
$$
G(cx)=G(x)
$$
for every $x\neq0$ and every nonzero real scalar $c$.

::: {.proof}
Since $B$ is positive definite,
$$
\inner{Bx}{x}>0
$$
for every $x\neq0$. Thus the denominator never vanishes on the domain, so $G$ is continuous there.

For $c\neq0$,
$$
\begin{aligned}
G(cx)
&=
\frac{\inner{A(cx)}{cx}}{\inner{B(cx)}{cx}}\\
&=
\frac{c^2\inner{Ax}{x}}{c^2\inner{Bx}{x}}\\
&=
G(x).
\end{aligned}
$$
:::

<1>2. The function $G$ attains a maximum on $\RR^n\setminus\{0\}$.

::: {.proof}
Restrict $G$ to the Euclidean unit sphere
$$
S^{n-1}=\{x\in\RR^n:\norm x=1\}.
$$
This sphere is compact, and step <1>1 shows that $G$ is continuous on it. Hence $G$ attains a maximum there, say at $u\in S^{n-1}$.

For any nonzero $x$, step <1>1 gives
$$
G(x)=G\left(\frac{x}{\norm x}\right).
$$
Thus the maximum on the unit sphere is also the maximum on the entire domain.
:::

<1>3. Let $u\neq0$ be any maximum point and put
$$
\lambda=G(u).
$$
Then
$$
Au=\lambda Bu.
$$

::: {.proof}
Fix any $y\in\RR^n$ and consider
$$
\varphi(t)=G(u+ty)
$$
for $t$ near $0$. Since $u$ is a global maximum point, $t=0$ is a local maximum of $\varphi$, so
$$
\varphi'(0)=0.
$$

Set
$$
N(t)=\inner{A(u+ty)}{u+ty},
\qquad
D(t)=\inner{B(u+ty)}{u+ty}.
$$
Because $A$ and $B$ are symmetric,
$$
N'(0)=2\inner{Au}{y},
\qquad
D'(0)=2\inner{Bu}{y}.
$$
The quotient rule therefore gives
$$
0
=
\varphi'(0)
=
\frac{
2\inner{Au}{y}D(0)
-
2N(0)\inner{Bu}{y}
}{
D(0)^2
}.
$$
Since
$$
\lambda=\frac{N(0)}{D(0)},
$$
this is equivalent to
$$
\inner{Au-\lambda Bu}{y}=0.
$$
As this holds for every $y\in\RR^n$,
$$
Au-\lambda Bu=0.
$$
:::

<1>4. Every maximum point $u$ is an eigenvector of
$$
\boxed{B^{-1}A},
$$
with eigenvalue $G(u)$.

::: {.proof}
Positive definiteness implies that $B$ is invertible: if $Bx=0$, then
$$
\inner{Bx}{x}=0,
$$
so positive definiteness forces $x=0$.

Applying $B^{-1}$ to the identity in step <1>3 gives
$$
B^{-1}Au
=
\lambda u
=
G(u)u.
$$
Since $u\neq0$, it is an eigenvector of $B^{-1}A$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>2 proves existence of a maximum, and step <1>4 identifies the required matrix and eigenvector relation.
:::
:::
