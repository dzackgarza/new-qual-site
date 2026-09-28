---
schema: qual/card@1
id: P-AZOFF-C07
kind: problem
title: Conformal map of a non-concentric circular region onto an annulus
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash reads `cone-to-one`; the surrounding conformal-mapping sentence identifies the intended phrase as `one-to-one`.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Chose rho=2-sqrt(3), whose reciprocal is 2+sqrt(3) and which satisfies
    1+rho^2=4rho. For T(z)=(z-rho)/(z-rho^{-1}), direct modulus identities
    show the unit circle is |T|=rho and the inner circle is |T|=rho^2.
    Thus T/rho maps the region bijectively and conformally onto
    rho<|w|<1. The source compilation contains no worked solution.
---

::: {.problem}
Let $\Omega \subset \mathbb { C }$ be the region inside the unit circle $| z | = 1$ and outside the circle $\begin{array} { r } { | z - \frac { 1 } { 4 } | = \frac { 1 } { 4 } } \end{array}$ . Find a one-to-one conformal map of Ω onto an annulus $r < | \boldsymbol { z } | < 1$ for an appropriate value of r.
:::

::: {.solution}
Put
$$
\rho=2-\sqrt3.
$$
Then
$$
0<\rho<1,
\qquad
\rho^{-1}=2+\sqrt3,
\qquad
1+\rho^2=4\rho.
$$
Define
$$
T(z)=\frac{z-\rho}{z-\rho^{-1}}.
$$

<1>1. For every $z\neq\rho^{-1}$,
$$
\abs{T(z)}^2-\rho^2
=
\frac{(1-\rho^2)(\abs z^2-1)}
{\abs{z-\rho^{-1}}^2}.
$$

::: {.proof}
Since $\rho\rho^{-1}=1$,
$$
\begin{aligned}
&\abs{z-\rho}^2
-
\rho^2\abs{z-\rho^{-1}}^2\\
&\qquad=
(1-\rho^2)\abs z^2+\rho^2-1\\
&\qquad=
(1-\rho^2)(\abs z^2-1).
\end{aligned}
$$
Dividing by
$$
\abs{z-\rho^{-1}}^2
$$
gives the identity.
:::

<1>2. For every $z\neq\rho^{-1}$,
$$
\abs{T(z)}^2-\rho^4
=
\frac{(1-\rho^4)
\left(\abs z^2-\frac12\operatorname{Re}z\right)}
{\abs{z-\rho^{-1}}^2}.
$$

::: {.proof}
Expanding gives
$$
\begin{aligned}
&\abs{z-\rho}^2
-
\rho^4\abs{z-\rho^{-1}}^2\\
&\qquad=
(1-\rho^4)\abs z^2
-
2\rho(1-\rho^2)\operatorname{Re}z.
\end{aligned}
$$
The relation
$$
1+\rho^2=4\rho
$$
implies
$$
2\rho(1-\rho^2)
=
\frac12(1-\rho^4).
$$
Substitution yields
$$
\abs{z-\rho}^2
-
\rho^4\abs{z-\rho^{-1}}^2
=
(1-\rho^4)
\left(\abs z^2-\frac12\operatorname{Re}z\right).
$$
Dividing by the denominator proves the claim.
:::

<1>3. The map $T$ sends $\Omega$ into the annulus
$$
\rho^2<\abs w<\rho.
$$

::: {.proof}
If $z\in\Omega$, then
$$
\abs z<1.
$$
Since $1-\rho^2>0$, step <1>1 gives
$$
\abs{T(z)}<\rho.
$$

The other defining inequality is
$$
\abs{z-\frac14}>\frac14.
$$
Squaring and simplifying gives
$$
\abs z^2-\frac12\operatorname{Re}z>0.
$$
Since $1-\rho^4>0$, step <1>2 therefore gives
$$
\abs{T(z)}>\rho^2.
$$
:::

<1>4. The map
$$
T:\Omega\longrightarrow
\{w\in\CC:\rho^2<\abs w<\rho\}
$$
is a conformal bijection.

::: {.proof}
The map $T$ is a Möbius transformation. Its pole
$$
\rho^{-1}=2+\sqrt3
$$
lies outside the unit disk, hence outside $\Omega$, and
$$
T'(z)
=
\frac{\rho-\rho^{-1}}{(z-\rho^{-1})^2}
\neq
0
$$
on $\Omega$.

For surjectivity, let
$$
\rho^2<\abs w<\rho.
$$
Since $\abs w<1$, one has $w\neq1$, and the Möbius inverse
$$
T^{-1}(w)
=
\frac{\rho^{-1}w-\rho}{w-1}
$$
is defined. Apply the identities in steps <1>1--<1>2 to
$$
z=T^{-1}(w).
$$
The inequality $\abs w<\rho$ forces $\abs z<1$, while
$\abs w>\rho^2$ forces
$$
\abs z^2-\frac12\operatorname{Re}z>0,
$$
equivalently
$$
\abs{z-\frac14}>\frac14.
$$
Thus $z\in\Omega$. Hence $T$ is onto the displayed annulus; injectivity
follows from the Möbius inverse.
:::

<1>5. A one-to-one conformal map of $\Omega$ onto an annulus
$$
r<\abs w<1
$$
is
$$
\boxed{
F(z)
=
\frac1{\rho}
\frac{z-\rho}{z-\rho^{-1}},
\qquad
r=\rho=2-\sqrt3.
}
$$

::: {.proof}
By step <1>4,
$$
\rho^2<\abs{T(z)}<\rho.
$$
Dividing by $\rho$ gives
$$
\rho<\abs{F(z)}<1.
$$
Multiplication by the nonzero constant $\rho^{-1}$ preserves conformality
and injectivity, so $F$ is the required conformal bijection.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives both the map and the required inner radius.
:::
:::
