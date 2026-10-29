---
schema: qual/card@1
id: E-YAYQB
kind: problem
title: Conformal map from the slit disc $\DD\setminus[1/2,1)$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
Find a conformal map
$$
\DD\setminus \left[ \frac12, 1\right) \to \DD.
$$
:::

::: {.solution}
Write $Q\coloneqq\{w : \Re w>0,\ \Im w>0\}$ for the open first quadrant and $\DD^+\coloneqq\DD\cap\HH$ for the upper half-disc.

::: pf

::: {.pf-step #move-slit}
$\varphi_1(z)\coloneqq\dfrac{z-1/2}{1-z/2}$ maps $\DD\setminus[1/2,1)$ conformally onto $\DD\setminus[0,1)$.

::: pf-proof
$\varphi_1$ is a disc automorphism, and on $[1/2,1]$ it is real and increasing with $\varphi_1(1/2)=0$ and $\varphi_1(1)=1$, so it maps $[1/2,1)$ onto $[0,1)$.
:::

:::

::: {.pf-step #root}
$\varphi_2(re^{i\theta})\coloneqq\sqrt r\,e^{i\theta/2}$, for $0<r<1$ and $0<\theta<2\pi$, maps $\DD\setminus[0,1)$ conformally onto $\DD^+$.

::: pf-proof
$\DD\setminus[0,1) = \{re^{i\theta} : 0<r<1,\ 0<\theta<2\pi\}$, and $\varphi_2$ is a holomorphic branch of $\sqrt z$ there with inverse $w\mapsto w^2$ on $\DD^+ = \{\rho e^{i\psi} : 0<\rho<1,\ 0<\psi<\pi\}$.
:::

:::

::: {.pf-step #quadrant}
$\varphi_3(w)\coloneqq\dfrac{1+w}{1-w}$ maps $\DD^+$ conformally onto $Q$.

::: pf-proof
For $w\in\DD$,
$$
\frac{1+w}{1-w} = \frac{(1+w)(1-\bar w)}{\abs{1-w}^2} = \frac{1-\abs w^2 + 2i\Im w}{\abs{1-w}^2},
$$
so $\varphi_3$ maps $\DD$ onto the right half-plane and $\{\Im w>0\}$ onto $\{\Im>0\}$; its inverse $u\mapsto\frac{u-1}{u+1}$ maps $Q$ back into $\DD^+$.
:::

:::

::: pf-step
$$
\boxed{f \coloneqq \varphi_5\circ\varphi_4\circ\varphi_3\circ\varphi_2\circ\varphi_1},\qquad \varphi_4(u)\coloneqq u^2,\quad \varphi_5(v)\coloneqq\frac{v-i}{v+i},
$$
is a conformal map of $\DD\setminus[1/2,1)$ onto $\DD$.

::: pf-proof
$\varphi_4$ maps $Q$ conformally onto $\HH$, and $\varphi_5$ maps $\HH$ conformally onto $\DD$ since $\abs{v-i}<\abs{v+i}$ exactly when $\Im v>0$.
Composing with steps [](#move-slit){.pf-ref}, [](#root){.pf-ref} and [](#quadrant){.pf-ref} gives a holomorphic bijection onto $\DD$.
:::

:::

:::

:::
