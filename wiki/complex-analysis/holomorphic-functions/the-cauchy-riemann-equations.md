---
title: The Cauchy-Riemann equations
order: 20
topics:
- Cauchy-Riemann
- Cauchy-Riemann Equations
- Partial Derivatives
---

# The Cauchy-Riemann equations

A map $f = u + iv$ that is real differentiable at $z_0$, regarded as a map $\RR^2\to\RR^2$, is complex differentiable at $z_0$ if and only if $u_x = v_y$ and $u_y = -v_x$ at $z_0$.

[[D-V6UQJ]]

[[D-E7A5W]]

[[D-KLTBZ]]

[[PR-37QA5]]

## Polar form

[[PR-OOHUL]]

::: {.proof}
Setting
$$
z = re^{i\theta} = r(\cos\theta + i\sin\theta ) = x+iy
$$
gives $x=r\cos\theta$ and $y=r\sin\theta$, so
$$
\begin{aligned}
x_r = \cos(\theta)&, x_\theta = -r\sin(\theta) \\
y_r = \sin(\theta)&, y_\theta = r\cos(\theta)
\end{aligned}.$$

By the chain rule,
$$
\begin{aligned}
u_r
&= u_x x_r + u_y y_r \\
&= v_y x_r -v_x y_r && \text{CR}\\
&= v_y \cos(\theta) - v_x \sin(\theta) \\
&= {1\over r}\qty{ v_y r\cos(\theta) - v_x r\sin(\theta) } \\
&= {1\over r}\qty { v_y y_\theta + v_x x_\theta} \\
&= {1\over r} v_\theta
\end{aligned},$$
and similarly
$$
\begin{aligned}
v_r
&= v_x x_r + v_y y_r \\
&= v_x \cos(\theta) + v_y\sin(\theta) \\
&= -u_y\cos(\theta) + u_x\sin(\theta) && \text{CR} \\
&= -{1\over r} u_\theta
\end{aligned}.$$
Thus
$$
\frac{\partial u}{\partial r}=\frac{1}{r} \frac{\partial v}{\partial \theta} \quad \text { and } \quad \frac{\partial v}{\partial r}=-\frac{1}{r} \frac{\partial u}{\partial \theta}
.$$

:::

The polar form applies directly to functions given in terms of $r$ and $\theta$.

## Wirtinger derivatives

In terms of the Wirtinger derivatives $\del$ and $\delbar$, the Cauchy–Riemann equations are the single equation $\delbar f = 0$.

[[D-OAFF5]]

[[PR-TVPCM]]

::: {.remark title="Computing with Wirtinger derivatives"}
$\overline{\delbar f(z)} = \del \overline f(z)$, and the basic differentials are $d(cz) = c\dz$ and $d(c\bar z) = c\dzbar$.
For example,
$$
\del \abs z^2 = \del (z\bar z) = \bar z, \qquad \delbar \abs z^2 = z, \qquad d\qty{\abs z^2} = \bar z \dz + z\dzbar
,$$
and
$$
\del \exp\qty{-\abs z^2} = \del \exp\qty{-z\bar z} = e^{-\abs z^2}\cdot\del(z\bar z) = \bar z e^{-\abs z^2}
.$$

:::

## Derivatives in coordinates

::: {.fact}
For a holomorphic $f$,
$$
f' = \dd{f}{z} = {1\over i}\dd{f}{y} = \dd{f}{x} = \dd u x + i \dd v x
.$$

:::

::: {.fact title="Differentials"}
$$
\begin{aligned}
dz &= dx + i~dy \\
d\bar z &= dx - i~dy \\
f_z &= f_x = f_y / i
\end{aligned}.$$

:::

::: {.remark title="The Jacobian is $\abs{f'}^2$"}
Regarding $f$ as a map $\RR^2\to\RR^2$ with $f(x+iy) = u+iv$, the Jacobian determinant is
$$
J = u_xv_y -v_x u_y = u_x^2 + v_x^2
$$
after applying CR, and on the other hand $\abs{f'(z)}^2 = \abs{u_x + iv_x}^2 = J$.
So a holomorphic map scales area infinitesimally by $\abs{f'}^2$ and is orientation preserving wherever $f'\neq 0$.

:::

[[PR-Y36BS]]

::: {.proof title="Holomorphic iff linear approximation"}
If $f'(z_0)$ exists, set $a\coloneqq f'(z_0)$ and
$$
\psi(h)
\coloneqq
\begin{cases}
\dfrac{f(z_0+h)-f(z_0)}{h}-a & h\neq 0,\\
0 & h=0.
\end{cases}
$$
Then $\psi(h)\to 0$ as $h\to 0$ by definition of $f'(z_0)$, and $f(z_0+h)-f(z_0)-ah = h\psi(h)$.

Conversely, if such $a$ and $\psi$ exist then for $h\neq 0$
$$
\frac{f(z_0+h)-f(z_0)}{h}
= a + \psi(h)
\to a
,$$
so $f'(z_0)=a$.
Continuity at $z_0$ is the same identity: $f(z_0+h)=f(z_0)+h\bigl(a+\psi(h)\bigr)\to f(z_0)$.

:::

## Solving real integrals with complex calculus

::: {.remark}
Since $e^{(3+2i)z}$ has antiderivative $e^{(3+2i)z}/(3+2i)$, restricting to real $z=x$ and taking real parts evaluates a real integral:
$$
\begin{aligned}
\int e^{3x}\cos(2x) \dx
&= \Re \int e^{3x}e^{2ix}\dx \\
&= \Re \int e^{(3+2i)x} \dx \\
&= \Re {e^{(3+2i)x} \over 3+2i} + C
\end{aligned}.$$

:::

## Exercises

[[E-BGKED]] [[E-PAQPF]]
[[E-6F2HU]]
[[E-FXYTL]]
[[E-WKY7C]]
[[E-UVNVV]]
