---
schema: qual/card@1
id: E-N6DX3
kind: problem
title: Cauchy–Riemann equations and elementary complex analysis
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
  - Meromorphic Functions
  - Harmonic Functions
relations: []
review: draft
---

::: exercise
- State the Cauchy-Riemann equations.

- Define what it means for a function to be

  - Holomorphic

  - Meromorphic

  - Analytic

  - Harmonic

  - Uniformly continuous

  - Uniformly bounded

  - Entire

- What does it mean for a sequence or series to uniformly converge?

- State the Laplace equation.

- What is the Dirichlet problem?

- Discuss how to carry out partial fraction decomposition

- Determine the radius of convergence of the power series for $\sqrt z$ expanded at $z_0= 4 + 3i$.

- What is the logarithmic derivative?

- Find a  function $f$ such that $f^2$ is analytic on the open unit disc but $f$ is not.

- Show that $f(z)=z^2$ is uniformly continuous on every disk $|z|<R$,
  but is not uniformly continuous on $\CC$.

  - Use that Lipschitz implies uniformly continuous.

- Identify $\RR^2$ with $\CC$ and give a necessary and sufficient condition
  for a real-differentiable function at $(a,b)$ to be complex differentiable
  at $a+ib$.

  - Derivation of CR equations: approach along totally real and totally imaginary paths for $h$.

- Let $f=u+iv$ be complex differentiable with continuous partial derivatives
  at $z=re^{i\theta}$, $r\ne0$. Derive the polar Cauchy--Riemann equations.

  - Polar coordinates, chain rule, Cauchy-Riemann equations.

- Suppose $f(z)=\sum_{n\ge0}a_nz^n$ has radius of convergence exactly $1$.
  Give an example whose series converges at every point of $S^1$; give an
  example for which $f$ is analytic at $1$ but $\sum a_n$ diverges; and prove
  that $f$ cannot be analytic at every point of $S^1$.

  - Converges everywhere on $S^1$: take $\sum z^k/k^2$.

- Find the Laurent expansions of
  \[
  {z+1\over z(z-1)^2}
  \]
  about $z=0$ and $z=1$.
:::

::: solution
The Cartesian Cauchy--Riemann equations for $f=u+iv$ are
\[
u_x=v_y,\qquad u_y=-v_x.
\]
A function on an open set is **holomorphic** if it is complex differentiable
at every point; **meromorphic** if it is holomorphic except for isolated poles;
**analytic** if it is locally represented by a convergent power series
(equivalently, in one complex variable, holomorphic); **harmonic** if it is
$C^2$ and satisfies $u_{xx}+u_{yy}=0$; **entire** if it is holomorphic on all
of $\CC$. Uniform continuity means that for every $\epsilon>0$ there is a
$\delta>0$ working simultaneously for all pairs of points in the domain;
uniform boundedness means that one constant $M$ bounds the modulus everywhere.
A sequence $f_n\to f$ converges uniformly if
$\sup_x|f_n(x)-f(x)|\to0$; a series converges uniformly when its partial sums
do. The Laplace equation is $u_{xx}+u_{yy}=0$. The Dirichlet problem asks for a
harmonic function on a domain with prescribed boundary values.

For partial fractions, factor the denominator over $\CC$ and write one term
$A_{j,k}/(z-a_j)^k$ for every multiplicity $k$ of every pole $a_j$; multiplying
through by the denominator and comparing coefficients (or evaluating
derivatives at the poles) determines the constants.

A local branch of $\sqrt z$ about $z_0=4+3i$ has radius of convergence
\[
\boxed{5}.
\]
Indeed, the open disk of radius $5$ about $z_0$ avoids $0$ and is simply
connected, so it admits a holomorphic square root. A larger Taylor disk would
contain $0$; if a holomorphic $g$ there satisfied $g^2=z$, then $g(0)=0$ and
differentiating would give $2g(0)g'(0)=1$, impossible.

The logarithmic derivative of a nonzero holomorphic function is $f'/f$.
An example with $f^2$ analytic but $f$ not analytic is
\[
f(z)=\begin{cases}1,&\Im z\ge0,\\-1,&\Im z<0,
\end{cases}
\qquad f^2\equiv1.
\]

For $f(z)=z^2$ and $|z|,|w|<R$,
\[
|z^2-w^2|\le2R|z-w|,
\]
so $z^2$ is uniformly continuous on that disk. On $\CC$, take
$z_n=n$ and $w_n=n+1/n$; then $|z_n-w_n|\to0$ but
$|z_n^2-w_n^2|\to2$, so uniform continuity fails.

If a real-differentiable map $f=u+iv$ is given at $(a,b)$, then it is complex
differentiable there exactly when its real derivative is $\CC$-linear,
equivalently exactly when the Cauchy--Riemann equations hold at $(a,b)$.

In polar coordinates, the chain rule gives
\[
u_r=u_x\cos\theta+u_y\sin\theta,
\qquad
v_\theta=r(-v_x\sin\theta+v_y\cos\theta).
\]
Using $u_x=v_y$ and $u_y=-v_x$ yields
\[
u_r={1\over r}v_\theta,
\qquad
v_r=-{1\over r}u_\theta.
\]

For the radius-one power-series questions:

1. $\sum_{n\ge1}z^n/n^2$ has radius $1$ and converges absolutely at every
   point of $S^1$.
2. $f(z)=1/(1+z)=\sum_{n\ge0}(-1)^nz^n$ has radius $1$ and is analytic at
   $1$, but $\sum_{n\ge0}(-1)^n$ diverges.
3. If $f$ were analytic at every point of $S^1$, compactness of $S^1$ would
   give finitely many neighborhoods on which $f$ is analytic, together
   containing an annulus around $S^1$. Joined with the unit disk, these give
   analyticity on a disk $|z|<1+\epsilon$ for some $\epsilon>0$, contradicting
   the assumed Taylor radius $1$.

Finally,
\[
{z+1\over z(z-1)^2}={1\over z}-{1\over z-1}+{2\over(z-1)^2}.
\]
About $0$ this gives
\[
{1\over z}+\sum_{n\ge0}(2n+3)z^n,
\qquad 0<|z|<1,
\]
and
\[
\sum_{n\ge2}(2n-3)z^{-n},
\qquad |z|>1.
\]
Writing $w=z-1$, the expansions about $1$ are
\[
{2\over w^2}-{1\over w}+\sum_{n\ge0}(-1)^nw^n,
\qquad 0<|w|<1,
\]
and
\[
{1\over w^2}+\sum_{n\ge3}(-1)^{n-1}w^{-n},
\qquad |w|>1.
\]
:::
