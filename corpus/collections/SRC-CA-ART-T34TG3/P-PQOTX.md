---
schema: qual/card@1
id: P-PQOTX
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{(a+\cos\theta)^2}=\frac{2\pi a}{(a^2-1)^{3/2}}$
  for $a>1$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
  - Poles
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, with the arithmetic redone: z = e^{i theta} gives a + cos(theta) = (z^2 + 2az + 1)/(2z) and d theta = dz/(iz), so the integral is (2/i) times the contour integral; the roots are -a +- sqrt(a^2-1) with product 1, and |z_+| = a - sqrt(a^2-1) < 1 exactly for a > 1, which is now shown rather than asserted; the residue at the simple pole is 1/(z_+ - z_-) = 1/(2 sqrt(a^2-1)); and J(a) = 2 pi/sqrt(a^2-1). Differentiation under the integral is justified by a - 1 > 0, and J'(a) = -2 pi a/(a^2-1)^{3/2} gives the stated value. The statement is unchanged.
---

::: {.problem}
Show that
$$
\int_{0}^{2 \pi} \frac{d \theta}{(a+\cos \theta)^{2}}=\frac{2 \pi a}{\left(a^{2}-1\right)^{3 / 2}}, \quad \text{whenever } a>1.
$$
:::

::: {.solution}
Compute $J(a)=\int_0^{2\pi}\frac{\dtheta}{a+\cos\theta}$ by residues, obtaining $2\pi/\sqrt{a^2-1}$, and then differentiate under the integral sign: the denominator $a+\cos\theta$ is bounded away from $0$ for $a>1$, and $\partial_a(a+\cos\theta)^{-1}=-(a+\cos\theta)^{-2}$, so $-J'(a)$ is the integral asked for. The argument is this card's own: no retained solution set covers this problem.

::: pf

::: {.pf-step #substitution}
With $z=e^{i\theta}$, $\displaystyle J(a)=\frac2i\oint_{\abs z=1}\frac{\dz}{z^2+2az+1}$.

::: pf-proof
On the unit circle $\cos\theta=\frac12(z+z^{-1})$ and $\dtheta=\dfrac{\dz}{iz}$. Hence
$$
a+\cos\theta=a+\frac12\Bigl(z+\frac1z\Bigr)=\frac{2az+z^2+1}{2z},
\qquad
\frac{\dtheta}{a+\cos\theta}=\frac{\dz}{iz}\cdot\frac{2z}{z^2+2az+1}=\frac{2\dz}{i(z^2+2az+1)},
$$
and $\theta$ running once through $[0,2\pi]$ is $z$ running once counterclockwise around the unit circle, so the integral becomes the displayed contour integral.
:::

:::


::: {.pf-step #roots}
The roots of $z^2+2az+1$ are $z_\pm=-a\pm\sqrt{a^2-1}$, and for $a>1$ exactly $z_+$ lies inside the unit circle.

::: pf-proof
The quadratic formula gives $z_\pm=-a\pm\sqrt{a^2-1}$; both are real and negative for $a>1$, and their product is $1$. Since $a-\sqrt{a^2-1}>0$ and $(a-\sqrt{a^2-1})(a+\sqrt{a^2-1})=a^2-(a^2-1)=1$, one has $z_+=-a+\sqrt{a^2-1}=-(a-\sqrt{a^2-1})$ with $\abs{z_+}=a-\sqrt{a^2-1}<1$, because $a-\sqrt{a^2-1}<1$ is equivalent to $a-1<\sqrt{a^2-1}$, i.e. to $(a-1)^2<a^2-1$, i.e. to $a>1$. And $\abs{z_-}=1/\abs{z_+}>1$.
:::

:::


::: {.pf-step #residue}
$\displaystyle\operatorname{Res}_{z=z_+}\frac1{z^2+2az+1}=\frac1{2\sqrt{a^2-1}}$.

::: pf-proof
The denominator factors as $(z-z_+)(z-z_-)$ with $z_+\ne z_-$, so the pole at $z_+$ is simple and the residue is $\dfrac{1}{z_+-z_-}=\dfrac{1}{2\sqrt{a^2-1}}$, since $z_+-z_-=2\sqrt{a^2-1}$.
:::

:::


::: {.pf-step #J}
$\displaystyle J(a)=\frac{2\pi}{\sqrt{a^2-1}}$ for $a>1$.

::: pf-proof
By steps [](#substitution){.pf-ref} and [](#roots){.pf-ref} the integrand is holomorphic on and inside the unit circle except at the simple pole $z_+$, so the residue theorem gives the contour integral as $2\pi i$ times the residue of step [](#residue){.pf-ref}. Therefore $J(a)=\dfrac2i\cdot2\pi i\cdot\dfrac1{2\sqrt{a^2-1}}=\dfrac{2\pi}{\sqrt{a^2-1}}$.
:::

:::


::: {.pf-step #differentiate}
$\displaystyle J'(a)=-\int_0^{2\pi}\frac{\dtheta}{(a+\cos\theta)^2}$ for $a>1$.

::: pf-proof
For $a>1$ and all $\theta$ one has $a+\cos\theta\ge a-1>0$, so the integrand $\frac{1}{a+\cos\theta}$ and its $a$-derivative $-\frac{1}{(a+\cos\theta)^2}$ are continuous on $[0,2\pi]\times(1,\infty)$ and the derivative is bounded by $1/(a-1)^2$ on a neighbourhood of each $a>1$. Differentiation under the integral sign is therefore legitimate, and it gives the displayed formula.
:::

:::


::: {.pf-step #conclusion}
$\displaystyle\int_0^{2\pi}\frac{\dtheta}{(a+\cos\theta)^2}=\frac{2\pi a}{(a^2-1)^{3/2}}$ for $a>1$.

::: pf-proof
Differentiate the closed form of step [](#J){.pf-ref}: $\dfrac{d}{da}2\pi(a^2-1)^{-1/2}=2\pi\cdot(-\tfrac12)(a^2-1)^{-3/2}\cdot2a=-\dfrac{2\pi a}{(a^2-1)^{3/2}}$. By step [](#differentiate){.pf-ref} this is minus the required integral, so the integral equals $\dfrac{2\pi a}{(a^2-1)^{3/2}}$.
:::

:::

:::
:::
