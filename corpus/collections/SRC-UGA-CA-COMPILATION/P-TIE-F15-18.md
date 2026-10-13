---
schema: qual/card@1
id: P-TIE-F15-18
kind: problem
title: Area of the image of an annulus under a univalent Laurent series
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 18.
---

::: {.problem}
Let $f ( z ) = \sum _ { n = - \infty } ^ { \infty } c _ { n } z ^ { n }$ be analytic and one-to-one in $r _ { 0 } < | z | < R _ { 0 }$ . For $r _ { 0 } < r < R < R _ { 0 }$ , let $D ( r , R )$ be the annulus $r < | z | < R$ . Show that the area of $f ( D ( r , R ) )$ is finite and is given by

$$
S = \pi \sum _ { n = - \infty } ^ { \infty } n | c _ { n } | ^ { 2 } ( R ^ { 2 n } - r ^ { 2 n } ) .
$$
:::

::: {.solution}
Write
$$
A(r,R)\coloneqq\{z:r<\abs{z}<R\}.
$$

<1>1. The derivative $f'(z)$ is nonzero throughout $A(r,R)$.

::: {.proof}
If $f'(z_0)=0$, then the local power-series expansion of the nonconstant holomorphic function $f-f(z_0)$ has a zero of order at least $2$ at $z_0$. The local mapping theorem would then make $f$ at least two-to-one near $z_0$, contradicting the assumed injectivity. Hence $f'(z)\ne0$.
:::

<1>2. The area $S$ of $f(A(r,R))$ is
$$
S
=
\int_{A(r,R)}\abs{f'(z)}^2\,dA(z).
$$

::: {.proof}
For a holomorphic function $f=u+iv$, the real Jacobian is
$$
J_f
=
u_xv_y-u_yv_x
=
u_x^2+u_y^2
=
\abs{f'(z)}^2
$$
by the Cauchy--Riemann equations. Step <1>1 gives local invertibility, and global injectivity gives multiplicity one. The change-of-variables formula therefore yields
$$
\operatorname{area}(f(A(r,R)))
=
\int_{A(r,R)}J_f\,dA
=
\int_{A(r,R)}\abs{f'(z)}^2\,dA.
$$
:::

<1>3. For every $\rho$ with $r\le\rho\le R$,
$$
\frac1{2\pi}
\int_0^{2\pi}
\abs{f'(\rho e^{i\theta})}^2\,d\theta
=
\sum_{n=-\infty}^{\infty}
n^2\abs{c_n}^2\rho^{2n-2}.
$$

::: {.proof}
The Laurent series of $f$ and its termwise derivative
$$
f'(z)
=
\sum_{n=-\infty}^{\infty}
n c_n z^{n-1}
$$
converge uniformly on the compact annulus $r\le\abs{z}\le R$. For finite Laurent partial sums, orthogonality gives
$$
\frac1{2\pi}
\int_0^{2\pi}
\left|
\sum_{n=-N}^{N}
n c_n\rho^{n-1}e^{i(n-1)\theta}
\right|^2d\theta
=
\sum_{n=-N}^{N}
n^2\abs{c_n}^2\rho^{2n-2}.
$$
Uniform convergence of the derivative series on the compact annulus permits passage to the limit, proving the identity.
:::

<1>4. The area is
$$
\boxed{
S
=
\pi
\sum_{n=-\infty}^{\infty}
n\abs{c_n}^2
\left(R^{2n}-r^{2n}\right).
}
$$

::: {.proof}
By steps <1>2 and <1>3 and polar coordinates,
$$
\begin{aligned}
S
&=
\int_r^R\int_0^{2\pi}
\abs{f'(\rho e^{i\theta})}^2
\rho\,d\theta\,d\rho\\
&=
2\pi
\int_r^R
\sum_{n=-\infty}^{\infty}
n^2\abs{c_n}^2\rho^{2n-1}\,d\rho.
\end{aligned}
$$
The summands are nonnegative, so Tonelli's theorem permits interchange of sum and integral. The $n=0$ term is identically $0$. For $n\ne0$,
$$
\int_r^R\rho^{2n-1}\,d\rho
=
\frac{R^{2n}-r^{2n}}{2n}.
$$
Therefore
$$
\begin{aligned}
S
&=
2\pi
\sum_{n\ne0}
n^2\abs{c_n}^2
\frac{R^{2n}-r^{2n}}{2n}\\
&=
\pi
\sum_{n\ne0}
n\abs{c_n}^2
\left(R^{2n}-r^{2n}\right).
\end{aligned}
$$
Adding the zero $n=0$ term gives the displayed formula.
:::

<1>5. Every term in the series in step <1>4 is nonnegative.

::: {.proof}
For $n>0$,
$$
R^{2n}-r^{2n}>0,
$$
so the product with $n$ is positive. For $n<0$,
$$
R^{2n}-r^{2n}<0,
$$
and multiplying by the negative integer $n$ again gives a positive number.
:::

<1>6. The area $S$ is finite.

::: {.proof}
The derivative $f'$ is continuous on the compact annulus
$$
\{z:r\le\abs{z}\le R\},
$$
so it is bounded there. Hence
$$
\int_{A(r,R)}\abs{f'(z)}^2\,dA<\infty.
$$
By step <1>2, this integral is exactly $S$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>4 proves the stated area formula, and step <1>6 proves finiteness.
:::
:::
