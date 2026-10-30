---
schema: qual/card@1
id: P-TIE-F15-17
kind: problem
title: Area of the image of a disk under a univalent function
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 17.
---

::: {.problem}
Let $f(z) = \sum_{n=0}^{\infty} c_{n}z^{n}$ be analytic and one-to-one in $\abs{z} < 1$. For $0 < r < 1$, let $D_{r}$ be the disk $\abs{z} < r$. Show that the area of $f(D_{r})$ is finite and is given by
$$
S = \pi\sum_{n=1}^{\infty} n\abs{c_{n}}^{2}r^{2n}.
$$

(Note that in general the area of $f(D_{1})$ is infinite.)
:::

::: {.solution}

Fix $0<r<1$ and write
$$
D_r\coloneqq\{z:\abs{z}<r\}.
$$

::: pf

::: {.pf-step #s1-1}

The derivative $f'(z)$ is nonzero for every $z\in D_r$.


::: pf-proof

Suppose $f'(z_0)=0$. Since $f$ is nonconstant and holomorphic, there is an integer $m\ge2$ and a holomorphic function $h$ with $h(z_0)\ne0$ such that
$$
f(z)-f(z_0)
=
(z-z_0)^m h(z)
$$
near $z_0$. The local mapping theorem then implies that nearby values of $f$ have $m$ preimages near $z_0$, contradicting injectivity. Hence $f'(z)\ne0$.

:::

:::

::: {.pf-step #s1-2}

The area $S$ of $f(D_r)$ satisfies
$$
S
=
\int_{D_r}\abs{f'(z)}^2\,dA(z).
$$


::: pf-proof

Write $f=u+iv$. The real Jacobian determinant of the map
$$
(x,y)\longmapsto(u(x,y),v(x,y))
$$
is
$$
J_f
=
u_xv_y-u_yv_x.
$$
By the Cauchy--Riemann equations,
$$
v_y=u_x,
\qquad
v_x=-u_y,
$$
so
$$
J_f
=
u_x^2+u_y^2
=
\abs{f'(z)}^2.
$$
By step [](#s1-1){.pf-ref} and the inverse function theorem, $f$ is locally a $C^1$ diffeomorphism; by the assumed global injectivity on $D_r$, the change-of-variables formula has multiplicity one. Therefore
$$
\operatorname{area}(f(D_r))
=
\int_{D_r}J_f\,dA
=
\int_{D_r}\abs{f'(z)}^2\,dA.
$$

:::

:::

::: {.pf-step #s1-3}

For every $0\le\rho\le r$,
$$
\frac1{2\pi}
\int_0^{2\pi}
\abs{f'(\rho e^{i\theta})}^2\,d\theta
=
\sum_{n=1}^{\infty}
n^2\abs{c_n}^2\rho^{2n-2}.
$$


::: pf-proof

Choose $s$ with $r<s<1$. The differentiated power series
$$
f'(z)
=
\sum_{n=1}^{\infty}n c_n z^{n-1}
$$
converges uniformly on $\abs{z}\le r$. For its $N$th partial sum,
$$
P_N(\rho e^{i\theta})
=
\sum_{n=1}^{N}
n c_n\rho^{n-1}e^{i(n-1)\theta}.
$$
Orthogonality of the exponential functions gives
$$
\frac1{2\pi}
\int_0^{2\pi}
\abs{P_N(\rho e^{i\theta})}^2\,d\theta
=
\sum_{n=1}^{N}
n^2\abs{c_n}^2\rho^{2n-2}.
$$
The uniform convergence $P_N\to f'$ on $\abs{z}\le r$ implies uniform convergence of the squared moduli on each circle, so letting $N\to\infty$ yields the identity.

:::

:::

::: {.pf-step #s1-4}

The area of $f(D_r)$ is
$$
\boxed{
S
=
\pi\sum_{n=1}^{\infty}
n\abs{c_n}^2r^{2n}.
}
$$


::: pf-proof

Using polar coordinates in step [](#s1-2){.pf-ref} and then step [](#s1-3){.pf-ref},
$$
\begin{aligned}
S
&=
\int_0^r\int_0^{2\pi}
\abs{f'(\rho e^{i\theta})}^2
\rho\,d\theta\,d\rho\\
&=
2\pi
\int_0^r
\sum_{n=1}^{\infty}
n^2\abs{c_n}^2\rho^{2n-2}
\rho\,d\rho.
\end{aligned}
$$
The summands are nonnegative, so Tonelli's theorem permits interchange of the sum and integral:
$$
\begin{aligned}
S
&=
2\pi
\sum_{n=1}^{\infty}
n^2\abs{c_n}^2
\int_0^r\rho^{2n-1}\,d\rho\\
&=
2\pi
\sum_{n=1}^{\infty}
n^2\abs{c_n}^2
\frac{r^{2n}}{2n}\\
&=
\pi
\sum_{n=1}^{\infty}
n\abs{c_n}^2r^{2n}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

The area is finite for every $r<1$.


::: pf-proof

Since $f'$ is continuous on the compact closed disk $\abs{z}\le r$, it is bounded there. Hence
$$
\int_{D_r}\abs{f'(z)}^2\,dA<\infty.
$$
By step [](#s1-2){.pf-ref}, this integral is exactly the area $S$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the stated formula, and step [](#s1-5){.pf-ref} gives finiteness.

:::

:::

:::

::: {.remark}
The area of $f(D_1)$ can be infinite: for the Koebe function $z/(1-z)^2=\sum_n nz^n$, the image of the unit disk is $\CC$ minus a ray.
:::
