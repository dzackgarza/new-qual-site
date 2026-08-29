---
title: The Cauchy-Riemann equations
order: 20
---

# The Cauchy–Riemann equations

The condition that a real-differentiable map $\RR^2 \to \RR^2$ is complex differentiable.

[[D-V6UQJ]]

[[D-E7A5W]]

[[D-KLTBZ]]

[[PR-37QA5]]

[[PR-OOHUL]]

## Polar form

:::{.proof}
Setting
\[
z = re^{i\theta} = r(\cos\theta + i\sin\theta ) = x+iy
\]
gives $x=r\cos\theta$, $y=r\sin\theta$, so
\[
x_r = \cos(\theta)&, x_\theta = -r\sin(\theta) \\
y_r = \sin(\theta)&, y_\theta = r\cos(\theta)
.\]

By the chain rule,
\[
u_r
&= u_x x_r + u_y y_r \\
&= v_y x_r -v_x y_r && \text{CR}\\
&= v_y \cos(\theta) - v_x \sin(\theta) \\
&= {1\over r}\qty{ v_y r\cos(\theta) - v_x r\sin(\theta) } \\
&= {1\over r}\qty { v_y y_\theta + v_x x_\theta} \\
&= {1\over r} v_\theta
,\]
and similarly
\[
v_r
&= v_x x_r + v_y y_r \\
&= v_x \cos(\theta) + v_y\sin(\theta) \\
&= -u_y\cos(\theta) + u_x\sin(\theta) && \text{CR} \\
&= -{1\over r} u_\theta
.\]
Thus
\[
\frac{\partial u}{\partial r}=\frac{1}{r} \frac{\partial v}{\partial \theta} \quad \text { and } \quad \frac{\partial v}{\partial r}=-\frac{1}{r} \frac{\partial u}{\partial \theta}
.\]

:::

Use the polar form on anything stated in $r$ and $\theta$; converting to $x$ and $y$ first is the usual way these computations become unpleasant.

[[PR-EMFAN]]

## Wirtinger derivatives

The equations collapse to one when written in $\del$ and $\delbar$: holomorphic means $\delbar f = 0$, that is, $f$ does not depend on $\bar z$.

[[D-OAFF5]]

[[PR-TVPCM]]

:::{.remark title="Computing with them"}
$\overline{\delbar f(z)} = \del \overline f(z)$, and the basic differentials are $d(cz) = c\dz$ and $d(c\bar z) = c\dzbar$.
Two computations that come up:
\[
\del \abs z^2 = \del (z\bar z) = \bar z, \qquad \delbar \abs z^2 = z, \qquad d\qty{\abs z^2} = \bar z \dz + z\dzbar
,\]
and
\[
\del \exp\qty{-\abs z^2} = \del \exp\qty{-z\bar z} = e^{-\abs z^2}\cdot\del(z\bar z) = \bar z e^{-\abs z^2}
.\]

:::

## Derivatives, and what they are the same as

:::{.fact}
For a holomorphic $f$,
\[
f' = \dd{f}{z} = {1\over i}\dd{f}{y} = \dd{f}{x} = \dd u x + i \dd v x
.\]

:::

:::{.fact title="Differentials"}
\[
dz &= dx + i~dy \\
d\bar z &= dx - i~dy \\
f_z &= f_x = f_y / i
.\]

:::

:::{.remark title="The Jacobian is $\abs{f'}^2$"}
Regarding $f$ as a map $\RR^2\to\RR^2$ with $f(x+iy) = u+iv$, the Jacobian determinant is
\[
J = u_xv_y -v_x u_y = u_x^2 + v_x^2
\]
after applying CR, and on the other hand $\abs{f'(z)}^2 = \abs{u_x + iv_x}^2 = J$.
So a holomorphic map scales area by $\abs{f'}^2$ and is orientation preserving wherever $f'\neq 0$, which is the analytic content of conformality.

:::

[[PR-Y36BS]]

:::{.proof title="Holomorphic iff linear approximation"}
If $f'(z_0)$ exists, set $a\da f'(z_0)$ and
\[
\psi(h)
\da
\begin{cases}
\dfrac{f(z_0+h)-f(z_0)}{h}-a & h\neq 0,\\
0 & h=0.
\end{cases}
\]
Then $\psi(h)\to 0$ as $h\to 0$ by definition of $f'(z_0)$, and $f(z_0+h)-f(z_0)-ah = h\psi(h)$.

Conversely, if such $a$ and $\psi$ exist then for $h\neq 0$
\[
\frac{f(z_0+h)-f(z_0)}{h}
= a + \psi(h)
\to a
,\]
so $f'(z_0)=a$.
Continuity at $z_0$ is the same identity: $f(z_0+h)=f(z_0)+h\bigl(a+\psi(h)\bigr)\to f(z_0)$.

:::

## Solving real integrals with complex calculus

:::{.remark}
$e^z$ is entire, so ordinary calculus with it is legal and often shorter:
\[
\int e^{3x}\cos(2x) \dx
&= \Re \int e^{3z}e^{2iz}\dz \\
&= \Re \int e^{(3+2i)z} \dz \\
&= \Re {e^{(3+2i)z} \over 3+2i} + C
.\]

:::

## Exercises

[[E-BGKED]] [[E-PAQPF]]
[[E-6F2HU]]
[[E-FXYTL]]
[[E-WKY7C]]
[[E-UVNVV]]
