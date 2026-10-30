---
schema: qual/card@1
id: E-AKF2O
kind: problem
title: $\int_\RR\frac{dx}{(1+x^2)^{n+1}}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source states the formula with no instruction and no range for n, followed by "Note that this solution can be written many ways" and the alternate forms (2n choose n) pi/4^n = (2n)(2n-1)...(n+1)/n! * pi/4^n. The statement asks to show the formula for integers n >= 0, and the alternate forms moved to a remark.'
---

::: {.exercise}
For each integer $n\ge0$, show that
$$
I \coloneqq \int_{-\infty}^{\infty} \frac{dx}{\left(1+x^{2}\right)^{n+1}}=\frac{(2 n) !}{4^{n}(n !)^{2}} \pi.
$$
:::

::: {.solution}
Let $f(z)=(1+z^2)^{-(n+1)}=(z+i)^{-(n+1)}(z-i)^{-(n+1)}$, and for $R>1$ let $\Gamma_R$ be the segment $[-R,R]$ followed by the positively oriented upper semicircle $C_R$ of radius $R$.

![Semicircular contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-05-57.png)

::: pf

::: {.pf-step #arc}
$\int_{C_R}f(z)\,dz\to0$ as $R\to\infty$.

::: pf-proof
On $C_R$, $\abs{1+z^2}\ge R^2-1$, so the integral is at most $\pi R/(R^2-1)^{n+1}\to0$.
:::

:::

::: {.pf-step #residue}
$2\pi i\Res_{z=i}f(z)=\frac{(2n)!}{4^n(n!)^2}\pi$.

::: pf-proof
The point $i$ is a pole of order $n+1$, so
$$
\begin{aligned}
\Res_{z=i}f(z)
&=\frac1{n!}\evaluated{\frac{d^n}{dz^n}(z+i)^{-(n+1)}}_{z=i}
=\frac{(-1)^n(n+1)(n+2)\cdots(2n)}{n!}(2i)^{-(2n+1)}\\
&=\frac{(2n)!}{(n!)^2}\cdot\frac{(-1)^n}{2^{2n+1}\,i\,(i^2)^n}
=\frac{(2n)!}{(n!)^2}\cdot\frac{1}{2^{2n+1}i}.
\end{aligned}
$$
Multiply by $2\pi i$.
:::

:::

::: pf-step
$I=\frac{(2n)!}{4^n(n!)^2}\pi$.

::: pf-proof
The only pole of $f$ in the upper half-plane is $i$, so the residue theorem gives $\int_{-R}^Rf(x)\,dx+\int_{C_R}f(z)\,dz=2\pi i\Res_{z=i}f(z)$ for $R>1$.
Let $R\to\infty$ and apply steps [](#arc){.pf-ref} and [](#residue){.pf-ref}.
:::

:::

:::

:::

::: {.remark}
The value can be written in several ways:
$$
I = \binom{2n}{n} \frac{\pi}{4^n}
= \frac{(2n)(2n-1)\cdots(n+1)}{n!}\, \frac{\pi}{4^n}.
$$
:::

::: {.remark title="Variations"}
For $n=1$ the formula gives $\int_\RR\frac{dx}{(1+x^2)^2}=\frac{\pi}{2}$.
Directly, the only pole in the upper half-plane is the double pole at $i$, with residue $\frac{d}{dz}(z+i)^{-2}\evalfrom_{z=i}=-2(2i)^{-3}=\frac{1}{4i}$, and the upper semicircle contributes at most $\pi R/(R^2-1)^2\to0$.
:::
