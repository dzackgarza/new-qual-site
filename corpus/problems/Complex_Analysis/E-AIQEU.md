---
schema: qual/card@1
id: E-AIQEU
kind: problem
title: $\int_{\mathbb R} e^{ax}\operatorname{sech}(x)\,dx$
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
\[
I \da \int_\RR {e^{ax} \over \cosh(x) }\dx,
\qquad \abs{\Re(a)}<1.
\]
Show that
\[
I=\pi\sec\qty{a\pi\over2}.
\]
:::

::: {.solution}
Set
\[
f(z)=\frac{e^{az}}{\cosh z}.
\]
The poles of $f$ occur at
\[
z=\qty{k+\frac12}\pi i,
\qquad k\in\ZZ.
\]
Integrate around the positively oriented rectangle with vertices $-R,R,R+i\pi,-R+i\pi$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-22_05-16-12.png)

Since
\[
\cosh(z+i\pi)=-\cosh z,
\qquad
e^{a(z+i\pi)}=e^{i\pi a}e^{az},
\]
the upper horizontal edge, oriented from $R+i\pi$ to $-R+i\pi$, contributes
\[
\int_R^{-R}f(x+i\pi)\,dx
=e^{i\pi a}\int_{-R}^R f(x)\,dx.
\]
Therefore the two horizontal edges contribute
\[
\qty{1+e^{i\pi a}}I_R,
\qquad
I_R=\int_{-R}^R\frac{e^{ax}}{\cosh x}\,dx.
\]

For $0\leq y\leq\pi$,
\[
\abs{\cosh(R+iy)}^2=\sinh^2R+\cos^2y\geq\sinh^2R.
\]
Thus, with a constant $C_a$ independent of $R$ and $y$,
\[
\abs{f(R+iy)}\leq C_a\frac{e^{R\Re a}}{\sinh R},
\qquad
\abs{f(-R+iy)}\leq C_a\frac{e^{-R\Re a}}{\sinh R}.
\]
The vertical-edge integrals therefore tend to zero when $-1<\Re a<1$.

The rectangle contains only the pole $z_0=i\pi/2$.
It is simple, and
\[
\Res_{z=z_0}f(z)
=\frac{e^{az_0}}{\sinh z_0}
=\frac{e^{i\pi a/2}}{i}
=-i e^{i\pi a/2}.
\]
Letting $R\to\infty$ in the residue theorem gives
\[
\qty{1+e^{i\pi a}}I
=2\pi e^{i\pi a/2}.
\]
Since
\[
1+e^{i\pi a}=2e^{i\pi a/2}\cos\qty{\pi a\over2},
\]
we obtain
\[
I=\pi\sec\qty{\pi a\over2}.
\]
:::
