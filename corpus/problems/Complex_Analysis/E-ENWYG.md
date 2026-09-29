---
schema: qual/card@1
id: E-ENWYG
kind: problem
title: $\int_0^\infty\frac{\log x}{(1+x^2)^2}\,dx$ by a keyhole contour
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
Evaluate
\[
I\da \int_0^\infty {\log x\over(1+x^2)^2}\,dx.
\]
:::

::: {.solution}
Let $\log$ be the branch with $0<\arg z<2\pi$ on $\CC\setminus[0,\infty)$, and let
\[
f(z)={\log^2 z\over(1+z^2)^2},\qquad (1+z^2)^2 = (z+i)^2(z-i)^2
.\]
Integrate $f$ over a keyhole contour with outer radius $R$ and inner radius $\rho$, slit along $[0,\infty)$:

![image_2021-06-09-02-11-59](../../assets/figures/image_2021-06-09-02-11-59.png)

Write $I$ for the requested integral and $A\coloneqq\int_0^\infty{dx\over(1+x^2)^2}={\pi\over4}$.

::: pf

::: {.pf-step #circles-vanish}
The circles of radii $R$ and $\rho$ contribute $0$ in the limit.

::: pf-proof
By the ML estimate, the outer circle contributes $O\qty{R(\log R+2\pi)^2/R^4}\to0$ and the inner circle contributes $O\qty{\rho(\abs{\log\rho}+2\pi)^2}\to0$.
:::

:::

::: {.pf-step #edges-contribution}
The two edges of the slit contribute $-4\pi i I+4\pi^2A$.

::: pf-proof
On the upper edge $\log z=\log x$, and on the lower edge, traversed from $\infty$ to $0$, $\log z=\log x+2\pi i$. So the edges contribute
\[
\int_0^\infty{\log^2x-(\log x+2\pi i)^2\over(1+x^2)^2}\,dx=-4\pi i I+4\pi^2A
.\]
:::

:::

::: {.pf-step #residues}
$\Res_{z=i}f=-{\pi\over4}+{i\pi^2\over16}$ and $\Res_{z=-i}f={3\pi\over4}-{9i\pi^2\over16}$.

::: pf-proof
With $h(z)=\log^2z$, $h'(z)=2\log z/z$, and on this branch $\log i=i\pi/2$, $\log(-i)=3\pi i/2$. At the double poles,
\[
\Res_{z=i}f=\dd{}{z}{h(z)\over(z+i)^2}\bigg|_{z=i}={h'(i)\over(2i)^2}-{2h(i)\over(2i)^3}={\pi\over-4}-{-\pi^2/2\over-8i}=-{\pi\over4}+{i\pi^2\over16}
,\]
\[
\Res_{z=-i}f=\dd{}{z}{h(z)\over(z-i)^2}\bigg|_{z=-i}={h'(-i)\over(-2i)^2}-{2h(-i)\over(-2i)^3}={-3\pi\over-4}-{-9\pi^2/2\over8i}={3\pi\over4}-{9i\pi^2\over16}
.\]
:::

:::

::: pf-step
$I=\boxed{-\pi/4}$.

::: pf-proof
By steps [](#circles-vanish){.pf-ref}, [](#edges-contribution){.pf-ref} and [](#residues){.pf-ref} and the residue theorem,
\[
-4\pi iI+4\pi^2A=2\pi i\qty{{\pi\over2}-{i\pi^2\over2}}=\pi^3+i\pi^2
.\]
The real parts agree since $A=\pi/4$, and the imaginary parts give $-4\pi I=\pi^2$.
:::

:::

:::

::: {.remark}
A contour with one logarithm also works: with the branch $-\pi/2<\arg z<3\pi/2$, integrate $\log z/(1+z^2)^2$ over the upper semicircle indented at $0$. The negative real axis contributes $I+i\pi A$, and the residue at the double pole $i$ is $\frac i4+\frac\pi8$, so $2I+i\pi A=-\frac\pi2+\frac{i\pi^2}4$ and again $I=-\pi/4$.
:::

