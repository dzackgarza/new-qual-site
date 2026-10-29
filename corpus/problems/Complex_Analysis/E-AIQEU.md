---
schema: qual/card@1
id: E-AIQEU
kind: problem
title: $\int_{\RR} e^{ax}\operatorname{sech}(x)\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Hyperbolic Functions
relations: []
review: draft
---

::: {.exercise}
$$
I \coloneqq \int_\RR \frac{e^{ax}}{\cosh(x)}\dx,
\qquad \abs{\Re(a)}<1.
$$
Show that
$$
I=\pi\sec\qty{\frac{a\pi}{2}}.
$$
:::

::: {.solution}
Let $f(z)=\frac{e^{az}}{\cosh z}$, whose poles are the points $\qty{k+\frac12}\pi i$, $k\in\ZZ$, and let $I_R=\int_{-R}^R f(x)\,dx$.
Integrate around the positively oriented rectangle $\Gamma_R$ with vertices $-R,R,R+i\pi,-R+i\pi$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-22_05-16-12.png)

::: pf

::: {.pf-step #horizontal}
The two horizontal edges of $\Gamma_R$ contribute $\qty{1+e^{i\pi a}}I_R$.

::: pf-proof
Since $\cosh(z+i\pi)=-\cosh z$ and $e^{a(z+i\pi)}=e^{i\pi a}e^{az}$, the upper edge, oriented from $R+i\pi$ to $-R+i\pi$, contributes
$$
\int_R^{-R}f(x+i\pi)\,dx
=e^{i\pi a}\int_{-R}^R f(x)\,dx.
$$
:::

:::

::: {.pf-step #vertical}
The integrals over the vertical edges tend to $0$ as $R\to\infty$.

::: pf-proof
For $0\leq y\leq\pi$, $\abs{\cosh(\pm R+iy)}^2=\sinh^2R+\cos^2y\geq\sinh^2R$ and $\abs{e^{a(\pm R+iy)}}\le e^{\pi\abs{\Im a}}e^{\pm R\Re a}$.
So the integrands are bounded by $e^{\pi\abs{\Im a}}e^{R\abs{\Re a}}/\sinh R$ on edges of length $\pi$, and this tends to $0$ because $\abs{\Re a}<1$.
:::

:::

::: {.pf-step #residue}
$\oint_{\Gamma_R}f(z)\,dz=2\pi e^{i\pi a/2}$ for $R>0$.

::: pf-proof
The rectangle contains only the simple pole $z_0=i\pi/2$, where
$$
\Res_{z=z_0}f(z)
=\frac{e^{az_0}}{\sinh z_0}
=\frac{e^{i\pi a/2}}{i}.
$$
Apply the residue theorem.
:::

:::

::: pf-step
$I=\boxed{\pi\sec\qty{\frac{\pi a}{2}}}$.

::: pf-proof
Letting $R\to\infty$ in steps [](#horizontal){.pf-ref}, [](#vertical){.pf-ref}, and [](#residue){.pf-ref} gives $\qty{1+e^{i\pi a}}I=2\pi e^{i\pi a/2}$.
Since $1+e^{i\pi a}=2e^{i\pi a/2}\cos\qty{\frac{\pi a}2}$, and $\cos\qty{\frac{\pi a}2}\neq0$ because $a$ is not an odd integer, dividing gives the value.
:::

:::

:::

:::
