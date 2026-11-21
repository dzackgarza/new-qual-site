---
schema: qual/card@1
id: P-CASP23D
kind: problem
title: "Injectivity from derivative condition and fixed-point rigidity for self-maps of D"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Injective Functions
  - Fixed Points
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured both parts into Lamport steps and checked them: the hypothesis puts
    f'(z)/f'(0) in the disc of radius 1 about 1, hence in the right half-plane, so the
    difference quotient, written as the integral of f'/f'(0) along the segment, has positive
    real part and cannot vanish; and for part (b) the conjugate F = phi o f o phi^-1 maps the
    disc into itself, fixes 0 and the nonzero point phi(b), so Schwarz's equality case makes it
    a rotation, which the fixed point forces to be the identity. Added: f'(0) != 0 and the
    half-plane argument, the integral formula for the difference quotient along the segment (the
    disc being convex), and phi(b) != 0. Both statements are true as printed.
---

::: {.problem}
Let $f(z)$ be analytic on $\DD$.
Prove the following statements.

(a) If $\abs{f'(z) - f'(0)} < \abs{f'(0)}$ for all $z \in \DD$, then $f(z)$ is injective.

(b) If $\abs{f(z)} < 1$ for all $z \in \DD$ and $f(z)$ has two distinct fixed points, then $f(z) = z$. (Hint: analytic automorphisms of $\DD$ and Schwarz's lemma could be useful.)
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #half-plane}
Under the hypothesis of (a), $f'(0)\ne0$ and $\operatorname{Re}\frac{f'(z)}{f'(0)}>0$ for every $z\in\DD$.

::: pf-proof
If $f'(0)=0$ the hypothesis would read $\abs{f'(z)}<0$, which is impossible, so $f'(0)\ne0$. Dividing by $f'(0)$, the hypothesis is $\abs{\frac{f'(z)}{f'(0)}-1}<1$, that is, the value lies in the disc of radius $1$ about $1$; and every point $w$ of that disc has $\operatorname{Re}w>0$, because $\operatorname{Re}w=1+\operatorname{Re}(w-1)\ge1-\abs{w-1}>0$.
:::

:::

::: {.pf-step #quotient}
For $z_1\ne z_2$ in $\DD$,
$$
\frac{f(z_2)-f(z_1)}{f'(0)(z_2-z_1)}=\int_0^1\frac{f'\bigl(z_1+t(z_2-z_1)\bigr)}{f'(0)}\,dt .
$$

::: pf-proof
The segment $t\mapsto z_1+t(z_2-z_1)$ lies in the convex set $\DD$, and $\frac{d}{dt}f(z_1+t(z_2-z_1))=(z_2-z_1)f'(z_1+t(z_2-z_1))$; integrating in $t$ from $0$ to $1$ gives $f(z_2)-f(z_1)$ equal to $(z_2-z_1)$ times the integral, and dividing by the nonzero $f'(0)(z_2-z_1)$ gives the claim.
:::

:::

::: {.pf-step}
(a) $f$ is injective.

::: pf-proof
By steps [](#half-plane){.pf-ref} and [](#quotient){.pf-ref} the displayed quotient is the integral of a function whose real part is continuous and positive on $[0,1]$, so the real part of the integral is positive, and in particular the quotient is nonzero. Hence $f(z_2)\ne f(z_1)$ whenever $z_1\ne z_2$, that is, $f$ is injective.
:::

:::

::: {.pf-step #conjugate}
Let $a\ne b$ be distinct fixed points of $f$ and $\phi$ a disc automorphism with $\phi(a)=0$. Then $F\coloneqq\phi\circ f\circ\phi^{-1}$ maps $\DD$ into $\DD$, fixes $0$, and fixes $w\coloneqq\phi(b)\ne0$.

::: pf-proof
$\phi^{-1}$ and $\phi$ are automorphisms of $\DD$ and $f(\DD)\subset\DD$ by hypothesis, so $F$ maps $\DD$ into $\DD$. $F(0)=\phi(f(\phi^{-1}(0)))=\phi(f(a))=\phi(a)=0$, and $F(w)=\phi(f(b))=\phi(b)=w$; finally $w\ne0$ because $\phi$ is injective and $b\ne a$.
:::

:::

::: {.pf-step #rotation}
There is $\theta\in\RR$ with $F(z)=e^{i\theta}z$.

::: pf-proof
$F$ is holomorphic on the disc with $F(0)=0$ and $\abs{F(z)}<1$ there, so Schwarz's lemma gives $\abs{F(z)}\le\abs{z}$. At the nonzero point $w$ of step [](#conjugate){.pf-ref} one has $\abs{F(w)}=\abs{w}$, so the equality case of Schwarz's lemma applies and $F$ is a rotation.
:::

:::

::: {.pf-step}
(b) $f(z)=z$.

::: pf-proof
By steps [](#conjugate){.pf-ref} and [](#rotation){.pf-ref}, $e^{i\theta}w=F(w)=w$ with $w\ne0$, so $e^{i\theta}=1$ and $F$ is the identity. Then $f=\phi^{-1}\circ F\circ\phi=\operatorname{id}_{\DD}$, so every analytic self-map of the disc with two distinct fixed points is the identity, as claimed.
:::

:::

:::
:::
