---
schema: qual/card@1
id: E-XYEP4
kind: problem
title: $1/x\sqrt{x^2-1}$
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

:::{.exercise}
\[
\int_{1}^{\infty} \frac{d x}{x \sqrt{x^{2}-1}} = {\pi \over 2}
.\]

:::

:::{.solution}
Write $f(z) \da (z^2-1)^{-{1\over 2}}/z$.
In order for $(z^2-1)^{-{1\over 2}}$ to be well-defined, one needs to introduce a branch cut. 
Note that $f$ has a simple pole at $z=0$ and is holomorphic away from $z=0$ **if** $z^2-1$ is not on the positive real axis, where we've chosen the branch cut $\theta = 0$ for $\Log(z)$ and define $z^{1\over 2} = e^{{1\over 2}\Log(z)}$.
But $z^2-1 \in \RR_{\geq 0} \iff z\in [-1, 1]^c$, which is what we've cut.

So take the branch cut $(-\infty, 1] \union [1, \infty)$ and use the following indented double-keyhole contour:

![figures/2021-07-29_18-53-35.png](../../assets/figures/2021-07-29_18-53-35.png)

Contributions along $C_8$ and $C_6$: note that $\int_{C_8}f \to I$, the desired integral.
For reference, note that $z^2-1 = (z+1)(z-1)$, and we can parameterize
\[
C_8 = \ts{t+1+ i\eps \st t\in [\eps, R] } \implies \\
\int_{C_8}f(z)\dz \to \int_0^\infty t\inv (t+2)^{-{1\over 2}} t^{-{1\over 2}} \dt
,\]
where on $C_8$ we choose a branch of the square root so that $\arg(z+1) \in [-\pi, \pi)$ and $\arg(z-1)\in [-\pi, \pi)$.
Now consider $C_6$.
Write $\zeta_0 \da e^{2\pi i}$, then
\[
C_6 = \ts{\zeta_0 t + 1 - i\eps \st t\in [\eps, R]} \implies \\
\int_{C_6} f(z)\dz 
&\to \int_R^{\eps} (\zeta_0 t)\inv(\zeta_0 t + 2)^{-{1\over 2}}(\zeta_0 t)^{-{1\over 2}}\dt \\
&\to -\zeta_0^{-{3 \over 2}} \int_0^\infty t\inv (t+2)^{-{1\over 2}} t^{-{1\over 2}}\dt \\
&= I
,\]
since $-\zeta_0^{-{3\over 2}} \da -e^{-3\pi i} = 1$.
So in the limit $\eps\to 0, R\to\infty$,
\[
\qty{ \int_{C_8} + \int_{C_6}}f \too 2I
.\]

The contribution from $C_2$:
parameterize
\[
C_2 = \ts{s + i\eps \st x\in [-R, -1-\eps]}
,\]
which implies
\[
\int_{C_2}f(z)\dz 
&= \int_{-\infty}^{-1} {1\over s\sqrt{s^2-1}}\ds \\
&= - \int_{\infty}^{1} {1\over (-x) \sqrt{(-x)^2-1}}\dx,\qquad x=-s,\, \dx = -\ds \\
&= \int_\infty^1 {1\over (-x) \sqrt{ (-x)^2 - 1} }\dx \\
&= - \int_\infty^1 {1\over x \sqrt{ x^2 - 1} }\dx \\
&= \int_1^\infty {1\over x \sqrt{ x^2 - 1} }\dx \\
&= I
,\]
so the same argument as above shows
\[
\qty{ \int_{C_2} + \int_{C_4}}f \too 2I
.\]

Computing the residues: the full contour encloses a simple pole at $z=0$, so
\[
2\pi i \Res_{z=0} f(z) = 2\pi i \lim_{z\to 0} {1\over \sqrt{z^2-1}} = 2\pi \cdot (-i) = 2\pi
.\]

So by the residue theorem,
\[
2\pi = 2I + 2I \implies I = {\pi \over 2}
.\]
:::

