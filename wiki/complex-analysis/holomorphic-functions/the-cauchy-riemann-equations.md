---
title: The Cauchy--Riemann equations
order: 20
topics:
- Cauchy-Riemann
- Partial Derivatives
---

# The Cauchy--Riemann equations

The [[PR-37QA5|Cauchy--Riemann equations]] are the real form of complex differentiability: they turn one complex derivative into a pair of real first-order equations on $u=\Re f$ and $v=\Im f$.

[[D-V6UQJ]]

[[D-E7A5W]]

[[D-KLTBZ]]

[[PR-37QA5]]

## Polar form

::: {.proposition}
Let $f=u+iv$ be real differentiable on an open set and write $z=re^{i\theta}$ with $r>0$.
Then $f$ satisfies the Cauchy--Riemann equations at $z$ if and only if
$$
\frac{\partial u}{\partial r}=\frac1r\frac{\partial v}{\partial \theta},
\qquad
\frac1r\frac{\partial u}{\partial \theta}=-\frac{\partial v}{\partial r}.
$$
This is the computation of [@SS03, ch. 1, Exercise 9].
:::

[[E-SS1.EX-9]]

## Wirtinger derivatives

[[D-OAFF5]]

[[PR-TVPCM]]

::: {.remark title="Computing with Wirtinger derivatives"}
For a constant $c$, $\overline{\delbar f(z)} = \del \overline f(z)$, and the basic differentials are $d(cz) = c\dz$ and $d(c\bar z) = c\dzbar$.
For example,
$$
\del \abs z^2 = \del (z\bar z) = \bar z, \qquad \delbar \abs z^2 = z, \qquad d\qty{\abs z^2} = \bar z \dz + z\dzbar
,$$
and
$$
\del \exp\qty{-\abs z^2} = \del \exp\qty{-z\bar z} = e^{-\abs z^2}\cdot\del(-z\bar z) = -\bar z e^{-\abs z^2}
.$$

:::

::: {.remark title="The Jacobian is $\abs{f'}^2$"}
A holomorphic $f=u+iv$ is real differentiable as a map $\RR^2\to\RR^2$, with Jacobian determinant $\det J_f(z)=\abs{f'(z)}^2$; so it scales area infinitesimally by $\abs{f'}^2$ and is orientation preserving wherever $f'\neq0$ [@SS03, ch. 1, Proposition 2.3].
:::

## Solving real integrals with complex calculus

::: {.example title="An integral by real parts"}
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
[[P-AZOFF-E03]]
[[E-WKY7C]]
[[E-UVNVV]]
