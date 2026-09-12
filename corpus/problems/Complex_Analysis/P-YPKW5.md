---
schema: qual/card@1
id: P-YPKW5
kind: problem
title: 'Real differentiability: definition, partials without differentiability, and
  real but nowhere complex differentiability'
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Cauchy-Riemann
  - Counterexamples
relations: []
review: draft
---

::: problem
a.  
Complete this definition: "$f: \RR^n\to \RR^m$ is real-differentiable a point $p\in \RR^n$ iff there exists a linear transformation..."

b.
Give an example of a function $f:\RR^2\to \RR$ whose first-order partial derivatives exist everywhere but $f$ is not differentiable at $(0, 0)$.

c.
Give an example of a function $f: \RR^2 \to \RR$ which is real-differentiable everywhere but nowhere complex-differentiable.
:::

::: solution
**(a)** A map $f:\mathbb R^n\to\mathbb R^m$ is differentiable at $p$ if there
exists a linear map $L:\mathbb R^n\to\mathbb R^m$ such that
\[
\lim_{h\to0}
\frac{\|f(p+h)-f(p)-Lh\|}{\|h\|}=0.
\]
The map $L$, necessarily unique, is the derivative $Df(p)$.

**(b)** Define
\[
f(x,y)=
\begin{cases}
\dfrac{x^3}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
\]
Away from the origin it is smooth. At $(0,0)$,
\[
f_x(0,0)=1,
\qquad
f_y(0,0)=0.
\]
If $f$ were differentiable there, its derivative would be $L(x,y)=x$. Along
$y=x$,
\[
f(x,x)-L(x,x)=\frac{x}{2}-x=-\frac{x}{2},
\]
whose absolute value divided by $\sqrt2|x|$ does not tend to $0$. Hence $f$ is
not differentiable at the origin although both first partial derivatives exist
everywhere.

**(c)** Identify $\mathbb R^2$ with $\mathbb C$ and $\mathbb R$ with the real
axis in $\mathbb C$. The function
\[
f(x,y)=x=\Re z
\]
is real-linear, hence real-differentiable everywhere. Its real and imaginary
parts are $u(x,y)=x$ and $v(x,y)=0$, so the Cauchy--Riemann equation
$u_x=v_y$ would require $1=0$. Thus it is nowhere complex-differentiable.
:::
