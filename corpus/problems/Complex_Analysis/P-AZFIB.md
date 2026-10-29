---
schema: qual/card@1
id: P-AZFIB
kind: problem
title: $2\abs{f'(0)}\le\operatorname{diam} f(\DD)$, with equality iff $f$ is linear
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Schwarz Lemma
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.problem}
Suppose $f: \DD \to \CC$ is holomorphic and let $d \coloneqq \sup_{z, w\in \DD}\abs{f(z) - f(w)}$ be the diameter of the image of $f$.
Show that $2 \abs{f'(0)} \leq d$, and that equality holds iff $f$ is linear, so $f(z) = a_1 z + a_2$.
:::

::: {.hint}
$$
2f'(0) = \frac{1}{2\pi i} \int_{\abs \xi = r} \frac{ f(\xi) - f(-\xi)  }{\xi^2} \, d\xi
$$
whenever $0<r<1$.
:::

::: {.solution}

If $d=\infty$ the inequality holds and equality is impossible, and if $d=0$ then $f$ is constant, so both claims hold with $a_1=0$.
Assume $0<d<\infty$.

::: pf

::: pf-step
$2\abs{f'(0)}\le d$.

::: pf-proof
The function $h(z)\coloneqq(f(z)-f(-z))/d$ is holomorphic on $\DD$, satisfies $h(0)=0$, and $\abs{h}\le1$ because $\abs{f(z)-f(-z)}\le d$.
Schwarz's lemma gives $\abs{h'(0)}\le1$, and $h'(0)=2f'(0)/d$.
:::

:::

::: pf-step
If $f(z)=a_1z+a_2$, then $2\abs{f'(0)}=d$.

::: pf-proof
$\abs{f(z)-f(w)}=\abs{a_1}\abs{z-w}$, whose supremum over $z,w\in\DD$ is $2\abs{a_1}=2\abs{f'(0)}$.
:::

:::

::: pf-step
If $2\abs{f'(0)}=d$, then $f$ is affine.

::: pf-proof

Then $f'(0)\neq0$, and $F(z)\coloneqq(f(z)-f(0))/f'(0)$ satisfies $F(0)=0$, $F'(0)=1$ and $\operatorname{diam}F(\DD)=2$.
For $0<r<1$ let $D_r\coloneqq\sup\{\abs{F(z)-F(w)} : \abs{z},\abs{w}\le r\}$.

::: {.pf-step #odd-part}
$F(z)-F(-z)=2z$ on $\DD$.

::: pf-proof
The odd part $F_o(z)\coloneqq(F(z)-F(-z))/2$ maps $\DD$ into $\overline{\DD}$, satisfies $F_o(0)=0$ and $F_o'(0)=1$; the equality case of Schwarz's lemma gives $F_o(z)=z$.
:::

:::

::: {.pf-step #monotone}
$D_r/r$ is nondecreasing in $r$.

::: pf-proof
$F$ is nonconstant, so by the maximum modulus principle in each variable the supremum defining $D_r$ is attained with $\abs{z}=\abs{w}=r$.
For $\abs{u}=1$ let $H_u(z)\coloneqq(F(z)-F(-uz))/z$, with its removable value at $0$.
Writing $w=-uz$ gives $D_r/r=\max_{\abs{u}=1}\max_{\abs{z}=r}\abs{H_u(z)}=\max_{\abs{u}=1}\max_{\abs{z}\le r}\abs{H_u(z)}$ by the maximum modulus principle, and the right side is nondecreasing in $r$.
:::

:::

::: {.pf-step #diam-r}
$D_r=2r$ for $0<r<1$.

::: pf-proof
Step [](#odd-part){.pf-ref} gives $D_r\ge2r$, and $D_r\le2$, so $2\le D_r/r\le 2/s$ whenever $r\le s<1$, by step [](#monotone){.pf-ref}.
Letting $s\to1$ gives $D_r/r\le2$.
:::

:::

::: {.pf-step #real-derivative}
$\Im F'(w)=0$ for every $w\in\DD\setminus\{0\}$.

::: pf-proof
Let $r=\abs{w}$ and $G(z)\coloneqq(F(z)-F(-w))/2$.
By step [](#diam-r){.pf-ref}, $\abs{G(z)}\le r$ for $\abs{z}\le r$, and by step [](#odd-part){.pf-ref}, $G(w)=w$.
So $\phi(\theta)\coloneqq\abs{G(we^{i\theta})}^2$ has a maximum at $\theta=0$, and
$$
0=\phi'(0)=2\Re\left(\overline{G(w)}\,iwG'(w)\right)=-2\abs{w}^2\Im G'(w)=-\abs{w}^2\Im F'(w).
$$
:::

:::

::: pf-step
$f$ is affine.

::: pf-proof
By step [](#real-derivative){.pf-ref} and continuity, the holomorphic function $F'$ takes real values on $\DD$, so by the open mapping theorem it is constant, equal to $F'(0)=1$.
With $F(0)=0$ this gives $F(z)=z$, so $f(z)=f'(0)z+f(0)$.
:::

:::

:::

:::

:::

:::
