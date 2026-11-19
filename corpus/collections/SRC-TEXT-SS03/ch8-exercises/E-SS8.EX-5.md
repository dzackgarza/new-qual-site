---
schema: qual/card@1
id: E-SS8.EX-5
kind: problem
title: A conformal map from the half-disc onto the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, and checked: Im(z + 1/z) =
    y(1 - 1/|z|^2) from 1/z = conj(z)/|z|^2, negative on the half-disc, so Im f > 0 there; the
    injectivity identity (z-w)(1 - 1/(zw)) = 0 is correct and |zw| < 1 excludes the second
    factor; the two roots of z^2 + 2 eta z + 1 = 0 are reciprocal with nonzero discriminant
    4(eta^2 - 1) because eta^2 = 1 would make eta real, and Im(1/z) = -Im(z)/|z|^2 puts exactly
    one of them in the upper half-plane. One detail the prose left implicit is now a step: that
    root has Im z > 0 and |z| < 1, so it lies in the half-disc, the |z| = 1 and |z| > 1 cases
    being excluded by the reality of z + 1/z and by the sign of Im(z + 1/z). f'(z) = -(1/2)(1 -
    z^-2) vanishes only at z = +-1, on the boundary, so f is conformal. Statement and hint
    unchanged; no retained solution set covers the exercises of Stein-Shakarchi.
---

::: {.exercise}
Prove that $f(z) = -\frac{1}{2}(z + 1/z)$ is a conformal map from the half-disc $\{z = x + iy : \abs{z} < 1,\ y > 0\}$ to the upper half-plane.

[Hint: The equation $f(z) = w$ reduces to the quadratic equation $z^2 + 2wz + 1 = 0$, which has two distinct roots in $\CC$ whenever $w \neq \pm 1$. This is certainly the case if $w \in \halfplane$.]
:::

::: {.solution}
Write $D_+=\{\abs z<1,\ \Im z>0\}$ and $f(z)=-\tfrac12(z+z^{-1})$. The imaginary part of $z+z^{-1}$ is $y(1-\abs z^{-2})$, which is negative on $D_+$, so $f$ lands in the upper half-plane; $f$ is injective there because $z+z^{-1}=w+w^{-1}$ forces $z=w$ when $\abs{zw}<1$; and $f$ is onto the upper half-plane because the two roots of $z^2+2\eta z+1=0$ are reciprocal and nonreal, so exactly one is in the upper half-plane, and the argument above excludes $\abs z\ge1$ for that one. Since $f'$ has no zero in $D_+$, $f$ is conformal. The argument is this card's own; no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #imaginary}
For $z=x+iy\ne0$, $\displaystyle\Im\Bigl(z+\frac1z\Bigr)=y\Bigl(1-\frac1{\abs z^2}\Bigr)$.

::: pf-proof
$\dfrac1z=\dfrac{\overline z}{\abs z^2}=\dfrac{x-iy}{x^2+y^2}$, so $z+\dfrac1z=x+\dfrac{x}{\abs z^2}+i\Bigl(y-\dfrac{y}{\abs z^2}\Bigr)$, which gives the display. In particular $\Im(z+z^{-1})$ has the sign of $y$ when $\abs z>1$, vanishes when $\abs z=1$, and has the opposite sign to $y$ when $\abs z<1$.
:::

:::


::: {.pf-step #into}
$f(D_+)\subseteq\halfplane$.

::: pf-proof
For $z\in D_+$ one has $0<\abs z<1$ and $y=\Im z>0$, so by step [](#imaginary){.pf-ref} $\Im(z+z^{-1})=y(1-\abs z^{-2})<0$; hence $\Im f(z)=-\tfrac12\Im(z+z^{-1})>0$.
:::

:::


::: {.pf-step #injective}
$f$ is injective on $D_+$.

::: pf-proof
Let $z,w\in D_+$ with $f(z)=f(w)$. Then $z+z^{-1}=w+w^{-1}$, that is
$$
(z-w)+\frac{w-z}{zw}=(z-w)\Bigl(1-\frac1{zw}\Bigr)=0 .
$$
Since $\abs z<1$ and $\abs w<1$ give $\abs{zw}<1$, one has $1/(zw)\ne1$, so the second factor is nonzero and $z=w$.
:::

:::


::: {.pf-step #roots}
For $\eta\in\halfplane$ the equation $f(z)=\eta$, that is $z^2+2\eta z+1=0$, has two distinct roots, they are reciprocal, they are not real, and exactly one of them lies in $\halfplane$.

::: pf-proof
The equation is a quadratic with product of roots $1$ and sum $-2\eta$; the discriminant is $4(\eta^2-1)$, which is nonzero because $\eta^2=1$ would make $\eta=\pm1$ real, so there are two distinct roots $z$ and $1/z$. If $z$ were real then $\eta=-\tfrac12(z+1/z)$ would be real, so neither root is real. Finally $\Im(1/z)=-\Im(z)/\abs z^2$ has the sign opposite to $\Im z$, so of the two roots exactly one has positive imaginary part.
:::

:::


::: {.pf-step #onto}
Every $\eta\in\halfplane$ is $f(z)$ for some $z\in D_+$.

::: pf-proof
Let $z$ be the root of step [](#roots){.pf-ref} lying in $\halfplane$. If $\abs z=1$ then $z+1/z=2\Re z$ is real, so $\eta=-\tfrac12(z+1/z)$ would be real, which it is not; hence $\abs z\ne1$. If $\abs z>1$, then by step [](#imaginary){.pf-ref} $\Im(z+1/z)$ has the sign of $\Im z>0$, so $\Im f(z)<0$, contradicting $f(z)=\eta\in\halfplane$. Therefore $\abs z<1$, and with $\Im z>0$ this says $z\in D_+$ and $f(z)=\eta$.
:::

:::


::: {.pf-step #conformal}
$f$ is holomorphic on $D_+$, $f'\ne0$ there, and therefore $f$ is a conformal map of $D_+$ onto $\halfplane$.

::: pf-proof
$f'(z)=-\tfrac12(1-z^{-2})$, which vanishes exactly when $z^2=1$, that is at $z=\pm1$; neither lies in $D_+$, since $\abs{\pm1}=1$ is excluded. So $f$ is holomorphic with nonvanishing derivative on $D_+$; a holomorphic function with nonzero derivative is conformal at each point, and by steps [](#injective){.pf-ref} and [](#onto){.pf-ref} it is a bijection of $D_+$ onto $\halfplane$, so it is a conformal map of the one onto the other.
:::

:::

:::
:::
