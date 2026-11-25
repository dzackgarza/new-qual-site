---
title: The Cauchy--Riemann equations
order: 20
topics:
- Cauchy-Riemann
- Partial Derivatives
---

# The Cauchy--Riemann equations

The [[D-CREQS|Cauchy--Riemann equations]] are the real form of complex differentiability: they turn one complex derivative into a pair of real first-order equations on $u=\Re f$ and $v=\Im f$.

[[D-V6UQJ]]

[[D-E7A5W]]

[[D-KLTBZ]]

[[D-CREQS]]

[[PR-37QA5]]

## Polar form

[[E-SS1.EX-9]]

## Wirtinger derivatives

[[D-OAFF5]]

[[PR-TVPCM]]

Conjugation interchanges the two operators, $\overline{\delbar f}=\del\bar f$, and for a constant $c$ the basic differentials are $d(cz)=c\dz$ and $d(c\bar z)=c\dzbar$.

::: {.example title="Wirtinger derivatives of $\abs z^2$ and of $e^{-\abs z^2}$"}
For example,
$$
\del \abs z^2 = \del (z\bar z) = \bar z, \qquad \delbar \abs z^2 = z, \qquad d\qty{\abs z^2} = \bar z \dz + z\dzbar
,$$
and
$$
\del \exp\qty{-\abs z^2} = \del \exp\qty{-z\bar z} = e^{-\abs z^2}\cdot\del(-z\bar z) = -\bar z e^{-\abs z^2}
.$$

:::

[[T-JACOB]]

## Solving real integrals with complex calculus

::: {.example title="An integral by real parts"}
Since $e^{(3+2i)z}$ has antiderivative $e^{(3+2i)z}/(3+2i)$, restricting to real $z=x$ and taking real parts evaluates a real integral:
$$
\begin{aligned}
\int e^{3x}\cos(2x) \dx
&= \Re \int e^{3x}e^{2ix}\dx \\
&= \Re \int e^{(3+2i)x} \dx \\
&= \Re {e^{(3+2i)x} \over 3+2i} + C
\end{aligned}
$$.

:::

## Exercises

[[E-BGKED]]
[[E-THK2Z]]
[[P-AZOFF-E03]]
[[E-WKY7C]]
[[E-UVNVV]]
