---
schema: qual/card@1
id: P-CAF09E
kind: problem
title: '$\int_0^\infty x/(x^4+1)\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Evaluate the integral $\int_0^{\infty} \frac{x\,dx}{x^4 + 1}$ via residue theory.
It is not necessary to simplify your answer.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own residue computation follows, with the pole and residue, the arc estimate and the two axis pieces as separate steps.

::: pf

::: {.pf-step #residue}
In the first quadrant $F(z)=z/(z^{4}+1)$ has the single simple pole $z_{0}=e^{i\pi/4}$, with $\operatorname{Res}(F,z_{0})=-i/4$.

::: pf-proof
$z^{4}+1=0$ gives $z^{4}=-1$, that is $z=e^{i(\pi+2k\pi)/4}$ for $k=0,1,2,3$: the roots $e^{i\pi/4},e^{3i\pi/4},e^{5i\pi/4},e^{7i\pi/4}$, of which only $e^{i\pi/4}$ has positive imaginary part and positive real part. The zeros are simple because $(z^{4}+1)'=4z^{3}\ne0$ there. At a simple pole with $F=p/q$, $\operatorname{Res}=p(z_{0})/q'(z_{0})=z_{0}/(4z_{0}^{3})=1/(4z_{0}^{2})=1/(4i)=-i/4$, since $z_{0}^{2}=e^{i\pi/2}=i$ and $1/i=-i$.
:::

:::

::: {.pf-step #arc}
The integral over the quarter-circle of radius $R$ tends to $0$.

::: pf-proof
On $\abs{z}=R$ one has $\abs{F(z)}=\abs{z}/\abs{z^{4}+1}\le R/(R^{4}-1)$, and the arc has length $\pi R/2$, so the arc integral is at most $\frac{\pi R^{2}}{2(R^{4}-1)}\to0$.
:::

:::

::: {.pf-step #axes}
The integral along the imaginary axis tends to the same value $I=\int_{0}^{\infty}\frac{x}{x^{4}+1}dx$ as along the real axis.

::: pf-proof
On the imaginary axis $z=iy$ with $y$ from $R$ down to $0$, $dz=i\,dy$ and $z^{4}+1=y^{4}+1$, so $\int_{iR}^{0}F\,dz=\int_{R}^{0}\frac{iy}{y^{4}+1}i\,dy=\int_{R}^{0}\frac{-y}{y^{4}+1}dy=\int_{0}^{R}\frac{y}{y^{4}+1}dy$, which tends to $I$; on the real axis the integral tends to $I$ by definition.
:::

:::

::: {.pf-qed}
The residue theorem gives $2I=\lim_{R\to\infty}\oint F\,dz=2\pi i\cdot\Big(-\frac{i}{4}\Big)=\frac{\pi}{2}$, using steps [](#residue){.pf-ref}, [](#arc){.pf-ref} and [](#axes){.pf-ref}; hence $I=\dfrac{\pi}{4}$.
:::

:::

:::
