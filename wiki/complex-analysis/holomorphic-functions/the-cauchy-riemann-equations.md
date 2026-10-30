---
title: The Cauchy--Riemann equations
order: 20
topics:
- Cauchy-Riemann
- Cauchy-Riemann Equations
- Partial Derivatives
---

# The Cauchy--Riemann equations

A map $f = u + iv$ that is real differentiable at $z_0$, regarded as a map $\RR^2\to\RR^2$, is complex differentiable at $z_0$ if and only if $u_x = v_y$ and $u_y = -v_x$ at $z_0$.

[[D-V6UQJ]]

[[D-E7A5W]]

[[D-KLTBZ]]

[[PR-37QA5]]

## Polar form

[[E-SS1.EX-9]]

The polar form applies directly to functions given in terms of $r$ and $\theta$.

## Wirtinger derivatives

In terms of the Wirtinger derivatives $\del$ and $\delbar$, the Cauchy--Riemann equations are the single equation $\delbar f = 0$.

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

[[E-BGKED]]
[[E-THK2Z]]
[[E-FXYTL]]
[[E-WKY7C]]
[[E-UVNVV]]
